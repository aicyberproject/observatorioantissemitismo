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
        ("index.html#painel", "Painel", "painel"),
        ("indicadores.html", "Indicadores", "indicadores"),
        ("boletim/index.html", "Boletim", "boletim"),
        ("index.html#preservar", "Preservar evid&ecirc;ncias", "preservar"),
        ("index.html#denuncie", "Denunciar", "denunciar"),
        ("index.html#legislacao", "Legisla&ccedil;&atilde;o", "legislacao"),
        ("biblioteca.html", "Biblioteca", "biblioteca"),
        ("sobre.html", "Sobre", "sobre"),
    ]
    return "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if k == atual else ""}>{r}</a>'
        for h, r, k in itens)


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


def main():
    feitos = [
        pagina("sobre.html", "Sobre o Observat&oacute;rio",
               "O que e o prototipo do Observatorio, qual definicao adota, de onde vem o conteudo e o que ele nao e.",
               "sobre", SOBRE),
        pagina("privacidade.html", "Pol&iacute;tica de privacidade",
               "Este sitio nao coleta dado pessoal. O que fica no navegador, quais terceiros estao envolvidos e seus direitos sob a LGPD.",
               "", PRIVACIDADE),
        pagina("termos.html", "Termos de uso",
               "Natureza do servico, limites da orientacao juridica, conteudo de terceiros, licenca e reuso.",
               "", TERMOS),
    ]
    print("paginas institucionais: " + ", ".join(feitos))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
