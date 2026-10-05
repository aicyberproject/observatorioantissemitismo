"""Testes do script de referencia, sobre dados sinteticos gerados aqui.

Nenhum dado real entra nos testes. Os identificadores sinteticos tem um prefixo
reconhecivel, para o teste de vazamento procurar por ele em toda saida.
"""

import bz2
import csv
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import reproduza_disque100 as r  # noqa: E402

PREFIXO = "SINTETICO"
CABECALHO = ["hash", "Data_de_cadastro", "UF", "Religião_da_vítima", "Motivação", "violacao"]
LRC = "LIBERDADE>DE RELIGIÃO ou CRENÇA"

MAPA = {
    "colunas": {
        "id_denuncia": "hash",
        "data": "Data_de_cadastro",
        "ramo_violacao": {"coluna": "violacao", "separador": ">", "niveis": 2},
        "subtipo_violacao": {"coluna": "violacao", "separador": ">", "posicao": 2},
        "religiao_vitima": "Religião_da_vítima",
        "motivacao": "Motivação",
    },
    "formato_data": "%Y-%m-%d",
    "valores": {
        "ramo_lrc": LRC,
        "religiao_judaismo": "Judaísmo",
        "motivacao_religiao": "Em razão da religião",
        "motivacao_discurso_odio": "Em razão de discurso de ódio",
        "religiao_ausente": ["NULL", "NÃO SABE"],
        "religiao_ausente_variante_n": ["NULL"],
    },
}


def ident(n):
    return f"{PREFIXO}{n:04d}XYZ"


def linhas_2024():
    """Denuncias sinteticas de 2024. Comentario ao lado: o que cada uma testa."""
    L = []
    # 1: tres linhas, uma denuncia (distintas contra linhas); ramo LRC com subtipo
    L += [[ident(1), "2024-02-01", "SP", "NÃO SABE", "", f"{LRC}>Culto"]] * 3
    # 2: ramo LRC sem subtipo
    L += [[ident(2), "2024-03-01", "RJ", "", "", LRC]]
    # 3: ramo Igualdade, nao conta no ramo LRC
    L += [[ident(3), "2024-04-01", "MG", "Católica", "Em razão de discurso de ódio", "IGUALDADE>DISCRIMINAÇÃO"]]
    # 4: vitima judaismo e ramo LRC na mesma linha
    L += [[ident(4), "2024-05-01", "SP", "Judaísmo", "", f"{LRC}>Crença"]]
    # 5: vitima judaismo numa linha, ramo LRC em outra linha da mesma denuncia
    L += [[ident(5), "2024-08-01", "SP", "Judaísmo", "", "IGUALDADE>DISCRIMINAÇÃO"],
          [ident(5), "2024-08-01", "SP", "", "", f"{LRC}>Culto"]]
    # 6: vitima judaismo sem nenhuma linha no ramo LRC
    L += [[ident(6), "2024-09-01", "PR", "judaismo", "Em razão de discurso de ódio", "INTEGRIDADE>PSÍQUICA>CONSTRANGIMENTO"]]
    return L


def grava_csv(caminho, linhas, comprimir=False):
    texto = []
    for row in [CABECALHO, *linhas]:
        texto.append(";".join(row))
    dados = ("﻿" + "\n".join(texto) + "\n").encode("utf-8")
    if comprimir:
        caminho.write_bytes(bz2.compress(dados))
    else:
        caminho.write_bytes(dados)


@pytest.fixture
def cenario(tmp_path):
    dados = tmp_path / "dados"
    dados.mkdir()
    todas = linhas_2024()
    s1 = [x for x in todas if x[1] < "2024-07-01"]
    s2 = [x for x in todas if x[1] >= "2024-07-01"]
    grava_csv(dados / "disque100-primeiro-semestre-2024.csv.bz2", s1, comprimir=True)
    grava_csv(dados / "disque100-segundo-semestre-2024.csv", s2)
    mapa = tmp_path / "colunas.json"
    mapa.write_text(json.dumps(MAPA, ensure_ascii=False), encoding="utf-8")
    esperados = tmp_path / "esperados.csv"
    with open(esperados, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";", lineterminator="\n")
        w.writerow(["id", "descricao", "esperado", "tipo", "item_do_anexo_e"])
        for cid, (unidade, _per, _f) in r.DEFINICOES.items():
            w.writerow([cid, "x", "0,00" if unidade == "percentual" else "0", "percentual" if unidade == "percentual" else "inteiro", "E.11"])
    return {"dados": dados, "mapa": mapa, "esperados": esperados, "saida": tmp_path / "saida"}


def roda(cenario, capsys, *extra):
    cod = r.main(["reproduzir", str(cenario["dados"]), "--colunas", str(cenario["mapa"]),
                  "--esperados", str(cenario["esperados"]), "--saida", str(cenario["saida"]), *extra])
    out = capsys.readouterr()
    resultado = {}
    arq = cenario["saida"] / "resultado_conferencia.csv"
    if arq.exists():
        for linha in csv.DictReader(open(arq, encoding="utf-8"), delimiter=";"):
            resultado[linha["id"]] = linha
    return cod, out, resultado


def test_distintas_contra_linhas(cenario, capsys):
    cod, _, res = roda(cenario, capsys)
    assert cod == 0
    assert res["c03"]["calculado"] == "9"  # linhas de 2024
    assert res["c04"]["calculado"] == "6"  # denuncias distintas de 2024


def test_ramo_com_e_sem_subtipo(cenario, capsys):
    _, _, res = roda(cenario, capsys)
    # denuncias 1 (com subtipo), 2 (sem subtipo), 4 e 5; nao a 3 (Igualdade) nem a 6
    assert res["c10"]["calculado"] == "4"


def test_vitima_judaismo_com_e_sem_ramo(cenario, capsys):
    _, _, res = roda(cenario, capsys)
    assert res["c15"]["calculado"] == "3"  # 4, 5 e 6 (normalizacao de caixa e acento)
    assert res["c18"]["calculado"] == "1"  # so a 6 nao tem linha no ramo
    assert res["c18-L"]["calculado"] == "2"  # 5 e 6: nenhuma linha combina judaismo e ramo


def test_preenchimento_duas_variantes(cenario, capsys):
    _, _, res = roda(cenario, capsys)
    # preenchida: denuncias 3, 4, 5, 6 de 6 (Nao informado e vazio sao ausencia)
    assert res["c23"]["calculado"] == "66,67"
    # linhas preenchidas: 3, 4, 5 (primeira), 6 = 4 de 9
    assert res["c23-B"]["calculado"] == "44,44"
    # variante N: so NULL e vazio sao ausencia, e NAO SABE conta como preenchida
    assert res["c23-N"]["calculado"] == "83,33"
    assert res["c23-BN"]["calculado"] == "77,78"
    assert res["c23"]["situacao"] == "diverge"  # esperado sintetico 0,00
    assert res["c23-N"]["situacao"] == "diverge"


def test_motivacao(cenario, capsys):
    _, _, res = roda(cenario, capsys)
    assert res["c20"]["calculado"] == "2"


def test_periodo_ausente_vira_lacuna(cenario, capsys):
    _, _, res = roda(cenario, capsys)
    assert res["c07"]["situacao"] == "lacuna"
    assert res["c02"]["situacao"] == "lacuna"
    assert (cenario["saida"] / "lacunas.md").exists()


def test_mapa_ausente_para_e_registra_lacuna(cenario, capsys):
    cenario["mapa"].unlink()
    cod, out, res = roda(cenario, capsys)
    assert cod == 2
    assert res == {}
    assert "Mapa de colunas" in (cenario["saida"] / "lacunas.md").read_text(encoding="utf-8")


def test_coluna_inexistente_para_e_registra_lacuna(cenario, capsys):
    mapa = json.loads(cenario["mapa"].read_text(encoding="utf-8"))
    mapa["colunas"]["religiao_vitima"] = "Coluna_que_nao_existe"
    cenario["mapa"].write_text(json.dumps(mapa), encoding="utf-8")
    cod, _, res = roda(cenario, capsys)
    assert cod == 2
    assert res == {}
    assert "Coluna_que_nao_existe" in (cenario["saida"] / "lacunas.md").read_text(encoding="utf-8")


def test_deterministico(cenario, capsys):
    roda(cenario, capsys)
    a = {p.name: p.read_bytes() for p in cenario["saida"].iterdir()}
    roda(cenario, capsys)
    b = {p.name: p.read_bytes() for p in cenario["saida"].iterdir()}
    assert a.keys() == b.keys()
    for nome in a:
        la = [x for x in a[nome].splitlines() if not x.startswith(b"Data e hora")]
        lb = [x for x in b[nome].splitlines() if not x.startswith(b"Data e hora")]
        assert la == lb, nome


def test_nenhuma_linha_de_dado_na_saida(cenario, capsys):
    r.main(["inspecionar", str(cenario["dados"]), "--saida", str(cenario["saida"])])
    out1 = capsys.readouterr()
    _, out2, _ = roda(cenario, capsys)
    textos = [out1.out, out1.err, out2.out, out2.err]
    textos += [p.read_text(encoding="utf-8") for p in cenario["saida"].iterdir()]
    for t in textos:
        assert PREFIXO not in t
        assert "XYZ" not in t


def test_erro_de_leitura_nao_ecoa_conteudo(tmp_path, capsys):
    dados = tmp_path / "dados"
    dados.mkdir()
    # linha com campos a mais: o pandas falha, e a mensagem original citaria a linha
    (dados / "disque100-primeiro-semestre-2024.csv").write_text(
        "hash;x\n" + f"{ident(9)};a\n" + f"{ident(8)};b;c;d\n", encoding="utf-8"
    )
    cod = r.main(["inspecionar", str(dados), "--saida", str(tmp_path / "saida")])
    out = capsys.readouterr()
    assert cod == 1
    assert PREFIXO not in out.out + out.err
