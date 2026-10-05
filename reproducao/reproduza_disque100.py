#!/usr/bin/env python3
"""Script de referencia do kit "Reproduza o achado" (microdados abertos do Disque 100).

Reproduz os 25 totais do relatorio preliminar conjunto do Eixo 3, versao 2.0, Anexo E,
item E.11, a partir dos arquivos CSV dos microdados abertos publicados pelo MDHC.

Dois subcomandos:

  inspecionar  descreve as colunas de cada arquivo (nome, tipo inferido, numero de
               valores distintos) e, so para colunas de baixa cardinalidade, os valores
               e suas contagens. Serve para preencher o mapa de colunas.
  reproduzir   calcula os totais, compara com os esperados e grava a conferencia.

Regra de privacidade: o script nunca imprime, exporta ou grava linha da base. So
agregados. Mensagens de erro citam o arquivo e o tipo do erro, nunca o conteudo.

Regra de falsificabilidade: as definicoes de cada total estao declaradas em DEFINICOES,
abaixo, antes de qualquer execucao. Onde ha ambiguidade, as variantes sao calculadas e
reportadas todas, com a principal indicada. Divergencia e resultado, e nao erro.
"""

from __future__ import annotations

import argparse
import bz2
import csv
import datetime as dt
import gzip
import hashlib
import json
import platform
import re
import sys
import unicodedata
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ESPERADOS_PADRAO = AQUI.parent / "data" / "relatorio-v2" / "disque100_reproducao.csv"
SAIDA_PADRAO = AQUI / "saida"

PADRAO_ARQUIVO = re.compile(
    r"^disque100-(primeiro|segundo)-semestre-(\d{4})\.csv(\.bz2|\.gz)?$", re.IGNORECASE
)
TAMANHO_BLOCO = 250_000
LIMITE_DISTINTOS = 200
MINIMO_FORMA = 50
# Colunas cujo nome sugere identificador nunca tem valores listados, qualquer que seja a
# cardinalidade.
NOME_IDENTIFICADOR = re.compile(r"hash|^id|_id$|protocolo|cpf|cnpj|nome|telefone|e-?mail", re.I)

CHAVES_MAPA = ["id_denuncia", "data", "ramo_violacao", "subtipo_violacao", "religiao_vitima", "motivacao"]
CHAVES_VALORES = [
    "ramo_lrc",
    "religiao_judaismo",
    "motivacao_religiao",
    "motivacao_discurso_odio",
    "religiao_ausente",
]

# ---------------------------------------------------------------------------
# Definicoes declaradas antes da execucao (falsificabilidade).
#
# Unidades
#   linha     cada linha do arquivo, que combina denuncia, vitima, suspeito e violacao.
#   denuncia  valor distinto do identificador de denuncia, contado uma vez no periodo.
#             Nunca se somam contagens de semestres: conta-se a uniao do periodo.
#
# Periodo (atribuicao)
#   data     ano e mes da data de cadastro da linha. 1o semestre = meses 1 a 6.
#   arquivo  ano e semestre do nome do arquivo.
#   Principal: "data" para todos os totais de denuncia e de recorte; "arquivo" para os
#   totais de linhas do arquivo (c01, c03, c05, c07), que o Anexo E define pelo arquivo.
#   Sem coluna de data no mapa, vale "arquivo" para tudo, e isso vai para lacunas.md.
#   A outra atribuicao e sempre calculada e reportada como variante.
#
# Filtros (comparacao por igualdade apos normalizacao: caixa, acentos e espacos)
#   ramo LRC            ramo da violacao igual a valores.ramo_lrc
#   vitima judaismo     religiao da vitima igual a valores.religiao_judaismo
#   religiao preenchida religiao da vitima nao vazia e fora de valores.religiao_ausente
#   motivacao           motivacao igual a valores.motivacao_religiao ou
#                       valores.motivacao_discurso_odio
#
# Comparacao com o esperado
#   inteiros: igualdade exata. Percentuais: igualdade com duas casas decimais,
#   arredondamento meio para cima.
# ---------------------------------------------------------------------------
DEFINICOES = {
    "c01": ("linhas", "2023", "todas as linhas"),
    "c02": ("denuncias", "2023", "todas as denuncias"),
    "c03": ("linhas", "2024", "todas as linhas"),
    "c04": ("denuncias", "2024", "todas as denuncias"),
    "c05": ("linhas", "2025", "todas as linhas"),
    "c06": ("denuncias", "2025", "todas as denuncias"),
    "c07": ("linhas", "2026-S1", "todas as linhas"),
    "c08": ("denuncias", "2026-S1", "todas as denuncias"),
    "c09": ("denuncias", "2023", "ramo LRC"),
    "c10": ("denuncias", "2024", "ramo LRC"),
    "c11": ("denuncias", "2025", "ramo LRC"),
    "c12": ("linhas", "2023", "ramo LRC"),
    "c13": ("linhas", "2025", "ramo LRC"),
    "c14": ("denuncias", "2023", "vitima judaismo"),
    "c15": ("denuncias", "2024", "vitima judaismo"),
    "c16": ("denuncias", "2025", "vitima judaismo"),
    "c17": ("denuncias", "2026-S1", "vitima judaismo"),
    "c18": ("denuncias", "2024", "vitima judaismo sem ramo LRC"),
    "c19": ("denuncias", "2023", "motivacao religiao"),
    "c20": ("denuncias", "2024", "motivacao discurso de odio"),
    "c21": ("denuncias", "2025", "motivacao discurso de odio"),
    "c22": ("percentual", "2023", "religiao preenchida"),
    "c23": ("percentual", "2024", "religiao preenchida"),
    "c24": ("percentual", "2025", "religiao preenchida"),
    "c25": ("percentual", "2026-S1", "religiao preenchida"),
}

TEXTO_DEFINICOES = {
    "todas as linhas": "Linhas do periodo. Principal: atribuicao pelo arquivo.",
    "todas as denuncias": "Denuncias distintas do periodo.",
    "ramo LRC": "Linhas, ou denuncias distintas, com ramo da violacao igual a ramo_lrc.",
    "vitima judaismo": "Denuncias distintas com ao menos uma linha com religiao da vitima igual a religiao_judaismo.",
    "vitima judaismo sem ramo LRC": (
        "Principal: denuncias com vitima judaismo que nao tem nenhuma linha no ramo LRC. "
        "Variante L: denuncias com vitima judaismo sem nenhuma linha que combine, na mesma linha, "
        "vitima judaismo e ramo LRC."
    ),
    "motivacao religiao": "Denuncias distintas com ao menos uma linha com motivacao igual a motivacao_religiao.",
    "motivacao discurso de odio": "Denuncias distintas com ao menos uma linha com motivacao igual a motivacao_discurso_odio.",
    "religiao preenchida": (
        "Principal (A): denuncias distintas com ao menos uma linha com religiao da vitima preenchida, "
        "sobre denuncias distintas do periodo. Variante B: linhas com religiao preenchida sobre linhas do periodo. "
        "Ausencia: vazio e os rotulos de religiao_ausente. Variantes N e BN, se o mapa trouxer "
        "religiao_ausente_variante_n: o mesmo calculo com essa lista mais restrita de rotulos de ausencia."
    ),
}

PERIODOS = ["2023", "2024", "2025", "2026-S1"]


class Lacuna(Exception):
    """Falta de informacao que impede o calculo. E achado, e nao falha."""


class ErroSaneado(Exception):
    """Erro cuja mensagem foi construida pelo script e nao contem dado da base."""


# ---------------------------------------------------------------------------
# Utilitarios
# ---------------------------------------------------------------------------


def normaliza(valor: str) -> str:
    texto = unicodedata.normalize("NFKD", str(valor))
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return " ".join(texto.casefold().split())


def sha256_e_tamanho(caminho: Path) -> tuple[str, int]:
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest(), caminho.stat().st_size


def abre_binario(caminho: Path):
    nome = caminho.name.lower()
    if nome.endswith(".bz2"):
        return bz2.open(caminho, "rb")
    if nome.endswith(".gz"):
        return gzip.open(caminho, "rb")
    return open(caminho, "rb")


def le_cabecalho(caminho: Path) -> tuple[list[str], str, str]:
    """Le so a primeira linha. Devolve colunas, separador e codificacao."""
    with abre_binario(caminho) as f:
        bruto = f.readline()
    try:
        texto = bruto.decode("utf-8-sig")
        codificacao = "utf-8-sig"
    except UnicodeDecodeError:
        texto = bruto.decode("latin-1")
        codificacao = "latin-1"
    sep = ";" if texto.count(";") >= texto.count(",") else ","
    colunas = next(csv.reader([texto.rstrip("\r\n")], delimiter=sep))
    return colunas, sep, codificacao


def descobre_arquivos(pasta: Path) -> tuple[list[dict], list[str]]:
    """Lista os arquivos semestrais em ordem fixa (ano, semestre)."""
    if not pasta.is_dir():
        raise ErroSaneado(f"Pasta de dados nao encontrada: {pasta}")
    achados: dict[tuple[int, int], Path] = {}
    ignorados = []
    for p in sorted(pasta.iterdir(), key=lambda x: x.name):
        if not p.is_file():
            continue
        m = PADRAO_ARQUIVO.match(p.name)
        if not m:
            ignorados.append(p.name)
            continue
        chave = (int(m.group(2)), 1 if m.group(1).lower() == "primeiro" else 2)
        if chave in achados:
            raise ErroSaneado(
                f"Dois arquivos para o mesmo semestre: {achados[chave].name} e {p.name}. Deixe so um na pasta."
            )
        achados[chave] = p
    arquivos = [{"caminho": achados[k], "ano": k[0], "semestre": k[1]} for k in sorted(achados)]
    return arquivos, ignorados


def periodo_de(ano: int, mes_ou_semestre: int, por_mes: bool) -> str:
    if ano == 2026:
        primeiro = mes_ou_semestre <= 6 if por_mes else mes_ou_semestre == 1
        return "2026-S1" if primeiro else "2026-S2"
    return str(ano)


def fmt_pct(numerador: int, denominador: int) -> str:
    if denominador == 0:
        return ""
    v = (Decimal(numerador) * 100 / Decimal(denominador)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{v}".replace(".", ",")


def le_esperados(caminho: Path) -> dict[str, dict]:
    if not caminho.is_file():
        raise ErroSaneado(f"Arquivo de totais esperados nao encontrado: {caminho}")
    esperados = {}
    with open(caminho, encoding="utf-8", newline="") as f:
        for linha in csv.DictReader(f, delimiter=";"):
            esperados[linha["id"]] = linha
    return esperados


def importa_pandas():
    try:
        import pandas as pd  # noqa: PLC0415
    except ImportError as exc:  # pragma: no cover
        raise ErroSaneado("A biblioteca pandas nao esta instalada. Rode: pip install -r requirements.txt") from exc
    return pd


def le_blocos(caminho: Path, sep: str, codificacao: str, usecols=None):
    """Le o arquivo em blocos, tudo como texto. Erros de leitura saem saneados."""
    pd = importa_pandas()
    try:
        leitor = pd.read_csv(
            caminho,
            sep=sep,
            encoding=codificacao,
            dtype=str,
            na_filter=False,
            usecols=usecols,
            chunksize=TAMANHO_BLOCO,
            compression="infer",
            on_bad_lines="error",
        )
        yield from leitor
    except Exception as exc:  # noqa: BLE001
        # A mensagem original pode ecoar conteudo de linha. Nao e repassada.
        raise ErroSaneado(f"Falha de leitura em {caminho.name} ({type(exc).__name__}). Conteudo omitido.") from None


def grava(caminho: Path, texto: str) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


# ---------------------------------------------------------------------------
# inspecionar
# ---------------------------------------------------------------------------

RE_INTEIRO = re.compile(r"^-?\d+$")
RE_DECIMAL = re.compile(r"^-?\d+[.,]\d+$")
RE_DATA = re.compile(r"^(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})([ T]\d{2}:\d{2}(:\d{2}(\.\d+)?)?)?$")


def tipo_inferido(valores) -> str:
    nao_vazios = [v for v in valores if v != ""]
    if not nao_vazios:
        return "vazio"
    for nome, regex in (("inteiro", RE_INTEIRO), ("decimal", RE_DECIMAL), ("data", RE_DATA)):
        if all(regex.match(v) for v in nao_vazios):
            return nome
    return "texto"


def mascara(valor: str) -> str:
    """Forma do valor, sem o valor: digito vira 9, letra vira a, e o tamanho fica."""
    return re.sub(r"[^\W\d_]", "a", re.sub(r"\d", "9", valor))


def inspecionar(pasta: Path, saida: Path) -> str:
    arquivos, ignorados = descobre_arquivos(pasta)
    partes = [
        "# Inspecao dos microdados do Disque 100",
        "",
        "Gerado por `reproduza_disque100.py inspecionar`. Nenhuma linha da base consta deste arquivo.",
        f"Valores listados apenas para colunas com ate {LIMITE_DISTINTOS} valores distintos, menos distintos",
        "que metade das linhas e nome que nao sugere identificador. Para as demais, so a contagem, o",
        f"tamanho e as formas (digito vira 9, letra vira a) comuns a ao menos {MINIMO_FORMA} valores distintos.",
        "",
    ]
    if not arquivos:
        partes.append("Nenhum arquivo no padrao `disque100-<primeiro|segundo>-semestre-AAAA.csv[.bz2|.gz]`.")
    for arq in arquivos:
        caminho = arq["caminho"]
        colunas, sep, cod = le_cabecalho(caminho)
        contagens: list[dict] = [dict() for _ in colunas]
        linhas = 0
        for bloco in le_blocos(caminho, sep, cod):
            linhas += len(bloco)
            for i in range(len(colunas)):
                acum = contagens[i]
                for valor, n in bloco.iloc[:, i].value_counts(sort=False).items():
                    acum[valor] = acum.get(valor, 0) + int(n)
        sha, tamanho = sha256_e_tamanho(caminho)
        partes += [
            f"## {caminho.name}",
            "",
            f"- Linhas: {linhas}",
            f"- Tamanho em bytes: {tamanho}",
            f"- SHA-256: `{sha}`",
            f"- Separador: `{sep}`; codificacao: {cod}; colunas: {len(colunas)}",
            "",
            "| # | Coluna | Tipo inferido | Distintos | Vazios |",
            "|---|---|---|---|---|",
        ]
        detalhes = []
        for i, nome in enumerate(colunas):
            acum = contagens[i]
            partes.append(f"| {i + 1} | {nome} | {tipo_inferido(acum)} | {len(acum)} | {acum.get('', 0)} |")
            lista_valores = (
                len(acum) <= LIMITE_DISTINTOS and len(acum) <= max(linhas // 2, 1) and not NOME_IDENTIFICADOR.search(nome)
            )
            if lista_valores:
                itens = sorted(acum.items(), key=lambda kv: (-kv[1], kv[0]))
                detalhes += [f"### {caminho.name} :: {nome}", "", "| Valor | Contagem |", "|---|---|"]
                detalhes += [f"| {v if v != '' else '(vazio)'} | {n} |" for v, n in itens]
                detalhes.append("")
            else:
                # Forma de um valor so pode ser mostrada se muitos valores distintos a
                # compartilham. Forma de valor unico (caso de identificador) seria
                # impressao digital do registro, e a contagem revelaria suas linhas.
                formas: dict[str, list] = {}
                for v, n in acum.items():
                    f = formas.setdefault(mascara(v), [0, 0])
                    f[0] += n
                    f[1] += 1
                comuns = [(forma, n) for forma, (n, dist) in formas.items() if dist >= MINIMO_FORMA]
                top = sorted(comuns, key=lambda kv: (-kv[1], kv[0]))[:5]
                tamanhos = [len(v) for v in acum]
                detalhes += [
                    f"### {caminho.name} :: {nome}",
                    "",
                    f"Valores nao listados ({len(acum)} distintos; tamanho de {min(tamanhos)} a {max(tamanhos)} caracteres).",
                    f"Formas compartilhadas por ao menos {MINIMO_FORMA} valores distintos, ate cinco:",
                    "",
                ]
                detalhes += [f"- `{forma}`: {n} linhas" for forma, n in top] or ["- nenhuma"]
                detalhes.append("")
        partes += ["", *detalhes]
    if ignorados:
        partes += ["## Arquivos ignorados por nao seguirem o padrao de nome", ""]
        partes += [f"- {n}" for n in ignorados]
        partes.append("")
    texto = "\n".join(partes) + "\n"
    grava(saida / "inspecao.md", texto)
    return texto


# ---------------------------------------------------------------------------
# Mapa de colunas
# ---------------------------------------------------------------------------


def le_mapa(caminho: Path) -> dict:
    if not caminho.is_file():
        raise Lacuna(f"Mapa de colunas nao encontrado: {caminho.name}. Copie colunas.exemplo.json e preencha.")
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def spec_coluna(mapa: dict, chave: str):
    """Devolve (coluna, separador, nivel) ou None. Aceita texto ou objeto.

    Coluna hierarquica (por exemplo `RAMO>SUBRAMO>SUBTIPO`): `niveis: n` toma os n
    primeiros niveis, unidos pelo separador; `posicao: i` toma so o nivel i (base 0).
    """
    bruto = mapa.get("colunas", {}).get(chave)
    if bruto in (None, ""):
        return None
    if isinstance(bruto, str):
        return bruto, None, None
    if "niveis" in bruto:
        return bruto["coluna"], bruto["separador"], ("niveis", int(bruto["niveis"]))
    return bruto["coluna"], bruto.get("separador"), ("posicao", int(bruto.get("posicao", 0)))


def valida_mapa(mapa: dict, arquivos: list[dict]) -> list[str]:
    """Devolve a lista de lacunas. Lacuna em coluna obrigatoria impede o calculo."""
    lacunas = []
    for chave in CHAVES_MAPA:
        if spec_coluna(mapa, chave) is None and chave not in ("data", "subtipo_violacao"):
            lacunas.append(f"Coluna logica `{chave}` sem correspondencia no mapa.")
    for chave in CHAVES_VALORES:
        if chave not in mapa.get("valores", {}):
            lacunas.append(f"Valor de referencia `{chave}` ausente do mapa.")
    for arq in arquivos:
        colunas, _, _ = le_cabecalho(arq["caminho"])
        for chave in CHAVES_MAPA:
            spec = spec_coluna(mapa, chave)
            if spec and spec[0] not in colunas:
                lacunas.append(f"Coluna `{spec[0]}` (`{chave}`) nao existe no cabecalho de {arq['caminho'].name}.")
    return lacunas


def extrai(serie, separador, nivel):
    if separador is None:
        return serie
    modo, n = nivel
    unicos = serie.unique()
    tabela = {}
    for u in unicos:
        partes = [p.strip() for p in u.split(separador)]
        if modo == "niveis":
            tabela[u] = separador.join(partes[:n]) if len(partes) >= n else ""
        else:
            tabela[u] = partes[n] if len(partes) > n else ""
    return serie.map(tabela)


def normaliza_serie(serie):
    unicos = serie.unique()
    return serie.map({u: normaliza(u) for u in unicos})


# ---------------------------------------------------------------------------
# reproduzir
# ---------------------------------------------------------------------------


class Acumulador:
    """Conjuntos de denuncias e contagens de linhas por (atribuicao, periodo, filtro)."""

    def __init__(self):
        self.linhas: dict[tuple, int] = {}
        self.ids: dict[tuple, set] = {}

    def soma(self, chave: tuple, n: int):
        self.linhas[chave] = self.linhas.get(chave, 0) + n

    def junta(self, chave: tuple, valores):
        self.ids.setdefault(chave, set()).update(valores)

    def n_linhas(self, chave):
        return self.linhas.get(chave, 0)

    def n_ids(self, chave):
        return len(self.ids.get(chave, ()))

    def conjunto(self, chave):
        return self.ids.get(chave, set())




def processa(arquivos: list[dict], mapa: dict, controles: dict) -> tuple[Acumulador, dict]:
    pd = importa_pandas()
    val = mapa["valores"]
    alvo = {
        "lrc": normaliza(val["ramo_lrc"]),
        "jud": normaliza(val["religiao_judaismo"]),
        "mot_religiao": normaliza(val["motivacao_religiao"]),
        "mot_odio": normaliza(val["motivacao_discurso_odio"]),
    }
    ausente = {normaliza(v) for v in val["religiao_ausente"]} | {""}
    ausente_n = None
    if "religiao_ausente_variante_n" in val:
        ausente_n = {normaliza(v) for v in val["religiao_ausente_variante_n"]} | {""}
    fmt_data = mapa.get("formato_data")

    s_id = spec_coluna(mapa, "id_denuncia")
    s_data = spec_coluna(mapa, "data")
    s_ramo = spec_coluna(mapa, "ramo_violacao")
    s_sub = spec_coluna(mapa, "subtipo_violacao")
    s_rel = spec_coluna(mapa, "religiao_vitima")
    s_mot = spec_coluna(mapa, "motivacao")
    usadas = sorted({s[0] for s in (s_id, s_data, s_ramo, s_sub, s_rel, s_mot) if s})

    acum = Acumulador()
    info = {"sem_data": 0, "data_fora_do_arquivo": 0, "subtipos_lrc": {}}
    for arq in arquivos:
        colunas, sep, cod = le_cabecalho(arq["caminho"])
        p_arq = periodo_de(arq["ano"], arq["semestre"], por_mes=False)
        rotulo_sem = f"{arq['ano']}-S{arq['semestre']}"
        for bloco in le_blocos(arq["caminho"], sep, cod, usecols=usadas):
            ids = bloco[s_id[0]]
            ramo = normaliza_serie(extrai(bloco[s_ramo[0]], s_ramo[1], s_ramo[2]))
            rel = normaliza_serie(bloco[s_rel[0]])
            mot = normaliza_serie(bloco[s_mot[0]])
            mascaras = {
                "todas": pd.Series(True, index=bloco.index),
                "lrc": ramo == alvo["lrc"],
                "jud": rel == alvo["jud"],
                "rel_preenchida": ~rel.isin(ausente),
                **({"rel_preenchida_n": ~rel.isin(ausente_n)} if ausente_n is not None else {}),
                "mot_religiao": mot == alvo["mot_religiao"],
                "mot_odio": mot == alvo["mot_odio"],
            }
            mascaras["jud_lrc_mesma_linha"] = mascaras["jud"] & mascaras["lrc"]

            if s_data:
                bruto = bloco[s_data[0]]
                unicos = bruto.unique()
                datas = pd.to_datetime(pd.Series(unicos), format=fmt_data, errors="coerce")
                tabela = dict(zip(unicos, datas))
                data = bruto.map(tabela)
                ok = data.notna()
                info["sem_data"] += int((~ok).sum())
                periodo_data = pd.Series("sem data", index=bloco.index)
                anos = data.dt.year.astype("Int64")
                meses = data.dt.month.astype("Int64")
                p = anos.astype(str).where(anos != 2026, "2026-S" + (meses > 6).map({True: "2", False: "1"}).astype(str))
                periodo_data = periodo_data.where(~ok, p)
                fora = ok & (periodo_data != p_arq)
                info["data_fora_do_arquivo"] += int(fora.sum())
            else:
                data = None
                periodo_data = pd.Series(p_arq, index=bloco.index)

            for filtro, m in mascaras.items():
                # atribuicao pelo arquivo
                acum.soma(("arquivo", p_arq, filtro), int(m.sum()))
                acum.junta(("arquivo", p_arq, filtro), ids[m].unique())
                acum.soma(("semestre", rotulo_sem, filtro), int(m.sum()))
                acum.junta(("semestre", rotulo_sem, filtro), ids[m].unique())
                # atribuicao pela data
                for per, grupo in ids[m].groupby(periodo_data[m], sort=True):
                    acum.soma(("data", per, filtro), len(grupo))
                    acum.junta(("data", per, filtro), grupo.unique())

            # controle: ultima data com motivacao religiosa
            if data is not None:
                mr = mascaras["mot_religiao"] & data.notna()
                if mr.any():
                    ultima = data[mr].max()
                    atual = controles.get("ultima_mot_religiao")
                    if atual is None or ultima > atual:
                        controles["ultima_mot_religiao"] = ultima
            # agregado de subtipos no ramo LRC (denuncias por subtipo, por arquivo)
            if s_sub:
                sub = extrai(bloco[s_sub[0]], s_sub[1], s_sub[2])
                for rot, grupo in ids[mascaras["lrc"]].groupby(sub[mascaras["lrc"]], sort=True):
                    info["subtipos_lrc"].setdefault((rotulo_sem, rot), set()).update(grupo.unique())
    info["subtipos_lrc"] = {k: len(v) for k, v in sorted(info["subtipos_lrc"].items())}
    return acum, info


def calcula(acum: Acumulador, principal_data: bool) -> list[dict]:
    """Monta as linhas de resultado: principal e variantes de cada total."""
    resultados = []
    att_principal = "data" if principal_data else "arquivo"

    def valor(unidade, att, per, filtro_def):
        if filtro_def == "vitima judaismo sem ramo LRC":
            jud = acum.conjunto((att, per, "jud"))
            return {
                "": len(jud - acum.conjunto((att, per, "lrc"))),
                "L": len(jud - acum.conjunto((att, per, "jud_lrc_mesma_linha"))),
            }
        filtro = {
            "todas as linhas": "todas",
            "todas as denuncias": "todas",
            "ramo LRC": "lrc",
            "vitima judaismo": "jud",
            "motivacao religiao": "mot_religiao",
            "motivacao discurso de odio": "mot_odio",
            "religiao preenchida": "rel_preenchida",
        }[filtro_def]
        if unidade == "linhas":
            return {"": acum.n_linhas((att, per, filtro))}
        if unidade == "denuncias":
            return {"": acum.n_ids((att, per, filtro))}
        res = {
            "": fmt_pct(acum.n_ids((att, per, filtro)), acum.n_ids((att, per, "todas"))),
            "B": fmt_pct(acum.n_linhas((att, per, filtro)), acum.n_linhas((att, per, "todas"))),
        }
        if (att, per, "rel_preenchida_n") in acum.linhas:
            res["N"] = fmt_pct(acum.n_ids((att, per, "rel_preenchida_n")), acum.n_ids((att, per, "todas")))
            res["BN"] = fmt_pct(acum.n_linhas((att, per, "rel_preenchida_n")), acum.n_linhas((att, per, "todas")))
        return res

    for cid, (unidade, per, filtro_def) in DEFINICOES.items():
        # linhas do arquivo: o Anexo E define pelo arquivo
        ap = "arquivo" if filtro_def == "todas as linhas" else att_principal
        atribuicoes = [ap]
        if principal_data:
            atribuicoes.append("data" if ap == "arquivo" else "arquivo")
        for att in atribuicoes:
            tem_dado = acum.n_linhas((att, per, "todas")) > 0
            for sufixo, v in valor(unidade, att, per, filtro_def).items():
                partes = [cid] + ([sufixo] if sufixo else []) + ([att] if att != ap else [])
                resultados.append(
                    {"id": "-".join(partes), "calculado": v if tem_dado else "", "atribuicao": att,
                     "principal": att == ap and not sufixo}
                )
    return resultados


def situacao(calculado, esperado, tipo) -> str:
    if calculado == "" or calculado is None:
        return "lacuna"
    if tipo == "percentual":
        return "confere" if str(calculado) == str(esperado) else "diverge"
    return "confere" if int(calculado) == int(esperado) else "diverge"


def reproduzir(pasta: Path, mapa_caminho: Path, esperados_caminho: Path, saida: Path) -> int:
    esperados = le_esperados(esperados_caminho)
    arquivos, ignorados = descobre_arquivos(pasta)
    try:
        mapa = le_mapa(mapa_caminho)
        lacunas = valida_mapa(mapa, arquivos)
    except Lacuna as exc:
        lacunas = [str(exc)]
        mapa = None
    if not arquivos:
        lacunas.append("Nenhum arquivo semestral encontrado na pasta indicada.")
    if lacunas:
        grava(
            saida / "lacunas.md",
            "# Lacunas\n\nO calculo foi interrompido. Nada foi inventado.\n\n" + "".join(f"- {l}\n" for l in lacunas),
        )
        print("Lacuna: o calculo foi interrompido. Ver saida/lacunas.md.", file=sys.stderr)
        return 2

    controles: dict = {}
    acum, info = processa(arquivos, mapa, controles)
    principal_data = spec_coluna(mapa, "data") is not None
    resultados = calcula(acum, principal_data)

    # controles de 2023 (E.11.9)
    resultados += [
        {"id": "c19-ctl-2023S1", "calculado": acum.n_ids(("semestre", "2023-S1", "mot_religiao")) if acum.n_linhas(("semestre", "2023-S1", "todas")) else "", "esperado": "502", "tipo": "inteiro", "atribuicao": "semestre", "principal": False},
        {"id": "c19-ctl-2023S2", "calculado": acum.n_ids(("semestre", "2023-S2", "mot_religiao")) if acum.n_linhas(("semestre", "2023-S2", "todas")) else "", "esperado": "140", "tipo": "inteiro", "atribuicao": "semestre", "principal": False},
    ]
    ultima = controles.get("ultima_mot_religiao")
    resultados.append({"id": "c19-ctl-ultima-data", "calculado": ultima.strftime("%Y-%m-%d") if ultima is not None else "", "esperado": "2023-08-31", "tipo": "data", "atribuicao": "data", "principal": False})

    linhas_csv = ["id;calculado;esperado;situacao"]
    divergentes, lacunas_periodo = [], []
    for r in resultados:
        base = r["id"].split("-")[0]
        esp = r.get("esperado", esperados.get(base, {}).get("esperado", ""))
        tipo = r.get("tipo", esperados.get(base, {}).get("tipo", "inteiro"))
        if tipo == "data":
            sit = "lacuna" if r["calculado"] == "" else ("confere" if r["calculado"] == esp else "diverge")
        else:
            sit = situacao(r["calculado"], esp, tipo)
        r["situacao"] = sit
        linhas_csv.append(f"{r['id']};{r['calculado']};{esp};{sit}")
        if r["principal"] and sit == "diverge":
            divergentes.append(r["id"])
        if r["principal"] and sit == "lacuna":
            lacunas_periodo.append(r["id"])
    grava(saida / "resultado_conferencia.csv", "\n".join(linhas_csv) + "\n")

    if lacunas_periodo:
        presentes = ", ".join(f"{a['ano']}-S{a['semestre']}" for a in arquivos)
        grava(
            saida / "lacunas.md",
            "# Lacunas\n\n"
            f"Totais principais sem arquivo do periodo na pasta: {', '.join(lacunas_periodo)}.\n"
            f"Semestres presentes: {presentes}.\n",
        )
    elif (saida / "lacunas.md").exists():
        (saida / "lacunas.md").unlink()

    grava(saida / "execucao.md", relatorio_execucao(arquivos, ignorados, mapa, principal_data, info, resultados))
    conf = sum(1 for r in resultados if r["principal"] and r["situacao"] == "confere")
    princ = sum(1 for r in resultados if r["principal"])
    print(f"Totais principais: {princ}. Conferem: {conf}. Divergem: {len(divergentes)}. Lacuna: {len(lacunas_periodo)}.")
    print("Resultado em saida/resultado_conferencia.csv e saida/execucao.md.")
    return 0


def relatorio_execucao(arquivos, ignorados, mapa, principal_data, info, resultados) -> str:
    pd = importa_pandas()
    linhas = [
        "# Execucao do script de referencia do Disque 100",
        "",
        f"Data e hora da execucao: {dt.datetime.now().astimezone().isoformat(timespec='seconds')}",
        "",
        "## Ambiente",
        "",
        f"- Python {platform.python_version()} ({platform.python_implementation()})",
        f"- pandas {pd.__version__}",
        f"- numpy {__import__('numpy').__version__}",
        "",
        "## Arquivos lidos, na ordem de processamento",
        "",
        "SHA-256 e tamanho do arquivo como esta na pasta (comprimido, se for `.bz2` ou `.gz`).",
        "",
        "| Arquivo | Bytes | SHA-256 |",
        "|---|---|---|",
    ]
    for arq in arquivos:
        sha, tam = sha256_e_tamanho(arq["caminho"])
        linhas.append(f"| {arq['caminho'].name} | {tam} | `{sha}` |")
    if ignorados:
        linhas += ["", "Ignorados por nao seguirem o padrao de nome: " + ", ".join(ignorados) + "."]
    linhas += [
        "",
        "## Mapa de colunas usado",
        "",
        "```json",
        json.dumps(mapa, ensure_ascii=False, indent=2, sort_keys=True),
        "```",
        "",
        "## Definicoes aplicadas",
        "",
        f"- Atribuicao de periodo principal: {'data de cadastro' if principal_data else 'semestre do arquivo (sem coluna de data)'}; "
        "para linhas do arquivo (c01, c03, c05, c07), o arquivo.",
        "- Denuncias: identificador distinto na uniao do periodo, sem somar semestres.",
        "- Comparacao: inteiros por igualdade exata; percentuais com duas casas, arredondamento meio para cima.",
        "- Sufixos de variante: `-data` e `-arquivo` indicam a outra atribuicao de periodo; `-B`, linhas sobre linhas;"
        " `-L`, criterio na mesma linha.",
        "",
    ]
    for chave, texto in TEXTO_DEFINICOES.items():
        linhas.append(f"- {chave}: {texto}")
    linhas += [
        "",
        "## Controles agregados",
        "",
        f"- Linhas sem data reconhecivel: {info['sem_data']}",
        f"- Linhas cuja data cai fora do semestre do arquivo: {info['data_fora_do_arquivo']}",
        "",
        "Denuncias distintas do ramo LRC por subtipo e semestre do arquivo:",
        "",
        "| Semestre | Subtipo | Denuncias |",
        "|---|---|---|",
    ]
    for (sem, sub), n in info["subtipos_lrc"].items():
        linhas.append(f"| {sem} | {sub if sub else '(vazio)'} | {n} |")
    linhas += ["", "## Resultado", "", "| Id | Calculado | Situacao | Principal |", "|---|---|---|---|"]
    for r in resultados:
        linhas.append(f"| {r['id']} | {r['calculado']} | {r['situacao']} | {'sim' if r['principal'] else 'nao'} |")
    return "\n".join(linhas) + "\n"


# ---------------------------------------------------------------------------
# Linha de comando
# ---------------------------------------------------------------------------


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="reproduza_disque100.py",
        description="Reproduz os totais do Anexo E, E.11, a partir dos microdados abertos do Disque 100.",
    )
    sub = parser.add_subparsers(dest="comando", required=True)
    p_ins = sub.add_parser("inspecionar", help="descreve as colunas, sem imprimir linha da base")
    p_ins.add_argument("pasta", type=Path, help="pasta com os arquivos CSV semestrais")
    p_ins.add_argument("--saida", type=Path, default=SAIDA_PADRAO)
    p_rep = sub.add_parser("reproduzir", help="calcula os totais e confere com os esperados")
    p_rep.add_argument("pasta", type=Path, help="pasta com os arquivos CSV semestrais")
    p_rep.add_argument("--colunas", type=Path, default=AQUI / "colunas.json", help="mapa de colunas")
    p_rep.add_argument("--esperados", type=Path, default=ESPERADOS_PADRAO)
    p_rep.add_argument("--saida", type=Path, default=SAIDA_PADRAO)
    args = parser.parse_args(argv)
    try:
        if args.comando == "inspecionar":
            print(inspecionar(args.pasta, args.saida), end="")
            return 0
        return reproduzir(args.pasta, args.colunas, args.esperados, args.saida)
    except ErroSaneado as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001
        print(f"Erro inesperado ({type(exc).__name__}). Conteudo omitido por seguranca.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
