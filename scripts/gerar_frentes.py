#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as paginas que incorporam as Frentes 1 e 2 do Eixo 3: achados, painel
do Disque 100, mapa de bases e canais, modelo de formulario e assistente de
encaminhamento.

Fonte unica: o relatorio preliminar conjunto das Frentes 1 e 2, versao 2.0, de
02/10/2026. Os quadros vieram dele para data/relatorio-v2/, e este modulo so
le esses arquivos. Nenhuma pagina daqui recolhe dado: nao ha formulario que
envie, nem armazenamento no navegador.

    python3 scripts/gerar_frentes.py
"""
import html
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from gerar_paginas import pagina  # noqa: E402

DADOS = RAIZ / "data" / "relatorio-v2"
DATA = "3 de outubro de 2026"

PRELIMINAR = (
    '<p class="fonte" role="note" style="border-left: 4px solid currentColor; padding-left: 14px; margin: 22px 0 0; max-width: 74ch">'
    '<strong>Documento preliminar, sujeito &agrave; delibera&ccedil;&atilde;o do Eixo 3 em 14/10/2026. '
    'N&atilde;o constitui posi&ccedil;&atilde;o do Eixo, da Iniciativa ou do Conselho.</strong></p>')

RESSALVA_DEFINICAO = (
    '<p class="fonte" role="note" style="margin: 22px 0 0; max-width: 74ch">'
    '<strong>Ressalva de defini&ccedil;&atilde;o.</strong> Os dados existentes foram produzidos sob defini&ccedil;&otilde;es '
    'e metodologias pr&oacute;prias de cada fonte e n&atilde;o s&atilde;o representativos da defini&ccedil;&atilde;o '
    'adotada pela Iniciativa.</p>')


def esc(t):
    return html.escape(t, quote=False)


def carrega(nome):
    return json.loads((DADOS / nome).read_text(encoding="utf-8"))


def tabela(legenda, cabecalho, linhas, classe="tab-kpi"):
    th = "".join(f'<th scope="col">{c}</th>' for c in cabecalho)
    corpo = "".join(
        "<tr>" + "".join(
            (f'<th scope="row">{c}</th>' if i == 0 else f"<td>{c}</td>")
            for i, c in enumerate(l)) + "</tr>"
        for l in linhas)
    return (f'<div class="tab-rolagem"><table class="{classe}">'
            f'<caption class="sr-only">{legenda}</caption>'
            f'<thead><tr>{th}</tr></thead><tbody>{corpo}</tbody></table></div>')


ABERTURA = ('<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); '
            'padding-bottom: clamp(10px, 2vw, 20px)">')


# ---------------------------------------------------------------------------
# T2. Achados das Frentes 1 e 2
# ---------------------------------------------------------------------------

def achados():
    q = carrega("quadro8.json")["quadro8"]
    corpo = carrega("achados_corpo.json")["achados"]
    ordem = lambda a: (int(a["n"].split("-")[0]), a["n"])
    corpo = sorted(corpo, key=ordem)

    PAG_D100 = '<a href="disque100.html">p&aacute;gina do Disque 100</a>' if (RAIZ / "disque100.html").exists() else "p&aacute;gina do Disque 100"
    linhas8 = [[esc(a["n"]), esc(a["achado"]), esc(a["fonte"]), esc(a["confianca"])] for a in q]
    linhas_corpo = [[esc("Achado " + a["n"]), esc(a["texto"]), esc("Seção " + a["secao"])] for a in corpo]

    return f"""{ABERTURA}
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Achados</p>
  <h1 class="h1" style="margin-top: 24px">Achados das Frentes 1 e 2</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">A invisibilidade estat&iacute;stica do antissemitismo no Brasil n&atilde;o &eacute; aus&ecirc;ncia de fen&ocirc;meno. &Eacute; <strong>aus&ecirc;ncia de medida</strong>.</p>
  {PRELIMINAR}
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Esta p&aacute;gina reproduz os achados do relat&oacute;rio preliminar conjunto das Frentes 1 e 2 do Eixo 3, vers&atilde;o 2.0, de 02/10/2026, com a fonte e o grau de confian&ccedil;a que o pr&oacute;prio relat&oacute;rio atribui a cada um. O relat&oacute;rio &eacute; documento de trabalho e n&atilde;o est&aacute; publicado aqui. Atualizada em {DATA}. As recomenda&ccedil;&otilde;es do relat&oacute;rio n&atilde;o s&atilde;o reproduzidas.</p>
</section>

<section class="band"><div class="wrap section">
  <p class="eyebrow">A formula&ccedil;&atilde;o de refer&ecirc;ncia</p>
  <h2 class="h2" style="max-width: 34ch">A ausência de medida tem três manifestações</h2>
  <ul class="scope-list" style="margin-top: 20px; max-width: 76ch">
    <li><strong>Categoria inexistente.</strong> A maior parte das bases examinadas n&atilde;o tem categoria que identifique o antissemitismo.</li>
    <li><strong>Categoria existente que n&atilde;o mede.</strong> No Disque 100 existe o campo de religi&atilde;o da v&iacute;tima, mas ele mede atributo da v&iacute;tima, opera dentro de uma viola&ccedil;&atilde;o e est&aacute; vazio na maioria dos registros.</li>
    <li><strong>S&eacute;rie publicada n&atilde;o compar&aacute;vel.</strong> As divulga&ccedil;&otilde;es variam em unidade, janela e filtro, e n&atilde;o h&aacute; como compar&aacute;-las entre si.</li>
  </ul>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">As causas s&atilde;o duas e cumulativas. A primeira &eacute; a aus&ecirc;ncia de medida na entrada, sanável por marcador. A segunda &eacute; a aus&ecirc;ncia de rastreabilidade do desfecho na sa&iacute;da, que decorre em parte de limite normativo leg&iacute;timo, o segredo de justi&ccedil;a, e n&atilde;o de falha institucional.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch"><strong>Regra de leitura:</strong> aus&ecirc;ncia de evid&ecirc;ncia n&atilde;o equivale a evid&ecirc;ncia de aus&ecirc;ncia. Cada s&eacute;rie reproduzida neste sítio indica a defini&ccedil;&atilde;o e a metodologia da fonte.</p>
  {RESSALVA_DEFINICAO}
</div></section>

<section class="wrap section" id="quadro8">
  <h2 class="h2" style="max-width: 34ch">Quadro de achados consolidados</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Os achados A1 a A17 v&ecirc;m da Frente 1. Os achados A18 a A37 v&ecirc;m do levantamento da Frente 2. Grau alto exige fonte prim&aacute;ria verificada por quem atribui o grau. Leitura por reprodu&ccedil;&atilde;o, por resumo ou por informa&ccedil;&atilde;o n&atilde;o conferida recebe grau m&eacute;dio ou baixo. Respostas institucionais por despacho aparecem sem o n&uacute;mero do processo.</p>
  {tabela("Achados consolidados A1 a A37, com fonte e grau de confiança", ["N&ordm;", "Achado", "Fonte", "Confian&ccedil;a"], linhas8)}
  <p class="fonte" style="margin-top: 22px">Fonte: relat&oacute;rio preliminar conjunto, vers&atilde;o 2.0, Quadro 8. Os n&uacute;meros do Disque 100 est&atilde;o detalhados, com unidade, janela e divulga&ccedil;&atilde;o de origem, na {PAG_D100}.</p>
</section>

<section class="band"><div class="wrap section" id="corpo">
  <h2 class="h2" style="max-width: 34ch">Achados numerados do corpo do relatório</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Cada achado traz a se&ccedil;&atilde;o de origem no relat&oacute;rio. O relat&oacute;rio n&atilde;o atribui grau pr&oacute;prio a estes achados: o grau de confian&ccedil;a consta do quadro acima para os achados A1 a A37, a que eles se relacionam.</p>
  {tabela("Achados numerados do corpo do relatório", ["Achado", "Texto", "Origem"], linhas_corpo)}
</div></section>
"""


def main():
    feitos = [
        pagina("achados.html", "Achados das Frentes 1 e 2",
               "Achados do relatorio preliminar conjunto das Frentes 1 e 2 do Eixo 3, com fonte e grau de confianca. Documento preliminar.",
               "achados.html", achados()),
    ]
    print("paginas das Frentes 1 e 2: " + ", ".join(feitos))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
