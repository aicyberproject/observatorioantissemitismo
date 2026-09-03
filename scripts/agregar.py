#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le os feeds de data/feeds.json e escreve data/noticias.json.

Roda no build do GitHub Pages. Nao grava nada no repositorio: o arquivo de
saida entra apenas no artefato publicado. Falha de uma fonte nao derruba a
coleta; o que foi obtido e publicado, e o que faltou fica registrado.

    python3 scripts/agregar.py [caminho_de_saida]
"""
import json, pathlib, re, sys, unicodedata
import urllib.request, urllib.error
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

RAIZ = pathlib.Path(__file__).resolve().parent.parent
UA = ("Mozilla/5.0 (compatible; ObservatorioAntissemitismo/1.0; "
      "+https://aicyberproject.github.io/observatorioantissemitismo/)")
TEMPO_LIMITE = 25
MAX_ITENS = 90
MAX_POR_FONTE = 6

# Os sete radares ja sao consultas por palavra-chave, e o feed do CAM cobre
# exclusivamente antissemitismo: entram sem filtro. Todos os demais publicam
# alem do recorte deste Observatorio e passam pelo filtro de termos.
SEM_FILTRO = {"cam"}

TERMOS = [
    "antissemit", "antisemit", "judeu", "judia", "judaic", "judaism", "jewish",
    "holocausto", "holocaust", "shoah", "nazi", "suastica", "swastika",
    "sinagoga", "synagogue", "ihra", "kipa", "israelita",
    "racismo religioso", "intolerancia religiosa", "religious intolerance",
    "crime de odio", "crimes de odio", "discurso de odio", "hate crime",
    "hate speech", "xenofob", "islamofob", "islamophob", "7.716", "ellwanger",
]

NS = {"atom": "http://www.w3.org/2005/Atom",
      "dc": "http://purl.org/dc/elements/1.1/",
      "content": "http://purl.org/rss/1.0/modules/content/"}


def sem_acento(t):
    t = unicodedata.normalize("NFD", t or "")
    return "".join(c for c in t if unicodedata.category(c) != "Mn").lower()


def pertinente(texto):
    n = sem_acento(texto)
    return any(termo in n for termo in TERMOS)


def baixar(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
    })
    with urllib.request.urlopen(req, timeout=TEMPO_LIMITE) as r:
        return r.read()


def texto(el):
    if el is None:
        return ""
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


def quando(bruto):
    if not bruto:
        return None
    bruto = bruto.strip()
    try:
        d = parsedate_to_datetime(bruto)
    except (TypeError, ValueError, IndexError):
        try:
            d = datetime.fromisoformat(bruto.replace("Z", "+00:00"))
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc)


def ler_rss(raiz):
    for it in raiz.iter("item"):
        fonte_el = it.find("source")
        yield {
            "titulo": texto(it.find("title")),
            "link": texto(it.find("link")),
            "data": quando(texto(it.find("pubDate")) or texto(it.find("dc:date", NS))),
            "veiculo": texto(fonte_el) if fonte_el is not None else "",
            "veiculo_url": (fonte_el.get("url") or "") if fonte_el is not None else "",
        }


def ler_atom(raiz):
    for e in raiz.iter("{http://www.w3.org/2005/Atom}entry"):
        link = ""
        for l in e.findall("atom:link", NS):
            if l.get("rel") in (None, "alternate"):
                link = l.get("href") or ""
                break
        yield {
            "titulo": texto(e.find("atom:title", NS)),
            "link": link,
            "data": quando(texto(e.find("atom:published", NS)) or texto(e.find("atom:updated", NS))),
            "veiculo": "",
            "veiculo_url": "",
        }


def chave(link, titulo):
    l = re.sub(r"[?#].*$", "", (link or "").lower()).rstrip("/")
    return l or sem_acento(titulo)[:90]


def coletar(fonte, categoria):
    fid, nome, url = fonte["id"], fonte["nome"], fonte["url"]
    radar = fonte.get("tipo") == "radar_de_busca"
    escopo = "br" if fonte.get("idioma") == "PT" and fonte.get("escopo") in ("Nacional",) else "mundo"
    if fid == "onu-pt":
        escopo = "mundo"
    saida, erro = [], None
    try:
        raiz = ET.fromstring(baixar(url))
    except Exception as e:                                  # noqa: BLE001
        return [], f"{nome}: {type(e).__name__}"
    itens = list(ler_rss(raiz)) or list(ler_atom(raiz))
    for it in itens:
        if not it["titulo"] or not it["link"]:
            continue
        if not (radar or fid in SEM_FILTRO) and not pertinente(it["titulo"]):
            continue
        if it["titulo"].lower().startswith(("http://", "https://")):
            continue
        veiculo = it["veiculo"] or nome
        if radar:
            # O Google Noticias entrega o titulo como "Manchete - Veiculo". O
            # sufixo pode conter hifen no proprio nome do veiculo, e por isso a
            # remocao por padrao generico falha. Primeiro tenta casar o nome do
            # veiculo declarado no <source>, que e o caso exato.
            bruto = it["titulo"]
            if veiculo:
                alvo = sem_acento(veiculo)
                nu = sem_acento(bruto)
                pos = nu.rfind(" - " + alvo)
                if pos > 0 and pos + 3 + len(alvo) == len(nu):
                    bruto = bruto[:pos].strip()
            t = re.sub(r"\s+-\s+[^-]{2,40}$", "", bruto).strip()
            it["titulo"] = t or bruto or it["titulo"]
        saida.append({
            "titulo": it["titulo"][:220],
            "link": it["link"],
            "fonte": veiculo[:60],
            "escopo": escopo,
            "publicado_em": it["data"].isoformat() if it["data"] else None,
            "via": "Google Notícias" if radar else None,
            "feed": fid,
            "categoria": categoria,
        })
        if len(saida) >= MAX_POR_FONTE:
            break
    return saida, erro


def main():
    destino = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "data" / "noticias.json"
    catalogo = json.loads((RAIZ / "data" / "feeds.json").read_text(encoding="utf-8"))
    tarefas = [(f, c["nome"]) for c in catalogo["categorias"] for f in c["fontes"]]

    with ThreadPoolExecutor(max_workers=8) as pool:
        resultados = list(pool.map(lambda a: coletar(*a), tarefas))

    itens, vistos, falhas = [], set(), []
    for (lista, erro) in resultados:
        if erro:
            falhas.append(erro)
        for it in lista:
            k = chave(it["link"], it["titulo"])
            kt = sem_acento(it["titulo"])[:70]
            if k in vistos or kt in vistos:
                continue
            vistos.add(k)
            vistos.add(kt)
            itens.append(it)

    itens.sort(key=lambda i: i["publicado_em"] or "", reverse=True)
    itens = itens[:MAX_ITENS]

    saida = {
        "esquema": "noticias-agregadas/1",
        "gerado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fontes_consultadas": len(tarefas),
        "fontes_com_falha": falhas,
        "total": len(itens),
        "no_brasil": sum(1 for i in itens if i["escopo"] == "br"),
        "no_mundo": sum(1 for i in itens if i["escopo"] == "mundo"),
        "itens": itens,
    }
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{destino}: {len(itens)} itens "
          f"({saida['no_brasil']} BR / {saida['no_mundo']} mundo), "
          f"{len(falhas)} falha(s) de {len(tarefas)} fontes")
    for f in falhas:
        print("  falhou:", f)


if __name__ == "__main__":
    main()
