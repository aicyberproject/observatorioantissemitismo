#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as paginas institucionais: sobre, privacidade e termos de uso.

Compartilham cabecalho, menu e rodape com o resto do sitio. Ficam em script para
que a navegacao nao divirja entre paginas quando um item novo entra no menu.

    python3 scripts/gerar_paginas.py
"""
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://aicyberproject.github.io/observatorioantissemitismo"
ATUALIZADO = "4 de setembro de 2026"

FAIXA = """<div class="proto-bar" role="note">
  <div class="wrap proto-inner">
    <span class="proto-tag">Prot&oacute;tipo</span>
    <p class="proto-text">Vers&atilde;o de trabalho, sem car&aacute;ter oficial. Em elabora&ccedil;&atilde;o no Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento, ainda n&atilde;o apreciada pelo Eixo nem pela reuni&atilde;o de coordenadores. N&atilde;o representa posi&ccedil;&atilde;o do CDESS, da Presid&ecirc;ncia da Rep&uacute;blica ou de qualquer &oacute;rg&atilde;o citado.</p>
  </div>
</div>"""

def MENU(atual=""):
    itens = [
        ("index.html#painel", "Painel"),
        ("indicadores.html", "Indicadores"),
        ("boletim/index.html", "Boletim"),
        ("index.html#preservar", "Preservar evid&ecirc;ncias"),
        ("index.html#denuncie", "Denunciar"),
        ("index.html#legislacao", "Legisla&ccedil;&atilde;o"),
        ("acervo.html", "Acervos"),
        ("biblioteca.html", "Biblioteca"),
        ("sobre.html", "Sobre"),
    ]
    return "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == atual else ""}>{r}</a>'
        for h, r in itens)


def RODAPE():
    return f"""</main>
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
        <nav><a href="index.html#topo">In&iacute;cio</a><a href="index.html#painel">Painel</a><a href="indicadores.html">Indicadores</a><a href="boletim/index.html">Boletim</a><a href="index.html#preservar">Preservar evid&ecirc;ncias</a><a href="index.html#denuncie">Denunciar</a><a href="biblioteca.html">Biblioteca</a></nav>
      </div>
      <div>
        <p class="footer-head">Institucional</p>
        <nav><a href="sobre.html">Sobre o Observat&oacute;rio</a><a href="metodologia.html">Metodologia</a><a href="taxonomia.html">Taxonomia proposta</a><a href="privacidade.html">Pol&iacute;tica de privacidade</a><a href="termos.html">Termos de uso</a><a href="boletim/feed.xml">Feed RSS</a><a href="indicadores.html#dados">Dados abertos</a></nav>
      </div>
    </div>
    <p class="footer-legal">&copy; 2026 Observat&oacute;rio do Antissemitismo no Brasil &middot; Prot&oacute;tipo, vers&atilde;o de trabalho &middot; C&oacute;digo e conte&uacute;do sob licen&ccedil;a MIT</p>
  </div>
</footer>
<div class="lgpd" id="lgpd" hidden>
  <div class="wrap lgpd-inner">
    <div class="lgpd-text">
      <p class="eyebrow">Prote&ccedil;&atilde;o de dados &middot; LGPD</p>
      <p>Este portal n&atilde;o usa cookie de rastreamento, n&atilde;o coleta endere&ccedil;o de e-mail e n&atilde;o pede dado pessoal. Guarda apenas prefer&ecirc;ncia de exibi&ccedil;&atilde;o no seu pr&oacute;prio navegador. <a href="privacidade.html">Leia a pol&iacute;tica de privacidade</a>.</p>
    </div>
    <button class="btn-ink" id="lgpd-ok" type="button">Entendido</button>
  </div>
</div>
<script src="js/app.js" defer></script>
</body>
</html>
"""


def pagina(arquivo, titulo, descricao, atual, corpo):
    doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="status" content="prototipo">
<title>{titulo} &middot; Prot&oacute;tipo do Observat&oacute;rio</title>
<meta name="description" content="{descricao}">
<meta name="author" content="Eixo 3 &mdash; Seguran&ccedil;a e Monitoramento">
<meta name="theme-color" content="#F5F3EF">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Prot&oacute;tipo &middot; Observat&oacute;rio do Antissemitismo no Brasil">
<meta property="og:title" content="{titulo} &middot; Prot&oacute;tipo do Observat&oacute;rio">
<link rel="canonical" href="{BASE}/{arquivo}">
<link rel="alternate" type="application/rss+xml" title="Boletim do Observat&oacute;rio" href="boletim/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Work+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/main.css">
<link rel="stylesheet" href="css/indicadores.css">
</head>
<body>
{FAIXA}
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
  <nav class="wrap nav" aria-label="Navega&ccedil;&atilde;o principal">{MENU(atual)}</nav>
</header>
<main>
{corpo}
{RODAPE()}"""
    (RAIZ / arquivo).write_text(doc, encoding="utf-8")
    return arquivo


# ---------------------------------------------------------------------------
# Sobre
# ---------------------------------------------------------------------------

SOBRE = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Sobre</p>
  <h1 class="h1" style="margin-top: 24px">Sobre o Observat&oacute;rio</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Monitorar &eacute; o ponto de partida, n&atilde;o a conclus&atilde;o. A agrega&ccedil;&atilde;o mostra o que est&aacute; sendo dito. A responsabiliza&ccedil;&atilde;o depende de den&uacute;ncia formal, prova preservada e acompanhamento processual.</p>
</section>

<section class="wrap section" style="padding-top: clamp(24px, 3vw, 40px)">
  <div class="met-grid">
    <div>
      <h2 class="h2" style="max-width: 24ch">O que &eacute; esta p&aacute;gina</h2>
      <p class="body" style="margin: 18px 0 0">Um <strong>prot&oacute;tipo</strong> em elabora&ccedil;&atilde;o no Eixo 3, de Seguran&ccedil;a e Monitoramento, da Iniciativa de Enfrentamento ao Antissemitismo. Serve para demonstrar o desenho de um observat&oacute;rio p&uacute;blico de monitoramento, orienta&ccedil;&atilde;o e prote&ccedil;&atilde;o de direitos.</p>
      <p class="body" style="margin: 14px 0 0">Ainda n&atilde;o foi apreciado pelo Eixo nem levado &agrave; reuni&atilde;o de coordenadores. N&atilde;o constitui manifesta&ccedil;&atilde;o do CDESS, da Presid&ecirc;ncia da Rep&uacute;blica ou de qualquer &oacute;rg&atilde;o mencionado no conte&uacute;do. Os canais de den&uacute;ncia listados s&atilde;o oficiais e funcionam de forma independente deste prot&oacute;tipo.</p>

      <h2 class="h2" style="max-width: 26ch; margin-top: clamp(34px, 4vw, 50px)">O achado que motiva o trabalho</h2>
      <p class="body" style="margin: 18px 0 0">N&atilde;o se trata de aus&ecirc;ncia de fen&ocirc;meno, mas de aus&ecirc;ncia de instrumento de medida.</p>
      <p class="body" style="margin: 14px 0 0">Nenhuma base p&uacute;blica examinada possui categoria aut&ocirc;noma de antissemitismo: Anu&aacute;rio do F&oacute;rum Brasileiro de Seguran&ccedil;a P&uacute;blica, SaferNet, Comunica PF, Disque 100, boletins de ocorr&ecirc;ncia estaduais e Tabelas Processuais Unificadas do CNJ. O fen&ocirc;meno &eacute; dissolvido em inj&uacute;ria racial, racismo, intoler&acirc;ncia religiosa, amea&ccedil;a ou &ldquo;outros crimes&rdquo;.</p>
      <p class="body" style="margin: 14px 0 0">S&atilde;o duas causas cumulativas. A aus&ecirc;ncia de categoria na entrada, san&aacute;vel por marcador administrativo, sem lei nova. E a aus&ecirc;ncia de rastreabilidade do desfecho na sa&iacute;da, que decorre em parte de limite normativo leg&iacute;timo, o segredo de justi&ccedil;a. Apenas a primeira &eacute; san&aacute;vel por decis&atilde;o t&eacute;cnica.</p>
      <p class="body" style="margin: 14px 0 0">A <a href="indicadores.html">p&aacute;gina de indicadores</a> registra as duas coisas: o que hoje &eacute; mensur&aacute;vel e, ao lado, as vinte lacunas que nenhuma base preenche, com o motivo de cada uma.</p>
    </div>
    <div>
      <h2 class="h2" style="max-width: 22ch">Defini&ccedil;&atilde;o adotada</h2>
      <p class="body" style="margin: 18px 0 0">O enquadramento &eacute; o fixado pelo Supremo Tribunal Federal no <strong>HC 82.424/RS</strong>, de 2003: o antissemitismo se qualifica como racismo, crime inafian&ccedil;&aacute;vel e imprescrit&iacute;vel nos termos do art. 5&ordm;, XLII, da Constitui&ccedil;&atilde;o Federal.</p>
      <p class="body" style="margin: 14px 0 0">&Eacute; o enquadramento vigente no direito brasileiro e n&atilde;o depende de ado&ccedil;&atilde;o de instrumento internacional. Sobre a controv&eacute;rsia p&uacute;blica quanto a defini&ccedil;&otilde;es internacionais, este Observat&oacute;rio n&atilde;o toma posi&ccedil;&atilde;o e n&atilde;o &eacute; a inst&acirc;ncia competente para resolv&ecirc;-la.</p>

      <h2 class="h2" style="max-width: 22ch; margin-top: clamp(34px, 4vw, 50px)">De onde vem o conte&uacute;do</h2>
      <ul class="scope-list scope-is" style="margin-top: 18px">
        <li><strong>Painel e boletim:</strong> agrega&ccedil;&atilde;o autom&aacute;tica de 21 fontes p&uacute;blicas, com link para a publica&ccedil;&atilde;o de origem.</li>
        <li><strong>Indicadores:</strong> relat&oacute;rios j&aacute; publicados por terceiros, com ano de refer&ecirc;ncia, base de c&aacute;lculo e selo de proced&ecirc;ncia.</li>
        <li><strong>Legisla&ccedil;&atilde;o e biblioteca:</strong> texto normativo, ac&oacute;rd&atilde;os e documentos de refer&ecirc;ncia, com link para a fonte.</li>
        <li><strong>Canais de den&uacute;ncia:</strong> formul&aacute;rios oficiais das pr&oacute;prias institui&ccedil;&otilde;es.</li>
      </ul>
      <p class="body" style="margin: 18px 0 0">Nenhum n&uacute;mero desta p&aacute;gina &eacute; produzido pelo Observat&oacute;rio. A autoridade &eacute; sempre a publica&ccedil;&atilde;o de origem.</p>
    </div>
  </div>
</section>

<section class="band"><div class="wrap section">
  <p class="eyebrow">O que &eacute; e o que n&atilde;o &eacute;</p>
  <div class="scope-grid" style="margin-top: 24px">
    <div>
      <h3 class="h3-display">O que &eacute;</h3>
      <ul class="scope-list scope-is">
        <li>Plataforma p&uacute;blica de monitoramento de incidentes de antissemitismo no Brasil.</li>
        <li>Superf&iacute;cie de leitura que remete ao ve&iacute;culo original, com aviso expl&iacute;cito quando o item chega por intermedi&aacute;rio de busca.</li>
        <li>Guia pr&aacute;tico de canais oficiais de den&uacute;ncia e de preserva&ccedil;&atilde;o de provas.</li>
        <li>Registro das lacunas de medi&ccedil;&atilde;o, que s&atilde;o o principal achado do Eixo.</li>
      </ul>
    </div>
    <div>
      <h3 class="h3-display">O que n&atilde;o &eacute;</h3>
      <ul class="scope-list scope-isnot">
        <li>N&atilde;o &eacute; ve&iacute;culo de not&iacute;cia: nada &eacute; reportado originalmente aqui.</li>
        <li>N&atilde;o emite opini&atilde;o editorial nem carrega posi&ccedil;&atilde;o pol&iacute;tico-partid&aacute;ria.</li>
        <li>N&atilde;o substitui registro de ocorr&ecirc;ncia, den&uacute;ncia formal ou assist&ecirc;ncia jur&iacute;dica.</li>
        <li>N&atilde;o &eacute; fonte oficial: a autoridade &eacute; sempre a publica&ccedil;&atilde;o de origem.</li>
        <li>N&atilde;o recebe den&uacute;ncia. Encaminha aos canais que a recebem.</li>
      </ul>
    </div>
  </div>
</div></section>

<section class="wrap section">
  <h2 class="h2" style="max-width: 26ch">Correções e contato</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Erro em verbete, indicador, data ou endere&ccedil;o &eacute; defeito a corrigir, n&atilde;o detalhe. Enquanto este prot&oacute;tipo n&atilde;o tiver endere&ccedil;o institucional definitivo, o caminho para apontar erro &eacute; o reposit&oacute;rio p&uacute;blico do c&oacute;digo, onde qualquer pessoa pode abrir uma questão.</p>
  <div class="pills" style="margin-top: 22px">
    <a class="pill pill-solid" href="https://github.com/aicyberproject/observatorioantissemitismo/issues" target="_blank" rel="noopener">Apontar erro ou sugerir corre&ccedil;&atilde;o &rarr;</a>
    <a class="pill" href="indicadores.html#metodologia">Metodologia &rarr;</a>
  </div>
  <p class="fonte" style="margin-top: 22px">Toda corre&ccedil;&atilde;o aceita fica registrada no hist&oacute;rico p&uacute;blico do c&oacute;digo, com data e motivo. N&atilde;o h&aacute; edi&ccedil;&atilde;o silenciosa.</p>
</section>
"""


# ---------------------------------------------------------------------------
# Privacidade
# ---------------------------------------------------------------------------

PRIVACIDADE = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Privacidade</p>
  <h1 class="h1" style="margin-top: 24px">Pol&iacute;tica de privacidade</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 68ch">Resumo em uma frase: <strong>este s&iacute;tio n&atilde;o coleta dado pessoal nenhum.</strong> N&atilde;o pede seu nome, n&atilde;o pede seu e-mail, n&atilde;o usa cookie de rastreamento e n&atilde;o envia nada seu para lugar algum.</p>
  <p class="body" style="margin: 18px 0 0; max-width: 68ch">Atualizada em {ATUALIZADO}. Aplica-se ao prot&oacute;tipo publicado em <code>aicyberproject.github.io/observatorioantissemitismo</code>.</p>
</section>

<section class="wrap section" style="padding-top: clamp(20px, 3vw, 36px)">
  <div class="met-grid">
    <div>
      <h2 class="h2" style="max-width: 24ch">O que n&atilde;o &eacute; coletado</h2>
      <ul class="scope-list scope-isnot" style="margin-top: 18px">
        <li>Nome, e-mail, telefone ou qualquer identifica&ccedil;&atilde;o.</li>
        <li>Cookie de rastreamento, de publicidade ou de perfilamento.</li>
        <li>Ferramenta de an&aacute;lise de audi&ecirc;ncia de terceiro.</li>
        <li>Conte&uacute;do de den&uacute;ncia, relato de incidente ou arquivo.</li>
        <li>Endere&ccedil;o para envio de boletim. A assinatura &eacute; por feed RSS, que n&atilde;o exige cadastro.</li>
      </ul>

      <h2 class="h2" style="max-width: 26ch; margin-top: clamp(34px, 4vw, 50px)">A ferramenta de hash</h2>
      <p class="body" style="margin: 18px 0 0">A se&ccedil;&atilde;o de preserva&ccedil;&atilde;o de evid&ecirc;ncias oferece o c&aacute;lculo do resumo criptogr&aacute;fico SHA-256 de arquivos. &Eacute; a &uacute;nica parte do s&iacute;tio que recebe algo seu, e ela foi constru&iacute;da para que <strong>nada saia do seu navegador</strong>.</p>
      <ul class="scope-list scope-is" style="margin-top: 16px">
        <li>O arquivo n&atilde;o &eacute; enviado a servidor nenhum.</li>
        <li>O conte&uacute;do &eacute; lido apenas para o c&aacute;lculo, n&atilde;o &eacute; exibido nem guardado.</li>
        <li>Nada fica salvo no aparelho. Fechar a p&aacute;gina descarta tudo.</li>
        <li>O c&oacute;digo dessa ferramenta n&atilde;o cont&eacute;m nenhuma chamada de rede, e isso &eacute; verific&aacute;vel por quem quiser conferir o c&oacute;digo-fonte.</li>
      </ul>
    </div>
    <div>
      <h2 class="h2" style="max-width: 24ch">O que fica no seu navegador</h2>
      <p class="body" style="margin: 18px 0 0">Duas prefer&ecirc;ncias de exibi&ccedil;&atilde;o, guardadas em <code>sessionStorage</code>, que &eacute; apagado ao fechar a aba:</p>
      <ul class="scope-list scope-is" style="margin-top: 16px">
        <li>Se voc&ecirc; j&aacute; viu a abertura, para que ela n&atilde;o se repita na mesma visita.</li>
        <li>Se voc&ecirc; j&aacute; fechou este aviso de prote&ccedil;&atilde;o de dados.</li>
      </ul>
      <p class="body" style="margin: 16px 0 0">Nenhuma das duas identifica voc&ecirc;, e nenhuma sai do seu aparelho.</p>

      <h2 class="h2" style="max-width: 26ch; margin-top: clamp(34px, 4vw, 50px)">Terceiros envolvidos</h2>
      <p class="body" style="margin: 18px 0 0">Honestidade sobre o que n&atilde;o est&aacute; sob nosso controle:</p>
      <ul class="scope-list scope-is" style="margin-top: 16px">
        <li><strong>GitHub Pages</strong> hospeda o s&iacute;tio e registra acesso em log de servidor, conforme a pol&iacute;tica do pr&oacute;prio GitHub.</li>
        <li><strong>Google Fonts</strong> serve as fontes tipogr&aacute;ficas. A requisi&ccedil;&atilde;o parte do seu navegador para o servidor do Google.</li>
        <li><strong>Links externos.</strong> Ao clicar em uma manchete ou em um canal de den&uacute;ncia, voc&ecirc; sai daqui. O que acontece no destino segue a pol&iacute;tica do destino.</li>
      </ul>
      <p class="body" style="margin: 16px 0 0">Sete das 21 fontes do painel s&atilde;o buscas no Google Not&iacute;cias. Nesses casos o item traz o aviso <em>via Google Not&iacute;cias</em>, porque o clique passa por um intermedi&aacute;rio antes de chegar ao ve&iacute;culo.</p>
    </div>
  </div>
</section>

<section class="band"><div class="wrap section">
  <h2 class="h2" style="max-width: 30ch">Seus direitos sob a LGPD</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">A Lei Geral de Prote&ccedil;&atilde;o de Dados, Lei n&ordm; 13.709/2018, assegura ao titular os direitos de confirma&ccedil;&atilde;o, acesso, corre&ccedil;&atilde;o, anonimiza&ccedil;&atilde;o, portabilidade, elimina&ccedil;&atilde;o e revoga&ccedil;&atilde;o de consentimento.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Como este prot&oacute;tipo n&atilde;o coleta dado pessoal, n&atilde;o h&aacute; base de dados sua a acessar, corrigir ou eliminar. Se e quando passar a haver, esta p&aacute;gina ser&aacute; atualizada <strong>antes</strong> da coleta come&ccedil;ar, e n&atilde;o depois, e o registro da mudan&ccedil;a ficar&aacute; p&uacute;blico no hist&oacute;rico do c&oacute;digo.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Enquanto o prot&oacute;tipo n&atilde;o tiver endere&ccedil;o institucional definitivo, n&atilde;o h&aacute; encarregado de prote&ccedil;&atilde;o de dados designado, porque n&atilde;o h&aacute; tratamento a encarregar. Quest&otilde;es sobre esta pol&iacute;tica podem ser levantadas no <a href="https://github.com/aicyberproject/observatorioantissemitismo/issues" target="_blank" rel="noopener">reposit&oacute;rio p&uacute;blico do c&oacute;digo</a>.</p>
</div></section>

<section class="wrap section">
  <h2 class="h2" style="max-width: 30ch">Se voc&ecirc; foi v&iacute;tima ou testemunha</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Este s&iacute;tio n&atilde;o recebe den&uacute;ncia e n&atilde;o deve receber. Os canais listados na se&ccedil;&atilde;o de den&uacute;ncia s&atilde;o das pr&oacute;prias institui&ccedil;&otilde;es, e cada uma tem pol&iacute;tica de privacidade pr&oacute;pria, que vale a pena ler antes de enviar um relato.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Se precisar de anonimato, a SaferNet Brasil recebe den&uacute;ncia an&ocirc;nima, e o Disque 100 tamb&eacute;m aceita den&uacute;ncia sem identifica&ccedil;&atilde;o.</p>
  <div class="pills" style="margin-top: 22px">
    <a class="pill pill-solid" href="index.html#preservar">Preservar evid&ecirc;ncias &rarr;</a>
    <a class="pill" href="index.html#denuncie">Canais de den&uacute;ncia &rarr;</a>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Termos de uso
# ---------------------------------------------------------------------------

TERMOS = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Termos de uso</p>
  <h1 class="h1" style="margin-top: 24px">Termos de uso</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 68ch">O conte&uacute;do &eacute; livre para reuso, com cita&ccedil;&atilde;o da fonte de origem. Este prot&oacute;tipo n&atilde;o &eacute; fonte oficial, n&atilde;o presta assist&ecirc;ncia jur&iacute;dica e n&atilde;o recebe den&uacute;ncia.</p>
  <p class="body" style="margin: 18px 0 0; max-width: 68ch">Atualizados em {ATUALIZADO}.</p>
</section>

<section class="wrap section" style="padding-top: clamp(20px, 3vw, 36px)">
  <div class="met-grid">
    <div>
      <h2 class="h2" style="max-width: 24ch">1. Natureza do servi&ccedil;o</h2>
      <p class="body" style="margin: 18px 0 0">Este &eacute; um <strong>prot&oacute;tipo</strong>, vers&atilde;o de trabalho em elabora&ccedil;&atilde;o no Eixo 3 da Iniciativa de Enfrentamento ao Antissemitismo. N&atilde;o foi apreciado pelo Eixo nem pela reuni&atilde;o de coordenadores, e n&atilde;o constitui manifesta&ccedil;&atilde;o do CDESS, da Presid&ecirc;ncia da Rep&uacute;blica ou de qualquer &oacute;rg&atilde;o citado no conte&uacute;do.</p>
      <p class="body" style="margin: 14px 0 0">O conte&uacute;do pode mudar ou sair do ar sem aviso, e o endere&ccedil;o atual n&atilde;o &eacute; definitivo.</p>

      <h2 class="h2" style="max-width: 24ch; margin-top: clamp(34px, 4vw, 50px)">2. O que este s&iacute;tio n&atilde;o faz</h2>
      <ul class="scope-list scope-isnot" style="margin-top: 18px">
        <li>N&atilde;o recebe den&uacute;ncia. Encaminha aos canais oficiais que a recebem.</li>
        <li>N&atilde;o presta assist&ecirc;ncia jur&iacute;dica nem substitui advogado ou Defensoria.</li>
        <li>N&atilde;o substitui boletim de ocorr&ecirc;ncia nem den&uacute;ncia formal.</li>
        <li>N&atilde;o produz not&iacute;cia. Agrega e remete &agrave; publica&ccedil;&atilde;o de origem.</li>
        <li>N&atilde;o certifica prova. A ferramenta de hash calcula um resumo; f&eacute; p&uacute;blica quem d&aacute; &eacute; a ata notarial.</li>
      </ul>
    </div>
    <div>
      <h2 class="h2" style="max-width: 26ch">3. Orienta&ccedil;&atilde;o jur&iacute;dica e limites</h2>
      <p class="body" style="margin: 18px 0 0">O material sobre legisla&ccedil;&atilde;o, jurisprud&ecirc;ncia e preserva&ccedil;&atilde;o de provas tem finalidade informativa. N&atilde;o &eacute; parecer, n&atilde;o considera as circunst&acirc;ncias do seu caso e n&atilde;o cria rela&ccedil;&atilde;o de patroc&iacute;nio.</p>
      <p class="body" style="margin: 14px 0 0">Norma muda, ac&oacute;rd&atilde;o &eacute; superado e prazo corre. Antes de agir com base no que leu aqui, confira no texto de origem, que est&aacute; sempre linkado, e procure orienta&ccedil;&atilde;o profissional.</p>

      <h2 class="h2" style="max-width: 26ch; margin-top: clamp(34px, 4vw, 50px)">4. Conte&uacute;do de terceiros</h2>
      <p class="body" style="margin: 18px 0 0">As manchetes do painel e do boletim s&atilde;o de seus respectivos ve&iacute;culos, exibidas como t&iacute;tulo e link. A responsabilidade pelo conte&uacute;do &eacute; de quem publicou. A inclus&atilde;o de uma fonte no monitoramento n&atilde;o significa endosso da sua linha editorial, e a aus&ecirc;ncia n&atilde;o significa recusa.</p>
      <p class="body" style="margin: 14px 0 0">Se voc&ecirc; &eacute; respons&aacute;vel por um ve&iacute;culo e n&atilde;o deseja ser agregado, o pedido pode ser feito no reposit&oacute;rio p&uacute;blico e ser&aacute; atendido.</p>
    </div>
  </div>
</section>

<section class="band"><div class="wrap section">
  <h2 class="h2" style="max-width: 30ch">5. Licen&ccedil;a e reuso</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">O c&oacute;digo e o conte&uacute;do editorial pr&oacute;prio est&atilde;o sob <a href="https://github.com/aicyberproject/observatorioantissemitismo/blob/main/LICENSE" target="_blank" rel="noopener">licen&ccedil;a MIT</a>. As s&eacute;ries em <a href="indicadores.html#dados">dados abertos</a> podem ser reutilizadas livremente.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch"><strong>Ao reutilizar um n&uacute;mero, cite a fonte prim&aacute;ria, e n&atilde;o este prot&oacute;tipo.</strong> Nenhum dado aqui &eacute; produzido pelo Observat&oacute;rio: todos v&ecirc;m de relat&oacute;rios publicados por terceiros, identificados no dicion&aacute;rio de campos que acompanha cada s&eacute;rie. Citar o prot&oacute;tipo como origem do dado seria incorreto.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Cada s&eacute;rie carrega selo de proced&ecirc;ncia: <em>conferido no acervo</em>, quando o valor foi checado contra o documento de origem, e <em>citado, prim&aacute;ria n&atilde;o consultada</em>, quando a fonte est&aacute; declarada mas a publica&ccedil;&atilde;o n&atilde;o foi aberta. Respeite a distin&ccedil;&atilde;o ao reutilizar.</p>
</div></section>

<section class="wrap section">
  <div class="met-grid">
    <div>
      <h2 class="h2" style="max-width: 26ch">6. Uso do feed e do agregador</h2>
      <p class="body" style="margin: 18px 0 0">O <a href="boletim/feed.xml">feed RSS</a> &eacute; p&uacute;blico e pode ser assinado por qualquer leitor, sem cadastro. Reuso automatizado &eacute; bem-vindo, desde que preserve o link para a publica&ccedil;&atilde;o de origem e n&atilde;o apresente o conte&uacute;do como sendo deste Observat&oacute;rio.</p>
      <p class="body" style="margin: 14px 0 0">Requisi&ccedil;&atilde;o automatizada em volume desproporcional ao uso leg&iacute;timo pode ser bloqueada pela hospedagem, que n&atilde;o est&aacute; sob nosso controle.</p>
    </div>
    <div>
      <h2 class="h2" style="max-width: 26ch">7. Corre&ccedil;&otilde;es</h2>
      <p class="body" style="margin: 18px 0 0">Erro em verbete, indicador, data ou endere&ccedil;o &eacute; defeito a corrigir. Aponte no <a href="https://github.com/aicyberproject/observatorioantissemitismo/issues" target="_blank" rel="noopener">reposit&oacute;rio p&uacute;blico</a>.</p>
      <p class="body" style="margin: 14px 0 0">Toda corre&ccedil;&atilde;o aceita fica registrada no hist&oacute;rico p&uacute;blico, com data e motivo. N&atilde;o h&aacute; edi&ccedil;&atilde;o silenciosa.</p>
    </div>
  </div>
  <p class="fonte" style="margin-top: 26px">Estes termos s&atilde;o regidos pela legisla&ccedil;&atilde;o brasileira. Enquanto durar a condi&ccedil;&atilde;o de prot&oacute;tipo, prevalece sobre qualquer disposi&ccedil;&atilde;o acima o aviso da faixa superior: vers&atilde;o de trabalho, sem car&aacute;ter oficial.</p>
</section>
"""


# ---------------------------------------------------------------------------
# Metodologia
# ---------------------------------------------------------------------------

METODOLOGIA = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Metodologia</p>
  <h1 class="h1" style="margin-top: 24px">Metodologia</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Como cada n&uacute;mero desta p&aacute;gina foi obtido, sobre que base foi calculado, e o que ele n&atilde;o mede. Atualizada em {{ATUALIZADO}}.</p>
  <p class="body" style="margin: 18px 0 0; max-width: 70ch">Esta p&aacute;gina tem endere&ccedil;o pr&oacute;prio de prop&oacute;sito. Metodologia enterrada dentro de um relat&oacute;rio n&atilde;o &eacute; cit&aacute;vel, e quem contesta um n&uacute;mero precisa poder apontar exatamente para a regra que o produziu.</p>
</section>

<section class="wrap section" style="padding-top: clamp(20px, 3vw, 36px)">
  <div class="met-grid">
    <div>
      <h2 class="h2" style="max-width: 24ch">Defini&ccedil;&atilde;o adotada</h2>
      <p class="body" style="margin: 18px 0 0">O enquadramento &eacute; o fixado pelo Supremo Tribunal Federal no HC 82.424/RS, de 2003: o antissemitismo se qualifica como racismo, crime inafian&ccedil;&aacute;vel e imprescrit&iacute;vel nos termos do art. 5&ordm;, XLII, da Constitui&ccedil;&atilde;o Federal. &Eacute; o enquadramento vigente no direito brasileiro e n&atilde;o depende de ado&ccedil;&atilde;o de instrumento internacional.</p>
      <p class="body" style="margin: 14px 0 0">As fontes agregadas nesta p&aacute;gina adotam defini&ccedil;&otilde;es operacionais pr&oacute;prias, que nem sempre coincidem entre si. Onde a diverg&ecirc;ncia afeta a leitura, o texto diz.</p>

      <h2 class="h2" style="max-width: 24ch; margin-top: clamp(34px, 4vw, 50px)">O que entra</h2>
      <p class="body" style="margin: 18px 0 0">Somente dado agregado, de origem p&uacute;blica e j&aacute; publicado por terceiro. <strong>Nenhum n&uacute;mero &eacute; produzido pelo Observat&oacute;rio.</strong> N&atilde;o h&aacute;, em nenhum ponto, dado pessoal, den&uacute;ncia individualizada ou informa&ccedil;&atilde;o sob sigilo.</p>

      <h2 class="h2" style="max-width: 24ch; margin-top: clamp(34px, 4vw, 50px)">Bases de c&aacute;lculo</h2>
      <p class="body" style="margin: 18px 0 0">Percentual sem base declarada &eacute; percentual que engana. Cada gr&aacute;fico informa sobre que denominador foi calculado. Onde a base mudou entre um ano e outro, a compara&ccedil;&atilde;o direta est&aacute; desaconselhada no pr&oacute;prio gr&aacute;fico, com a raz&atilde;o.</p>
      <p class="body" style="margin: 14px 0 0">Dois exemplos que est&atilde;o na p&aacute;gina. A distribui&ccedil;&atilde;o geogr&aacute;fica de 2025 n&atilde;o &eacute; compar&aacute;vel com a de 2024, porque mudou a forma de captar a localiza&ccedil;&atilde;o. E os percentuais de plataforma de 2024 incidiam sobre 846 casos classificados em redes sociais, e n&atilde;o sobre as 1.310 ocorr&ecirc;ncias online do ano.</p>
    </div>
    <div>
      <h2 class="h2" style="max-width: 26ch">Natureza do dado</h2>
      <p class="body" style="margin: 18px 0 0">Cada n&uacute;mero carrega uma marca de natureza: contagem de fonte comunit&aacute;ria, registro oficial agregado, monitoramento de imprensa, pesquisa de percep&ccedil;&atilde;o ou apura&ccedil;&atilde;o de outra jurisdi&ccedil;&atilde;o.</p>
      <p class="body" style="margin: 14px 0 0"><strong>N&uacute;meros de naturezas diferentes n&atilde;o s&atilde;o somados nem comparados diretamente.</strong> A pr&aacute;tica vem do ODIHR, organismo da OSCE que mant&eacute;m dois acervos separados e nunca os junta: o que vem do Estado &eacute; registrado como crime, o que vem da sociedade civil como incidente, com a raz&atilde;o declarada de que n&atilde;o se consegue verificar se o segundo grupo se qualifica como crime.</p>
      <p class="body" style="margin: 14px 0 0">Aqui a disciplina &eacute; a mesma, por motivo pr&aacute;tico: como nenhuma base estatal brasileira tem categoria aut&ocirc;noma de antissemitismo, misturar contagem comunit&aacute;ria com dado policial produziria n&uacute;mero sem denominador.</p>

      <h2 class="h2" style="max-width: 26ch; margin-top: clamp(34px, 4vw, 50px)">Grau de verifica&ccedil;&atilde;o</h2>
      <p class="body" style="margin: 18px 0 0">Cada bloco tamb&eacute;m traz um selo. <strong>Conferido no acervo</strong> indica n&uacute;mero checado contra o documento de origem. <strong>Citado, prim&aacute;ria n&atilde;o consultada</strong> indica n&uacute;mero cuja fonte est&aacute; declarada, mas cuja publica&ccedil;&atilde;o n&atilde;o foi aberta.</p>
      <p class="body" style="margin: 14px 0 0">Nenhum identificador administrativo ou n&uacute;mero de processo n&atilde;o confirmado foi transcrito em lugar nenhum do s&iacute;tio.</p>
    </div>
  </div>
</section>

<section class="band"><div class="wrap section">
  <h2 class="h2" style="max-width: 32ch">Subnotifica&ccedil;&atilde;o: o limite que a pr&oacute;pria fonte declara</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">A s&eacute;rie brasileira mede den&uacute;ncias recebidas por canais da sociedade civil, <strong>n&atilde;o incid&ecirc;ncia</strong>. Toda leitura de alta ou de queda mistura varia&ccedil;&atilde;o do fen&ocirc;meno com varia&ccedil;&atilde;o da propens&atilde;o a denunciar e do alcance dos canais.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">A pr&oacute;pria fonte mede esse limite. Na pesquisa intracomunit&aacute;ria de 2025, apenas 32,58% de quem sofreu um incidente o denunciou. Entre as raz&otilde;es declaradas para n&atilde;o denunciar: 19,27% n&atilde;o consideraram o fato grave o suficiente, 14,01% n&atilde;o confiavam na efic&aacute;cia do registro, 11,84% n&atilde;o sabiam onde denunciar, 8,05% temeram exposi&ccedil;&atilde;o social e 6,65% relataram medo de retalia&ccedil;&atilde;o.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">A refer&ecirc;ncia europeia aponta a mesma ordem de grandeza: a Ag&ecirc;ncia da Uni&atilde;o Europeia para os Direitos Fundamentais estima que 80% das v&iacute;timas n&atilde;o levam o incidente a nenhuma autoridade.</p>
</div></section>

<section class="wrap section">
  <div class="met-grid">
    <div>
      <h2 class="h2" style="max-width: 26ch">Como o painel de not&iacute;cias funciona</h2>
      <p class="body" style="margin: 18px 0 0">Vinte e uma fontes p&uacute;blicas consultadas doze vezes por dia. Quatorze s&atilde;o feeds de ve&iacute;culos e institui&ccedil;&otilde;es. Sete s&atilde;o buscas permanentes no Google Not&iacute;cias, em quatro idiomas: esses itens chegam com endere&ccedil;o de redirecionamento e por isso trazem o aviso <em>via Google Not&iacute;cias</em>.</p>
      <p class="body" style="margin: 14px 0 0">Deduplica&ccedil;&atilde;o por URL normalizada e por similaridade de t&iacute;tulo. Filtro por termo aplicado a todas as fontes menos as sete de busca e o feed dedicado ao tema.</p>
      <p class="body" style="margin: 14px 0 0">A p&aacute;gina declara <strong>quantas fontes responderam</strong> em cada coleta e nomeia as que faltaram. Sem isso, uma fonte pode falhar indefinidamente sem que ningu&eacute;m perceba, o que de fato aconteceu com duas at&eacute; 04/09/2026.</p>
    </div>
    <div>
      <h2 class="h2" style="max-width: 26ch">Como o hist&oacute;rico e o boletim funcionam</h2>
      <p class="body" style="margin: 18px 0 0">Cada coleta acumula no arquivo do dia, deduplicando. Dias anteriores nunca s&atilde;o alterados. Reten&ccedil;&atilde;o de 400 dias.</p>
      <p class="body" style="margin: 14px 0 0"><strong>O que a s&eacute;rie mede:</strong> manchetes agregadas por dia, e n&atilde;o incidentes. &Eacute; indicador de cobertura de imprensa e de alcance das fontes monitoradas. O aviso est&aacute; dentro do pr&oacute;prio arquivo de &iacute;ndice, para que n&atilde;o se perca na reutiliza&ccedil;&atilde;o.</p>
      <p class="body" style="margin: 14px 0 0">O boletim re&uacute;ne uma edi&ccedil;&atilde;o por semana ISO, com sele&ccedil;&atilde;o <strong>por data e sem ju&iacute;zo editorial</strong>. N&atilde;o cabe a este prot&oacute;tipo escolher o que &eacute; mais relevante.</p>
    </div>
  </div>
  <div class="pills" style="margin-top: 26px">
    <a class="pill pill-solid" href="taxonomia.html">Taxonomia proposta &rarr;</a>
    <a class="pill" href="indicadores.html#dados">Dados abertos e dicion&aacute;rio &rarr;</a>
    <a class="pill" href="indicadores.html">Painel de lacunas &rarr;</a>
  </div>
</section>
"""



# ---------------------------------------------------------------------------
# Taxonomia proposta
# ---------------------------------------------------------------------------

CAMPOS = [
    ("Natureza do fato", "Sim", "explícito / implícito / potencial / não confirmado"),
    ("Modalidade principal", "Sim", "discurso de ódio / ameaça / incitação / violência / vandalismo / propaganda extremista / negacionismo / discriminação / assédio / conspiração"),
    ("Modalidade secundária", "Não", "as mesmas categorias, em seleção múltipla"),
    ("Meio de ocorrência", "Sim", "online / offline / híbrido"),
    ("Ambiente específico", "Não", "rede social / escola / universidade / culto / evento / trabalho / outro"),
    ("Alvo atingido", "Sim", "pessoa / grupo / instituição / patrimônio"),
    ("Motivação aparente", "Não", "estereótipo clássico / neonazismo / negacionismo / conspiração / religioso / político instrumentalizado / não identificado"),
    ("Nível de risco", "Sim", "1 / 2 / 3 / 4"),
    ("Risco imediato", "Sim", "sim / não"),
    ("Escalada potencial", "Não", "sim / não"),
    ("Organização", "Não", "isolado / reiterado / grupo / célula extremista / rede digital"),
    ("Evidência disponível", "Não", "print / vídeo / áudio / link / documento"),
    ("Evidência preservada", "Não", "sim / não"),
    ("Encaminhamento", "Sim", "Polícia Federal / Polícia Civil / Ministério Público / MDHC / arquivado / outro"),
    ("Status do caso", "Sim", "recebido / em triagem / encaminhado / concluído / arquivado"),
]

COMPARADO = [
    ("OSCE / ODIHR", "57 Estados participantes",
     "Nove motivações de viés, cada uma com página própria: racista e xenófoba, anti-Roma, "
     "antissemita, anti-muçulmana, anticristã, outra por religião ou crença, por deficiência, "
     "de gênero e anti-LGBTI.",
     "Define crime de ódio como ofensa penal <strong>somada a</strong> motivação de viés.",
     "https://hatecrime.osce.org/our-methodology"),
    ("CST", "Reino Unido",
     "Seis categorias de incidente: violência extrema, agressão, dano e profanação, ameaças, "
     "material impresso e comportamento abusivo. Cruzadas com o eixo online e offline.",
     "Publica também o número de relatos recebidos e descartados na triagem.",
     "https://cst.org.uk/antisemitism/report-antisemitism"),
    ("SPCJ", "França",
     "Dois eixos, atos contra pessoas e atos contra bens, subdivididos e cruzados com cinco "
     "tipos de local: internet, espaço público, meio escolar, sítios comunitários e esfera privada.",
     "A estrutura deriva da terminologia do Ministério do Interior francês.",
     "https://www.spcj.org/antisemitisme/guide-classification-rapport-antisemtisme"),
    ("RIAS", "Alemanha",
     "Adota a definição de trabalho da IHRA, operacionalizada para o contexto alemão, "
     "e analisa quatro eixos: tipo de incidente, pessoas atingidas, formas de manifestação "
     "e fundo político-ideológico.",
     "Os relatos são verificados em diálogo com quem relatou antes do registro.",
     "https://report-antisemitism.de/en/arbeitsweisen/"),
    ("FRA", "União Europeia",
     "Documento de 2026 com seção dedicada ao reconhecimento e registro da motivação de viés "
     "antissemita, defendendo policiais treinados para identificar indicadores de viés.",
     "Declara que o registro é inconsistente entre Estados-membros e que os dados não são comparáveis.",
     "https://fra.europa.eu/en/publication/2026/antisemitism-overview"),
]

TAXONOMIA = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; <a href="metodologia.html">Metodologia</a> &nbsp;/&nbsp; Taxonomia</p>
  <h1 class="h1" style="margin-top: 24px">Taxonomia proposta</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Quinze campos para classificar uma ocorr&ecirc;ncia de antissemitismo. &Eacute; <strong>proposta do Eixo 3</strong>, e n&atilde;o padr&atilde;o adotado: nenhuma base p&uacute;blica brasileira a implementa hoje.</p>
  <p class="body" style="margin: 18px 0 0; max-width: 70ch">Esta p&aacute;gina existe por uma raz&atilde;o pr&aacute;tica. A taxonomia &eacute; o &uacute;nico artefato do trabalho que pode ser publicado <strong>antes</strong> de haver dado para classificar, e &eacute; o que se leva a uma mesa institucional para sustentar a proposta de marcador. Ter endere&ccedil;o pr&oacute;prio e cit&aacute;vel &eacute; parte da fun&ccedil;&atilde;o.</p>
  <p class="body" style="margin: 18px 0 0; max-width: 70ch">Atualizada em {ATUALIZADO}. Corresponde ao Anexo II dos instrumentos de modelagem do Eixo 3.</p>
</section>

<section class="band"><div class="wrap section">
  <p class="eyebrow">O ponto central</p>
  <h2 class="h2" style="max-width: 34ch">Vi&eacute;s &eacute; atributo do fato, n&atilde;o tipo penal</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">O antissemitismo <strong>n&atilde;o precisa virar crime aut&ocirc;nomo para ser contado.</strong> Precisa ser um marcador de motiva&ccedil;&atilde;o, anexo a crimes que j&aacute; existem no direito brasileiro: inj&uacute;ria racial, racismo, amea&ccedil;a, dano, incita&ccedil;&atilde;o.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Essa &eacute; a forma adotada por cinco das principais plataformas internacionais examinadas, e nenhuma delas trata o antissemitismo como tipo penal pr&oacute;prio. E h&aacute; precedente dom&eacute;stico da mesma natureza: em 2022 o Conselho Nacional de Justi&ccedil;a inseriu assuntos de intoler&acirc;ncia religiosa nas Tabelas Processuais Unificadas <strong>por ato administrativo</strong>, e mant&eacute;m painel extra&iacute;do do DataJud. A recomenda&ccedil;&atilde;o central deste Eixo n&atilde;o depende de lei nova.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">O argumento emp&iacute;rico est&aacute; na <a href="indicadores.html#instauracao">p&aacute;gina de indicadores</a>: quando o n&uacute;cleo tem&aacute;tico &eacute; tipificado na entrada, a taxa de instaura&ccedil;&atilde;o no Minist&eacute;rio P&uacute;blico Federal quadruplica. A persecu&ccedil;&atilde;o responde ao que consegue enxergar.</p>
</div></section>

<section class="wrap section">
  <h2 class="h2" style="max-width: 30ch">Os quinze campos</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Formato operacional, pensado para formul&aacute;rio ou sistema de registro. Sete campos obrigat&oacute;rios, oito facultativos.</p>
  <div class="tab-rolagem">
    <table class="tab-kpi">
      <caption class="sr-only">Campos da taxonomia proposta, com obrigatoriedade e op&ccedil;&otilde;es padronizadas</caption>
      <thead><tr><th scope="col">Campo</th><th scope="col">Obrigat&oacute;rio</th><th scope="col">Op&ccedil;&otilde;es padronizadas</th></tr></thead>
      <tbody>{''.join(
        f'<tr><th scope="row">{c}</th>'
        f'<td><span class="status {"st-par" if o == "Sim" else "st-sem"}">{o}</span></td>'
        f'<td class="motivo">{v}</td></tr>' for c, o, v in CAMPOS)}</tbody>
    </table>
  </div>
  <p class="fonte" style="margin-top: 22px">O instrumento original tra&iacute;a tamb&eacute;m regras de valida&ccedil;&atilde;o autom&aacute;tica, como alerta para risco 3 ou 4 e encaminhamento priorit&aacute;rio quando h&aacute; ind&iacute;cio de c&eacute;lula extremista. Essas regras pressup&otilde;em um sistema que ainda n&atilde;o existe e por isso n&atilde;o s&atilde;o reproduzidas aqui como se estivessem em opera&ccedil;&atilde;o.</p>
</section>

<section class="band"><div class="wrap section">
  <p class="eyebrow">Leitura comparada</p>
  <h2 class="h2" style="max-width: 32ch">Como outras jurisdi&ccedil;&otilde;es classificam</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">Cinco plataformas com taxonomia declarada, conferidas em 04/09/2026 por leitura da p&aacute;gina de metodologia de cada uma. Nenhuma trata antissemitismo como tipo penal aut&ocirc;nomo.</p>
  <div class="comp-lista">{''.join(
    f'<div class="comp-item"><div class="comp-id"><span class="comp-nome">{n}</span>'
    f'<span class="comp-org">{o}</span></div><div><p class="body">{d}</p>'
    f'<p class="comp-nota">{nota}</p>'
    f'<p class="tl-src"><a href="{u}" target="_blank" rel="noopener">Metodologia declarada &rarr;</a></p></div></div>'
    for n, o, d, nota, u in COMPARADO)}</div>
</div></section>

<section class="wrap section">
  <h2 class="h2" style="max-width: 32ch">O que falta para a taxonomia funcionar</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Uma taxonomia sem campo na entrada &eacute; documento, n&atilde;o instrumento. O <a href="indicadores.html">painel de lacunas</a> registra os vinte indicadores da matriz proposta e o motivo de cada um estar vazio. A s&iacute;ntese &eacute; esta:</p>
  <ul class="scope-list scope-isnot" style="margin-top: 20px; max-width: 76ch">
    <li>Nenhuma base p&uacute;blica examinada tem categoria aut&ocirc;noma de antissemitismo: Anu&aacute;rio do F&oacute;rum Brasileiro de Seguran&ccedil;a P&uacute;blica, SaferNet, Comunica PF, Disque 100, boletins de ocorr&ecirc;ncia estaduais e Tabelas Processuais Unificadas do CNJ.</li>
    <li>Nenhuma base de entrada classifica risco em quatro n&iacute;veis.</li>
    <li>N&atilde;o h&aacute; campo que distinga alvo institucional de alvo individual.</li>
    <li>N&atilde;o h&aacute; campo de preserva&ccedil;&atilde;o de evid&ecirc;ncia.</li>
    <li>O desfecho processual esbarra em limite normativo leg&iacute;timo, o segredo de justi&ccedil;a, que n&atilde;o &eacute; falha a contornar.</li>
  </ul>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">Duas causas cumulativas, portanto. A aus&ecirc;ncia de categoria na entrada, san&aacute;vel por ato administrativo. E a aus&ecirc;ncia de rastreabilidade na sa&iacute;da, que decorre em parte de prote&ccedil;&atilde;o leg&iacute;tima. <strong>Apenas a primeira depende de decis&atilde;o t&eacute;cnica.</strong></p>
  <div class="pills" style="margin-top: 24px">
    <a class="pill pill-solid" href="indicadores.html">Painel de lacunas &rarr;</a>
    <a class="pill" href="metodologia.html">Metodologia &rarr;</a>
  </div>
</section>
"""

def main():
    feitos = [
        pagina("sobre.html", "Sobre o Observat&oacute;rio",
               "O que e o prototipo do Observatorio, qual definicao adota, de onde vem o conteudo e o que ele nao e.",
               "sobre.html", SOBRE),
        pagina("privacidade.html", "Pol&iacute;tica de privacidade",
               "Este sitio nao coleta dado pessoal. O que fica no navegador, quais terceiros estao envolvidos e seus direitos sob a LGPD.",
               "", PRIVACIDADE),
        pagina("termos.html", "Termos de uso",
               "Natureza do servico, limites da orientacao juridica, conteudo de terceiros, licenca e reuso.",
               "", TERMOS),
        pagina("metodologia.html", "Metodologia",
               "Como cada numero foi obtido, sobre que base foi calculado e o que ele nao mede.",
               "", METODOLOGIA),
        pagina("taxonomia.html", "Taxonomia proposta",
               "Quinze campos para classificar uma ocorrencia. Proposta do Eixo 3, com leitura comparada de cinco jurisdicoes.",
               "", TAXONOMIA),
    ]
    print("paginas institucionais: " + ", ".join(feitos))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
