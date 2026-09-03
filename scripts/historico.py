#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Persistencia da coleta: instantaneo diario e indice acumulado.

O painel e regerado a cada execucao do deploy e sobrescreve o anterior. Sem
persistencia, nada do que o Observatorio observa sobrevive ao ciclo seguinte, e
serie propria nunca se forma. Este modulo grava um instantaneo por dia e mantem
um indice que a pagina e o boletim leem.

Granularidade diaria, e nao por execucao: 48 arquivos por dia seriam ruido. A
execucao do dia sobrescreve o arquivo do dia, acumulando os itens vistos e
deduplicando por chave de link. O arquivo do dia anterior nunca e tocado.

    python3 scripts/historico.py                      # usa data/noticias.json
    python3 scripts/historico.py caminho/noticias.json
"""
import json
import pathlib
import re
import sys
import unicodedata
from datetime import date, datetime, timedelta, timezone

RAIZ = pathlib.Path(__file__).resolve().parent.parent
HIST = RAIZ / "data" / "historico"
RETENCAO_DIAS = 400          # pouco mais de um ano; mantem a serie sem inflar o repo


def sem_acento(t):
    t = unicodedata.normalize("NFD", t or "")
    return "".join(c for c in t if unicodedata.category(c) != "Mn").lower()


def chave(item):
    """Mesma normalizacao do agregador, para que dias distintos deduplifiquem."""
    l = re.sub(r"[?#].*$", "", (item.get("link") or "").lower()).rstrip("/")
    return l or sem_acento(item.get("titulo"))[:90]


def semana_iso(d):
    a, s, _ = d.isocalendar()
    return f"{a}-S{s:02d}"


def grava_instantaneo(dados, dia=None, dir_hist=HIST):
    """Acumula os itens do dia em data/historico/AAAA-MM-DD.json."""
    dia = dia or date.today()
    dir_hist.mkdir(parents=True, exist_ok=True)
    alvo = dir_hist / f"{dia.isoformat()}.json"

    anterior = {}
    if alvo.exists():
        try:
            for it in json.loads(alvo.read_text(encoding="utf-8")).get("itens", []):
                anterior[chave(it)] = it
        except (ValueError, OSError):
            anterior = {}

    novos = 0
    for it in dados.get("itens", []):
        k = chave(it)
        if k not in anterior:
            anterior[k] = it
            novos += 1

    itens = sorted(anterior.values(), key=lambda i: i.get("publicado_em") or "", reverse=True)
    saida = {
        "esquema": "instantaneo-diario/1",
        "dia": dia.isoformat(),
        "semana_iso": semana_iso(dia),
        "atualizado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "coletas_no_dia": 1 if not alvo.exists() else None,
        "fontes_consultadas": dados.get("fontes_consultadas"),
        "fontes_com_falha": dados.get("fontes_com_falha", []),
        "total": len(itens),
        "no_brasil": sum(1 for i in itens if i.get("escopo") == "br"),
        "no_mundo": sum(1 for i in itens if i.get("escopo") != "br"),
        "itens": itens,
    }
    saida.pop("coletas_no_dia")
    alvo.write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return alvo, novos, len(itens)


def poda(dir_hist=HIST, dias=RETENCAO_DIAS):
    limite = date.today() - timedelta(days=dias)
    removidos = []
    for f in dir_hist.glob("????-??-??.json"):
        try:
            if date.fromisoformat(f.stem) < limite:
                f.unlink()
                removidos.append(f.name)
        except ValueError:
            continue
    return removidos


def reconstroi_indice(dir_hist=HIST):
    """Indice enxuto: contagem por dia e por semana, sem repetir as manchetes."""
    dias, semanas = [], {}
    for f in sorted(dir_hist.glob("????-??-??.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        reg = {
            "dia": d.get("dia") or f.stem,
            "semana_iso": d.get("semana_iso"),
            "total": d.get("total", 0),
            "no_brasil": d.get("no_brasil", 0),
            "no_mundo": d.get("no_mundo", 0),
            "fontes_com_falha": len(d.get("fontes_com_falha") or []),
            "arquivo": f.name,
        }
        dias.append(reg)
        s = semanas.setdefault(reg["semana_iso"], {
            "semana_iso": reg["semana_iso"], "dias": 0,
            "total": 0, "no_brasil": 0, "no_mundo": 0,
            "primeiro_dia": reg["dia"], "ultimo_dia": reg["dia"],
        })
        s["dias"] += 1
        s["total"] += reg["total"]
        s["no_brasil"] += reg["no_brasil"]
        s["no_mundo"] += reg["no_mundo"]
        s["primeiro_dia"] = min(s["primeiro_dia"], reg["dia"])
        s["ultimo_dia"] = max(s["ultimo_dia"], reg["dia"])

    indice = {
        "esquema": "indice-historico/1",
        "atualizado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "aviso": ("Contagem de manchetes agregadas por dia, nao de incidentes. "
                  "Mede cobertura de imprensa e alcance das fontes monitoradas, "
                  "nao incidencia do fenomeno."),
        "primeiro_dia": dias[0]["dia"] if dias else None,
        "ultimo_dia": dias[-1]["dia"] if dias else None,
        "dias_com_registro": len(dias),
        "dias": dias,
        "semanas": [semanas[k] for k in sorted(semanas)],
    }
    alvo = dir_hist / "indice.json"
    alvo.write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return alvo, len(dias), len(semanas)


def main():
    origem = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "data" / "noticias.json"
    if not origem.exists():
        print(f"{origem}: ausente. A coleta falhou ou nao rodou; historico intacto.")
        return 0
    dados = json.loads(origem.read_text(encoding="utf-8"))
    alvo, novos, total = grava_instantaneo(dados)
    removidos = poda()
    idx, ndias, nsem = reconstroi_indice()
    print(f"{alvo.name}: {novos} novos, {total} no dia")
    if removidos:
        print(f"  podados por retencao: {len(removidos)}")
    print(f"{idx.name}: {ndias} dias, {nsem} semanas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
