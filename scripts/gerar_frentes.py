#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as paginas que incorporam as Frentes 1 e 2 do Eixo 3: achados, painel
do Disque 100, mapa de bases e canais, modelo de formulario e assistente de
encaminhamento.

Fonte unica: o relatorio preliminar conjunto das Frentes 1 e 2, versao 2.0, de
05/10/2026. Os quadros vieram dele para data/relatorio-v2/, e este modulo so
le esses arquivos. Nenhuma pagina daqui recolhe dado: nao ha formulario que
envie, nem armazenamento no navegador.

    python3 scripts/gerar_frentes.py
"""
import html
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from gerar_paginas import pagina  # noqa: E402

DADOS = RAIZ / "data" / "relatorio-v2"
DATA = "5 de outubro de 2026"
REL_V2 = "relat&oacute;rio preliminar conjunto, vers&atilde;o 2.0, de 05/10/2026"

PRELIMINAR = (
    '<p class="fonte" role="note" style="border-left: 4px solid currentColor; padding-left: 14px; margin: 22px 0 0; max-width: 74ch">'
    '<strong>Documento preliminar, em aprecia&ccedil;&atilde;o pelos participantes das Frentes 1 e 2, que podem apresentar '
    'destaques, sugest&otilde;es e eventuais vetos. Os destaques n&atilde;o resolvidos ser&atilde;o deliberados na reuni&atilde;o '
    'de encerramento dos trabalhos, em 14/10/2026. N&atilde;o constitui posi&ccedil;&atilde;o do Eixo, da Iniciativa ou do Conselho.</strong></p>')

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
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Esta p&aacute;gina reproduz os achados do relat&oacute;rio preliminar conjunto das Frentes 1 e 2 do Eixo 3, vers&atilde;o 2.0, de 05/10/2026, com a fonte e o grau de confian&ccedil;a que o pr&oacute;prio relat&oacute;rio atribui a cada um. O relat&oacute;rio &eacute; documento de trabalho e n&atilde;o est&aacute; publicado aqui. Atualizada em {DATA}. As recomenda&ccedil;&otilde;es do relat&oacute;rio n&atilde;o s&atilde;o reproduzidas.</p>
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

<section class="wrap section" id="levantamento">
  <p class="eyebrow">Como a Frente 2 foi levantada</p>
  <h2 class="h2" style="max-width: 34ch">O instrumento de coleta n&atilde;o retornou preenchido</h2>
  <ul class="scope-list" style="margin-top: 20px; max-width: 76ch">
    <li>O instrumento de coleta da Frente 2 <strong>n&atilde;o retornou preenchido pelas institui&ccedil;&otilde;es</strong>.</li>
    <li>O levantamento <strong>n&atilde;o foi exclusivamente em fontes abertas</strong> (ata de 30/09/2026, item 5.2). Combinou pesquisa em fontes p&uacute;blicas, pesquisa interna da respons&aacute;vel t&eacute;cnica da Frente 2, em parte revalidada a partir de informa&ccedil;&atilde;o dos pr&oacute;prios minist&eacute;rios, o relat&oacute;rio oficial do Disque 100 obtido junto &agrave; Ouvidoria Nacional de Direitos Humanos e os microdados abertos do Disque 100.</li>
    <li>As perguntas que o instrumento dirigia a cada institui&ccedil;&atilde;o, em especial a do v&iacute;nculo entre monitoramento e registro, seguem sem resposta.</li>
    <li>Onde se apoia em fontes p&uacute;blicas, o levantamento mede a <strong>publicidade da capacidade institucional</strong>, e n&atilde;o a capacidade em si. Aus&ecirc;ncia de documento p&uacute;blico n&atilde;o equivale a inexist&ecirc;ncia de capacidade.</li>
  </ul>
  <p class="fonte" style="margin-top: 22px">Fonte: {REL_V2}, se&ccedil;&otilde;es 2.5 e 4.1.</p>
</section>

<section class="wrap section" id="quadro8">
  <h2 class="h2" style="max-width: 34ch">Quadro de achados consolidados</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Os achados A1 a A17 v&ecirc;m da Frente 1. Os achados A18 a A37 v&ecirc;m do levantamento da Frente 2, n&atilde;o exclusivamente em fontes abertas. Grau alto exige fonte prim&aacute;ria verificada por quem atribui o grau. Leitura por reprodu&ccedil;&atilde;o, por resumo ou por informa&ccedil;&atilde;o n&atilde;o conferida recebe grau m&eacute;dio ou baixo. Respostas institucionais por despacho aparecem sem o n&uacute;mero do processo.</p>
  {tabela("Achados consolidados A1 a A37, com fonte e grau de confiança", ["N&ordm;", "Achado", "Fonte", "Confian&ccedil;a"], linhas8)}
  <p class="fonte" style="margin-top: 22px">Fonte: relat&oacute;rio preliminar conjunto, vers&atilde;o 2.0, Quadro 8. Os n&uacute;meros do Disque 100 est&atilde;o detalhados, com unidade, janela e divulga&ccedil;&atilde;o de origem, na {PAG_D100}.</p>
</section>

<section class="band"><div class="wrap section" id="corpo">
  <h2 class="h2" style="max-width: 34ch">Achados numerados do corpo do relatório</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Cada achado traz a se&ccedil;&atilde;o de origem no relat&oacute;rio. O relat&oacute;rio n&atilde;o atribui grau pr&oacute;prio a estes achados: o grau de confian&ccedil;a consta do quadro acima para os achados A1 a A37, a que eles se relacionam.</p>
  {tabela("Achados numerados do corpo do relatório", ["Achado", "Texto", "Origem"], linhas_corpo)}
</div></section>

<section class="wrap section" id="coordenacao">
  <p class="eyebrow">Se&ccedil;&atilde;o 5.3</p>
  <h2 class="h2" style="max-width: 34ch">A lacuna &eacute; de coordena&ccedil;&atilde;o, n&atilde;o de iniciativa</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Em registro, capacita&ccedil;&atilde;o e preven&ccedil;&atilde;o, as solu&ccedil;&otilde;es espec&iacute;ficas para o antissemitismo localizadas no Brasil s&atilde;o subnacionais. Fora do curr&iacute;culo de Hist&oacute;ria, que nomeia o Holocausto como conte&uacute;do, n&atilde;o se localizou, em fonte p&uacute;blica, instrumento federal com recorte pr&oacute;prio de antissemitismo, embora se tenham localizado instrumentos federais com recorte pr&oacute;prio para outros grupos. Estados e munic&iacute;pios disp&otilde;em de recortes pr&oacute;prios sem arquitetura que os articule (Achado 13).</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">A pesquisa interna da respons&aacute;vel t&eacute;cnica da Frente 2 chegou ao mesmo resultado: n&atilde;o identificou a&ccedil;&atilde;o espec&iacute;fica de enfrentamento ao antissemitismo em nenhum minist&eacute;rio, apenas pol&iacute;ticas de crimes de &oacute;dio em geral, com volume expressivo nos recortes de g&ecirc;nero, popula&ccedil;&atilde;o LGBT e crian&ccedil;as e adolescentes (ata de 30/09/2026, item 6.1). O que falta n&atilde;o &eacute; iniciativa, &eacute; coordena&ccedil;&atilde;o.</p>
</section>

<section class="band"><div class="wrap section" id="fragmentacao">
  <p class="eyebrow">Se&ccedil;&atilde;o 5.4</p>
  <h2 class="h2" style="max-width: 34ch">Fragmenta&ccedil;&atilde;o dos pontos de entrada</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">O invent&aacute;rio de canais online de den&uacute;ncia de crimes de &oacute;dio, verificado em 3 de outubro de 2026, d&aacute; a dimens&atilde;o dessa fragmenta&ccedil;&atilde;o. Re&uacute;ne cerca de quarenta canais federais, estaduais e da sociedade civil. Em 15 das 27 unidades federadas, nenhum canal estadual foi comprovado nesta coleta, o que n&atilde;o prova que ele n&atilde;o exista. Os &uacute;nicos canais espec&iacute;ficos de antissemitismo localizados s&atilde;o n&atilde;o estatais, os da CONIB, que registram sob defini&ccedil;&atilde;o divergente da emitida pelo eixo de Conceitua&ccedil;&atilde;o.</p>
  <div class="pills" style="margin-top: 22px"><a class="pill pill-solid" href="canais.html">Invent&aacute;rio de canais &rarr;</a></div>
  <p class="fonte" style="margin-top: 22px">Fonte: {REL_V2}, se&ccedil;&atilde;o 5.4 e Anexo F.</p>
</div></section>
"""


# ---------------------------------------------------------------------------
# T3. Painel do Disque 100, sob a regra E.9.2.4 do Anexo E
# ---------------------------------------------------------------------------

REL30 = "Relat&oacute;rio oficial do Disque 100 sobre viol&ecirc;ncia relacionada &agrave; liberdade religiosa, emitido em 30/09/2026"
MICRO = "Microdados abertos do Disque 100 (MDHC), por semestre"


def disque100():
    BASES_PILL = '<a class="pill" href="bases.html">Mapa de bases e canais &rarr;</a>' if (RAIZ / "bases.html").exists() else ""
    oficial = tabela(
        "Série oficial de denúncias de violência relacionada à liberdade religiosa, 2023 a 27/09/2026",
        ["Ano", "Den&uacute;ncias", "Unidade", "Janela", "Divulga&ccedil;&atilde;o de origem",
         "Religi&atilde;o da v&iacute;tima n&atilde;o informada", "V&iacute;tima de religi&atilde;o juda&iacute;smo"],
        [["2023", "1.482", "denúncia", "ano civil", REL30, "1.229 (83%)", "1"],
         ["2024", "2.472", "denúncia", "ano civil", REL30, "1.842 (75%)", "2"],
         ["2025", "2.723", "denúncia", "ano civil", REL30, "2.016 (74%)", "6"],
         ["2026", "1.768", "denúncia", "1&ordm;/01 a 27/09/2026", REL30, "920 (52%)", "4"]])

    ramo = tabela(
        "Ramo de liberdade de religião ou crença nos microdados abertos, denúncias distintas",
        ["Ano", "Den&uacute;ncias distintas no ramo", "Unidade", "Janela", "Origem", "Propor&ccedil;&atilde;o do total oficial do mesmo ano"],
        [["2023", "960", "denúncia distinta, fixada pelo analista", "ano civil", MICRO, "65%"],
         ["2024", "1.546", "denúncia distinta, fixada pelo analista", "ano civil", MICRO, "63%"],
         ["2025", "2.619", "denúncia distinta, fixada pelo analista", "ano civil", MICRO, "96%"]])

    divulg = tabela(
        "Divulgações do MDHC, com a unidade que cada uma declara",
        ["Divulga&ccedil;&atilde;o", "Valor", "Unidade como rotulada", "Refer&ecirc;ncia temporal"],
        [["Janeiro de 2024", "2.124", "viola&ccedil;&otilde;es", "2023"],
         ["Janeiro de 2025", "1.481", "den&uacute;ncias", "2023"],
         ["Janeiro de 2026", "2.472", "rotulado como viola&ccedil;&otilde;es; o relat&oacute;rio oficial de 30/09/2026 trata o mesmo n&uacute;mero como den&uacute;ncias", "2024"],
         ["Janeiro de 2026", "2.774", "casos", "janela de treze meses, de janeiro de 2025 a janeiro de 2026, que n&atilde;o corresponde ao ano civil"],
         ["Outubro de 2024", "1.227 den&uacute;ncias e 1.940 viola&ccedil;&otilde;es", "duas unidades distintas, na mesma comunica&ccedil;&atilde;o", "1&ordm; semestre de 2024"]])

    judias = tabela(
        "Denúncias com vítima de religião declarada judaísmo, em relação ao ramo de liberdade de religião ou crença",
        ["Per&iacute;odo", "Den&uacute;ncias com v&iacute;tima judia", "No ramo de liberdade de religi&atilde;o ou cren&ccedil;a", "Fora do ramo"],
        [["2023", "17", "0", "100%"],
         ["2024", "21", "2", "90%"],
         ["2025", "16", "5", "69%"],
         ["1&ordm; semestre de 2026", "39", "4", "90%"]])

    preench = tabela(
        "Preenchimento da religião da vítima nos microdados abertos",
        ["Per&iacute;odo", "Den&uacute;ncias da base com a religi&atilde;o da v&iacute;tima preenchida"],
        [["2023", "3,61%"], ["2024", "6,08%"], ["2025", "4,01%"], ["1&ordm; semestre de 2026", "14,06%"]])

    return f"""{ABERTURA}
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; <a href="achados.html">Achados</a> &nbsp;/&nbsp; Disque 100</p>
  <h1 class="h1" style="margin-top: 24px">Disque 100: o que a base mede e o que n&atilde;o mede</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">O campo existe, e a medida n&atilde;o. O Disque 100 registra a religi&atilde;o da v&iacute;tima, mas n&atilde;o tem valor de motiva&ccedil;&atilde;o religiosa ou antissemita, e as divulga&ccedil;&otilde;es p&uacute;blicas n&atilde;o se comparam entre si.</p>
  {PRELIMINAR}
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Atualizada em {DATA}. Fonte: relat&oacute;rio preliminar conjunto das Frentes 1 e 2, vers&atilde;o 2.0, item 3.1.5, Quadro 8 e Anexo E, itens E.9.2 e E.11. Os n&uacute;meros n&atilde;o s&atilde;o produzidos por este sítio.</p>
  {RESSALVA_DEFINICAO}
</section>

<section class="band"><div class="wrap section" id="regra">
  <p class="eyebrow">Regra de leitura</p>
  <h2 class="h2" style="max-width: 34ch">Todo n&uacute;mero declara unidade, janela e divulga&ccedil;&atilde;o de origem</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">Nenhum valor da Ouvidoria Nacional de Direitos Humanos &eacute; citado sem que se declare, no mesmo per&iacute;odo, a unidade, a janela temporal e a divulga&ccedil;&atilde;o de origem. <strong>Compara&ccedil;&atilde;o entre anos apoiada em divulga&ccedil;&otilde;es diferentes fica vedada.</strong> As duas s&eacute;ries abaixo t&ecirc;m origem, unidade e filtro distintos e <strong>nunca s&atilde;o somadas nem comparadas</strong> como se fossem a mesma.</p>
</div></section>

<section class="wrap section" id="oficial">
  <p class="eyebrow">S&eacute;rie oficial</p>
  <h2 class="h2" style="max-width: 34ch">Den&uacute;ncias de viol&ecirc;ncia relacionada &agrave; liberdade religiosa</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">O relat&oacute;rio oficial foi obtido junto &agrave; Ouvidoria Nacional de Direitos Humanos pela respons&aacute;vel t&eacute;cnica da Frente 2 e encaminhado ao Eixo em 30/09/2026, a partir de pedido sobre os dados divulgados. N&atilde;o &eacute; resposta &agrave; dilig&ecirc;ncia D01, cujas perguntas sobre marcador, fluxo e integra&ccedil;&atilde;o seguem sem resposta. Ele declara contar den&uacute;ncias e reproduz os totais divulgados. Os treze casos com v&iacute;tima de religi&atilde;o juda&iacute;smo no per&iacute;odo s&atilde;o piso, porque a religi&atilde;o da v&iacute;tima n&atilde;o &eacute; informada na maioria das den&uacute;ncias. Os valores n&atilde;o foram conferidos no painel original.</p>
  {oficial}
  <p class="fonte" style="margin-top: 22px">Fonte: {REL30}, obtido junto &agrave; Ouvidoria Nacional de Direitos Humanos pela respons&aacute;vel t&eacute;cnica da Frente 2 e encaminhado ao Eixo 3 em 30/09/2026. Confian&ccedil;a alta quanto ao relat&oacute;rio, com a confer&ecirc;ncia contra o painel pendente (achado A35).</p>
</section>

<section class="band"><div class="wrap section" id="microdados">
  <p class="eyebrow">Microdados abertos</p>
  <h2 class="h2" style="max-width: 34ch">O ramo de liberdade de religi&atilde;o ou cren&ccedil;a</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">A &aacute;rvore de viola&ccedil;&otilde;es da base n&atilde;o tem categoria chamada intoler&acirc;ncia religiosa. A correspond&ecirc;ncia usada pelo Eixo &eacute; o ramo &ldquo;Liberdade de religi&atilde;o ou cren&ccedil;a&rdquo;, com os subtipos de cren&ccedil;a, de culto e n&atilde;o cren&ccedil;a. A contagem &eacute; de den&uacute;ncias distintas, unidade fixada pelo analista.</p>
  {ramo}
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">O ramo cresce 69% entre 2024 e 2025, e a s&eacute;rie oficial, 10%. As duas n&atilde;o s&atilde;o a mesma s&eacute;rie. O filtro oficial abrange den&uacute;ncias que os microdados abertos n&atilde;o classificam no ramo e n&atilde;o &eacute; documentado, de modo que a diferen&ccedil;a &eacute; de composi&ccedil;&atilde;o. N&atilde;o se pode ler o crescimento do ramo como crescimento do fen&ocirc;meno.</p>
  <p class="fonte" style="margin-top: 22px">Fonte: {MICRO}, 2023 a 2025; processamento do Eixo 3. Confian&ccedil;a m&eacute;dia (achados A29 e A32).</p>
</div></section>

<section class="wrap section" id="divulgacoes">
  <p class="eyebrow">Divulga&ccedil;&otilde;es do MDHC</p>
  <h2 class="h2" style="max-width: 34ch">A unidade e a janela variam entre divulga&ccedil;&otilde;es</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Den&uacute;ncia e viola&ccedil;&atilde;o n&atilde;o s&atilde;o unidades equivalentes, porque uma den&uacute;ncia pode registrar mais de uma viola&ccedil;&atilde;o. Nenhuma das divulga&ccedil;&otilde;es examinadas traz nota metodol&oacute;gica que as distinga.</p>
  {divulg}
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">O relat&oacute;rio oficial de 30/09/2026 registra os totais como den&uacute;ncias. A divulga&ccedil;&atilde;o de janeiro de 2026 tem, portanto, <strong>imprecis&atilde;o de r&oacute;tulo, e n&atilde;o erro de contagem</strong>. N&atilde;o h&aacute; evid&ecirc;ncia de inconsist&ecirc;ncia na base: o que se documenta &eacute; a aus&ecirc;ncia de nota metodol&oacute;gica nas divulga&ccedil;&otilde;es e de documenta&ccedil;&atilde;o do filtro.</p>
  <p class="fonte" style="margin-top: 22px">Fonte: divulga&ccedil;&otilde;es do MDHC lidas por reprodu&ccedil;&atilde;o; relat&oacute;rio oficial de 30/09/2026. Confian&ccedil;a m&eacute;dia, com a confer&ecirc;ncia contra o painel original interrompida por bloqueio de acesso (achados A18 e A34).</p>
</section>

<section class="band"><div class="wrap section" id="catalogo">
  <p class="eyebrow">Motiva&ccedil;&atilde;o</p>
  <h2 class="h2" style="max-width: 34ch">Quebra do cat&aacute;logo em setembro de 2023</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">At&eacute; agosto de 2023, a coluna de motiva&ccedil;&atilde;o trazia de 54 a 62 valores por m&ecirc;s, entre eles &ldquo;em raz&atilde;o da religi&atilde;o&rdquo;, registrado em 642 den&uacute;ncias de 2023, com &uacute;ltimo registro em 31 de agosto. A partir de setembro de 2023, o cat&aacute;logo caiu para 15 a 22 valores por m&ecirc;s, sem o valor religioso. Nenhum valor religioso ou antissemita consta de 2024, de 2025 nem do primeiro semestre de 2026. A base n&atilde;o tem dicion&aacute;rio de dados, e a causa da mudan&ccedil;a n&atilde;o &eacute; identific&aacute;vel nos dados. A coluna de motiva&ccedil;&atilde;o n&atilde;o &eacute; comparável entre 2023 e 2024.</p>
  <p class="fonte" style="margin-top: 22px">Fonte: {MICRO}, 2023 a 2026. Confian&ccedil;a alta quanto ao fato; a causa depende de consulta ao MDHC (achados A31 e A36).</p>
</div></section>

<section class="wrap section" id="vitimas-judias">
  <p class="eyebrow">V&iacute;timas de religi&atilde;o judaica</p>
  <h2 class="h2" style="max-width: 34ch">A maior parte das den&uacute;ncias fica fora do ramo</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">De 2023 ao primeiro semestre de 2026, entre 69 e 100 por cento das den&uacute;ncias com v&iacute;tima de religi&atilde;o declarada juda&iacute;smo ficam fora do ramo de liberdade de religi&atilde;o ou cren&ccedil;a. <strong>Os n&uacute;meros s&atilde;o piso</strong>, porque a religi&atilde;o da v&iacute;tima est&aacute; preenchida em minoria das den&uacute;ncias.</p>
  {judias}
  <p class="fonte" style="margin-top: 22px">Fonte: {MICRO}, 2023 a 2026; contagem de den&uacute;ncias distintas, por ano civil e, em 2026, at&eacute; o fim do 1&ordm; semestre. Confian&ccedil;a alta, com 21 como piso em 2024 (achados A30 e A37).</p>
</section>

<section class="band"><div class="wrap section" id="preenchimento">
  <p class="eyebrow">Religi&atilde;o da v&iacute;tima</p>
  <h2 class="h2" style="max-width: 34ch">Preenchimento do campo e o salto de 2026</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">O campo mede atributo da v&iacute;tima, e n&atilde;o a motiva&ccedil;&atilde;o do agressor, e opera apenas dentro de uma viola&ccedil;&atilde;o. Esteve vazio em cerca de tr&ecirc;s quartos das den&uacute;ncias de 2023 a 2025. No primeiro semestre de 2026, o preenchimento subiu a 14,06%, ainda minorit&aacute;rio, por causa n&atilde;o identific&aacute;vel nos dados. Por isso a afirma&ccedil;&atilde;o de que o campo est&aacute; vazio vale para 2023 a 2025, e n&atilde;o para 2026.</p>
  {preench}
  <p class="fonte" style="margin-top: 22px">Fonte: {MICRO}; percentuais sobre as den&uacute;ncias da base, n&atilde;o do recorte. Confian&ccedil;a alta para os valores (achado A7).</p>
</div></section>

<section class="wrap section" id="limites">
  <h2 class="h2" style="max-width: 34ch">O que n&atilde;o h&aacute;, e o que depende de consulta</h2>
  <ul class="scope-list scope-isnot" style="margin-top: 20px; max-width: 76ch">
    <li>Os microdados abertos n&atilde;o trazem coluna de encaminhamento, &oacute;rg&atilde;o de destino, status ou desfecho. Existe rastreabilidade individual no sistema, sem agrega&ccedil;&atilde;o em s&eacute;rie (achado A25).</li>
    <li>Dependem de consulta ao MDHC: o filtro do relat&oacute;rio oficial e das divulga&ccedil;&otilde;es; o corte de dados da divulga&ccedil;&atilde;o de janeiro de 2026 e a diverg&ecirc;ncia do Rio de Janeiro; a causa da quebra de cat&aacute;logo em setembro de 2023; a causa do aumento do preenchimento da religi&atilde;o em 2026.</li>
    <li>A aus&ecirc;ncia de evid&ecirc;ncia n&atilde;o equivale a evid&ecirc;ncia de aus&ecirc;ncia: o que aqui se registra &eacute; o que as bases p&uacute;blicas n&atilde;o permitem medir.</li>
  </ul>
  <div class="pills" style="margin-top: 24px">
    <a class="pill pill-solid" href="achados.html">Todos os achados &rarr;</a>
    {BASES_PILL}
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# T4. Mapa das bases e canais
# ---------------------------------------------------------------------------

def bases():
    d = carrega("bases.json")
    linhas = [[esc(b["base"]), esc(b["orgao"]), esc(b["categoria"]), esc(b["proxima"]),
               esc(b["unidade"]), esc(b["desfecho"])] for b in d["bases"]]
    leitura = esc(d["leitura"].replace("Leitura do quadro.", "", 1).strip())
    return f"""{ABERTURA}
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; <a href="achados.html">Achados</a> &nbsp;/&nbsp; Bases e canais</p>
  <h1 class="h1" style="margin-top: 24px">Mapa das bases e canais</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Dezoito bases e canais examinados, com a pergunta que importa: o instrumento tem categoria que identifique o antissemitismo, e a base permite saber o que aconteceu com o registro depois da entrada?</p>
  {PRELIMINAR}
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Posi&ccedil;&atilde;o de 18 de agosto de 2026, conforme o Anexo B do relat&oacute;rio preliminar conjunto, vers&atilde;o 2.0. Atualizada em {DATA}. A coluna de categoria responde se existe, no instrumento, valor ou campo que identifique o antissemitismo de forma separ&aacute;vel na extra&ccedil;&atilde;o. A coluna de desfecho responde se a base permite saber o que aconteceu com o registro.</p>
  {RESSALVA_DEFINICAO}
</section>

<section class="wrap section" id="quadro">
  {tabela("Quadro comparativo das bases e canais examinados pelo Eixo 3", ["Base ou canal", "&Oacute;rg&atilde;o ou entidade", "Categoria aut&ocirc;noma de antissemitismo", "Categoria mais pr&oacute;xima dispon&iacute;vel", "Unidade de contagem", "Desfecho rastre&aacute;vel"], linhas)}
  <p class="fonte" style="margin-top: 22px">Fonte: relat&oacute;rio preliminar conjunto, vers&atilde;o 2.0, Anexo B, quadro B.1. A unidade de contagem difere entre as bases (comunica&ccedil;&atilde;o, manifesta&ccedil;&atilde;o, den&uacute;ncia, boletim, chamado, processo, procedimento, ocorr&ecirc;ncia validada), e por isso os n&uacute;meros de bases distintas n&atilde;o se somam. Os canais de den&uacute;ncia de crimes de &oacute;dio, com endere&ccedil;o e verifica&ccedil;&atilde;o de 03/10/2026, est&atilde;o no <a href="canais.html">invent&aacute;rio de canais</a>.</p>
</section>

<section class="band"><div class="wrap section" id="leitura">
  <p class="eyebrow">Leitura do quadro</p>
  <h2 class="h2" style="max-width: 34ch">Poucas categorias, quase nenhum desfecho</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">{leitura}</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">A aus&ecirc;ncia de categoria autônoma n&atilde;o equivale &agrave; aus&ecirc;ncia do fen&ocirc;meno. Ver os <a href="achados.html">achados</a> e o painel do <a href="disque100.html">Disque 100</a>.</p>
</div></section>
"""


# ---------------------------------------------------------------------------
# T7. Modelo demonstrativo de formulario. Nao envia nem guarda nada.
# ---------------------------------------------------------------------------

AVISO_FORM = ("Modelo para discuss&atilde;o com os &oacute;rg&atilde;os de registro. Esta p&aacute;gina n&atilde;o &eacute; canal de den&uacute;ncia, "
              "n&atilde;o envia e n&atilde;o guarda nenhuma informa&ccedil;&atilde;o.")

SIM_NAO = ["sim", "não"]
MODALIDADES = ["discurso de ódio", "incitação", "ameaça", "violência física",
                                                         "vandalismo ou dano ao patrimônio",
                                                         "propaganda extremista ou neonazista",
                                                         "negação ou distorção do Holocausto",
                                                         "discriminação institucional ou social",
                                                         "assédio ou perseguição", "conteúdo conspiratório antissemita"]

# Blocos da Ficha Padrao (Anexo D.1). Cada campo: (rotulo, tipo, opcoes).
FICHA = [
    ("1. Identificação do registro", [
        ("Identificador único do caso", "text", None), ("Data do registro", "date", None),
        ("Hora do registro", "time", None),
        ("Canal de entrada", "select", ["Polícia Federal", "Disque 100", "Polícia Civil", "Ministério Público",
                                        "plataforma digital", "escola ou universidade",
                                        "organização da sociedade civil", "outro"]),
        ("Órgão receptor", "text", None), ("Responsável pelo registro", "text", None)]),
    ("2. Dados da ocorrência", [
        ("Data do fato", "date", None), ("Hora aproximada", "time", None),
        ("Unidade federada", "text", None), ("Município", "text", None), ("Local específico", "text", None),
        ("Meio de ocorrência", "select", ["online", "offline", "híbrido"]),
        ("Ambiente específico", "select", ["rede social", "aplicativo de mensagens", "fórum ou plataforma digital",
                                           "escola", "universidade", "local de culto", "evento público", "trabalho",
                                           "espaço público", "outro"])]),
    ("3. Descrição resumida", [("Texto livre, com limite de quinze linhas", "textarea", None)]),
    ("4. Natureza do fato", [
        ("Natureza do fato", "select", ["antissemitismo explícito", "antissemitismo implícito ou codificado",
                                        "potencial antissemitismo, em apuração", "não confirmado"])]),
    ("5. Modalidade da conduta", [
        ("Modalidade principal", "select", MODALIDADES),
        ("Modalidades secundárias", "check", MODALIDADES)]),
    ("6. Alvo atingido", [
        ("Alvo atingido", "select", ["pessoa individual", "grupo ou coletividade judaica", "instituição judaica",
                                     "patrimônio, memória ou símbolos", "outro grupo vulnerabilizado associado"]),
        ("Campo de detalhamento", "text", None)]),
    ("7. Motivação aparente", [
        ("Motivação aparente", "select", ["estereótipo clássico antijudaico", "neonazismo ou supremacismo branco",
                                          "negacionismo ou revisionismo do Holocausto", "teoria conspiratória",
                                          "antissemitismo religioso", "antissemitismo político instrumentalizado",
                                          "motivação não identificada"])]),
    ("8. Gravidade e risco", [
        ("Nível de risco", "select", ["1", "2", "3", "4"]), ("Risco imediato", "select", SIM_NAO),
        ("Potencial de escalada", "select", SIM_NAO)]),
    ("9. Organização e articulação", [
        ("Organização e articulação", "select", ["caso isolado", "reiteração pelo mesmo autor", "grupo coordenado",
                                                 "indício de célula extremista", "rede digital organizada",
                                                 "não identificado"])]),
    ("10. Evidências disponíveis", [
        ("Tipos de evidência", "check", ["captura de tela", "vídeo", "áudio", "endereço de conteúdo", "documento",
                                         "imagem", "outro"]),
        ("Evidência preservada", "select", SIM_NAO),
        ("Registro de hash e cadeia de custódia", "select", SIM_NAO)]),
    ("11. Encaminhamento", [
        ("Encaminhamento", "select", ["triagem concluída", "encaminhado à Polícia Federal", "encaminhado à Polícia Civil",
                                      "encaminhado ao Ministério Público", "encaminhado ao MDHC",
                                      "medida preventiva acionada", "arquivado", "outro"]),
        ("Data do encaminhamento", "date", None), ("Responsável", "text", None), ("Prazo de retorno", "text", None)]),
    ("12. Observações complementares", [("Campo aberto", "textarea", None)]),
]

NUCLEO = ["Identificador único do caso", "Data e hora do registro", "Canal de entrada",
          "Unidade federada e município", "Meio de ocorrência", "Modalidade da conduta", "Descrição resumida",
          "Alvo principal", "Indício de motivação antissemita", "Nível de risco", "Necessidade de resposta urgente",
          "Encaminhamento dado", "Existência de evidência anexada", "Possível vínculo com extremismo organizado",
          "Status do caso"]


def _campo(bid, n, rot, tipo, ops):
    cid = f"f{bid}-{n}"
    if tipo == "select":
        o = "".join(f"<option>{esc(x)}</option>" for x in ops)
        return f'<label class="frm-campo" for="{cid}"><span>{esc(rot)}</span><select id="{cid}"><option value="">(selecione)</option>{o}</select></label>'
    if tipo == "check":
        c = "".join(f'<label><input type="checkbox"> {esc(x)}</label>' for x in ops)
        return f'<div class="frm-campo"><span>{esc(rot)}</span><div class="frm-opcoes">{c}</div></div>'
    if tipo == "textarea":
        return f'<label class="frm-campo" for="{cid}"><span>{esc(rot)}</span><textarea id="{cid}" placeholder="Campo demonstrativo. Não digite dado real."></textarea></label>'
    return f'<label class="frm-campo" for="{cid}"><span>{esc(rot)}</span><input id="{cid}" type="{tipo}" autocomplete="off"></label>'


def formulario_modelo():
    ENC = 'ou o <a href="encaminhar.html">assistente de encaminhamento</a>' if (RAIZ / "encaminhar.html").exists() else ""
    blocos = []
    for bid, (titulo, campos) in enumerate(FICHA, 1):
        cs = "".join(_campo(bid, n, r, t, o) for n, (r, t, o) in enumerate(campos, 1))
        blocos.append(f'<fieldset><legend>{esc(titulo)}</legend>{cs}</fieldset>')
    nucleo = "".join(f"<li>{esc(x)}</li>" for x in NUCLEO)
    return f"""{ABERTURA}
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; <a href="achados.html">Achados</a> &nbsp;/&nbsp; Modelo de formul&aacute;rio</p>
  <h1 class="h1" style="margin-top: 24px">Modelo demonstrativo de ficha de registro</h1>
  <p class="frm-aviso" role="note">{AVISO_FORM}</p>
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Os campos s&atilde;o os da ficha padr&atilde;o nacional de registro de den&uacute;ncia (Anexo D.1 do relat&oacute;rio preliminar conjunto, vers&atilde;o 2.0), em vers&atilde;o de trabalho, e o n&uacute;cleo m&iacute;nimo de interoperabilidade (D.2.1). Existe para que os &oacute;rg&atilde;os de registro avaliem a proposta. <strong>N&atilde;o digite dado real</strong>: nada do que se escreve aqui sai do aparelho, e a p&aacute;gina n&atilde;o tem como receber den&uacute;ncia. Para denunciar, use os <a href="index.html#denuncie">canais de den&uacute;ncia</a> {ENC}.</p>
  {PRELIMINAR}
  {RESSALVA_DEFINICAO}
  <p class="body" style="margin: 14px 0 0; max-width: 72ch">Atualizada em {DATA}. A ficha n&atilde;o contempla campo de status do caso, presente no n&uacute;cleo m&iacute;nimo e na oitava camada da taxonomia conceitual (ver <a href="taxonomia.html">taxonomia proposta</a>).</p>
</section>

<section class="wrap section" id="ficha">
  <h2 class="h2" style="max-width: 34ch">Ficha padr&atilde;o, doze blocos</h2>
  <form class="frm" id="modelo" novalidate autocomplete="off">
{chr(10).join(blocos)}
    <p class="frm-aviso" role="note">{AVISO_FORM}</p>
    <button class="btn-ink" type="submit" disabled aria-disabled="true">Enviar (desabilitado: modelo demonstrativo)</button>
  </form>
</section>

<section class="band"><div class="wrap section" id="nucleo">
  <h2 class="h2" style="max-width: 34ch">N&uacute;cleo m&iacute;nimo de interoperabilidade</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Quinze campos definidos como n&uacute;cleo m&iacute;nimo (D.2.1), para que registros de &oacute;rg&atilde;os diferentes possam ser lidos em conjunto.</p>
  <ol class="scope-list" style="margin-top: 20px; max-width: 76ch">{nucleo}</ol>
  <p class="fonte" style="margin-top: 22px">Fonte: relat&oacute;rio preliminar conjunto, vers&atilde;o 2.0, Anexo D, itens D.1 e D.2.1. Proposta em vers&atilde;o de trabalho, n&atilde;o deliberada. Nenhum &oacute;rg&atilde;o a adotou.</p>
</div></section>
"""


# ---------------------------------------------------------------------------
# T15. Inventario de canais de denuncia de crimes de odio (Anexo F). Os canais
# vem de data/relatorio-v2/canais.json, fonte unica desta pagina e do assistente.
# ---------------------------------------------------------------------------

MARCA_IHRA = ("Espec&iacute;fico de antissemitismo, sob a defini&ccedil;&atilde;o de trabalho da IHRA, "
              "divergente da emitida pelo eixo de Conceitua&ccedil;&atilde;o")


def link_canal(url, rotulo=None):
    """Endereco como link externo. O texto e o proprio endereco, para o leitor ver para onde vai."""
    return (f'<a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener" '
            f'style="overflow-wrap: anywhere">{esc(rotulo or url)}</a>')


def celula_canal(c):
    marca = f'<br><span class="fonte"><strong>{MARCA_IHRA}.</strong></span>' if c.get("especifico_antissemitismo") else ""
    return esc(c["canal"]) + marca


def linhas_canais(lista, com_uf=False):
    out = []
    for c in lista:
        l = [esc(c["orgao"]), celula_canal(c), link_canal(c["endereco"]), esc(c["verificacao"])]
        if com_uf:
            l.insert(0, esc(c["uf"]))
        out.append(l)
    return out


def destaques_canais():
    return """<ul class="scope-list" style="margin-top: 20px; max-width: 76ch">
    <li>O invent&aacute;rio foi <strong>verificado em 03/10/2026 pela coordena&ccedil;&atilde;o do Eixo 3</strong>, com uso de ferramentas web.</li>
    <li>Trata de canais de den&uacute;ncia de <strong>crimes de &oacute;dio em geral</strong>, e n&atilde;o de canais de antissemitismo.</li>
    <li>A maioria dos canais <strong>n&atilde;o abrange o antissemitismo de forma espec&iacute;fica</strong>. A exce&ccedil;&atilde;o s&atilde;o os canais da CONIB, que registram sob a defini&ccedil;&atilde;o de trabalho da IHRA, conceitualmente divergente da Defini&ccedil;&atilde;o de Antissemitismo emitida pelo eixo de Conceitua&ccedil;&atilde;o em 24/08/2026. O que se registra por esse canal n&atilde;o equivale ao antissemitismo definido pela Iniciativa.</li>
    <li>O s&iacute;tio n&atilde;o recebe den&uacute;ncia, n&atilde;o cria nem padroniza canal, e p&aacute;gina no ar n&atilde;o garante atendimento.</li>
  </ul>"""


def rico(t):
    """Texto do inventario com negrito em **: escapa e converte. Remissoes a secoes do inventario viram itens do Anexo F."""
    t = esc(t).replace("a se\u00e7\u00e3o 5", "o item F.5").replace("a se\u00e7\u00e3o 6", "o item F.6").replace("da se\u00e7\u00e3o 6", "do item F.6")
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)


def lista_e(itens):
    return itens[0] if len(itens) == 1 else ", ".join(itens[:-1]) + " e " + itens[-1]


def canais():
    d = carrega("canais.json")
    uniao = tabela("Canais da União, verificados em 03/10/2026",
                   ["&Oacute;rg&atilde;o", "Canal", "Endere&ccedil;o", "Verifica&ccedil;&atilde;o em 03/10/2026"],
                   linhas_canais(d["uniao"]))
    estados = tabela("Canais estaduais, por unidade federada, verificados em 03/10/2026",
                     ["UF", "&Oacute;rg&atilde;o", "Canal", "Endere&ccedil;o", "Verifica&ccedil;&atilde;o em 03/10/2026"],
                     linhas_canais(d["estados"], com_uf=True))
    acresc = tabela("Canais estaduais acrescentados depois do inventário",
                    ["UF", "&Oacute;rg&atilde;o", "Canal", "Endere&ccedil;o", "Situa&ccedil;&atilde;o"],
                    linhas_canais(d["acrescentados_apos_inventario"]["canais"], com_uf=True))
    sociedade = tabela("Canais da sociedade civil, verificados em 03/10/2026",
                       ["Organiza&ccedil;&atilde;o", "Canal", "Endere&ccedil;o", "Verifica&ccedil;&atilde;o em 03/10/2026"],
                       linhas_canais(d["sociedade_civil"]))
    tem = "".join(
        f'<li><strong>{esc(t["orgao"])}</strong>, {esc(t["canal"])} ({esc(t["ambito"])}): {link_canal(t["endereco"])}. {esc(t["verificacao"])}.</li>'
        for t in d["tematicos"])
    fora = "".join(
        "<li>" + (f'<code style="overflow-wrap: anywhere">{esc(f["endereco"])}</code>' if f["endereco"] else esc(f["descricao"])) + f'. {esc(f["motivo"])}.</li>'
        for f in d["fora_do_inventario"])
    contatos = ", ".join(link_canal(c["endereco"], c["organizacao"]) for c in d["contatos_gerais"])
    sem = esc("; ".join(d["sem_canal_identificado"]))
    nc = d["nao_comprovado"]
    nc_li = "".join(f"<li><strong>{esc(k)}:</strong> {esc(lista_e(v))}.</li>" for k, v in nc.items() if k != "introducao")
    limites = "".join(f"<li>{rico(x)}</li>" for x in d["limites"])
    rec = d["recomendacao_nao_deliberada"]
    crit = "".join(f"<li>{rico(x)}</li>" for x in rec["criterios"])
    return f"""{ABERTURA}
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; <a href="achados.html">Achados</a> &nbsp;/&nbsp; Invent&aacute;rio de canais</p>
  <h1 class="h1" style="margin-top: 24px">Invent&aacute;rio de canais de den&uacute;ncia de crimes de &oacute;dio</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Canais online mantidos pela Uni&atilde;o, pelos estados e por organiza&ccedil;&otilde;es da sociedade civil. Os munic&iacute;pios ficaram fora do escopo.</p>
  {destaques_canais()}
  {PRELIMINAR}
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Entra no invent&aacute;rio o canal cuja p&aacute;gina estava no ar em 3 de outubro de 2026 e cujo meio de envio foi identificado no c&oacute;digo da p&aacute;gina. <strong>Regra de leitura:</strong> aus&ecirc;ncia de evid&ecirc;ncia n&atilde;o equivale a evid&ecirc;ncia de aus&ecirc;ncia. A falta de uma unidade federada na tabela significa s&oacute; que nenhum canal foi comprovado nesta coleta. Atualizada em {DATA}. Os endere&ccedil;os servem para <a href="encaminhar.html">encaminhar</a> o caso, e este s&iacute;tio n&atilde;o &eacute; canal de den&uacute;ncia. Se houver risco agora, ligue 190.</p>
</section>

<section class="wrap section" id="uniao">
  <h2 class="h2" style="max-width: 34ch">Uni&atilde;o</h2>
  {uniao}
  <p class="body" style="margin: 18px 0 0; max-width: 74ch"><strong>Canais tem&aacute;ticos, n&atilde;o espec&iacute;ficos de crime de &oacute;dio.</strong> Entram porque recebem viol&ecirc;ncia motivada por g&ecirc;nero.</p>
  <ul class="scope-list" style="margin-top: 12px; max-width: 76ch">{tem}</ul>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch"><strong>Endere&ccedil;os testados e fora do invent&aacute;rio.</strong></p>
  <ul class="scope-list" style="margin-top: 12px; max-width: 76ch">{fora}</ul>
</section>

<section class="band"><div class="wrap section" id="estados">
  <h2 class="h2" style="max-width: 34ch">Estados</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Doze unidades federadas t&ecirc;m canal comprovado nesta coleta. Nas outras quinze, nenhum canal estadual foi comprovado, o que n&atilde;o prova que ele n&atilde;o exista.</p>
  {estados}
  <p class="body" style="margin: 18px 0 0; max-width: 74ch"><strong>P&aacute;ginas no ar sem canal de den&uacute;ncia identificado:</strong> {sem}.</p>
  <h3 class="h3" style="margin-top: 28px">Acrescentados depois do invent&aacute;rio</h3>
  <p class="body" style="margin: 12px 0 0; max-width: 74ch">{esc(d["acrescentados_apos_inventario"]["nota"])}</p>
  {acresc}
</div></section>

<section class="wrap section" id="sociedade-civil">
  <h2 class="h2" style="max-width: 34ch">Sociedade civil</h2>
  {sociedade}
  <p class="body" style="margin: 18px 0 0; max-width: 74ch"><strong>Contatos gerais, n&atilde;o canais de den&uacute;ncia.</strong> {contatos} t&ecirc;m formul&aacute;rio ou e-mail de contato, mas nenhum formul&aacute;rio de den&uacute;ncia de crime de &oacute;dio.</p>
</section>

<section class="band"><div class="wrap section" id="nao-comprovado">
  <h2 class="h2" style="max-width: 34ch">N&atilde;o comprovado nesta coleta (F.5)</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">{esc(nc["introducao"])}</p>
  <ul class="scope-list" style="margin-top: 16px; max-width: 76ch">{nc_li}</ul>
</div></section>

<section class="wrap section" id="limites">
  <h2 class="h2" style="max-width: 34ch">Limites do m&eacute;todo (F.6)</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch"><strong>Ausência de evidência não equivale a evidência de ausência.</strong></p>
  <ol class="scope-list" style="margin-top: 16px; max-width: 76ch">{limites}</ol>
</section>

<section class="band"><div class="wrap section" id="recomendacao">
  <h2 class="h2" style="max-width: 34ch">Recomenda&ccedil;&atilde;o (F.7)</h2>
  <p class="frm-aviso" role="note"><strong>Recomenda&ccedil;&atilde;o n&atilde;o deliberada.</strong> {esc(rec["aviso"])}</p>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">{esc(rec["texto"])}</p>
  <ol class="scope-list" style="margin-top: 16px; max-width: 76ch">{crit}</ol>
  <p class="fonte" style="margin-top: 22px">Fonte: {REL_V2}, se&ccedil;&atilde;o 5.4 e Anexo F. Invent&aacute;rio verificado em 03/10/2026 pela coordena&ccedil;&atilde;o do Eixo 3, com ferramentas web (arquivo {esc(d["fonte"]["arquivo"])}).</p>
</div></section>
"""


# ---------------------------------------------------------------------------
# T8. Assistente de encaminhamento. Nao recolhe dado: e uma lista, sem formulario.
# ---------------------------------------------------------------------------

# Os canais vem de data/relatorio-v2/canais.json, a mesma fonte da pagina
# canais.html. Quem decide e a competencia declarada por cada canal, nao este
# sitio. Contam como canal os grupos uniao, estados, sociedade_civil e
# tematicos. Ficam fora o que o inventario testou e excluiu
# (fora_do_inventario) e os contatos gerais de ONGs (contatos_gerais).
GRUPOS_CANAL = ("uniao", "estados", "sociedade_civil", "tematicos", "acrescentados")

NOMES_UF = {"CE": "Cear&aacute;", "DF": "Distrito Federal", "ES": "Esp&iacute;rito Santo", "GO": "Goi&aacute;s",
            "MG": "Minas Gerais", "PR": "Paran&aacute;", "RJ": "Rio de Janeiro", "RR": "Roraima",
            "RS": "Rio Grande do Sul", "SC": "Santa Catarina", "SP": "S&atilde;o Paulo", "TO": "Tocantins"}

# (chave de preservar.html, titulo, ids de canais em ordem, observacao). So
# canais federais e da sociedade civil: o fato ocorrido em um estado vai ao
# bloco por unidade federada (criterio 3 do item F.7).
ROTAS = [
    ("online", "Conte&uacute;do em rede social, site ou coment&aacute;rio", ["safernet", "pf", "mpf", "falabr", "d100", "conib"],
     "Preserve antes de denunciar: o conte&uacute;do pode ser apagado."),
    ("ameaca", "Mensagem direta, amea&ccedil;a ou intimida&ccedil;&atilde;o", ["pf", "comunicapf", "d100", "conib", "conib-fisesp"],
     "Se houver risco agora, ligue 190 antes de qualquer outra coisa. A Pol&iacute;cia Federal recebe comunica&ccedil;&atilde;o de crimes, e o fato ocorrido em um estado pode ir &agrave; Pol&iacute;cia Civil da unidade federada."),
    ("patrimonio", "Picha&ccedil;&atilde;o, dano ou profana&ccedil;&atilde;o de patrim&ocirc;nio", ["mpf", "d100", "conib"],
     "Fotografe o local antes de qualquer limpeza. O registro do fato costuma ser na Pol&iacute;cia Civil do estado."),
    ("fisica", "Agress&atilde;o f&iacute;sica, ou tentativa", ["dpu", "d100", "conib-fisesp"],
     "Se houver risco agora, ligue 190 antes de qualquer outra coisa. Procure atendimento m&eacute;dico, se for o caso. O registro do fato &eacute; na Pol&iacute;cia Civil do estado."),
    ("institucional", "Discrimina&ccedil;&atilde;o em escola, universidade ou trabalho", ["d100", "mpf", "dpu", "conib"],
     "Guarde mensagens, comunicados e nomes de testemunhas, sem expor terceiros."),
    ("objeto", "Material impresso, panfleto ou objeto deixado", ["pf", "mpf", "d100"],
     "N&atilde;o manuseie mais do que o necess&aacute;rio e fotografe onde foi encontrado."),
]


def mapa_canais():
    d = carrega("canais.json")
    d["acrescentados"] = d["acrescentados_apos_inventario"]["canais"]
    return d, {c["id"]: c for g in GRUPOS_CANAL for c in d[g]}


def item_canal(c, uf=False):
    """Item de lista: orgao, canal, endereco e a verificacao do inventario, sem texto proprio."""
    marca = f' <strong class="fonte">{MARCA_IHRA}.</strong>' if c.get("especifico_antissemitismo") else ""
    depois = ' <strong class="fonte">Acrescentado depois do invent&aacute;rio de 03/10/2026.</strong>' if c.get("acrescentado_apos_inventario") else ""
    return (f'<li><strong>{esc(c["orgao"])}</strong>, {esc(c["canal"])}: {link_canal(c["endereco"])}. '
            f'<span class="fonte">{esc(c["verificacao"])}.</span>{marca}{depois}</li>')


def encaminhar():
    d, por_id = mapa_canais()
    grade = "".join(
        f'<li><a class="prs-tipo" href="#{k}"><span class="prs-tipo-n">{i:02d}</span>'
        f'<span class="prs-tipo-t">{t}</span></a></li>' for i, (k, t, _, _) in enumerate(ROTAS, 1))
    secoes = []
    for k, titulo, canais_rota, obs in ROTAS:
        itens = "".join(item_canal(por_id[c]) for c in canais_rota)
        secoes.append(
            f'<section class="wrap section" id="{k}" style="padding-top: 0">'
            f'<h2 class="h2" style="max-width: 34ch">{titulo}</h2>'
            f'<p class="body" style="margin: 14px 0 0; max-width: 74ch">{obs}</p>'
            f'<ol class="scope-list" style="margin-top: 16px; max-width: 76ch">{itens}</ol>'
            f'<p class="fonte" style="margin-top: 14px"><a href="#estados">Canais da sua unidade federada &darr;</a> &nbsp;&middot;&nbsp; '
            f'<a href="preservar.html#{k}">Como preservar a evid&ecirc;ncia deste tipo &rarr;</a></p>'
            f'</section>')
    # todos os canais federais, temáticos federais e da sociedade civil, na ordem do inventario
    todos = "".join(item_canal(c) for c in d["uniao"] + d["sociedade_civil"] + [t for t in d["tematicos"] if t["ambito"] == "Uni\u00e3o"])
    por_uf = {}
    for c in d["estados"] + [t for t in d["tematicos"] if t["ambito"] == "Estado"] + d["acrescentados"]:
        por_uf.setdefault(c["uf"], []).append(c)
    ufs = "".join(
        f'<details style="margin-top: 12px"><summary><strong>{uf}</strong>, {NOMES_UF[uf]}</summary>'
        f'<ul class="scope-list" style="margin-top: 12px; max-width: 76ch">{"".join(item_canal(c) for c in por_uf[uf])}</ul></details>'
        for uf in sorted(por_uf))
    crit = "".join(f"<li>{rico(x)}</li>" for x in d["recomendacao_nao_deliberada"]["criterios"])
    return f"""{ABERTURA}
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Encaminhamento</p>
  <h1 class="h1" style="margin-top: 24px">Para onde encaminhar</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Escolha o tipo de incidente, ou a unidade federada, e veja os canais do <a href="canais.html">invent&aacute;rio de canais de den&uacute;ncia de crimes de &oacute;dio</a>. Primeiro os &oacute;rg&atilde;os p&uacute;blicos, depois a sociedade civil.</p>
  <ul class="scope-list" style="margin-top: 20px; max-width: 76ch">
    <li>O invent&aacute;rio foi <strong>verificado em 03/10/2026 pela coordena&ccedil;&atilde;o do Eixo 3</strong>, com uso de ferramentas web.</li>
    <li>Trata de canais de den&uacute;ncia de <strong>crimes de &oacute;dio em geral</strong>.</li>
    <li>A maioria dos canais <strong>n&atilde;o abrange o antissemitismo de forma espec&iacute;fica</strong>. A exce&ccedil;&atilde;o s&atilde;o os canais da CONIB, que registram sob a defini&ccedil;&atilde;o de trabalho da IHRA, conceitualmente divergente da Defini&ccedil;&atilde;o de Antissemitismo emitida pelo eixo de Conceitua&ccedil;&atilde;o em 24/08/2026.</li>
    <li>Este s&iacute;tio <strong>n&atilde;o recebe den&uacute;ncia</strong>, n&atilde;o cria nem padroniza canal, e p&aacute;gina no ar n&atilde;o garante atendimento.</li>
  </ul>
  <p class="frm-aviso" role="note">Esta p&aacute;gina n&atilde;o recolhe nenhum dado: a escolha do tipo ou da unidade federada &eacute; um link ou uma lista que se abre, n&atilde;o &eacute; enviada nem guardada. N&atilde;o &eacute; canal de den&uacute;ncia. Se houver risco agora, ligue 190.</p>
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">A indica&ccedil;&atilde;o segue o que o invent&aacute;rio registra, e n&atilde;o tem valida&ccedil;&atilde;o institucional. Um canal pode encaminhar o caso a outro, e n&atilde;o h&aacute;, segundo o diagn&oacute;stico do Eixo 3, &oacute;rg&atilde;o definido para den&uacute;ncias espec&iacute;ficas de antissemitismo. Fonte: {REL_V2}, se&ccedil;&atilde;o 5.4 e Anexo F.</p>
  {PRELIMINAR}
  <p class="body" style="margin: 22px 0 0; max-width: 72ch"><strong>Por tipo de incidente</strong></p>
  <ul class="prs-tipos" style="margin-top: 14px">{grade}</ul>
  <p class="body" style="margin: 14px 0 0"><a href="#estados">Por unidade federada &darr;</a> &nbsp;&middot;&nbsp; <a href="#todos">Todos os canais federais e da sociedade civil &darr;</a></p>
</section>
{"".join(secoes)}
<section class="band"><div class="wrap section" id="estados">
  <h2 class="h2" style="max-width: 34ch">Por unidade federada</h2>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Doze unidades federadas t&ecirc;m canal estadual comprovado no invent&aacute;rio. Para o fato ocorrido em um estado, a recomenda&ccedil;&atilde;o n&atilde;o deliberada &eacute; procurar o &oacute;rg&atilde;o competente para o fato, e n&atilde;o o que tem o formul&aacute;rio mais completo.</p>
  {ufs}
  <p class="body" style="margin: 22px 0 0; max-width: 74ch"><strong>Demais unidades federadas.</strong> Use as vias federais acima. A falta de canal estadual comprovado nesta coleta n&atilde;o prova que ele n&atilde;o exista.</p>
</div></section>

<section class="wrap section" id="todos">
  <h2 class="h2" style="max-width: 34ch">Todos os canais federais e da sociedade civil</h2>
  <ol class="scope-list" style="margin-top: 16px; max-width: 76ch">{todos}</ol>
</section>

<section class="band"><div class="wrap section" id="criterios">
  <h2 class="h2" style="max-width: 34ch">Crit&eacute;rios de escolha</h2>
  <p class="frm-aviso" role="note"><strong>Recomenda&ccedil;&atilde;o n&atilde;o deliberada.</strong> {esc(d["recomendacao_nao_deliberada"]["aviso"])}</p>
  <ol class="scope-list" style="margin-top: 16px; max-width: 76ch">{crit}</ol>
  <div class="pills" style="margin-top: 22px">
    <a class="pill pill-solid" href="canais.html">Invent&aacute;rio de canais &rarr;</a>
    <a class="pill" href="index.html#denuncie">Canais na capa &rarr;</a>
    <a class="pill" href="preservar.html">Preservar evid&ecirc;ncias &rarr;</a>
  </div>
</div></section>
"""


# ---------------------------------------------------------------------------
# Agenda futura: experimentos. Ideias de servico que nao fazem parte do mandato
# do Eixo 3 e dependem de decisao da coordenacao-geral. So o relogio de
# preservacao funciona, e so faz conta de data no navegador.
# ---------------------------------------------------------------------------

EXPERIMENTOS = [
    ("Verificador de número do Disque 100",
     "A pessoa escolhe um número publicado, como 2.472, e a página responde qual unidade ele declara (denúncia, violação ou caso), qual janela cobre, de qual divulgação vem e com o que não pode ser comparado.",
     "Achado A18 e página do Disque 100. Os dados já estão no sítio.",
     "Jornalistas, pesquisadores e organismos que citam esses números sem saber que a unidade muda entre divulgações.",
     "Ideia, não implementada. Esforço baixo."),
    ("Kit \"Reproduza o achado\"",
     "Publicar o método da análise dos microdados abertos do Disque 100, com os passos e os totais esperados, para que qualquer pessoa chegue aos mesmos números.",
     "Achados A29 a A32 e A35 a A37, Anexo E, item E.11.",
     "Pesquisadores no Brasil e no exterior, em versão em inglês. Dá credibilidade externa ao observatório.",
     "Ideia, não implementada. Esforço médio."),
    ("Atlas de práticas subnacionais",
     "Reunir, com fonte, as soluções específicas para o antissemitismo localizadas em estados e municípios, como o subtítulo de intolerância religiosa nos registros do Rio de Janeiro e a formação de servidores no Paraná.",
     "Achados A19 e A20 e o Achado 13, sobre a coordenação.",
     "Gestores públicos que queiram conhecer o que já existe.",
     "Ideia, não implementada. Hoje há poucos itens verificados, e a página ficaria rala."),
    ("Roteiro de protocolo de ameaça a instituição",
     "Lista de passos para uma instituição religiosa ou comunitária que receba ameaça, na falta de protocolo nacional.",
     "Achado A21, que registra a ausência de protocolo nacional.",
     "Instituições comunitárias.",
     "Ideia, fora do mandato do Eixo 3, que levanta limitações e não cria protocolo. Só com decisão da coordenação-geral."),
]


def agenda_futura():
    cartoes = "".join(
        f'<li><strong>{esc(t)}.</strong> {esc(o)} <span class="fonte">Base: {esc(b)} Interesse: {esc(q)} Situação: {esc(e)}</span></li>'
        for t, o, b, q, e in EXPERIMENTOS)
    return f"""{ABERTURA}
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Agenda futura</p>
  <h1 class="h1" style="margin-top: 24px">Agenda futura: experimentos</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Servi&ccedil;os que o observat&oacute;rio poderia oferecer a partir dos achados, e que ainda n&atilde;o fazem parte dele. S&atilde;o ideias e experimentos, e n&atilde;o recomenda&ccedil;&otilde;es do Eixo.</p>
  <ul class="scope-list" style="margin-top: 20px; max-width: 76ch">
    <li><strong>N&atilde;o deliberados.</strong> O Eixo 3 levanta limita&ccedil;&otilde;es e sugere ajustes pontuais. Servi&ccedil;o novo amplia o escopo, e entra na pauta s&oacute; por decis&atilde;o da coordena&ccedil;&atilde;o-geral.</li>
    <li><strong>N&atilde;o recolhem dado.</strong> Nenhum envia, grava ou lembra o que se digita.</li>
    <li><strong>N&atilde;o s&atilde;o orienta&ccedil;&atilde;o jur&iacute;dica</strong> nem canal de den&uacute;ncia.</li>
  </ul>
  {PRELIMINAR}
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Atualizada em {DATA}. Fonte: achados do {REL_V2}, e nota t&eacute;cnica do Eixo 3 de 04/10/2026 sobre o rel&oacute;gio de preserva&ccedil;&atilde;o, em revis&atilde;o jur&iacute;dica.</p>
</section>

<section class="wrap section" id="relogio-preservacao">
  <p class="eyebrow">Experimento em funcionamento</p>
  <h2 class="h2" style="max-width: 34ch">Rel&oacute;gio de preserva&ccedil;&atilde;o</h2>
  <p class="frm-aviso" role="note">Experimento em revis&atilde;o jur&iacute;dica. O c&aacute;lculo &eacute; uma estimativa de car&aacute;ter informativo e n&atilde;o substitui advogado, Defensoria P&uacute;blica, registro de ocorr&ecirc;ncia nem ata notarial. Se houver risco agora, ligue 190.</p>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">A lei obriga certos provedores a guardar registros por tempo limitado, e depois o registro deve ser exclu&iacute;do. Informe a data e veja at&eacute; quando, em tese, o registro existe. O achado A24 mostra que n&atilde;o h&aacute; padr&atilde;o p&uacute;blico de preserva&ccedil;&atilde;o nos &oacute;rg&atilde;os de recebimento.</p>
  <div class="frm" style="margin-top: 18px; max-width: 46ch">
    <label class="frm-campo" for="rel-data"><span>Data da postagem, se souber. Se n&atilde;o, a data em que voc&ecirc; viu o conte&uacute;do</span><input id="rel-data" type="date" autocomplete="off"></label>
    <button class="btn-ink" type="button" id="rel-calcular">Calcular</button>
    <div id="rel-saida" aria-live="polite"></div>
    <noscript><p class="body">O c&aacute;lculo precisa de JavaScript. Nada &eacute; enviado.</p></noscript>
  </div>
  <h3 class="h3" style="margin-top: 30px">O que isto calcula e o que n&atilde;o faz</h3>
  <ul class="scope-list" style="margin-top: 12px; max-width: 76ch">
    <li>Calcula a data at&eacute; a qual a lei obriga o provedor a guardar os registros de acesso a aplica&ccedil;&otilde;es (6 meses) e de conex&atilde;o (1 ano), contados da cria&ccedil;&atilde;o de cada registro, de data a data. Se o dia n&atilde;o existir no m&ecirc;s final, usa o &uacute;ltimo dia do m&ecirc;s, que &eacute; a leitura mais cedo.</li>
    <li>N&atilde;o guarda o conte&uacute;do. A guarda recai sobre registros, e n&atilde;o sobre o que foi publicado.</li>
    <li>N&atilde;o vale para provedor sem estabelecimento no Pa&iacute;s: o acesso a registros dele segue a coopera&ccedil;&atilde;o internacional, em regra a Conven&ccedil;&atilde;o de Budapeste, e pode n&atilde;o existir pelo caminho nacional.</li>
    <li>Quem pede ao provedor que guarde os registros por mais tempo &eacute; a autoridade policial, administrativa ou o Minist&eacute;rio P&uacute;blico, e n&atilde;o o particular. O particular pode ir a ju&iacute;zo, por advogado ou pela Defensoria, para pedir o fornecimento. A prorroga&ccedil;&atilde;o n&atilde;o recupera registro j&aacute; exclu&iacute;do.</li>
    <li>Existem outros prazos, como o de decad&ecirc;ncia do direito de representa&ccedil;&atilde;o em certos crimes. Este experimento n&atilde;o os calcula.</li>
  </ul>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">O que fazer antes da data: <a href="preservar.html">preserve o conte&uacute;do</a>, registre a ocorr&ecirc;ncia na Pol&iacute;cia, no Minist&eacute;rio P&uacute;blico ou no canal que o <a href="encaminhar.html">assistente de encaminhamento</a> indicar, e guarde o protocolo.</p>
  <p class="fonte" style="margin-top: 22px">Regra de c&aacute;lculo e d&uacute;vidas jur&iacute;dicas: nota t&eacute;cnica do Eixo 3, 04/10/2026. O termo inicial n&atilde;o est&aacute; fixado em lei nem em decreto: a contagem desde a cria&ccedil;&atilde;o do registro &eacute; decis&atilde;o de trabalho do Eixo, sujeita &agrave; revis&atilde;o jur&iacute;dica.</p>
</section>

<section class="band"><div class="wrap section" id="outros-experimentos">
  <p class="eyebrow">Ideias, ainda n&atilde;o implementadas</p>
  <h2 class="h2" style="max-width: 34ch">Outros experimentos considerados</h2>
  <ul class="scope-list" style="margin-top: 20px; max-width: 80ch">{cartoes}</ul>
  <p class="body" style="margin: 22px 0 0; max-width: 74ch">Qualquer um deles pode ser objeto de pesquisa acad&ecirc;mica e de decis&atilde;o da coordena&ccedil;&atilde;o-geral. Nenhum depende de coleta de dado pessoal.</p>
</div></section>
"""


def main():
    feitos = [
        pagina("achados.html", "Achados das Frentes 1 e 2",
               "Achados do relatorio preliminar conjunto das Frentes 1 e 2 do Eixo 3, com fonte e grau de confianca. Documento preliminar.",
               "achados.html", achados()),
        pagina("disque100.html", "Disque 100",
               "O que a base do Disque 100 mede e o que nao mede: unidade, janela e divulgacao de origem de cada numero. Documento preliminar.",
               "", disque100()),
        pagina("bases.html", "Mapa das bases e canais",
               "Quadro das bases e canais examinados pelo Eixo 3: categoria autonoma de antissemitismo, categoria mais proxima, unidade de contagem e desfecho rastreavel. Documento preliminar.",
               "", bases()),
        pagina("formulario-modelo.html", "Modelo de formulário",
               "Modelo demonstrativo da ficha padrao de registro e do nucleo minimo de interoperabilidade. Nao e canal de denuncia, nao envia e nao guarda informacao.",
               "", formulario_modelo(), scripts=("js/formulario-modelo.js",)),
        pagina("agenda-futura.html", "Agenda futura: experimentos",
               "Experimentos e ideias de servico a partir dos achados, nao deliberados: relogio de preservacao e outras propostas. Nao recolhe dado.",
               "", agenda_futura(), scripts=("js/relogio.js",)),
        pagina("canais.html", "Inventário de canais de denúncia de crimes de ódio",
               "Inventario de canais online de denuncia de crimes de odio no Brasil, verificado em 03/10/2026: Uniao, estados e sociedade civil. Documento preliminar.",
               "", canais()),
        pagina("encaminhar.html", "Para onde encaminhar",
               "Indica, por tipo de incidente e por unidade federada, os canais do inventario de 03/10/2026. Nao recolhe dado.",
               "", encaminhar()),
    ]
    print("paginas das Frentes 1 e 2: " + ", ".join(feitos))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
