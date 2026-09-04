#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as edicoes semanais do boletim a partir de data/historico/.

Uma pagina por semana ISO, um indice e um feed RSS. Tudo derivado dos
instantaneos diarios: sem historico persistido nao existe boletim, e por isso
este script roda depois de scripts/historico.py no deploy.

O boletim nao e veiculo de noticia. Cada item remete a publicacao de origem,
como no painel. A selecao e por data, sem juizo editorial: seria indevido este
prototipo escolher o que e mais relevante.

    python3 scripts/gerar_boletim.py
"""
import html
import json
import pathlib
from collections import defaultdict
from datetime import date, datetime, timezone
from email.utils import format_datetime

RAIZ = pathlib.Path(__file__).resolve().parent.parent
HIST = RAIZ / "data" / "historico"
SAIDA = RAIZ / "boletim"
BASE = "https://aicyberproject.github.io/observatorioantissemitismo"
POR_ESCOPO = 10          # itens por recorte em cada edicao
EDICOES_NO_FEED = 12

E = lambda s: html.escape(str(s or ""), quote=True)
MES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
       "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]


def por_extenso(iso):
    try:
        d = date.fromisoformat(iso)
    except (ValueError, TypeError):
        return iso or ""
    return f"{d.day} de {MES[d.month - 1]} de {d.year}"


def carrega_semanas():
    """Agrupa os instantaneos diarios por semana ISO, deduplicando por link."""
    semanas = defaultdict(lambda: {"itens": {}, "dias": set(), "falhas": set()})
    for f in sorted(HIST.glob("????-??-??.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        sem = d.get("semana_iso")
        if not sem:
            continue
        s = semanas[sem]
        s["dias"].add(d.get("dia") or f.stem)
        for nome in (d.get("fontes_com_falha") or []):
            s["falhas"].add(str(nome).split(":")[0].strip())
        for it in d.get("itens", []):
            k = (it.get("link") or it.get("titulo") or "").strip().lower()
            if k and k not in s["itens"]:
                s["itens"][k] = it
    return semanas


def cabeca(titulo, descricao, canonico, extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="status" content="prototipo">
<title>{E(titulo)}</title>
<meta name="description" content="{E(descricao)}">
<meta name="author" content="Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento">
<meta name="theme-color" content="#F5F3EF">
<link rel="canonical" href="{E(canonico)}">
<link rel="alternate" type="application/rss+xml" title="Boletim do Observat&oacute;rio" href="{BASE}/boletim/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Work+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/main.css">
<link rel="stylesheet" href="../css/indicadores.css">{extra_css}
</head>
<body>
<div class="proto-bar" role="note">
  <div class="wrap proto-inner">
    <span class="proto-tag">Prot&oacute;tipo</span>
    <p class="proto-text">Vers&atilde;o de trabalho, sem car&aacute;ter oficial. Em elabora&ccedil;&atilde;o no Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento, ainda n&atilde;o apreciada pelo Eixo nem pela reuni&atilde;o de coordenadores. N&atilde;o representa posi&ccedil;&atilde;o do CDESS, da Presid&ecirc;ncia da Rep&uacute;blica ou de qualquer &oacute;rg&atilde;o citado.</p>
  </div>
</div>
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
  <nav class="wrap nav" aria-label="Navega&ccedil;&atilde;o principal"><a href="../index.html#painel">Painel</a><a href="../indicadores.html">Indicadores</a><a href="index.html" aria-current="page">Boletim</a><a href="../index.html#preservar">Preservar evid&ecirc;ncias</a><a href="../index.html#denuncie">Denunciar</a><a href="../index.html#legislacao">Legisla&ccedil;&atilde;o</a><a href="../biblioteca.html">Biblioteca</a><a href="../sobre.html">Sobre</a></nav>
</header>
<main>
"""


RODAPE = """</main>
<footer class="footer">
  <div class="wrap footer-inner">
    <div class="footer-cols">
      <div>
        <p class="footer-brand">Observat&oacute;rio do Antissemitismo</p>
        <p class="footer-text">Boletim semanal derivado do painel de monitoramento. Cada item remete &agrave; publica&ccedil;&atilde;o de origem.</p>
        <p class="footer-org">Prot&oacute;tipo em elabora&ccedil;&atilde;o no Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento, no &acirc;mbito da Iniciativa de Enfrentamento ao Antissemitismo. Documento de trabalho, sem car&aacute;ter oficial e sem valida&ccedil;&atilde;o do CDESS ou da Presid&ecirc;ncia da Rep&uacute;blica.</p>
      </div>
      <div>
        <p class="footer-head">Navega&ccedil;&atilde;o</p>
        <nav><a href="../index.html#topo">In&iacute;cio</a><a href="../index.html#painel">Painel</a><a href="../indicadores.html">Indicadores</a><a href="index.html">Boletim</a><a href="../index.html#preservar">Preservar evid&ecirc;ncias</a><a href="../index.html#denuncie">Denunciar</a><a href="../biblioteca.html">Biblioteca</a></nav>
      </div>
      <div>
        <p class="footer-head">Institucional</p>
        <nav><a href="../sobre.html">Sobre o Observat&oacute;rio</a><a href="../privacidade.html">Pol&iacute;tica de privacidade</a><a href="../termos.html">Termos de uso</a><a href="feed.xml">Feed RSS</a><a href="../indicadores.html#dados">Dados abertos</a></nav>
      </div>
    </div>
    <p class="footer-legal">&copy; 2026 Observat&oacute;rio do Antissemitismo no Brasil &middot; Prot&oacute;tipo, vers&atilde;o de trabalho &middot; C&oacute;digo e conte&uacute;do sob licen&ccedil;a MIT</p>
  </div>
</footer>
</body>
</html>
"""


def bloco_itens(itens, rotulo):
    if not itens:
        return ""
    linhas = []
    for n in itens:
        via = (f'<span class="bol-via">via {E(n.get("via"))}</span>'
               if n.get("via") else "")
        quando = (n.get("publicado_em") or "")[:10]
        linhas.append(
            f'<li class="bol-item">'
            f'<a href="{E(n.get("link"))}" target="_blank" rel="noopener noreferrer">{E(n.get("titulo"))}'
            f'<span class="sr-only"> (abre em nova aba, no site de origem)</span></a>'
            f'<p class="bol-meta"><span>{E(n.get("fonte"))}</span>'
            f'<span>{E(quando)}</span>{via}</p></li>')
    return (f'<h2 class="h2 bol-h2">{E(rotulo)}</h2>'
            f'<ol class="bol-lista">{"".join(linhas)}</ol>')


def gera_edicao(sem, dados, anterior, seguinte):
    itens = list(dados["itens"].values())
    itens.sort(key=lambda i: i.get("publicado_em") or "", reverse=True)
    br = [i for i in itens if i.get("escopo") == "br"][:POR_ESCOPO]
    wo = [i for i in itens if i.get("escopo") != "br"][:POR_ESCOPO]
    dias = sorted(dados["dias"])
    periodo = (f"{por_extenso(dias[0])} a {por_extenso(dias[-1])}"
               if len(dias) > 1 else por_extenso(dias[0]) if dias else sem)
    titulo = f"Boletim {sem}"
    nav = []
    if anterior:
        nav.append(f'<a href="{anterior}.html">&larr; Edi&ccedil;&atilde;o anterior</a>')
    if seguinte:
        nav.append(f'<a href="{seguinte}.html">Edi&ccedil;&atilde;o seguinte &rarr;</a>')
    falhas = ""
    if dados["falhas"]:
        falhas = ('<p class="coleta-falhas" style="margin-top:22px">'
                  '<span class="label">Fontes sem resposta em alguma coleta da semana</span>'
                  f'<span class="coleta-nomes">{E(" · ".join(sorted(dados["falhas"])))}</span></p>')
    corpo = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="../index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; <a href="index.html">Boletim</a> &nbsp;/&nbsp; {E(sem)}</p>
  <h1 class="h1" style="margin-top: 24px">Boletim da semana {E(sem)}</h1>
  <p class="lead" style="margin: 22px 0 0; max-width: 68ch">{E(periodo)}. {len(itens)} manchetes agregadas das fontes monitoradas, {len([i for i in itens if i.get('escopo') == 'br'])} no Brasil e {len(itens) - len([i for i in itens if i.get('escopo') == 'br'])} no mundo. Abaixo, as mais recentes de cada recorte.</p>
  <p class="body" style="margin: 16px 0 0; max-width: 68ch">Este boletim n&atilde;o reporta nada originalmente e n&atilde;o emite ju&iacute;zo editorial. A sele&ccedil;&atilde;o &eacute; por data. A autoridade &eacute; sempre a publica&ccedil;&atilde;o de origem, e o clique leva at&eacute; ela.</p>
  {falhas}
</section>
<section class="wrap section" style="padding-top: clamp(28px, 3vw, 44px)">
  {bloco_itens(br, "No Brasil")}
  {bloco_itens(wo, "No mundo")}
  <p class="bol-nav">{" &nbsp;·&nbsp; ".join(nav)}</p>
</section>
"""
    pag = cabeca(f"{titulo} · Prot&oacute;tipo do Observat&oacute;rio",
                 f"Boletim semanal do Observatório: {periodo}.",
                 f"{BASE}/boletim/{sem}.html") + corpo + RODAPE
    (SAIDA / f"{sem}.html").write_text(pag, encoding="utf-8")
    return {"semana": sem, "periodo": periodo, "total": len(itens),
            "br": len([i for i in itens if i.get("escopo") == "br"]),
            "ultimo_dia": dias[-1] if dias else None}


def gera_indice(edicoes):
    if edicoes:
        linhas = "".join(
            f'<li class="bol-edicao"><a href="{E(e["semana"])}.html">'
            f'<span class="bol-sem">{E(e["semana"])}</span>'
            f'<span class="bol-per">{E(e["periodo"])}</span>'
            f'<span class="bol-tot">{e["total"]} manchetes</span></a></li>'
            for e in edicoes)
        lista = f'<ol class="bol-edicoes">{linhas}</ol>'
    else:
        lista = ('<p class="notice" style="margin-top:28px">Nenhuma edi&ccedil;&atilde;o ainda. '
                 'A primeira sai quando houver uma semana de hist&oacute;rico acumulado.</p>')
    corpo = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="../index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Boletim</p>
  <h1 class="h1" style="margin-top: 24px">Boletim semanal</h1>
  <p class="lead" style="margin: 22px 0 0; max-width: 70ch">Uma edi&ccedil;&atilde;o por semana, montada automaticamente a partir do hist&oacute;rico do painel. Re&uacute;ne as manchetes agregadas das fontes monitoradas, separadas entre Brasil e mundo, com link para a publica&ccedil;&atilde;o de origem.</p>
</section>
<section class="wrap section" style="padding-top: clamp(24px, 3vw, 40px)">
  <div class="assinar">
    <div>
      <h2 class="h2" style="max-width: 26ch">Como acompanhar</h2>
      <p class="body" style="margin: 18px 0 0; max-width: 62ch">O feed RSS abaixo publica cada edi&ccedil;&atilde;o assim que ela &eacute; gerada. Funciona em qualquer leitor de feeds e em v&aacute;rios clientes de e-mail, sem que este prot&oacute;tipo precise guardar endere&ccedil;o de ningu&eacute;m.</p>
      <div class="pills" style="margin-top: 22px">
        <a class="pill pill-solid" href="feed.xml">Feed RSS do boletim &rarr;</a>
        <a class="pill" href="../indicadores.html#dados">Dados abertos &rarr;</a>
      </div>
    </div>
    <div class="notice">
      <p class="notice-flag"><span class="dot"></span><span>Envio por e-mail em decis&atilde;o</span></p>
      <p class="body" style="margin: 16px 0 0">O envio autom&aacute;tico por e-mail exige guardar uma lista de assinantes, o que um s&iacute;tio est&aacute;tico n&atilde;o faz. Depende de servi&ccedil;o externo ou de lista institucional, e de pol&iacute;tica de privacidade publicada.</p>
      <p class="body" style="margin: 14px 0 0">Enquanto essa decis&atilde;o n&atilde;o for tomada, este prot&oacute;tipo <strong>n&atilde;o coleta endere&ccedil;o de e-mail</strong>. A assinatura &eacute; pelo feed.</p>
    </div>
  </div>
  {lista}
</section>
"""
    pag = cabeca("Boletim semanal &middot; Prot&oacute;tipo do Observat&oacute;rio",
                 "Edições semanais do boletim do Observatório, geradas a partir do histórico do painel.",
                 f"{BASE}/boletim/") + corpo + RODAPE
    (SAIDA / "index.html").write_text(pag, encoding="utf-8")


def gera_feed(edicoes):
    """Feed deterministico: lastBuildDate deriva da edicao mais recente, e nao
    da hora da execucao. Sem isso o arquivo mudaria a cada build, sujando o diff
    de um arquivo que e versionado como retaguarda."""
    def carimbo(iso):
        try:
            return format_datetime(datetime.fromisoformat(iso).replace(tzinfo=timezone.utc))
        except (TypeError, ValueError):
            return None
    agora = None
    for e in edicoes:
        agora = carimbo(e.get("ultimo_dia"))
        if agora:
            break
    if not agora:
        agora = format_datetime(datetime(2026, 1, 1, tzinfo=timezone.utc))
    itens = []
    for e in edicoes[:EDICOES_NO_FEED]:
        pub = carimbo(e.get("ultimo_dia")) or agora
        link = f"{BASE}/boletim/{e['semana']}.html"
        desc = (f"{e['periodo']}. {e['total']} manchetes agregadas, "
                f"{e['br']} no Brasil e {e['total'] - e['br']} no mundo. "
                "Cada item remete a publicacao de origem.")
        itens.append(f"""  <item>
   <title>{E('Boletim ' + e['semana'])}</title>
   <link>{E(link)}</link>
   <guid isPermaLink="true">{E(link)}</guid>
   <pubDate>{E(pub)}</pubDate>
   <description>{E(desc)}</description>
  </item>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
 <channel>
  <title>Boletim do Observatorio do Antissemitismo (prototipo)</title>
  <link>{BASE}/boletim/</link>
  <atom:link href="{BASE}/boletim/feed.xml" rel="self" type="application/rss+xml"/>
  <description>Edicoes semanais do boletim. Prototipo em elaboracao no Eixo 3, sem carater oficial. Cada item remete a publicacao de origem.</description>
  <language>pt-BR</language>
  <lastBuildDate>{E(agora)}</lastBuildDate>
  <generator>scripts/gerar_boletim.py</generator>
{chr(10).join(itens)}
 </channel>
</rss>
"""
    (SAIDA / "feed.xml").write_text(xml, encoding="utf-8")


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    semanas = carrega_semanas()
    chaves = sorted(semanas)
    edicoes = []
    for i, sem in enumerate(chaves):
        ant = chaves[i - 1] if i else None
        seg = chaves[i + 1] if i + 1 < len(chaves) else None
        edicoes.append(gera_edicao(sem, semanas[sem], ant, seg))
    edicoes.sort(key=lambda e: e["semana"], reverse=True)
    gera_indice(edicoes)
    gera_feed(edicoes)
    print(f"boletim: {len(edicoes)} edicao(oes), indice e feed gravados em {SAIDA.name}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
