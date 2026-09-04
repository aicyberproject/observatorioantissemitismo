#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica a navegacao canonica de layout.py em index.html e biblioteca.html.

Essas duas paginas nao sao geradas por script: index.html porque e a capa, com
conteudo e comportamento proprios, e biblioteca.html porque foi escrita a mao.
Justamente por isso eram as duas que divergiam, e foi numa delas que apareceram
quatro dos oito itens de menu sem destino apurados na auditoria.

Este script nao gera as paginas. Substitui nelas, no lugar, tres blocos:
o menu do cabecalho e os dois <nav> do rodape. O resto do arquivo nao e tocado.

    python3 scripts/sincroniza_navegacao.py            # aplica
    python3 scripts/sincroniza_navegacao.py --conferir # so verifica, nao escreve
"""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from layout import MENU, RODAPE_NAV, RODAPE_INST, RODAPE_EXTRA, _links  # noqa: E402

# pagina -> destino que deve ficar marcado como posicao corrente
PAGINAS = {
    "index.html": "index.html#painel",
    "biblioteca.html": "biblioteca.html",
}

RE_MENU = re.compile(
    r'(<nav class="wrap nav" aria-label="Navega&ccedil;&atilde;o principal">).*?(</nav>)',
    re.S)
RE_RODAPE = re.compile(
    r'(<p class="footer-head">(?:Navega&ccedil;&atilde;o|Institucional)</p>\s*\n\s*<nav>).*?(</nav>)',
    re.S)


def sincroniza(nome, atual):
    caminho = RAIZ / nome
    antes = caminho.read_text(encoding="utf-8")

    # 1. menu do cabecalho
    novo, n = RE_MENU.subn(
        lambda m: m.group(1) + MENU(nome, atual) + m.group(2), antes, count=1)
    if n != 1:
        raise SystemExit(f"{nome}: esperava 1 menu de cabecalho, achei {n}")

    # 2. os dois <nav> do rodape, na ordem em que aparecem
    nav_do_rodape = RODAPE_NAV + RODAPE_EXTRA.get(nome, [])
    listas = [nav_do_rodape, RODAPE_INST]
    contador = {"i": 0}

    def troca(m):
        i = contador["i"]
        contador["i"] += 1
        if i >= len(listas):
            raise SystemExit(f"{nome}: mais de dois <nav> de rodape")
        return m.group(1) + _links(listas[i], nome) + m.group(2)

    novo, n = RE_RODAPE.subn(troca, novo)
    if n != 2:
        raise SystemExit(f"{nome}: esperava 2 <nav> de rodape, achei {n}")

    return antes, novo


def main(conferir=False):
    divergentes = []
    for nome, atual in PAGINAS.items():
        antes, novo = sincroniza(nome, atual)
        if antes == novo:
            print(f"  {nome}: em dia")
            continue
        divergentes.append(nome)
        if conferir:
            print(f"  {nome}: DIVERGE da navegacao canonica")
        else:
            (RAIZ / nome).write_text(novo, encoding="utf-8")
            print(f"  {nome}: sincronizada")
    if conferir and divergentes:
        print(f"navegacao fora de sincronia em: {', '.join(divergentes)}")
        print("rode: python3 scripts/sincroniza_navegacao.py")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(conferir="--conferir" in sys.argv))
