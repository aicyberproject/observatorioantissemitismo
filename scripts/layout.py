#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fonte de verdade unica do cabecalho, do menu e do rodape do sitio.

Antes deste modulo havia cinco definicoes independentes de navegacao:
gerar_paginas.py, gerar_indicadores.py, gerar_serie.py, gerar_boletim.py e
index.html, este ultimo mantido a mao. A consequencia foi registrada na
auditoria: oito itens de menu apontando para ancoras inexistentes em duas
paginas, e rodapes que divergiam entre si, de modo que da pagina de acervos
nao se alcancava a serie e da serie nao se alcancava a legislacao.

A correcao de uma copia nao alcancava as outras. Por isso a lista de itens
passa a viver aqui, e cada gerador a consome.

CAMINHOS. Todos os destinos abaixo sao declarados relativos a RAIZ do sitio.
A funcao caminho() os reescreve relativos ao diretorio da pagina que esta
sendo gerada, o que resolve de uma vez os tres casos que antes eram feitos a
mao em cada gerador: pagina na raiz, pagina em subdiretorio, e link para a
propria pagina ou para um vizinho no mesmo subdiretorio.

    python3 scripts/layout.py        # autoteste dos caminhos
"""
import posixpath

BASE = "https://aicyberproject.github.io/observatorioantissemitismo"
ATUALIZADO = "4 de setembro de 2026"

# Endereco de contato e errata. Working address do prototipo, em dominio
# pessoal: nao e canal institucional, e a pagina de contato diz isso.
CONTATO = "observatorio@steniosantos.com"

FAIXA = """<div class="proto-bar" role="note">
  <div class="wrap proto-inner">
    <span class="proto-tag">Prot&oacute;tipo</span>
    <p class="proto-text">Vers&atilde;o de trabalho, sem car&aacute;ter oficial. Em elabora&ccedil;&atilde;o no Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento, ainda n&atilde;o apreciada pelo Eixo nem pela reuni&atilde;o de coordenadores. N&atilde;o representa posi&ccedil;&atilde;o do CDESS, da Presid&ecirc;ncia da Rep&uacute;blica ou de qualquer &oacute;rg&atilde;o citado.</p>
  </div>
</div>"""

# ---------------------------------------------------------------------------
# Listas canonicas
# ---------------------------------------------------------------------------

# Menu principal. Dez itens, na ordem em que Preservar vem antes de Denunciar,
# conforme a secao 3.1 da auditoria.
MENU_ITENS = [
    ("index.html#painel",     "Painel"),
    ("indicadores.html",      "Indicadores"),
    ("boletim/index.html",    "Boletim"),
    ("preservar.html",        "Preservar evid&ecirc;ncias"),
    ("index.html#denuncie",   "Denunciar"),
    ("index.html#legislacao", "Legisla&ccedil;&atilde;o"),
    ("serie/index.html",      "S&eacute;rie"),
    ("acervo.html",           "Acervos"),
    ("biblioteca.html",       "Biblioteca"),
    ("sobre.html",            "Sobre"),
]

# Rodape, coluna Navegacao. Uniao das quatro versoes que existiam, para que
# nenhuma pagina perca caminho que tinha.
RODAPE_NAV = [
    ("index.html#topo",       "In&iacute;cio"),
    ("index.html#painel",     "Painel"),
    ("indicadores.html",      "Indicadores"),
    ("boletim/index.html",    "Boletim"),
    ("preservar.html",        "Preservar evid&ecirc;ncias"),
    ("index.html#denuncie",   "Denunciar"),
    ("index.html#legislacao", "Legisla&ccedil;&atilde;o"),
    ("biblioteca.html",       "Biblioteca"),
]

# Rodape, coluna Institucional. Tambem uniao. "Dados abertos" aponta para a
# ancora #dados de indicadores.html, conferida existente.
RODAPE_INST = [
    ("sobre.html",            "Sobre o Observat&oacute;rio"),
    ("serie/index.html",      "S&eacute;rie: quem enfrentou"),
    ("acervo.html",           "Acervos e mem&oacute;ria"),
    ("metodologia.html",      "Metodologia"),
    ("taxonomia.html",        "Taxonomia proposta"),
    ("glossario.html",        "Gloss&aacute;rio"),
    ("contato.html",          "Contato e errata"),
    ("privacidade.html",      "Pol&iacute;tica de privacidade"),
    ("termos.html",           "Termos de uso"),
    ("boletim/feed.xml",      "Feed RSS"),
    ("indicadores.html#dados", "Dados abertos"),
]

# Itens de rodape que existem so em uma pagina, porque apontam para secoes
# dela. Preservados para que a unificacao nao remova caminho de ninguem.
RODAPE_EXTRA = {
    "index.html": [
        ("index.html#organizacao", "Como est&aacute; organizado"),
        ("index.html#escopo",      "Escopo"),
        ("index.html#sobre",       "Sobre"),
    ],
}

# Texto de apresentacao do rodape. Varia por secao, de proposito.
TEXTO_PADRAO = "Plataforma p&uacute;blica de monitoramento de incidentes, orienta&ccedil;&atilde;o jur&iacute;dica, canais de den&uacute;ncia e preserva&ccedil;&atilde;o de provas."

ORG = "Prot&oacute;tipo em elabora&ccedil;&atilde;o no Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento, no &acirc;mbito da Iniciativa de Enfrentamento ao Antissemitismo. Documento de trabalho, sem car&aacute;ter oficial e sem valida&ccedil;&atilde;o do CDESS ou da Presid&ecirc;ncia da Rep&uacute;blica."

LEGAL = "&copy; 2026 Observat&oacute;rio do Antissemitismo no Brasil &middot; Prot&oacute;tipo, vers&atilde;o de trabalho &middot; C&oacute;digo e conte&uacute;do sob licen&ccedil;a MIT"


# ---------------------------------------------------------------------------
# Caminhos
# ---------------------------------------------------------------------------

def caminho(destino, pagina):
    """Reescreve um destino declarado a partir da raiz como caminho relativo
    ao diretorio de `pagina`.

    Os dois argumentos sao caminhos a partir da raiz do sitio, por exemplo
    "index.html#painel" e "serie/primo-levi.html".

    Link para a propria pagina com fragmento devolve so o fragmento, que e o
    que faz o navegador rolar em vez de recarregar.
    """
    alvo, sep, frag = destino.partition("#")
    frag = (sep + frag) if sep else ""
    if alvo == pagina:
        return frag or posixpath.basename(alvo)
    rel = posixpath.relpath(alvo, posixpath.dirname(pagina) or ".")
    return rel + frag


def _links(itens, pagina, atual=""):
    saida = []
    for destino, rotulo in itens:
        marca = ' aria-current="page"' if destino == atual else ""
        saida.append(f'<a href="{caminho(destino, pagina)}"{marca}>{rotulo}</a>')
    return "".join(saida)


def MENU(pagina, atual=""):
    """Menu principal, com a posicao corrente marcada quando `atual` casa com
    um destino da lista."""
    return _links(MENU_ITENS, pagina, atual)


def CABECALHO(pagina, atual=""):
    """Faixa de prototipo, atalho de acessibilidade, marca e menu."""
    return f"""{FAIXA}
<a class="skip" href="#topo">Pular para o conte&uacute;do</a>
<header class="header">
  <div class="wrap header-top">
    <a class="brand" href="{caminho('index.html#topo', pagina)}">
      <span class="brand-mark" aria-hidden="true"></span>
      <span>
        <span class="brand-name">Observat&oacute;rio do Antissemitismo</span>
        <span class="brand-sub">Prot&oacute;tipo &middot; Eixo 3, Seguran&ccedil;a e Monitoramento</span>
      </span>
    </a>
    <div class="header-actions">
      <a class="btn-solid" href="{caminho('index.html#denuncie', pagina)}">Denunciar</a>
    </div>
  </div>
  <nav class="wrap nav" aria-label="Navega&ccedil;&atilde;o principal">{MENU(pagina, atual)}</nav>
</header>"""


def RODAPE(pagina, texto=None, lgpd=True, app=True, scripts=()):
    """Rodape completo.

    `lgpd` e `app` seguem parametrizados, mas hoje toda pagina do sitio usa os
    dois. As paginas de serie e de boletim nao os carregavam, e o efeito era
    que dezoito das vinte e nove paginas nao exibiam aviso de LGPD nenhum.

    js/app.js e defensivo: cada acesso ao DOM e guardado, ha ramo proprio para
    "paginas internas nao tem abertura", e a busca do painel so ocorre onde o
    painel existe. Rodar em pagina interna nao tem efeito alem de medir a faixa
    de prototipo e exibir o aviso.
    """
    nav = RODAPE_NAV + RODAPE_EXTRA.get(pagina, [])
    aviso = ""
    if lgpd:
        aviso = f"""
<div class="lgpd" id="lgpd" hidden>
  <div class="wrap lgpd-inner">
    <div class="lgpd-text">
      <p class="eyebrow">Prote&ccedil;&atilde;o de dados &middot; LGPD</p>
      <p>Este portal n&atilde;o usa cookie de rastreamento, n&atilde;o coleta endere&ccedil;o de e-mail e n&atilde;o pede dado pessoal. Guarda apenas prefer&ecirc;ncia de exibi&ccedil;&atilde;o no seu pr&oacute;prio navegador. <a href="{caminho('privacidade.html', pagina)}">Leia a pol&iacute;tica de privacidade</a>.</p>
    </div>
    <button class="btn-ink" id="lgpd-ok" type="button">Entendido</button>
  </div>
</div>"""
    script = ""
    if app:
        script = f'\n<script src="{caminho("js/app.js", pagina)}" defer></script>'
    for s in scripts:
        script += f'\n<script src="{caminho(s, pagina)}" defer></script>'
    return f"""</main>
<footer class="footer">
  <div class="wrap footer-inner">
    <div class="footer-cols">
      <div>
        <p class="footer-brand">Observat&oacute;rio do Antissemitismo</p>
        <p class="footer-text">{texto or TEXTO_PADRAO}</p>
        <p class="footer-org">{ORG}</p>
      </div>
      <div>
        <p class="footer-head">Navega&ccedil;&atilde;o</p>
        <nav>{_links(nav, pagina)}</nav>
      </div>
      <div>
        <p class="footer-head">Institucional</p>
        <nav>{_links(RODAPE_INST, pagina)}</nav>
      </div>
    </div>
    <p class="footer-legal">{LEGAL}</p>
  </div>
</footer>{aviso}{script}
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Autoteste dos caminhos
# ---------------------------------------------------------------------------

def _autoteste():
    casos = [
        # (destino, pagina, esperado)
        ("index.html#painel",      "index.html",             "#painel"),
        ("index.html#painel",      "indicadores.html",       "index.html#painel"),
        ("index.html#painel",      "serie/primo-levi.html",  "../index.html#painel"),
        ("index.html#painel",      "boletim/index.html",     "../index.html#painel"),
        ("serie/index.html",       "serie/index.html",       "index.html"),
        ("serie/index.html",       "serie/primo-levi.html",  "index.html"),
        ("serie/index.html",       "index.html",             "serie/index.html"),
        ("boletim/feed.xml",       "boletim/index.html",     "feed.xml"),
        ("boletim/feed.xml",       "index.html",             "boletim/feed.xml"),
        ("boletim/feed.xml",       "serie/index.html",       "../boletim/feed.xml"),
        ("indicadores.html#dados", "boletim/2026-S36.html",  "../indicadores.html#dados"),
        ("js/app.js",              "index.html",             "js/app.js"),
        ("js/app.js",              "serie/primo-levi.html",  "../js/app.js"),
        ("contato.html",           "serie/index.html",       "../contato.html"),
    ]
    falhas = 0
    for destino, pagina, esperado in casos:
        obtido = caminho(destino, pagina)
        if obtido != esperado:
            falhas += 1
            print(f"FALHA  {destino!r} em {pagina!r}: esperava {esperado!r}, obtive {obtido!r}")
    print(f"autoteste de caminhos: {len(casos) - falhas}/{len(casos)} ok")
    return falhas


if __name__ == "__main__":
    import sys
    sys.exit(1 if _autoteste() else 0)
