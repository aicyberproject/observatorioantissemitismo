#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a serie editorial semanal em serie/: indice e uma pagina por perfil.

Uma pagina por semana, com endereco proprio, para que cada perfil possa ser
citado e compartilhado isoladamente. A ordem vai do caso brasileiro ao
instrumento juridico universal, fechando na institucionalizacao, que e o que um
observatorio faz.

    python3 scripts/gerar_serie.py
"""
import html
import pathlib
import sys
from datetime import date, timedelta

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "serie"
BASE = "https://aicyberproject.github.io/observatorioantissemitismo"
INICIO = date(2026, 9, 7)          # segunda-feira da semana 1

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from serie_dados import PERFIS, PENDENTES  # noqa: E402
from gerar_paginas import FAIXA, ATUALIZADO  # noqa: E402

E = lambda s: html.escape(str(s or ""), quote=True)
MES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
       "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

MENU = [
 ("index.html#painel", "Painel"), ("indicadores.html", "Indicadores"),
 ("boletim/index.html", "Boletim"), ("index.html#preservar", "Preservar evid&ecirc;ncias"),
 ("index.html#denuncie", "Denunciar"), ("index.html#legislacao", "Legisla&ccedil;&atilde;o"),
 ("serie/index.html", "S&eacute;rie"), ("acervo.html", "Acervos"),
 ("biblioteca.html", "Biblioteca"), ("sobre.html", "Sobre"),
]


def semana_de(n):
    d = INICIO + timedelta(weeks=n - 1)
    f = d + timedelta(days=6)
    if d.month == f.month:
        return f"{d.day} a {f.day} de {MES[d.month-1]} de {d.year}"
    return f"{d.day} de {MES[d.month-1]} a {f.day} de {MES[f.month-1]} de {f.year}"


def cabeca(titulo, descricao, canonico):
    itens = []
    for h, r in MENU:
        # os caminhos sao relativos a serie/: o proprio indice da serie fica local
        alvo = "index.html" if h == "serie/index.html" else "../" + h
        atual = ' aria-current="page"' if h == "serie/index.html" else ""
        itens.append(f'<a href="{alvo}"{atual}>{r}</a>')
    menu = "".join(itens)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="status" content="prototipo">
<title>{titulo} &middot; Prot&oacute;tipo do Observat&oacute;rio</title>
<meta name="description" content="{E(descricao)}">
<meta name="author" content="Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento">
<meta name="theme-color" content="#F5F3EF">
<meta property="og:type" content="article">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Prot&oacute;tipo &middot; Observat&oacute;rio do Antissemitismo no Brasil">
<meta property="og:title" content="{titulo}">
<link rel="canonical" href="{canonico}">
<link rel="alternate" type="application/rss+xml" title="Boletim do Observat&oacute;rio" href="../boletim/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Work+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/main.css">
<link rel="stylesheet" href="../css/indicadores.css">
</head>
<body>
{FAIXA}
<a class="skip" href="#topo">Pular para o conte&uacute;do</a>
<header class="header">
  <div class="wrap header-top">
    <a class="brand" href="../index.html#topo">
      <span class="brand-mark" aria-hidden="true"></span>
      <span>
        <span class="brand-name">Observat&oacute;rio do Antissemitismo</span>
        <span class="brand-sub">Prot&oacute;tipo &middot; Eixo 3, Seguran&ccedil;a e Monitoramento</span>
      </span>
    </a>
    <div class="header-actions">
      <a class="btn-solid" href="../index.html#denuncie">Denunciar</a>
    </div>
  </div>
  <nav class="wrap nav" aria-label="Navega&ccedil;&atilde;o principal">{menu}</nav>
</header>
<main>
"""


RODAPE = """</main>
<footer class="footer">
  <div class="wrap footer-inner">
    <div class="footer-cols">
      <div>
        <p class="footer-brand">Observat&oacute;rio do Antissemitismo</p>
        <p class="footer-text">Quem enfrentou o antissemitismo. S&eacute;rie semanal, com fonte p&uacute;blica conferida em cada perfil.</p>
        <p class="footer-org">Prot&oacute;tipo em elabora&ccedil;&atilde;o no Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento, no &acirc;mbito da Iniciativa de Enfrentamento ao Antissemitismo. Documento de trabalho, sem car&aacute;ter oficial e sem valida&ccedil;&atilde;o do CDESS ou da Presid&ecirc;ncia da Rep&uacute;blica.</p>
      </div>
      <div>
        <p class="footer-head">Navega&ccedil;&atilde;o</p>
        <nav><a href="../index.html#topo">In&iacute;cio</a><a href="index.html">S&eacute;rie</a><a href="../acervo.html">Acervos e mem&oacute;ria</a><a href="../indicadores.html">Indicadores</a><a href="../boletim/index.html">Boletim</a><a href="../biblioteca.html">Biblioteca</a></nav>
      </div>
      <div>
        <p class="footer-head">Institucional</p>
        <nav><a href="../sobre.html">Sobre o Observat&oacute;rio</a><a href="index.html">S&eacute;rie: quem enfrentou</a><a href="../acervo.html">Acervos e mem&oacute;ria</a><a href="../metodologia.html">Metodologia</a><a href="../taxonomia.html">Taxonomia proposta</a><a href="../privacidade.html">Pol&iacute;tica de privacidade</a><a href="../termos.html">Termos de uso</a><a href="../boletim/feed.xml">Feed RSS</a></nav>
      </div>
    </div>
    <p class="footer-legal">&copy; 2026 Observat&oacute;rio do Antissemitismo no Brasil &middot; Prot&oacute;tipo, vers&atilde;o de trabalho &middot; C&oacute;digo e conte&uacute;do sob licen&ccedil;a MIT</p>
  </div>
</footer>
</body>
</html>
"""


def perfil(p, ant, seg):
    nav = []
    if ant:
        nav.append(f'<a href="{ant["id"]}.html">&larr; Semana {ant["n"]}</a>')
    nav.append('<a href="index.html">Todas as edi&ccedil;&otilde;es</a>')
    if seg:
        nav.append(f'<a href="{seg["id"]}.html">Semana {seg["n"]} &rarr;</a>')
    fontes = "".join(
        f'<li><a href="{E(u)}" target="_blank" rel="noopener">{n}'
        f'<span class="sr-only"> (abre em nova aba, no site de origem)</span></a></li>'
        for n, u in p["fontes"])
    diverg = ""
    if p["diverg"]:
        diverg = (f'<div class="ser-diverg"><p class="label">O que n&atilde;o se confirmou</p>'
                  f'<p class="body">{p["diverg"]}</p></div>')
    corpo = "".join(f'<p class="body">{x}</p>' for x in p["corpo"])
    return cabeca(
        f'{p["nome"]} &middot; semana {p["n"]}',
        f'{p["nome"]}: {p["chamada"]}',
        f'{BASE}/serie/{p["id"]}.html'
    ) + f"""<section class="wrap" id="topo" style="padding-top: clamp(40px, 5vw, 68px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="../index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; <a href="index.html">S&eacute;rie</a> &nbsp;/&nbsp; Semana {p["n"]}</p>
  <p class="ser-bloco">{p["bloco"]}</p>
  <h1 class="h1" style="margin-top: 16px">{p["nome"]}</h1>
  <p class="ser-vida">{p["vida"]} &middot; {p["nac"]}</p>
  <p class="lead" style="margin: 22px 0 0; max-width: 68ch">{p["chamada"]}</p>
</section>
<section class="wrap section" style="padding-top: clamp(20px, 3vw, 34px)">
  <div class="ser-corpo">{corpo}</div>
  <div class="ser-importa">
    <p class="label">Por que importa hoje</p>
    <p class="body">{p["importa"]}</p>
  </div>
  {diverg}
  <div class="ser-fontes">
    <p class="label">Fontes, conferidas em {ATUALIZADO}</p>
    <ol>{fontes}</ol>
  </div>
  <p class="bol-nav">{" &nbsp;&middot;&nbsp; ".join(nav)}</p>
</section>
""" + RODAPE


def indice():
    linhas = []
    for p in PERFIS:
        linhas.append(
            f'<li class="ser-item"><a href="{p["id"]}.html">'
            f'<span class="ser-n">Semana {p["n"]:02d}</span>'
            f'<span class="ser-meio"><span class="ser-nome">{p["nome"]}</span>'
            f'<span class="ser-chamada">{p["chamada"]}</span></span>'
            f'<span class="ser-quando">{semana_de(p["n"])}</span></a></li>')
    pend = "".join(f'<div class="repr-item"><h3 class="repr-nome">{n}</h3>'
                   f'<p class="body">{m}</p></div>' for n, m in PENDENTES)
    return cabeca(
        "Quem enfrentou o antissemitismo",
        "Serie semanal de perfis, com fonte publica conferida em cada um. Comeca pelos brasileiros.",
        f"{BASE}/serie/"
    ) + f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="../index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; S&eacute;rie</p>
  <h1 class="h1" style="margin-top: 24px">Quem enfrentou o antissemitismo</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Um perfil por semana, ao longo de dezesseis semanas. Come&ccedil;a pelos brasileiros, porque s&atilde;o os menos divulgados e os mais pr&oacute;ximos.</p>
  <p class="body" style="margin: 18px 0 0; max-width: 70ch">O arco vai do caso brasileiro ao instrumento jur&iacute;dico universal, e fecha na institucionaliza&ccedil;&atilde;o, que &eacute; o que um observat&oacute;rio faz. Cada perfil tem endere&ccedil;o pr&oacute;prio, para poder ser citado isoladamente.</p>
</section>

<section class="band"><div class="wrap section">
  <p class="eyebrow">Como esta s&eacute;rie foi feita</p>
  <h2 class="h2" style="max-width: 34ch">Fato muito repetido n&atilde;o &eacute; fato verificado</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">Cada perfil declara as fontes p&uacute;blicas conferidas. Onde a fonte prim&aacute;ria <strong>n&atilde;o confirma</strong> um dado de ampla circula&ccedil;&atilde;o, a diverg&ecirc;ncia fica registrada em vez de resolvida por escolha, num bloco pr&oacute;prio ao fim do texto.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Isso muda o que se l&ecirc;. N&uacute;meros de pessoas salvas, em particular, variam muito: em um caso as duas cifras divergem <em>na mesma p&aacute;gina</em> da mesma institui&ccedil;&atilde;o; em outro, a pr&oacute;pria fonte declara que o n&uacute;mero exato &eacute; desconhecido. A s&eacute;rie prefere registrar isso a escolher o n&uacute;mero mais impressionante.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">A <a href="verificacao-winton.html">semana 9</a> &eacute; inteiramente dedicada a um caso em que um fato de altíssima circula&ccedil;&atilde;o n&atilde;o se confirmou na institui&ccedil;&atilde;o que o concederia. Publicar a lacuna &eacute; mais &uacute;til que preench&ecirc;-la com o que circula.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">A s&eacute;rie n&atilde;o inclui perfil de pessoa cuja atua&ccedil;&atilde;o seja objeto de disputa pol&iacute;tica corrente no Brasil, e em dois casos recortou o escopo por essa raz&atilde;o, dizendo-o expressamente. O Observat&oacute;rio declara n&atilde;o emitir opini&atilde;o editorial nem carregar posi&ccedil;&atilde;o pol&iacute;tico-partid&aacute;ria.</p>
</div></section>

<section class="wrap section">
  <h2 class="h2" style="max-width: 30ch">As dezesseis edi&ccedil;&otilde;es</h2>
  <ol class="ser-lista">{"".join(linhas)}</ol>
</section>

<section class="band"><div class="wrap section">
  <h2 class="h2" style="max-width: 32ch">O que ficou de fora, e por qu&ecirc;</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">Tr&ecirc;s itens previstos n&atilde;o entraram. Registrar isso &eacute; parte do m&eacute;todo: perfil sem fonte prim&aacute;ria aberta n&atilde;o se publica.</p>
  <div class="repr-lista">{pend}</div>
</div></section>
""" + RODAPE


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    for i, p in enumerate(PERFIS):
        ant = PERFIS[i - 1] if i else None
        seg = PERFIS[i + 1] if i + 1 < len(PERFIS) else None
        (SAIDA / f'{p["id"]}.html').write_text(perfil(p, ant, seg), encoding="utf-8")
    (SAIDA / "index.html").write_text(indice(), encoding="utf-8")
    print(f"serie: {len(PERFIS)} perfis e indice gravados em {SAIDA.name}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
