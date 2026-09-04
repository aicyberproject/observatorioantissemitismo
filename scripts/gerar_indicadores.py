#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera indicadores.html a partir das series conferidas no acervo.

Os numeros ficam declarados aqui, em estruturas Python, e a geometria dos
graficos e calculada, nao desenhada a mao. Rodar de novo depois de atualizar
uma serie reproduz a pagina inteira.

    python3 scripts/gerar_indicadores.py
"""
import html
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent

# Paleta de graficos. Os dois tons passam os seis testes do validador sobre o
# papel #F5F3EF: faixa de luminosidade, piso de croma, separacao para daltonismo,
# piso de visao normal e contraste de 3:1.
S1 = "#1f5fae"   # serie 1
S2 = "#c2531f"   # serie 2
# Cinza de recuo. Nao e uma terceira categoria: e o "destacar um, recuar o resto"
# em barra de serie unica. Passa 3:1 sobre o papel e fica bem separado de S1.
NEUTRO = "#8C837A"
GRID = "#DCD6CC"
EIXO = "#B8B0A6"
TINTA = "#15120F"
PAPEL = "#F5F3EF"

# --------------------------------------------------------------------------
# Series. Cada bloco declara a fonte e o grau de verificacao.
# --------------------------------------------------------------------------

ANUAL = [
    # ano, total, online, offline
    (2022, 397, 202, 195),
    (2023, 1412, 1049, 363),
    (2024, 1788, 1310, 478),
    (2025, 989, 800, 189),
]

MESES = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
         "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

MENSAL = {
    2022: [42, 59, 24, 27, 13, 23, 14, 42, 28, 33, 73, 19],
    2023: [25, 19, 30, 45, 31, 31, 32, 44, 34, 388, 539, 192],
    2024: [175, 323, 236, 178, 143, 98, 88, 106, 112, 151, 116, 62],
}

GEO_2025 = [
    ("Sem estado informado", 462),
    ("São Paulo", 238),
    ("Demais estados", 126),
    ("Rio de Janeiro", 100),
    ("Rio Grande do Sul", 63),
]

GEO_2024 = [
    ("São Paulo", 900),
    ("Rio de Janeiro", 440),
    ("Demais estados", 170),
    ("Rio Grande do Sul", 146),
    ("Não definido", 132),
]

PLATAFORMA_2025 = [
    ("Instagram", 297), ("Não categorizadas", 151), ("X (Twitter)", 111),
    ("Facebook", 93), ("YouTube", 54), ("WhatsApp", 33), ("Threads", 27),
    ("TikTok", 15), ("Telegram", 12), ("Bluesky", 5), ("Discord", 2),
]

PLATAFORMA_2024 = [
    ("X (Twitter)", 402), ("Instagram", 314), ("Facebook", 103),
    ("Telegram", 17), ("LinkedIn", 10),
]

TRIAGEM_2025 = [
    ("Validadas como antissemitismo", 989),
    ("Sem conteúdo antissemita identificado", 216),
    ("Registro em duplicidade", 141),
    ("Informação insuficiente sobre o fato", 68),
    ("Avaliações inconclusivas", 14),
]

FUNIL_MPF = [
    ("Denúncias de neonazismo recebidas", 2774),
    ("Arquivadas por falta de materialidade", 2261),
    ("Procedimentos instaurados no MPF", 255),
    ("Remoções administrativas por provedores", 204),
    ("Remetidas a Ministérios Públicos estaduais", 54),
]

INSTAURACAO = [
    ("Neonazismo", 2774, 255),
    ("Intolerância religiosa", 2575, 58),
    ("Racismo em geral", 7210, 161),
]

# Matriz Nacional de KPIs (Anexo III), com o motivo de cada indicador estar vazio.
SEM_FONTE = "sem fonte"
AGUARDA = "aguardando marcador"
VEDADO = "vedado por segredo de justiça"
PARCIAL = "cobertura parcial"

KPIS = [
    ("Total de denúncias", "Sistema nacional", PARCIAL,
     "Existe pela via da sociedade civil (CONIB/FISESP/DSC). Não existe em base estatal."),
    ("Taxa por 100 mil habitantes", "Sistema + IBGE", PARCIAL,
     "Calculável sobre a série da sociedade civil, com a subnotificação embutida."),
    ("% de casos online", "Sistema nacional", PARCIAL,
     "Disponível na série da sociedade civil desde 2022."),
    ("% por modalidade", "Sistema nacional", AGUARDA,
     "Depende da taxonomia nacional, ainda não adotada pelas bases de entrada."),
    ("% de casos de alto risco", "Sistema nacional", AGUARDA,
     "Nenhuma base de entrada classifica risco em quatro níveis."),
    ("Nº de ameaças a instituições", "Sistema nacional", AGUARDA,
     "Não há campo que distinga alvo institucional de alvo individual."),
    ("Nº de casos com indício de extremismo", "Sistema nacional", SEM_FONTE,
     "Depende de análise de inteligência não publicada em série."),
    ("Tempo médio de triagem", "Sistema nacional", SEM_FONTE,
     "Nenhum canal publica marcas de tempo de triagem."),
    ("Tempo médio de encaminhamento", "Sistema nacional", SEM_FONTE,
     "Idem. Exigiria interoperabilidade entre receptor e órgão de destino."),
    ("% de registros completos", "Sistema nacional", SEM_FONTE,
     "Métrica interna de qualidade de base, não publicada."),
    ("% com evidência preservada", "Sistema nacional", SEM_FONTE,
     "Não há campo de preservação de evidência nas bases examinadas."),
    ("Nº de instituições com protocolo preventivo", "MEC + parceiros", SEM_FONTE,
     "Depende de levantamento junto ao Eixo de Educação."),
    ("Nº de capacitações realizadas", "MEC/ENAP/PF", SEM_FONTE,
     "Depende de D17 e da interface com o Eixo de Educação."),
    ("Nº de pessoas capacitadas", "Instituições parceiras", SEM_FONTE,
     "Idem."),
    ("Índice de recorrência", "Sistema nacional", VEDADO,
     "Exige identificar autoria reincidente, sob reserva de jurisdição."),
    ("Nº de casos com simbologia neonazista", "Sistema nacional", PARCIAL,
     "Proxy disponível no Report System SaferNet/MPF, sem recorte de antissemitismo."),
    ("Nº de casos conspiratórios", "Sistema nacional", AGUARDA,
     "Depende da taxonomia de conteúdo, hoje inexistente na entrada."),
    ("Nº de episódios híbridos", "Sistema nacional", AGUARDA,
     "Depende de campo que registre ocorrência simultânea online e offline."),
    ("% de casos com retorno ao denunciante", "Sistema nacional", SEM_FONTE,
     "Métrica de atendimento, não publicada por nenhum canal."),
    ("Índice de interoperabilidade", "Coordenação da Iniciativa", SEM_FONTE,
     "Depende de decisão de governança ainda não tomada."),
]

# Relatorio CONIB 2025 na integra, publico. Todos os valores da serie foram
# conferidos contra este documento, e nao apenas contra o Sumario Executivo.
CONIB25 = ("https://combateaoantissemitismo.org.br/wp-content/uploads/2026/04/"
           "Relatorio_Antissemitismo-no-Brasil-2025-FULL-PORT_vOK3_web.pdf")
LINK25 = (f'<a href="{CONIB25}" target="_blank" rel="noopener">'
          'Relat&oacute;rio de Antissemitismo no Brasil 2025</a>')

FMT = lambda n: f"{n:,}".replace(",", ".")
E = lambda s: html.escape(str(s), quote=True)


# --------------------------------------------------------------------------
# Desenho
# --------------------------------------------------------------------------

def escala_topo(maximo, passos=4):
    """Arredonda o topo do eixo para um numero limpo."""
    import math
    if maximo <= 0:
        return 1, [0]
    bruto = maximo / passos
    mag = 10 ** math.floor(math.log10(bruto))
    for m in (1, 2, 2.5, 5, 10):
        if mag * m >= bruto:
            passo = mag * m
            break
    topo = passo * passos
    return topo, [int(passo * i) for i in range(passos + 1)]


def svg_linha_mensal():
    """Serie mensal 2022-2024, uma serie, linha de 2px."""
    valores, rotulos = [], []
    for ano in (2022, 2023, 2024):
        for i, v in enumerate(MENSAL[ano]):
            valores.append(v)
            rotulos.append(f"{MESES[i]}/{ano}")
    W, H = 900, 320
    ml, mr, mt, mb = 52, 16, 20, 40
    pw, ph = W - ml - mr, H - mt - mb
    topo, ticks = escala_topo(max(valores))
    n = len(valores)
    px = lambda i: ml + (pw * i / (n - 1))
    py = lambda v: mt + ph - (ph * v / topo)

    p = [f"<svg class=\"viz\" style=\"min-width:{W}px\" viewBox=\"0 0 {W} {H}\" role=\"img\" "
         f"aria-label=\"Denúncias mês a mês de janeiro de 2022 a dezembro de 2024\">"]
    for t in ticks:
        y = py(t)
        p.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{W-mr}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
        p.append(f'<text class="tick" x="{ml-10}" y="{y+4:.1f}" text-anchor="end">{FMT(t)}</text>')
    # separadores de ano e rotulos
    for k, ano in enumerate((2022, 2023, 2024)):
        x0 = px(k * 12)
        if k:
            p.append(f'<line x1="{x0:.1f}" y1="{mt}" x2="{x0:.1f}" y2="{mt+ph}" stroke="{EIXO}" stroke-width="1"/>')
        p.append(f'<text class="tick" x="{px(k*12+5.5):.1f}" y="{H-12}" text-anchor="middle">{ano}</text>')
    d = " ".join(("M" if i == 0 else "L") + f"{px(i):.1f} {py(v):.1f}" for i, v in enumerate(valores))
    p.append(f'<path d="{d}" fill="none" stroke="{S1}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
    # pico direto: novembro de 2023
    ip = valores.index(max(valores))
    p.append(f'<circle cx="{px(ip):.1f}" cy="{py(valores[ip]):.1f}" r="4.5" fill="{S1}" stroke="{PAPEL}" stroke-width="2"/>')
    p.append(f'<text class="dlabel" x="{px(ip):.1f}" y="{py(valores[ip])-14:.1f}" text-anchor="middle">'
             f'{FMT(valores[ip])} em nov/2023</text>')
    # camada de leitura por ponto
    for i, v in enumerate(valores):
        p.append(f'<rect class="hit" x="{px(i)-pw/(n-1)/2:.1f}" y="{mt}" width="{pw/(n-1):.1f}" height="{ph}" '
                 f'fill="transparent" data-t="{E(rotulos[i])}" data-v="{FMT(v)} denúncias"><title>'
                 f'{E(rotulos[i])}: {FMT(v)} denúncias</title></rect>')
    p.append("</svg>")
    return "\n".join(p)


def svg_colunas_anuais():
    """Online e offline por ano, colunas empilhadas, duas series."""
    W, H = 760, 360
    ml, mr, mt, mb = 56, 16, 30, 46
    pw, ph = W - ml - mr, H - mt - mb
    topo, ticks = escala_topo(max(t for _, t, _, _ in ANUAL))
    banda = pw / len(ANUAL)
    larg = min(24, banda * 0.42)
    p = [f'<svg class="viz" style="min-width:{W}px" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="Ocorrências validadas por ano, separadas entre ambiente online e offline">']
    for t in ticks:
        y = mt + ph - ph * t / topo
        p.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{W-mr}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
        p.append(f'<text class="tick" x="{ml-10}" y="{y+4:.1f}" text-anchor="end">{FMT(t)}</text>')
    for i, (ano, total, on, off) in enumerate(ANUAL):
        cx = ml + banda * (i + .5)
        x = cx - larg / 2
        h_on = ph * on / topo
        h_off = ph * off / topo
        y_off = mt + ph - h_off
        y_on = y_off - h_on - 2          # 2px de papel separando os dois trechos
        p.append(f'<rect class="hit" x="{x:.1f}" y="{y_off:.1f}" width="{larg:.1f}" height="{h_off:.1f}" '
                 f'fill="{S2}" data-t="{ano} · offline" data-v="{FMT(off)} ocorrências">'
                 f'<title>{ano}, offline: {FMT(off)}</title></rect>')
        p.append(f'<rect class="hit" x="{x:.1f}" y="{y_on:.1f}" width="{larg:.1f}" height="{h_on:.1f}" rx="4" '
                 f'fill="{S1}" data-t="{ano} · online" data-v="{FMT(on)} ocorrências">'
                 f'<title>{ano}, online: {FMT(on)}</title></rect>')
        p.append(f'<text class="dlabel" x="{cx:.1f}" y="{y_on-10:.1f}" text-anchor="middle">{FMT(total)}</text>')
        p.append(f'<text class="tick" x="{cx:.1f}" y="{H-16}" text-anchor="middle">{ano}</text>')
    p.append("</svg>")
    return "\n".join(p)


def svg_barras(dados, destaque=None, unidade="ocorrências", altura_barra=26,
               rotulo_eixo="", formato=None):
    """Barras horizontais, uma serie. Valor na ponta.

    Quando ha destaque, a barra em foco fica na cor da serie e as demais recuam
    para o cinza: destacar uma e recuar o resto, e nao introduzir uma segunda
    categoria de cor que ja significa outra coisa no grafico empilhado.

    A calha dos rotulos e medida a partir do rotulo mais longo, para que nenhum
    texto seja cortado. O viewBox cresce junto, em vez de espremer o desenho.
    """
    n = len(dados)
    mr, mt = 70, 8
    # 7,3 px por caractere aproxima Work Sans em 13px; 24 px de respiro.
    ml = max(150, min(360, int(max(len(r) for r, _ in dados) * 7.3) + 24))
    pw = 470
    W = ml + pw + mr
    H = mt + n * altura_barra + 8 + (22 if rotulo_eixo else 0)
    maxv = max(v for _, v in dados)
    fmt = formato or FMT
    alvo = E(rotulo_eixo or "Distribuição por categoria")
    p = [f'<svg class="viz" style="min-width:{W}px" viewBox="0 0 {W} {H}" '
         f'role="img" aria-label="{alvo}">']
    for i, (rot, v) in enumerate(dados):
        y = mt + i * altura_barra
        larg = pw * v / maxv
        alt = min(18, altura_barra - 8)
        cor = S1 if (not destaque or rot in destaque) else NEUTRO
        p.append(f'<text class="cat" x="{ml-14}" y="{y+alt/2+4:.1f}" text-anchor="end">{E(rot)}</text>')
        p.append(f'<rect class="hit" x="{ml}" y="{y:.1f}" width="{max(larg,2):.1f}" height="{alt}" rx="4" '
                 f'fill="{cor}" data-t="{E(rot)}" data-v="{fmt(v)} {unidade}">'
                 f'<title>{E(rot)}: {fmt(v)}</title></rect>')
        p.append(f'<text class="dlabel" x="{ml+larg+10:.1f}" y="{y+alt/2+4:.1f}">{fmt(v)}</text>')
    p.append("</svg>")
    return "\n".join(p)


def tabela(cab, linhas, cls="tab-dados"):
    h = [f'<table class="{cls}"><thead><tr>']
    for i, c in enumerate(cab):
        al = ' class="num"' if i else ""
        h.append(f"<th{al}>{E(c)}</th>")
    h.append("</tr></thead><tbody>")
    for ln in linhas:
        h.append("<tr>")
        for i, c in enumerate(ln):
            al = ' class="num"' if i else ""
            h.append(f"<td{al}>{c}</td>")
        h.append("</tr>")
    h.append("</tbody></table>")
    return "".join(h)


def figura(titulo, subtitulo, svg, tab, nota, legenda=None, id_=None, nat=None):
    leg = ""
    if legenda:
        itens = "".join(
            f'<span class="key"><span class="swatch" style="background:{c}"></span>{E(r)}</span>'
            for r, c in legenda)
        leg = f'<div class="legend">{itens}</div>'
    ident = f' id="{id_}"' if id_ else ""
    return f"""<figure class="fig"{ident}>
  <figcaption>
    <h3 class="fig-title">{titulo}</h3>
    {natureza(nat) if nat else ""}
    <p class="fig-sub">{subtitulo}</p>
  </figcaption>
  {leg}
  <div class="viz-wrap">{svg}</div>
  <details class="tabela"><summary>Ver os números em tabela</summary>{tab}</details>
  <p class="fonte">{nota}</p>
</figure>"""


# --------------------------------------------------------------------------
# Montagem da pagina
# --------------------------------------------------------------------------

CAB = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="status" content="prototipo">
<title>Indicadores &middot; Prot&oacute;tipo do Observat&oacute;rio</title>
<meta name="description" content="Indicadores de antissemitismo no Brasil a partir de fontes secund&aacute;rias publicadas, e o painel das lacunas que nenhuma base hoje preenche.">
<meta name="author" content="Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento">
<meta name="theme-color" content="#F5F3EF">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Prot&oacute;tipo &middot; Observat&oacute;rio do Antissemitismo no Brasil">
<meta property="og:title" content="Indicadores &middot; Prot&oacute;tipo do Observat&oacute;rio">
<meta property="og:description" content="O que hoje &eacute; mensur&aacute;vel, e o que n&atilde;o &eacute;.">
<link rel="canonical" href="https://aicyberproject.github.io/observatorioantissemitismo/indicadores.html">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Work+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="alternate" type="application/rss+xml" title="Boletim do Observat&oacute;rio" href="boletim/feed.xml">
<link rel="stylesheet" href="css/main.css">
<link rel="stylesheet" href="css/indicadores.css">
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
    <a class="brand" href="index.html#topo">
      <span class="brand-mark" aria-hidden="true"></span>
      <span>
        <span class="brand-name">Observat&oacute;rio do Antissemitismo</span>
        <span class="brand-sub">Prot&oacute;tipo &middot; Eixo 3, Seguran&ccedil;a e Monitoramento</span>
      </span>
    </a>
    <div class="header-actions">
      <a class="btn-solid" href="index.html#denuncie">Denunciar</a>
    </div>
  </div>
  <nav class="wrap nav" aria-label="Navega&ccedil;&atilde;o principal"><a href="index.html#painel">Painel</a><a href="indicadores.html" aria-current="page">Indicadores</a><a href="boletim/index.html">Boletim</a><a href="index.html#preservar">Preservar evid&ecirc;ncias</a><a href="index.html#denuncie">Denunciar</a><a href="index.html#legislacao">Legisla&ccedil;&atilde;o</a><a href="biblioteca.html">Biblioteca</a><a href="sobre.html">Sobre</a></nav>
</header>
<main>
"""

RODAPE = """</main>
<footer class="footer">
  <div class="wrap footer-inner">
    <div class="footer-cols">
      <div>
        <p class="footer-brand">Observat&oacute;rio do Antissemitismo</p>
        <p class="footer-text">Plataforma p&uacute;blica de monitoramento de incidentes, orienta&ccedil;&atilde;o jur&iacute;dica, canais de den&uacute;ncia e preserva&ccedil;&atilde;o de provas.</p>
        <p class="footer-org">Prot&oacute;tipo em elabora&ccedil;&atilde;o no Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento, no &acirc;mbito da Iniciativa de Enfrentamento ao Antissemitismo. Documento de trabalho, sem car&aacute;ter oficial e sem valida&ccedil;&atilde;o do CDESS ou da Presid&ecirc;ncia da Rep&uacute;blica.</p>
      </div>
      <div>
        <p class="footer-head">Navega&ccedil;&atilde;o</p>
        <nav><a href="index.html#topo">In&iacute;cio</a><a href="index.html#painel">Painel</a><a href="indicadores.html">Indicadores</a><a href="boletim/index.html">Boletim</a><a href="index.html#preservar">Preservar evid&ecirc;ncias</a><a href="index.html#denuncie">Denunciar</a><a href="index.html#legislacao">Legisla&ccedil;&atilde;o</a><a href="biblioteca.html">Biblioteca</a><a href="index.html#sobre">Sobre</a></nav>
      </div>
      <div>
        <p class="footer-head">Institucional</p>
        <nav><a href="sobre.html">Sobre o Observat&oacute;rio</a><a href="privacidade.html">Pol&iacute;tica de privacidade</a><a href="termos.html">Termos de uso</a><a href="boletim/feed.xml">Feed RSS</a><a href="indicadores.html#dados">Dados abertos</a></nav>
      </div>
    </div>
    <p class="footer-legal">&copy; 2026 Observat&oacute;rio do Antissemitismo no Brasil &middot; Prot&oacute;tipo, vers&atilde;o de trabalho &middot; C&oacute;digo e conte&uacute;do sob licen&ccedil;a MIT</p>
  </div>
</footer>
<div class="lgpd" id="lgpd" hidden>
  <div class="wrap lgpd-inner">
    <div class="lgpd-text">
      <p class="eyebrow">Prote&ccedil;&atilde;o de dados &middot; LGPD</p>
      <p>Este portal utiliza apenas armazenamento local para prefer&ecirc;ncias de exibi&ccedil;&atilde;o. O tratamento de dados pessoais observa a Lei Geral de Prote&ccedil;&atilde;o de Dados. Nenhum dado pessoal, den&uacute;ncia ou identifica&ccedil;&atilde;o de v&iacute;tima consta desta p&aacute;gina: todos os n&uacute;meros s&atilde;o agregados e de origem p&uacute;blica.</p>
    </div>
    <button class="btn-ink" id="lgpd-ok" type="button">Entendido</button>
  </div>
</div>
<script src="js/app.js" defer></script>
<script src="js/indicadores.js" defer></script>
</body>
</html>
"""


# Natureza do dado, no modelo do ODIHR. Aquele organismo mantem dois acervos
# separados e nunca os soma: o que vem do Estado e registrado como "crimes", o que
# vem de sociedade civil como "incidents", com a razao declarada de que nao consegue
# verificar se o segundo grupo se qualifica como crime.
#
# Aqui a mesma disciplina. A serie da CONIB e contagem comunitaria; o Anuario do
# FBSP e dado policial estadual; a ADL e apuracao de outro pais; a G100 e pesquisa
# de percepcao. Somar ou comparar diretamente numeros de naturezas distintas e o
# erro que a ausencia de marcador estatal torna tentador.
NATUREZAS = {
    "comunitaria": ("contagem de fonte comunitária",
                    "Apurado por entidade da sociedade civil a partir de denúncia recebida em canal próprio. "
                    "Mede o que chega ao canal, não a incidência."),
    "oficial": ("registro oficial agregado",
                "Produzido por órgão público a partir de registro administrativo ou policial. "
                "Nenhuma base estatal brasileira possui categoria autônoma de antissemitismo."),
    "imprensa": ("monitoramento de imprensa",
                 "Derivado de cobertura jornalística agregada. Mede alcance da cobertura, não incidência."),
    "percepcao": ("pesquisa de percepção",
                  "Levantamento amostral de atitudes declaradas. Não conta ocorrências."),
    "externa": ("apuração de outra jurisdição",
                "Produzido em outro país, com definição, canais e população distintos. "
                "Serve para ordem de grandeza e para leitura de instrumento, não para comparação de volume."),
}


def natureza(chave):
    rot, exp = NATUREZAS[chave]
    return (f'<span class="nat nat-{chave}" title="{E(exp)}">{rot}</span>')


def selo(grau):
    cls = {"verificado": "sel-ok", "citado": "sel-cit", "lacuna": "sel-lac"}[grau]
    txt = {"verificado": "conferido no acervo",
           "citado": "citado, primária não consultada",
           "lacuna": "lacuna"}[grau]
    return f'<span class="selo {cls}">{txt}</span>'


def main():
    out = [CAB]

    # ---------------- abertura ----------------
    out.append(f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Indicadores</p>
  <h1 class="h1" style="margin-top: 24px">Indicadores e KPIs</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Esta p&aacute;gina tem duas camadas. A primeira re&uacute;ne o que hoje &eacute; mensur&aacute;vel, a partir de relat&oacute;rios p&uacute;blicos j&aacute; publicados. A segunda re&uacute;ne o que n&atilde;o &eacute;: a matriz de indicadores proposta pelo Eixo 3, com o motivo de cada campo estar vazio.</p>
  <p class="lead" style="margin: 16px 0 0; max-width: 70ch">A segunda camada &eacute; a mais importante. O achado central do Eixo 3 &eacute; que n&atilde;o se trata de aus&ecirc;ncia de fen&ocirc;meno, mas de aus&ecirc;ncia de instrumento de medida. A lacuna, aqui, &eacute; o resultado.</p>
</section>

<section class="metrics-band"><div class="wrap"><div class="metrics">
  <div class="metric"><p class="label">Ocorr&ecirc;ncias validadas</p><p class="num">989</p><p class="metric-note">em 2025 · de 1.428 registros recebidos</p></div>
  <div class="metric"><p class="label">Varia&ccedil;&atilde;o</p><p class="num">+149%</p><p class="metric-note">sobre 2022, quando foram 397</p></div>
  <div class="metric"><p class="label">Meio</p><p class="num">80,9%</p><p class="metric-note">ocorr&ecirc;ncias no ambiente digital</p></div>
  <div class="metric"><p class="label">Frequ&ecirc;ncia</p><p class="num">2,7</p><p class="metric-note">ocorr&ecirc;ncias validadas por dia</p></div>
</div>
<p class="metrics-src">{LINK25} &mdash; CONIB, FISESP e Departamento de Seguran&ccedil;a Comunit&aacute;ria. {selo("verificado")} {natureza("comunitaria")}</p>
</div></section>

<section class="wrap section">
  <p class="eyebrow">Camada 1 &middot; O que hoje &eacute; mensur&aacute;vel</p>
  <h2 class="h2">S&eacute;ries de fonte secund&aacute;ria</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">Nenhum n&uacute;mero desta camada &eacute; produzido pelo Observat&oacute;rio. Todos v&ecirc;m de relat&oacute;rios publicados por terceiros, com ano de refer&ecirc;ncia e base de c&aacute;lculo declarados. Onde a compara&ccedil;&atilde;o entre anos n&atilde;o &eacute; leg&iacute;tima, o texto diz por qu&ecirc;.</p>
</section>
""")

    # ---------------- serie mensal ----------------
    linhas = []
    for i, mes in enumerate(MESES):
        linhas.append([mes] + [FMT(MENSAL[a][i]) for a in (2022, 2023, 2024)])
    linhas.append(["<strong>Total</strong>"] + [f"<strong>{FMT(sum(MENSAL[a]))}</strong>" for a in (2022, 2023, 2024)])
    out.append('<div class="wrap section" style="padding-top:0">')
    out.append(figura(
        "Denúncias mês a mês, 2022 a 2024",
        "Série mensal contínua. O eixo do tempo mostra o degrau de outubro e novembro de 2023 e a permanência do patamar ao longo de 2024.",
        svg_linha_mensal(),
        tabela(["Mês", "2022", "2023", "2024"], linhas),
        f'Fonte: Relatório de Antissemitismo no Brasil 2024 — CONIB, FISESP e DSC. {selo("verificado")} '
        f'A série mensal de 2025 não consta do {LINK25} e por isso não foi incluída.',
        id_="serie-mensal", nat="comunitaria"))

    # ---------------- colunas anuais ----------------
    linhas = [[str(a), FMT(t), FMT(on), FMT(off), f"{on/t*100:.1f}%"] for a, t, on, off in ANUAL]
    out.append(figura(
        "Ocorrências validadas por ano e por ambiente",
        "Quatro anos completos. A retração de 2025 devolve o volume a um patamar acima do de 2022 e abaixo do pico de 2024. A participação do ambiente digital continuou subindo mesmo com a queda do total.",
        svg_colunas_anuais(),
        tabela(["Ano", "Total", "Online", "Offline", "% online"], linhas),
        f'Fontes: Relatório de Antissemitismo no Brasil 2024 e {LINK25}, CONIB, FISESP e DSC. {selo("verificado")} '
        'O total de 2023 aparece como 1.410 no relatório de 2024 e como 1.412 no de 2025. Adotou-se o valor revisado. '
        'A própria fonte registra que 2025 permanece 149,1% acima da linha de base de 2022.',
        legenda=[("Online", S1), ("Offline", S2)],
        id_="serie-anual", nat="comunitaria"))

    # ---------------- triagem ----------------
    linhas = [[r, FMT(v), f"{v/1428*100:.1f}%"] for r, v in TRIAGEM_2025]
    out.append(figura(
        "O que acontece com um registro recebido, 2025",
        "De 1.428 registros que chegaram aos canais em 2025, 989 foram validados como antissemitismo e 439 foram descartados na triagem. A taxa de descarte é indicador de qualidade do canal, raro de encontrar publicado.",
        svg_barras(TRIAGEM_2025, destaque={"Validadas como antissemitismo"}, unidade="registros",
                   rotulo_eixo="Destino dos 1.428 registros recebidos em 2025"),
        tabela(["Destino do registro", "Registros", "% de 1.428"], linhas),
        f'Fonte: {LINK25}, CONIB, FISESP e DSC. {selo("verificado")} '
        'A taxa de descarte em 2025 foi de 30,74%. Em 2024 o canal recebeu 3.167 denúncias brutas e '
        'descartou 43,55% delas: menos registros em duplicidade e menos registros impulsionados pelo '
        'clima de crise explicam parte da queda no volume validado.',
        id_="triagem", nat="comunitaria"))

    # ---------------- geografia ----------------
    tot25 = sum(v for _, v in GEO_2025)
    linhas = [[r, FMT(v), f"{v/tot25*100:.1f}%"] for r, v in GEO_2025]
    out.append(figura(
        "Onde as ocorrências foram registradas, 2025",
        "Quase metade dos registros não tem estado informado, sobretudo por serem incidentes digitais sem vínculo territorial. Esse é o maior grupo do gráfico e não pode ser omitido sem distorcer a leitura.",
        svg_barras(GEO_2025, destaque={"Sem estado informado"},
                   rotulo_eixo="Ocorrências validadas de 2025 por recorte geográfico"),
        tabela(["Recorte", "Ocorrências", "% de 989"], linhas),
        f'Fonte: {LINK25}. {selo("verificado")} '
        '<strong>Não comparar com 2024.</strong> Em 2024, São Paulo respondia por 900 ocorrências (50,3%) e o grupo sem definição por 132 (7,4%). '
        'A inversão entre os dois anos reflete mudança na forma de captar a localização, e não migração do fenômeno.',
        id_="geografia", nat="comunitaria"))

    # ---------------- plataformas ----------------
    linhas = [[r, FMT(v), f"{v/800*100:.1f}%"] for r, v in PLATAFORMA_2025]
    out.append(figura(
        "Plataformas das ocorrências online, 2025",
        "Base de cálculo: as 800 ocorrências validadas em ambiente digital. As 151 não categorizadas aparecem no gráfico porque são o segundo maior grupo.",
        svg_barras(PLATAFORMA_2025, altura_barra=24,
                   rotulo_eixo="Ocorrências online de 2025 por plataforma"),
        tabela(["Plataforma", "Ocorrências", "% de 800"], linhas),
        f'Fonte: {LINK25}. {selo("verificado")} '
        '<strong>Bases diferentes entre anos.</strong> Em 2024 o relatório apurou X com 402 ocorrências (48%) e Instagram com 314 (37%), '
        'mas sobre uma base de 846 casos classificados em redes sociais, e não sobre o total de 1.310 ocorrências online. '
        'A troca de liderança entre X e Instagram é real, e a magnitude não é comparável.',
        id_="plataformas", nat="comunitaria"))
    out.append("</div>")

    # ---------------- resposta institucional ----------------
    out.append("""<section class="band"><div class="wrap section">
  <p class="eyebrow">Camada 1 &middot; Resposta institucional</p>
  <h2 class="h2">O &uacute;nico recorte de desfecho dispon&iacute;vel</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">A aus&ecirc;ncia de rastreabilidade do desfecho &eacute; a segunda causa da invisibilidade estat&iacute;stica, e a mais dif&iacute;cil de sanar. Os n&uacute;meros abaixo s&atilde;o o que existe de p&uacute;blico sobre o que acontece depois da den&uacute;ncia. Nenhum deles tem recorte espec&iacute;fico de antissemitismo: o neonazismo &eacute; o proxy mais pr&oacute;ximo.</p>
</div>""")
    out.append('<div class="wrap section" style="padding-top:0">')
    linhas = [[r, FMT(v)] for r, v in FUNIL_MPF]
    out.append(figura(
        "Denúncias de neonazismo no Report System, 2022 a 2024",
        "Do volume recebido pela SaferNet e encaminhado ao Ministério Público Federal, 81,5% foram arquivadas por falta de elementos probatórios mínimos e 9,19% resultaram em procedimento instaurado.",
        svg_barras(FUNIL_MPF, destaque={"Procedimentos instaurados no MPF"}, unidade="registros",
                   altura_barra=30, rotulo_eixo="Denúncias de neonazismo no Report System, 2022 a 2024"),
        tabela(["Etapa", "Registros"], linhas),
        f'Fonte: SaferNet Brasil e Ministério Público Federal, Report System. {selo("citado")} '
        'Os números constam do levantamento reunido para o Eixo 3 em agosto de 2026. A publicação primária não foi consultada nesta versão do protótipo, '
        'e os identificadores administrativos indicados no levantamento seguem sem confirmação.',
        id_="funil", nat="oficial"))

    linhas = [[r, FMT(d), FMT(i), f"{i/d*100:.2f}%"] for r, d, i in INSTAURACAO]
    barras = [(r, round(i / d * 10000) / 100) for r, d, i in INSTAURACAO]
    out.append(figura(
        "Taxa de instauração no MPF por tema, 2022 a 2024",
        "Quando o núcleo temático é tipificado na entrada, a taxa de instauração quadruplica. É o argumento empírico a favor do marcador: a persecução responde ao que consegue enxergar.",
        svg_barras(barras, destaque={"Neonazismo"}, unidade="de instauração", altura_barra=34,
                   rotulo_eixo="Taxa de instauração no MPF por tema",
                   formato=lambda v: f"{v:.2f}".replace(".", ",") + "%"),
        tabela(["Tema", "Denúncias", "Instaurações", "Taxa"], linhas),
        f'Fonte: SaferNet Brasil e MPF. {selo("citado")} '
        'A categoria de intolerância religiosa é genérica: absorve o antissemitismo sem distingui-lo, o que é exatamente a lacuna que o Eixo 3 documenta.',
        id_="instauracao", nat="oficial"))
    out.append("</div></section>")

    # ---------------- benchmark internacional ----------------
    out.append(f"""<section class="wrap section">
  <p class="eyebrow">Camada 1 &middot; Leitura comparada</p>
  <h2 class="h2">Refer&ecirc;ncia internacional</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">Os dois indicadores abaixo servem a prop&oacute;sitos distintos. O primeiro d&aacute; ordem de grandeza a uma s&eacute;rie madura, com 46 anos de apura&ccedil;&atilde;o. O segundo mede a subnotifica&ccedil;&atilde;o, que &eacute; o que a s&eacute;rie brasileira n&atilde;o consegue enxergar.</p>
  <div class="tiles">
    <div class="tile"><p class="label">Estados Unidos &middot; 2024</p><p class="tile-num">9.354</p><p class="tile-txt">incidentes apurados no ano, alta de 5% sobre 2023 e de 893% em dez anos. Em 58,3% deles houve men&ccedil;&atilde;o a Israel ou ao sionismo, a primeira vez que esse recorte &eacute; maioria em 46 anos de s&eacute;rie.</p><p class="tile-src">ADL, Audit of Antisemitic Incidents 2024. {selo("citado")} {natureza("externa")}</p></div>
    <div class="tile"><p class="label">Uni&atilde;o Europeia</p><p class="tile-num">80%</p><p class="tile-txt">das v&iacute;timas n&atilde;o levam o incidente &agrave; pol&iacute;cia ou a qualquer autoridade. Na mesma pesquisa, 96% relataram ter sofrido alguma forma de antissemitismo no ano anterior, e menos de metade dos 27 Estados-membros mant&eacute;m registro desagregado.</p><p class="tile-src">FRA, Ag&ecirc;ncia da Uni&atilde;o Europeia para os Direitos Fundamentais. {selo("citado")} {natureza("percepcao")}</p></div>
  </div>
  <p class="body" style="margin: 26px 0 0; max-width: 74ch"><strong>A leitura que interessa ao Eixo 3 n&atilde;o &eacute; a compara&ccedil;&atilde;o de volume.</strong> Os n&uacute;meros brasileiro e norte-americano contam populações, canais e defini&ccedil;&otilde;es diferentes, e coloc&aacute;-los lado a lado sugeriria uma raz&atilde;o que os dados n&atilde;o sustentam. O que se compara &eacute; a exist&ecirc;ncia do instrumento: h&aacute; s&eacute;rie hist&oacute;rica de 46 anos em uma jurisdi&ccedil;&atilde;o, marcador oficial em 14 de 27 Estados-membros em outra, e nenhuma categoria aut&ocirc;noma em nenhuma base estatal brasileira.</p>
</section>""")

    # ---------------- camada 2: painel de lacunas ----------------
    grupos = {}
    for nome, fonte, status, motivo in KPIS:
        grupos.setdefault(status, []).append((nome, fonte, motivo))
    contagem = {k: len(v) for k, v in grupos.items()}
    linhas = []
    for nome, fonte, status, motivo in KPIS:
        cls = {SEM_FONTE: "st-sem", AGUARDA: "st-agu", VEDADO: "st-ved", PARCIAL: "st-par"}[status]
        linhas.append(
            f'<tr><th scope="row">{E(nome)}</th>'
            f'<td class="fonte-kpi">{E(fonte)}</td>'
            f'<td><span class="status {cls}">{E(status)}</span></td>'
            f'<td class="motivo">{E(motivo)}</td></tr>')
    out.append(f"""<section class="band"><div class="wrap section">
  <p class="eyebrow">Camada 2 &middot; O que n&atilde;o &eacute; mensur&aacute;vel</p>
  <h2 class="h2">Painel de lacunas</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">Abaixo est&aacute; a Matriz Nacional de KPIs proposta pelo Eixo 3, com seus vinte indicadores. Nenhum deles est&aacute; preenchido, e o motivo de cada um n&atilde;o estar &eacute; diferente. Essa distin&ccedil;&atilde;o &eacute; o resultado do trabalho, n&atilde;o a sua falha.</p>
  <div class="lac-resumo">
    <div class="lac-item"><span class="status st-par">{PARCIAL}</span><strong>{contagem.get(PARCIAL, 0)}</strong><p>Existe proxy em fonte da sociedade civil ou em base gen&eacute;rica, sem recorte de antissemitismo.</p></div>
    <div class="lac-item"><span class="status st-agu">{AGUARDA}</span><strong>{contagem.get(AGUARDA, 0)}</strong><p>Depende de categoria na entrada. San&aacute;vel por marcador, sem lei nova, como o CNJ fez em 2022.</p></div>
    <div class="lac-item"><span class="status st-sem">{SEM_FONTE}</span><strong>{contagem.get(SEM_FONTE, 0)}</strong><p>Nenhuma base publica o dado, nem de forma agregada nem sob outra categoria.</p></div>
    <div class="lac-item"><span class="status st-ved">{VEDADO}</span><strong>{contagem.get(VEDADO, 0)}</strong><p>Limite normativo leg&iacute;timo, derivado de medidas sob reserva de jurisdi&ccedil;&atilde;o. N&atilde;o &eacute; falha institucional.</p></div>
  </div>
  <div class="tab-rolagem">
    <table class="tab-kpi">
      <caption class="sr-only">Matriz Nacional de KPIs com a situa&ccedil;&atilde;o de cada indicador</caption>
      <thead><tr><th scope="col">Indicador</th><th scope="col">Fonte prevista</th><th scope="col">Situa&ccedil;&atilde;o</th><th scope="col">Por que est&aacute; vazio</th></tr></thead>
      <tbody>{''.join(linhas)}</tbody>
    </table>
  </div>
  <p class="fonte" style="margin-top: 22px">Anexo III &mdash; Matriz Nacional de KPIs, instrumento de modelagem do Eixo 3. A coluna de situa&ccedil;&atilde;o &eacute; leitura do Eixo sobre a disponibilidade de fonte em agosto de 2026, e n&atilde;o consta do instrumento original. {selo("lacuna")}</p>
</div></section>""")

    # ---------------- metodologia e dados abertos ----------------
    out.append(f"""<section class="wrap section" id="metodologia">
  <p class="eyebrow">Metodologia</p>
  <h2 class="h2">Como ler estes n&uacute;meros</h2>
  <div class="met-grid">
    <div>
      <h3 class="h3">Defini&ccedil;&atilde;o adotada</h3>
      <p class="body">O enquadramento &eacute; o fixado pelo Supremo Tribunal Federal no HC 82.424/RS, de 2003: o antissemitismo se qualifica como racismo, crime inafian&ccedil;&aacute;vel e imprescrit&iacute;vel. As fontes agregadas nesta p&aacute;gina adotam defini&ccedil;&otilde;es operacionais pr&oacute;prias, que nem sempre coincidem entre si.</p>
      <h3 class="h3" style="margin-top: 26px">O que entra</h3>
      <p class="body">Somente dado agregado, de origem p&uacute;blica e j&aacute; publicado por terceiro. Nenhum n&uacute;mero desta p&aacute;gina foi produzido pelo Observat&oacute;rio. N&atilde;o h&aacute;, em nenhum ponto, dado pessoal, den&uacute;ncia individualizada ou informa&ccedil;&atilde;o sob sigilo.</p>
      <h3 class="h3" style="margin-top: 26px">Natureza do dado, e por que ela importa</h3>
      <p class="body">Cada n&uacute;mero desta p&aacute;gina carrega uma marca de natureza. {natureza("comunitaria")} vem de entidade da sociedade civil, a partir de den&uacute;ncia recebida em canal pr&oacute;prio. {natureza("oficial")} vem de &oacute;rg&atilde;o p&uacute;blico, a partir de registro administrativo. {natureza("externa")} foi apurado em outro pa&iacute;s. {natureza("percepcao")} &eacute; levantamento amostral de atitudes, e n&atilde;o contagem de ocorr&ecirc;ncias.</p>
      <p class="body"><strong>N&uacute;meros de naturezas diferentes n&atilde;o s&atilde;o somados nem comparados diretamente nesta p&aacute;gina.</strong> A pr&aacute;tica vem do ODIHR, organismo da OSCE que mant&eacute;m dois acervos separados e nunca os junta: o que vem do Estado &eacute; registrado como crime, o que vem da sociedade civil como incidente, com a raz&atilde;o declarada de que n&atilde;o se consegue verificar se o segundo grupo se qualifica como crime. Aqui a disciplina &eacute; a mesma, por um motivo pr&aacute;tico: como nenhuma base estatal brasileira tem categoria aut&ocirc;noma de antissemitismo, misturar contagem comunit&aacute;ria com dado policial produziria n&uacute;mero sem denominador.</p>

      <h3 class="h3" style="margin-top: 26px">Grau de verifica&ccedil;&atilde;o</h3>
      <p class="body">Cada bloco traz um selo. {selo("verificado")} indica n&uacute;mero conferido contra o documento de origem, dispon&iacute;vel no acervo do Eixo 3. {selo("citado")} indica n&uacute;mero cuja fonte est&aacute; declarada, mas cuja publica&ccedil;&atilde;o primária n&atilde;o foi consultada nesta vers&atilde;o. Nenhum identificador administrativo ou n&uacute;mero de processo n&atilde;o confirmado foi transcrito.</p>
    </div>
    <div>
      <h3 class="h3">Subnotifica&ccedil;&atilde;o</h3>
      <p class="body">A s&eacute;rie brasileira mede den&uacute;ncias recebidas por canais da sociedade civil, n&atilde;o incid&ecirc;ncia. Toda leitura de alta ou de queda mistura varia&ccedil;&atilde;o do fen&ocirc;meno com varia&ccedil;&atilde;o da propens&atilde;o a denunciar e do alcance dos canais.</p>
      <p class="body">A pr&oacute;pria fonte mede esse limite. Na pesquisa intracomunit&aacute;ria de 2025, apenas 32,58% de quem sofreu um incidente o denunciou. Entre as raz&otilde;es para n&atilde;o denunciar: 19,27% n&atilde;o consideraram o fato grave o suficiente, 14,01% n&atilde;o confiavam na efic&aacute;cia do registro, 11,84% n&atilde;o sabiam onde denunciar, 8,05% temeram exposi&ccedil;&atilde;o social e 6,65% relataram medo de retalia&ccedil;&atilde;o. A refer&ecirc;ncia europeia, de 80% de subnotifica&ccedil;&atilde;o, aponta a mesma ordem de grandeza.</p>
      <h3 class="h3" style="margin-top: 26px">Bases de c&aacute;lculo</h3>
      <p class="body">Percentual sem base declarada &eacute; percentual que engana. Cada gr&aacute;fico informa sobre que denominador foi calculado. Onde a base mudou entre um ano e outro, a compara&ccedil;&atilde;o direta est&aacute; desaconselhada no pr&oacute;prio gr&aacute;fico, com a raz&atilde;o.</p>
      <h3 class="h3" style="margin-top: 26px">Aus&ecirc;ncia de dado estatal</h3>
      <p class="body">Nenhuma base p&uacute;blica examinada possui categoria aut&ocirc;noma de antissemitismo: Anu&aacute;rio do F&oacute;rum Brasileiro de Seguran&ccedil;a P&uacute;blica, SaferNet, Comunica PF, Disque 100, boletins de ocorr&ecirc;ncia estaduais e Tabelas Processuais Unificadas do CNJ. O fen&ocirc;meno &eacute; dissolvido em in&uacute;ria racial, racismo, intoler&acirc;ncia religiosa, amea&ccedil;a ou &ldquo;outros crimes&rdquo;. Por isso a camada 2 desta p&aacute;gina existe.</p>
    </div>
  </div>
</section>

<section class="wrap section" id="dados" style="padding-top: 0">
  <h2 class="h2">Dados abertos</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">As s&eacute;ries desta p&aacute;gina est&atilde;o dispon&iacute;veis em formato tabular, com dicion&aacute;rio de campos. A reutiliza&ccedil;&atilde;o &eacute; livre, com cita&ccedil;&atilde;o da fonte prim&aacute;ria, que &eacute; sempre a publica&ccedil;&atilde;o de origem, e n&atilde;o este prot&oacute;tipo.</p>
  <div class="dl-lista">
    <a class="dl" href="data/indicadores/serie_anual.csv" download><span class="dl-nome">S&eacute;rie anual 2022&ndash;2025</span><span class="dl-fmt">CSV</span></a>
    <a class="dl" href="data/indicadores/serie_mensal.csv" download><span class="dl-nome">S&eacute;rie mensal 2022&ndash;2024</span><span class="dl-fmt">CSV</span></a>
    <a class="dl" href="data/indicadores/distribuicao_2025.csv" download><span class="dl-nome">Geografia, plataformas e triagem, 2025</span><span class="dl-fmt">CSV</span></a>
    <a class="dl" href="data/indicadores/resposta_institucional.csv" download><span class="dl-nome">Resposta institucional 2022&ndash;2024</span><span class="dl-fmt">CSV</span></a>
    <a class="dl" href="data/indicadores/DICIONARIO.md" download><span class="dl-nome">Dicion&aacute;rio de campos e proced&ecirc;ncia</span><span class="dl-fmt">MD</span></a>
  </div>
</section>""")

    out.append(RODAPE)
    pathlib.Path(RAIZ / "indicadores.html").write_text("".join(out), encoding="utf-8")
    print("indicadores.html gravado")


if __name__ == "__main__":
    main()
