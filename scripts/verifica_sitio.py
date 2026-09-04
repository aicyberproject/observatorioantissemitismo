#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a integridade estrutural do sitio antes de publicar.

Existe por causa de um defeito que ficou no ar: oito itens de menu apontando
para ancoras que nao existiam nas paginas onde estavam. Nenhum teste pegaria
isso, porque nao havia teste. Estas cinco conferencias sao baratas e pegam a
classe inteira.

    python3 scripts/verifica_sitio.py

Devolve 0 se tudo passa e 1 na primeira falha, com o arquivo e o alvo. Nao
esta ligado ao deploy: os passos do workflow sao tolerantes a erro de proposito,
para que uma falha de coleta nao derrube a publicacao, e mudar isso e decisao
de coordenacao. Rode a mao antes de publicar.
"""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
IGNORA = {"preview", ".firecrawl", ".git", "node_modules", "__pycache__"}

RE_HREF = re.compile(r'href="([^"]+)"')
RE_SRC = re.compile(r'src="([^"]+)"')
RE_ID = re.compile(r'\bid="([^"]+)"')
RE_NAME = re.compile(r'\bname="([^"]+)"')
RE_MENU = re.compile(
    r'<nav class="wrap nav" aria-label="Navega&ccedil;&atilde;o principal">(.*?)</nav>',
    re.S)
RE_ROTULO = re.compile(r'>([^<>]*)</a>')


def paginas():
    for p in sorted(RAIZ.rglob("*.html")):
        if any(parte in IGNORA for parte in p.relative_to(RAIZ).parts):
            continue
        yield p


def externo(alvo):
    return alvo.startswith(("http://", "https://", "mailto:", "tel:", "data:", "//"))


def main():
    falhas = []
    docs = {p: p.read_text(encoding="utf-8") for p in paginas()}
    ids = {p: set(RE_ID.findall(t)) | set(RE_NAME.findall(t)) for p, t in docs.items()}
    menus = {}

    for p, t in docs.items():
        rel = p.relative_to(RAIZ)

        # 1. links locais resolvem em arquivo existente
        # 2. ancoras existem na pagina de destino
        for alvo in set(RE_HREF.findall(t)):
            if externo(alvo) or not alvo:
                continue
            arq, _, frag = alvo.partition("#")
            destino = p if not arq else (p.parent / arq).resolve()
            if arq:
                if not destino.exists():
                    falhas.append(f"link quebrado      {rel} -> {alvo}")
                    continue
            if frag and destino in ids:
                if frag not in ids[destino]:
                    falhas.append(f"ancora inexistente {rel} -> {alvo}")

        # 3. ativos referenciados existem
        for alvo in set(RE_SRC.findall(t)):
            if externo(alvo) or not alvo:
                continue
            if not (p.parent / alvo).exists():
                falhas.append(f"ativo ausente      {rel} -> {alvo}")

        # 4. o menu principal e o mesmo em toda parte, nos rotulos e na ordem
        m = RE_MENU.search(t)
        if not m:
            falhas.append(f"sem menu principal {rel}")
        else:
            menus[rel] = tuple(RE_ROTULO.findall(m.group(1)))

    # 5. nenhuma pagina fica orfa. Uma pagina publicada que nenhuma outra
    #    aponta so e alcancavel por quem ja sabe o endereco, o que e a mesma
    #    classe de defeito de um item de menu sem destino. Esta conferencia
    #    entrou depois de o glossario ter sido publicado orfao e as quatro
    #    conferencias acima passarem sem notar.
    apontadas = set()
    for p, texto in docs.items():
        for alvo in set(RE_HREF.findall(texto)):
            if externo(alvo) or not alvo:
                continue
            arq = alvo.partition("#")[0]
            if not arq:
                continue
            destino = (p.parent / arq).resolve()
            if destino != p and destino in docs:
                apontadas.add(destino)
    for p in sorted(docs):
        if p not in apontadas and p.name != "index.html":
            falhas.append(f"pagina orfa        {p.relative_to(RAIZ)}: nenhuma outra pagina a aponta")

    if menus:
        comum = max(set(menus.values()), key=lambda k: list(menus.values()).count(k))
        for rel, rotulos in sorted(menus.items()):
            if rotulos != comum:
                faltam = set(comum) - set(rotulos)
                sobram = set(rotulos) - set(comum)
                detalhe = []
                if faltam:
                    detalhe.append("faltam " + ", ".join(sorted(faltam)))
                if sobram:
                    detalhe.append("sobram " + ", ".join(sorted(sobram)))
                falhas.append(f"menu divergente    {rel}: " + "; ".join(detalhe or ["ordem diferente"]))

    print(f"paginas conferidas: {len(docs)}")
    if falhas:
        print(f"FALHAS: {len(falhas)}")
        for f in falhas:
            print("  " + f)
        return 1
    print("links locais, ancoras, ativos, menu e alcancabilidade: tudo consistente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
