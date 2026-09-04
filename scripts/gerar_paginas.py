#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as paginas institucionais: sobre, privacidade, termos, metodologia,
taxonomia e contato.

Cabecalho, menu e rodape vem de scripts/layout.py, que e a fonte de verdade
unica da navegacao do sitio. Este modulo nao declara mais menu proprio.

    python3 scripts/gerar_paginas.py
"""
import pathlib, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from layout import BASE, ATUALIZADO, CONTATO, FAIXA, CABECALHO, RODAPE  # noqa: E402

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
{CABECALHO(arquivo, atual)}
<main>
{corpo}
{RODAPE(arquivo)}"""
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
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Erro em verbete, indicador, data ou endere&ccedil;o &eacute; defeito a corrigir, n&atilde;o detalhe. A p&aacute;gina de <a href="contato.html">contato e errata</a> re&uacute;ne os dois caminhos: o endere&ccedil;o de trabalho do prot&oacute;tipo e o reposit&oacute;rio p&uacute;blico do c&oacute;digo, onde qualquer pessoa pode abrir uma quest&atilde;o e onde o pedido e a resposta ficam vis&iacute;veis.</p>
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
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Enquanto o prot&oacute;tipo n&atilde;o tiver endere&ccedil;o institucional definitivo, n&atilde;o h&aacute; encarregado de prote&ccedil;&atilde;o de dados designado, porque n&atilde;o h&aacute; tratamento a encarregar. Quest&otilde;es sobre esta pol&iacute;tica, e exerc&iacute;cio dos direitos acima se e quando houver dado a que se referirem, podem ser dirigidas a <a href="mailto:{CONTATO}"><code>{CONTATO}</code></a> ou levantadas no <a href="https://github.com/aicyberproject/observatorioantissemitismo/issues" target="_blank" rel="noopener">reposit&oacute;rio p&uacute;blico do c&oacute;digo</a>. A <a href="contato.html">p&aacute;gina de contato</a> detalha os dois caminhos.</p>

  <h2 class="h2" style="max-width: 26ch; margin-top: clamp(34px, 4vw, 50px)">Se voc&ecirc; escrever para o endere&ccedil;o de contato</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">O s&iacute;tio n&atilde;o tem formul&aacute;rio: o link de contato abre o seu pr&oacute;prio programa de correio, e nenhum dado seu trafega por este servidor. A mensagem que voc&ecirc; enviar por vontade pr&oacute;pria fica na caixa postal do endere&ccedil;o de trabalho, &eacute; lida pela equipe do Eixo 3 e serve apenas para tratar o que voc&ecirc; apontou. N&atilde;o alimenta lista de divulga&ccedil;&atilde;o, n&atilde;o &eacute; usada para outra finalidade e n&atilde;o &eacute; repassada a terceiro.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Por isso a p&aacute;gina de contato pede que a mensagem <strong>n&atilde;o</strong> contenha dado pessoal, seu ou de terceiro, nem conte&uacute;do de den&uacute;ncia ou de procedimento sigiloso. Uma errata sobre n&uacute;mero publicado n&atilde;o precisa de nenhum deles, e o endere&ccedil;o de trabalho de um prot&oacute;tipo n&atilde;o &eacute; lugar para dado sens&iacute;vel.</p>
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

# ---------------------------------------------------------------------------
# Contato e errata
# ---------------------------------------------------------------------------

CONTATO_PAG = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Contato e errata</p>
  <h1 class="h1" style="margin-top: 24px">Contato e errata</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Um observat&oacute;rio que publica n&uacute;mero e verbete precisa ter como receber corre&ccedil;&atilde;o. Esta p&aacute;gina existe para isso, e diz com precis&atilde;o o que este canal &eacute; e o que ele n&atilde;o &eacute;.</p>
</section>

<section class="wrap section" style="padding-top: clamp(24px, 3vw, 40px)">
  <div class="met-grid">
    <div>
      <h2 class="h2" style="max-width: 26ch">Este canal n&atilde;o recebe den&uacute;ncia</h2>
      <p class="body" style="margin: 18px 0 0"><strong>Se voc&ecirc; foi v&iacute;tima ou testemunha de um incidente antissemita, n&atilde;o escreva para c&aacute;.</strong> Este prot&oacute;tipo n&atilde;o recebe den&uacute;ncia, n&atilde;o a encaminha e n&atilde;o tem compet&ecirc;ncia para apurar. Um relato enviado para este endere&ccedil;o n&atilde;o produz efeito legal e n&atilde;o interrompe prazo nenhum.</p>
      <p class="body" style="margin: 14px 0 0">Os canais que recebem est&atilde;o na <a href="index.html#denuncie">se&ccedil;&atilde;o de den&uacute;ncia</a>, s&atilde;o das pr&oacute;prias institui&ccedil;&otilde;es e funcionam de forma independente deste prot&oacute;tipo. Antes disso, a <a href="index.html#preservar">se&ccedil;&atilde;o de preserva&ccedil;&atilde;o</a> orienta como guardar a prova, que &eacute; o que costuma se perder primeiro.</p>

      <h2 class="h2" style="max-width: 26ch; margin-top: clamp(34px, 4vw, 50px)">Para que serve, ent&atilde;o</h2>
      <p class="body" style="margin: 18px 0 0">Para apontar erro no que est&aacute; publicado aqui. Especificamente:</p>
      <ul class="body" style="margin: 14px 0 0; padding-left: 20px">
        <li>dado errado num indicador, ou fonte que n&atilde;o confirma o n&uacute;mero citado;</li>
        <li>verbete da <a href="biblioteca.html">biblioteca</a> com refer&ecirc;ncia incorreta, incompleta ou desatualizada;</li>
        <li>erro de fato na linha do tempo, inclusive placar de julgamento e data;</li>
        <li>endere&ccedil;o quebrado, canal de den&uacute;ncia que mudou, acervo que saiu do ar;</li>
        <li>perfil da <a href="serie/index.html">s&eacute;rie</a> cuja fonte prim&aacute;ria diga outra coisa;</li>
        <li>problema de acessibilidade que impe&ccedil;a a leitura da p&aacute;gina.</li>
      </ul>

      <h2 class="h2" style="max-width: 26ch; margin-top: clamp(34px, 4vw, 50px)">Endere&ccedil;o</h2>
      <p class="body" style="margin: 18px 0 0"><a href="mailto:{CONTATO}"><code>{CONTATO}</code></a></p>
      <div class="ser-diverg" style="margin-top: 18px">
        <p class="label">Leia antes de escrever</p>
        <p class="body">Este &eacute; um endere&ccedil;o de trabalho do prot&oacute;tipo, em dom&iacute;nio <strong>pessoal</strong>, e n&atilde;o um canal institucional. N&atilde;o &eacute; endere&ccedil;o do CDESS, da Presid&ecirc;ncia da Rep&uacute;blica nem de qualquer &oacute;rg&atilde;o citado no conte&uacute;do, e escrever para ele n&atilde;o constitui peti&ccedil;&atilde;o, requerimento nem protocolo perante nenhum deles. Quando o Observat&oacute;rio tiver endere&ccedil;o institucional definitivo, este canal ser&aacute; substitu&iacute;do e a mudan&ccedil;a ficar&aacute; registrada aqui.</p>
      </div>

      <h2 class="h2" style="max-width: 26ch; margin-top: clamp(34px, 4vw, 50px)">O que ajuda numa errata</h2>
      <p class="body" style="margin: 18px 0 0">Quatro coisas, e s&oacute; elas: o <strong>endere&ccedil;o da p&aacute;gina</strong>, o <strong>trecho</strong> como est&aacute; publicado, <strong>o que estaria correto</strong> e a <strong>fonte p&uacute;blica</strong> que sustenta a corre&ccedil;&atilde;o. Sem a fonte, a corre&ccedil;&atilde;o entra na fila de confer&ecirc;ncia como qualquer outra; com ela, resolve-se na leitura.</p>
      <p class="body" style="margin: 14px 0 0"><strong>N&atilde;o inclua dado pessoal</strong>, seu ou de terceiro, nem conte&uacute;do de den&uacute;ncia, de procedimento sigiloso ou de investiga&ccedil;&atilde;o. Uma errata sobre um n&uacute;mero publicado n&atilde;o precisa de nada disso.</p>
    </div>
    <div>
      <h2 class="h2" style="max-width: 22ch">Como a corre&ccedil;&atilde;o aparece</h2>
      <p class="body" style="margin: 18px 0 0">Erro confirmado n&atilde;o &eacute; apagado em sil&ecirc;ncio. A pr&aacute;tica j&aacute; aplicada nesta plataforma &eacute; publicar a <strong>nota de revis&atilde;o</strong> ao lado do item corrigido, dizendo o que estava escrito, o que passou a estar e em que fonte se conferiu. O hist&oacute;rico do c&oacute;digo &eacute; p&uacute;blico, e a altera&ccedil;&atilde;o fica rastre&aacute;vel nele.</p>
      <p class="body" style="margin: 14px 0 0">A biblioteca tem hoje dez notas desse tipo. A mais recente corrigiu o placar do <em>habeas corpus</em> 82.424/RS, que constava como oito a tr&ecirc;s e &eacute; de sete a tr&ecirc;s conforme a not&iacute;cia do julgamento no portal do Supremo.</p>

      <h2 class="h2" style="max-width: 22ch; margin-top: clamp(34px, 4vw, 50px)">Canal alternativo</h2>
      <p class="body" style="margin: 18px 0 0">Quem preferir registro p&uacute;blico pode abrir a quest&atilde;o no <a href="https://github.com/aicyberproject/observatorioantissemitismo/issues" rel="noopener">reposit&oacute;rio do c&oacute;digo</a>, onde o pedido e a resposta ficam vis&iacute;veis a qualquer pessoa. Para errata, esse caminho &eacute; prefer&iacute;vel: a corre&ccedil;&atilde;o e a raz&atilde;o dela ficam documentadas junto da mudan&ccedil;a.</p>

      <h2 class="h2" style="max-width: 22ch; margin-top: clamp(34px, 4vw, 50px)">O que acontece com sua mensagem</h2>
      <p class="body" style="margin: 18px 0 0">O s&iacute;tio n&atilde;o tem formul&aacute;rio e n&atilde;o coleta endere&ccedil;o de e-mail: o link acima abre o seu pr&oacute;prio programa de correio, e nada trafega por aqui. A mensagem que voc&ecirc; enviar fica na caixa postal do endere&ccedil;o, &eacute; lida pela equipe de trabalho do Eixo 3 e serve apenas para tratar o que voc&ecirc; apontou.</p>
      <p class="body" style="margin: 14px 0 0">N&atilde;o h&aacute; lista de divulga&ccedil;&atilde;o, e seu endere&ccedil;o n&atilde;o &eacute; usado para outra finalidade nem repassado a terceiro. A <a href="privacidade.html">pol&iacute;tica de privacidade</a> registra isso.</p>

      <h2 class="h2" style="max-width: 22ch; margin-top: clamp(34px, 4vw, 50px)">Prazo</h2>
      <p class="body" style="margin: 18px 0 0">Nenhum prazo &eacute; prometido. O prot&oacute;tipo &eacute; mantido por equipe de trabalho, sem plant&atilde;o. Erro de fato em n&uacute;mero publicado tem prioridade sobre pedido de conte&uacute;do novo, porque n&uacute;mero errado no ar &eacute; o defeito mais grave que um observat&oacute;rio pode ter.</p>
    </div>
  </div>
  <p class="body" style="margin: 26px 0 0; max-width: 70ch">Atualizada em {ATUALIZADO}.</p>
</section>
"""


# ---------------------------------------------------------------------------
# Preservar evidencias
# ---------------------------------------------------------------------------
#
# Frentes 24 e 25 da secao 8.5 da auditoria: seletor de tipo de incidente com o
# roteiro correspondente, e checklist dos primeiros 60 minutos. Nenhuma das duas
# recolhe dado, e e por isso que a auditoria manda fazer estas antes das outras
# duas frentes, que recolhem e sao decisao a parte.
#
# TRES DECISOES DE DESENHO, todas com a mesma razao: quem chega aqui pode estar
# em aparelho alheio, com conexao ruim, ou com pressa.
#
# 1. Os tipos sao ANCORAS, e nao filtro em JavaScript. Todo o conteudo esta no
#    DOM. Funciona sem script, imprime inteiro, e cada tipo tem endereco proprio
#    para poder ser passado a alguem.
# 2. O checklist usa caixa nativa, SEM script e SEM persistencia. Nada e gravado,
#    nem no proprio aparelho: marcar etapa concluida numa pagina de preservacao
#    de prova seria guardar rastro de caso, e nao preferencia de exibicao.
# 3. A ferramenta de hash NAO foi movida. Continua em index.html#preservar, onde
#    esta verificada e funcionando. Esta pagina remete a ela.

TIPOS = [
    ("online", "Conteúdo em rede social, site ou comentário",
     "discurso de ódio, negacionismo, conspiração", "online"),
    ("ameaca", "Mensagem direta, ameaça ou intimidação",
     "ameaça, assédio", "online ou híbrido"),
    ("patrimonio", "Pichação, dano ou profanação de patrimônio",
     "vandalismo", "offline"),
    ("fisica", "Agressão física, ou tentativa",
     "violência", "offline"),
    ("institucional", "Discriminação em escola, universidade ou trabalho",
     "discriminação, assédio", "offline ou híbrido"),
    ("objeto", "Material impresso, panfleto ou objeto deixado",
     "propaganda extremista", "offline"),
]

def _tipos_grade():
    itens = []
    for i, (chave, titulo, _, _) in enumerate(TIPOS, 1):
        itens.append(
            f'<li><a class="prs-tipo" href="#{chave}">'
            f'<span class="prs-tipo-n">{i:02d}</span>'
            f'<span class="prs-tipo-t">{titulo}</span></a></li>')
    return "".join(itens)

def _check(itens):
    linhas = []
    for i, (titulo, porque) in enumerate(itens, 1):
        linhas.append(
            f'<li><input type="checkbox" id="chk{i}">'
            f'<label for="chk{i}"><span class="prs-check-t">{titulo}</span>'
            f'<span class="prs-check-q">{porque}</span></label></li>')
    return "".join(linhas)

SESSENTA = [
    ("Grave a tela do conteúdo que se apaga sozinho",
     "Story, status, mensagem temporária e transmissão ao vivo somem em horas, e print não captura vídeo nem áudio. É o único item que pode ser impossível daqui a pouco."),
    ("Capture o perfil de quem publicou",
     "Nome de exibição, nome de usuário, endereço do perfil, biografia e número de seguidores. O perfil pode ser apagado, trocado de nome ou fechado em minutos, e sem ele a autoria fica em aberto."),
    ("Capture o conteúdo com o endereço, a data e a hora visíveis na tela",
     "Print em que se leia a URL inteira. Sem o endereço na imagem, a captura vale menos: não se sabe de onde saiu."),
    ("Salve a página completa, e não só a imagem",
     "Salvar como página web completa guarda o código, os comentários e a estrutura. É o que permite conferir depois o que o print recortou."),
    ("Anote quem viu",
     "Nome e contato de testemunhas, e o que cada uma presenciou. Memória se desfaz e disponibilidade se perde, e isso não se recupera com ferramenta nenhuma."),
    ("Fotografe o contexto físico antes de qualquer limpeza",
     "Foto ampla que situe o local, e depois a aproximação. Pichação é apagada rápido, muitas vezes no mesmo dia e por boa intenção."),
    ("Salve o endereço no Internet Archive",
     "A Wayback Machine cria uma cópia datada por terceiro, independente de você. Leva segundos e não depende do seu arquivo."),
    ("Só então calcule o resumo criptográfico",
     "O arquivo já é seu, e o hash pode ser calculado com calma. É o último passo justamente porque nada nele se perde com o tempo."),
]

PRESERVAR = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="index.html">Observatório</a> &nbsp;/&nbsp; Preservar evidências</p>
  <h1 class="h1" style="margin-top: 24px">Preservar evidências</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Prova de ato antissemita se perde por conta própria. Post é apagado, story expira, perfil é fechado, pichação é limpa. O que se captura na primeira hora costuma ser o que ainda existe.</p>

  <div class="prs-risco" role="note">
    <p class="prs-risco-t">Se há risco agora, não comece preservando.</p>
    <p class="body" style="margin: 10px 0 0">Ameaça em curso, perseguição, alguém ferido ou risco de agressão: ligue <span class="prs-fone">190</span>, ou <span class="prs-fone">192</span> se houver ferido. Integridade de pessoa vem antes de prova, e prova nenhuma compensa dano que podia ser evitado.</p>
    <p class="body" style="margin: 10px 0 0">É a exceção declarada à regra desta página. Fora dela, preserve antes de denunciar: o registro formal pode esperar minutos, o conteúdo online não.</p>
  </div>
</section>

<section class="wrap section" style="padding-top: clamp(24px, 3vw, 40px)">
  <p class="eyebrow">Os primeiros 60 minutos</p>
  <h2 class="h2" style="max-width: 26ch">Na ordem do que desaparece primeiro</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">A ordem abaixo <strong>não é por importância</strong>, e sim por prazo de validade. O que expira sozinho vem antes do que fica parado esperando. Um hash pode ser calculado amanhã; um story, não.</p>
  <p class="body" style="margin: 12px 0 0; max-width: 72ch">Nem tudo se aplica ao seu caso. Pule o que não couber.</p>

  <ul class="prs-check">{_check(SESSENTA)}</ul>
  <p class="step-note" style="margin: 14px 0 0">As caixas acima servem só para você não se perder na sequência. <strong>Nada é enviado e nada é guardado</strong>, nem neste aparelho: ao recarregar a página elas voltam em branco, de propósito.</p>
</section>

<section class="wrap section" style="padding-top: clamp(10px, 2vw, 24px)">
  <p class="eyebrow">Roteiro por tipo</p>
  <h2 class="h2" style="max-width: 24ch">O que capturar, em cada situação</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 72ch">Seis situações, porque o procedimento muda entre elas. Cada uma tem endereço próprio e pode ser passada a quem precisa.</p>
  <ul class="prs-tipos">{_tipos_grade()}</ul>

  <div class="prs-roteiro" id="online">
    <h3 class="h3-display">01 &middot; Conteúdo em rede social, site ou comentário</h3>
    <ul class="body prs-lista">
      <li>Print com o <strong>endereço completo visível</strong> na barra do navegador, mais data e hora do aparelho na tela.</li>
      <li>Print do <strong>perfil do autor</strong>: nome de exibição, nome de usuário, endereço do perfil e biografia. Nome de exibição muda; o nome de usuário e o endereço são o que identifica.</li>
      <li><strong>Salvar como página web completa</strong>, não só imagem. Guarda comentários, código e o que o print recortou.</li>
      <li>Se houver comentários relevantes, capture-os <strong>com o autor de cada um</strong>. Comentário sem autoria não serve para nada depois.</li>
      <li>Salve o endereço na <a href="https://web.archive.org/save" target="_blank" rel="noopener">Wayback Machine</a>, que gera cópia datada por terceiro.</li>
      <li><strong>Denuncie na própria plataforma também</strong>, e guarde o número do protocolo. É o que demonstra, depois, que a plataforma foi avisada e quando.</li>
    </ul>
    <p class="body" style="margin: 14px 0 0; max-width: 72ch"><strong>Conteúdo que se apaga sozinho</strong> &mdash; story, status, mensagem temporária, transmissão ao vivo &mdash; exige <strong>gravação de tela</strong>, e não print: print perde o vídeo, o áudio e a duração. Este é o caso em que a primeira hora decide se há prova.</p>
    <p class="prs-tax">Na taxonomia proposta: discurso de ódio, negacionismo, conspiração &middot; meio online</p>
    <p class="prs-volta"><a href="#topo">Voltar ao início</a></p>
  </div>

  <div class="prs-roteiro" id="ameaca">
    <h3 class="h3-display">02 &middot; Mensagem direta, ameaça ou intimidação</h3>
    <ul class="body prs-lista">
      <li><strong>Não responda e não confronte.</strong> Resposta costuma provocar escalada e, em alguns casos, apagamento do que existia.</li>
      <li><strong>Não apague a conversa</strong>, mesmo que seja penoso mantê-la. Apagar destrói a prova, não o fato.</li>
      <li>Capture a conversa <strong>inteira e em sequência</strong>, incluindo o que veio antes. Recorte de uma frase perde o contexto que mostra a intenção.</li>
      <li>Capture o <strong>número, o endereço de e-mail ou o perfil</strong> de origem, e o horário de cada mensagem.</li>
      <li>Se vier por carta, telefone ou recado: anote data, hora e teor logo, enquanto está fresco, e <strong>guarde o objeto sem manusear mais</strong> que o necessário.</li>
      <li>Havendo <strong>menção a arma, a endereço seu, a rotina sua ou a familiares</strong>, trate como risco imediato: <span class="prs-fone">190</span> primeiro.</li>
    </ul>
    <p class="prs-tax">Na taxonomia proposta: ameaça, assédio &middot; meio online ou híbrido</p>
    <p class="prs-volta"><a href="#topo">Voltar ao início</a></p>
  </div>

  <div class="prs-roteiro" id="patrimonio">
    <h3 class="h3-display">03 &middot; Pichação, dano ou profanação de patrimônio</h3>
    <ul class="body prs-lista">
      <li><strong>Não limpe, não cubra e não remova antes de fotografar.</strong> É o erro mais comum, e é feito por boa intenção: a vontade de apagar a ofensa apaga também a prova.</li>
      <li>Fotografe em <strong>três distâncias</strong>: o conjunto que situa o local, o plano médio, e a aproximação em que se leia a inscrição ou o símbolo.</li>
      <li>Inclua uma <strong>referência de escala</strong> na foto de aproximação, como uma régua ou objeto de tamanho conhecido, e registre a data e a hora.</li>
      <li>Registre <strong>onde exatamente</strong> foi: fachada, muro, portão, lápide, sala de aula. Em cemitério e em templo, o local é elemento do fato.</li>
      <li>Procure <strong>câmeras</strong> no local e na vizinhança e peça a preservação da gravação <strong>logo</strong>: sistema comum sobrescreve em poucos dias.</li>
      <li>Avise a <strong>administração do imóvel ou da instituição</strong> por escrito, e guarde o comprovante do aviso.</li>
    </ul>
    <p class="prs-tax">Na taxonomia proposta: vandalismo &middot; meio offline</p>
    <p class="prs-volta"><a href="#topo">Voltar ao início</a></p>
  </div>

  <div class="prs-roteiro" id="fisica">
    <h3 class="h3-display">04 &middot; Agressão física, ou tentativa</h3>
    <ul class="body prs-lista">
      <li><strong>Atendimento primeiro.</strong> <span class="prs-fone">192</span> para o SAMU, <span class="prs-fone">190</span> para a polícia. Aqui a ordem se inverte: preservação vem depois do cuidado.</li>
      <li>Procure <strong>atendimento médico ainda que a lesão pareça pequena</strong>. O registro do atendimento é o que documenta a lesão depois que ela cicatriza.</li>
      <li>Peça o <strong>exame de corpo de delito</strong> ao registrar a ocorrência. É ele que produz o laudo, e o prazo útil é curto.</li>
      <li>Fotografe as <strong>lesões</strong> no dia, e de novo nos dias seguintes: hematoma muda de cor e a evolução é informativa.</li>
      <li>Guarde <strong>roupa e objetos</strong> como estão, sem lavar, em saco de papel e não de plástico.</li>
      <li>Anote <strong>testemunhas</strong> antes de sair do local, se for possível fazê-lo com segurança.</li>
    </ul>
    <p class="prs-tax">Na taxonomia proposta: violência &middot; meio offline &middot; risco imediato: sim</p>
    <p class="prs-volta"><a href="#topo">Voltar ao início</a></p>
  </div>

  <div class="prs-roteiro" id="institucional">
    <h3 class="h3-display">05 &middot; Discriminação em escola, universidade ou trabalho</h3>
    <ul class="body prs-lista">
      <li>Há <strong>dois caminhos, e eles não se substituem</strong>: o canal interno da instituição e o externo. Usar o interno não impede o registro policial, e o interno costuma ter prazo próprio.</li>
      <li>Registre por escrito no <strong>canal formal</strong> &mdash; ouvidoria, coordenação, comissão, recursos humanos &mdash; e guarde o protocolo. Conversa de corredor não deixa rastro.</li>
      <li>Prefira <strong>e-mail a conversa presencial</strong> quando puder escolher: gera data, destinatário e teor.</li>
      <li>Mantenha uma <strong>cronologia própria</strong>: data, hora, local, quem estava, o que foi dito. Em caso reiterado, a sequência importa mais que o episódio isolado.</li>
      <li>Guarde <strong>o que já é documento</strong>: mensagens de grupo da turma ou da equipe, atas, avaliações, escalas, e-mails.</li>
      <li>Em <strong>escola com estudante menor de idade</strong>, o responsável deve ser comunicado e o Conselho Tutelar pode ser acionado.</li>
    </ul>
    <p class="prs-tax">Na taxonomia proposta: discriminação, assédio &middot; ambiente escola, universidade ou trabalho</p>
    <p class="prs-volta"><a href="#topo">Voltar ao início</a></p>
  </div>

  <div class="prs-roteiro" id="objeto">
    <h3 class="h3-display">06 &middot; Material impresso, panfleto ou objeto deixado</h3>
    <ul class="body prs-lista">
      <li><strong>Manuseie o mínimo.</strong> Se for possível fotografar sem pegar, fotografe primeiro.</li>
      <li>Registre <strong>onde estava e como estava</strong>: sob a porta, na caixa de correio, no para-brisa, colado em poste. O modo de entrega diz se houve deslocamento até você.</li>
      <li>Fotografe <strong>frente e verso</strong>, e o conjunto se houver mais de um exemplar.</li>
      <li>Guarde em <strong>envelope ou saco de papel</strong>, um item por invólucro, com data e local anotados por fora.</li>
      <li>Verifique se <strong>vizinhos receberam</strong> o mesmo. Distribuição em série muda a natureza do fato e sugere ação organizada.</li>
      <li>Se houver <strong>indício de organização</strong> &mdash; sigla, símbolo de grupo, endereço, convite para reunião &mdash; registre e mencione ao denunciar.</li>
    </ul>
    <p class="prs-tax">Na taxonomia proposta: propaganda extremista &middot; organização: possivelmente grupo ou célula</p>
    <p class="prs-volta"><a href="#topo">Voltar ao início</a></p>
  </div>
</section>

<section class="band">
  <div class="wrap section">
    <p class="eyebrow">Vale para todos os casos</p>
    <h2 class="h2" style="max-width: 24ch">O que não fazer</h2>
    <ul class="body prs-lista" style="max-width: 72ch">
      <li><strong>Não confronte o autor.</strong> Não melhora a prova e pode agravar o risco.</li>
      <li><strong>Não apague nada</strong>, nem a conversa, nem o e-mail, nem o objeto.</li>
      <li><strong>Não edite o arquivo original.</strong> Recorte, ajuste de brilho e marcação alteram o arquivo. Trabalhe sobre cópia e guarde o original intacto.</li>
      <li><strong>Não limpe o local</strong> antes de fotografar.</li>
      <li><strong>Não publique o print com dado pessoal de terceiro</strong> à mostra. Divulgar o endereço, o telefone ou o local de trabalho de alguém cria problema novo, inclusive para você.</li>
      <li><strong>Não conte só com a plataforma.</strong> Conteúdo denunciado é removido, e removido você não recupera. Capture antes de denunciar lá.</li>
    </ul>
  </div>
</section>

<section class="wrap section">
  <div class="met-grid">
    <div>
      <h2 class="h2" style="max-width: 24ch">Depois de preservar</h2>
      <p class="body" style="margin: 18px 0 0">Com a captura feita, três coisas dão peso ao que você guardou:</p>
      <ul class="body prs-lista">
        <li>O <a href="index.html#preservar">inventário de integridade</a> calcula o resumo SHA-256 dos seus arquivos. O cálculo é local e nada sai do navegador. Guarde o valor junto da prova.</li>
        <li>A <strong>ata notarial</strong>, em Tabelionato de Notas, tem fé pública, e é a prova mais forte para o Judiciário. O hash não substitui a ata: um demonstra que o arquivo não mudou, a outra atesta o que o tabelião viu.</li>
        <li>O <a href="index.html#denuncie">registro formal</a>, nos canais das próprias instituições. Guarde o número de protocolo de cada um.</li>
      </ul>
      <p class="bridge" style="margin-top: 26px">Prova preservada, próximo passo é a denúncia. <a href="index.html#denuncie">Ir para os canais de denúncia &rarr;</a></p>
    </div>
    <div>
      <h2 class="h2" style="max-width: 22ch">Limites desta página</h2>
      <p class="body" style="margin: 18px 0 0">Orientação informativa, e não parecer. Não considera as circunstâncias do seu caso e não cria relação de patrocínio. Antes de agir com base no que leu aqui, procure orientação profissional: <strong>Defensoria Pública</strong> ou advogado.</p>
      <p class="body" style="margin: 14px 0 0">Esta página <strong>não recebe denúncia</strong> e não substitui boletim de ocorrência. Os <a href="index.html#denuncie">canais de denúncia</a> são das próprias instituições e funcionam de forma independente deste protótipo.</p>
      <p class="body" style="margin: 14px 0 0">A base legal aplicável está na <a href="index.html#legislacao">seção de legislação</a> e na <a href="biblioteca.html">biblioteca</a>, com link para o texto de origem de cada norma. Norma muda e prazo corre: confira na origem.</p>
      <p class="body" style="margin: 14px 0 0">As classificações citadas ao pé de cada roteiro remetem à <a href="taxonomia.html">taxonomia proposta</a> pelo Eixo 3. É <strong>proposta, e não padrão adotado</strong>: nenhuma base pública brasileira a implementa hoje. Servem para leitura do fenômeno, e não como campo a preencher em formulário existente.</p>
      <p class="body" style="margin: 14px 0 0">Atualizada em {ATUALIZADO}.</p>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Glossario
# ---------------------------------------------------------------------------
#
# Item 7 da secao 8.2 da auditoria. A fonte e
# EIXO3/00_CONFIG/CONVENCOES_E_GLOSSARIO.md, curada em tres pontos:
#
# 1. Sairam os termos de processo interno, que nao dizem nada a um leitor de
#    fora: Frente 1, Frente 2, Diligencia D01-D17 e Matriz de Diligencias.
# 2. Entraram os termos que o proprio sitio usa e definia so de passagem:
#    natureza do dado, grau de verificacao, subnotificacao, lacuna, ata
#    notarial, resumo criptografico. As definicoes sao as ja publicadas nas
#    respectivas paginas, e nao versoes novas.
# 3. A entrada de taxonomia NAO repete a contagem da fonte interna, que fala
#    em "8 camadas". A pagina publicada declara quinze campos e nao usa a
#    palavra camada. Divergencia registrada na auditoria; aqui vale o que o
#    sitio sustenta.
#
# IHRA e a Declaracao de Jerusalem entram como o que sao, e nao como
# enquadramento adotado: o sitio adota o do STF no HC 82.424/RS e declara nao
# tomar posicao na controversia. A entrada repete essa posicao, em vez de
# deixar o leitor supor.

GRUPOS = [
    ("iniciativa", "A Iniciativa e este protótipo", [
        ("Iniciativa de Enfrentamento ao Antissemitismo", None,
         'Denominação oficial desde 31 de julho de 2026. Documentos expedidos antes disso preservam a denominação anterior, "GT Enfrentamento ao Antissemitismo".'),
        ("CDESS", "Conselho de Desenvolvimento Econômico, Social e Sustentável",
         'Colegiado no âmbito do qual a Iniciativa se desenvolve. Este protótipo não foi apreciado por ele e não constitui sua manifestação.'),
        ("Eixo 3", "Segurança e Monitoramento",
         'Um dos eixos temáticos da Iniciativa, e o responsável por este protótipo. Seu mandato é validar limitações institucionais de registro e monitoramento, não padronizar canais de denúncia.'),
        ("Protótipo", None,
         'A condição declarada deste sítio. Versão de trabalho, sem caráter oficial, não apreciada pelo Eixo nem pela reunião de coordenadores, e fora de indexação enquanto durar essa condição.'),
    ]),
    ("medida", "Como o fenômeno é medido, e por que mal se mede", [
        ("Invisibilidade estatística", None,
         'Diluição do fenômeno em categorias genéricas, o que produz falsa negatividade nas séries. Nenhuma base pública brasileira examinada tem categoria autônoma de antissemitismo: o fato entra como injúria racial, racismo, intolerância religiosa, ameaça ou "outros crimes", e deixa de ser contável como antissemitismo.'),
        ("Marcador", None,
         'Campo ou etiqueta que permite separar o antissemitismo de categorias mais amplas, sem criar tipo penal novo. É a recomendação central do Eixo 3, e não depende de lei: o Conselho Nacional de Justiça inseriu assuntos de intolerância religiosa nas Tabelas Processuais Unificadas por ato administrativo.'),
        ("Funil institucional", None,
         'Modelo de conversão denúncia → registro → apuração → processo, usado como referência metodológica. Serve para localizar em que etapa o caso se perde.'),
        ("Subnotificação", None,
         'Distância entre incidentes ocorridos e incidentes denunciados. Na pesquisa intracomunitária de 2025, 32,58% de quem sofreu um incidente o denunciou. Toda leitura de alta ou de queda nas séries mistura variação do fenômeno com variação da propensão a denunciar.'),
        ("Natureza do dado", None,
         'Marca que cada número da página de indicadores carrega, para que números de origens diferentes não sejam somados: contagem de fonte comunitária, registro oficial agregado, apuração de outra jurisdição e pesquisa de percepção. A prática vem do ODIHR, que mantém dois acervos separados e nunca os junta.'),
        ("Grau de verificação", None,
         'Selo que declara até onde a conferência foi: conferido no acervo, quando o valor foi checado contra o documento de origem; citado, primária não consultada, quando a fonte está declarada mas a publicação não foi aberta.'),
        ("Lacuna", None,
         'Ausência de dado que nenhuma base preenche. Neste trabalho a lacuna é registrada como achado, e não omitida como falha: a página de indicadores mantém painel próprio com vinte delas e o motivo de cada uma.'),
    ]),
    ("definicao", "Definição do fenômeno", [
        ("HC 82.424/RS", "Caso Ellwanger, 2003",
         'Julgamento em que o Supremo Tribunal Federal fixou que o antissemitismo se qualifica como racismo, crime inafiançável e imprescritível nos termos do art. 5º, XLII, da Constituição. É o enquadramento adotado por este Observatório. Decidido por maioria de sete a três.'),
        ("IHRA", "International Holocaust Remembrance Alliance",
         'Organização intergovernamental que mantém uma definição de trabalho de antissemitismo, adotada por diversos países. Este Observatório não adota instrumento internacional: o enquadramento vigente no direito brasileiro é o do HC 82.424/RS, e sobre a controvérsia quanto às definições internacionais o Observatório não toma posição e não é a instância competente para resolvê-la.'),
        ("Declaração de Jerusalém", "JDA, Jerusalem Declaration on Antisemitism",
         'Definição alternativa proposta por um grupo de acadêmicos, em parte como crítica à da IHRA. Vale aqui a mesma posição declarada acima.'),
    ]),
    ("instrumentos", "Instrumentos propostos pelo Eixo 3", [
        ("Taxonomia proposta", None,
         'Conjunto de quinze campos para classificar uma ocorrência, sete obrigatórios e oito facultativos. É proposta, e não padrão adotado: nenhuma base pública brasileira a implementa. O detalhamento está na página de taxonomia.'),
        ("Ficha Padrão Nacional", None,
         'Conjunto mínimo de campos proposto para registro de denúncia, de modo que canais diferentes produzam dado comparável.'),
        ("Nota de fronteira", None,
         'Documento que delimita a competência entre dois canais que se sobrepõem, por exemplo entre o Comunica PF e a Ouvidoria da Polícia Federal. Serve para que o denunciante não seja devolvido de um para o outro.'),
    ]),
    ("canais", "Canais e órgãos brasileiros", [
        ("Comunica PF", None,
         'Canal de notícia-crime da Polícia Federal.'),
        ("Disque 100", "Ouvidoria Nacional de Direitos Humanos, ONDH",
         'Canal de denúncia de violações de direitos humanos, no Ministério dos Direitos Humanos e da Cidadania.'),
        ("Fala.BR", None,
         'Plataforma integrada de ouvidoria e acesso à informação, da Controladoria-Geral da União.'),
        ("DECRADI", "Delegacia de Crimes Raciais e Delitos de Intolerância",
         'Delegacia especializada da Polícia Civil de São Paulo.'),
        ("GECRADI", "Grupo Especial de Combate aos Crimes Raciais e Delitos de Intolerância",
         'Grupo especializado no Ministério Público de São Paulo.'),
        ("MPF", "Ministério Público Federal",
         'Recebe representação sobre crime de competência federal, inclusive conteúdo online de alcance interestadual.'),
        ("Defensoria Pública", None,
         'Assistência jurídica gratuita a quem não tem condição de contratar advogado. É o caminho recomendado nesta plataforma para quem precisa de orientação sobre o próprio caso, que este protótipo não presta.'),
        ("TPU e DataJud", "Tabelas Processuais Unificadas e Base Nacional de Dados do Poder Judiciário",
         'Instrumentos do Conselho Nacional de Justiça. É onde um marcador de motivação produziria série judicial, e é o precedente de que a inserção pode ser feita por ato administrativo.'),
    ]),
    ("fontes", "Entidades e fontes de dados", [
        ("CONIB", "Confederação Israelita do Brasil",
         'Entidade de representação nacional. Publica relatório anual de antissemitismo no Brasil, que é a fonte dos indicadores da série brasileira desta plataforma.'),
        ("FISESP", "Federação Israelita do Estado de São Paulo",
         'Entidade estadual, com canal próprio de recebimento de relatos.'),
        ("SaferNet", None,
         'Organização da sociedade civil que opera central nacional de denúncias de crimes cibernéticos, em cooperação com o Ministério Público Federal.'),
        ("Fórum Brasileiro de Segurança Pública", "FBSP",
         'Organização que publica o Anuário Brasileiro de Segurança Pública, principal compilação de dados criminais do país. Examinado neste trabalho, e sem categoria autônoma de antissemitismo.'),
        ("ODIHR", "Office for Democratic Institutions and Human Rights",
         'Escritório da OSCE que mantém o principal acervo comparado de crimes de ódio. A disciplina de não somar dado oficial com dado da sociedade civil, adotada nesta plataforma, vem dele.'),
        ("FRA", "European Union Agency for Fundamental Rights",
         'Agência da União Europeia que produz pesquisas de percepção e de experiência de antissemitismo entre judeus europeus.'),
        ("ADL", "Anti-Defamation League",
         'Organização estadunidense que publica levantamento anual de incidentes antissemitas naquele país.'),
        ("INHOPE", None,
         'Rede internacional de hotlines de denúncia de conteúdo ilegal online.'),
    ]),
    ("prova", "Preservação de prova", [
        ("Ata notarial", None,
         'Instrumento lavrado em Tabelionato de Notas em que o tabelião atesta o que constatou. Tem fé pública, e é a prova mais forte para o Judiciário entre as tratadas nesta plataforma.'),
        ("Resumo criptográfico", "hash, SHA-256",
         'Valor calculado a partir de um arquivo, que muda se o arquivo mudar. Demonstra depois que o arquivo entregue é exatamente o capturado. Não substitui a ata notarial: um mostra que o arquivo não mudou, a outra atesta o que o tabelião viu.'),
        ("Wayback Machine", "Internet Archive",
         'Serviço que guarda cópia datada de uma página, feita por terceiro e independente do denunciante. Útil quando o conteúdo original é removido.'),
        ("Marco Civil da Internet", "Lei nº 12.965/2014",
         'Norma que disciplina, entre outras coisas, a guarda de registros de conexão e de acesso, e a responsabilidade de provedores. O texto e o histórico de julgamento estão na biblioteca e na seção de legislação.'),
    ]),
]


def _glossario_indice():
    return "".join(
        f'<li><a href="#{chave}">{titulo}</a></li>'
        for chave, titulo, _ in GRUPOS)


def _glossario_corpo():
    blocos = []
    for chave, titulo, termos in GRUPOS:
        itens = []
        for termo, sigla, texto in sorted(termos, key=lambda x: x[0].lower()):
            marca = f' <span class="glo-sigla">{sigla}</span>' if sigla else ""
            itens.append(f"<dt>{termo}{marca}</dt><dd>{texto}</dd>")
        blocos.append(
            f'<div class="glo-bloco" id="{chave}">'
            f'<h2 class="h2" style="max-width: 26ch">{titulo}</h2>'
            f'<dl class="glo-lista">{"".join(itens)}</dl></div>')
    return "".join(blocos)


GLOSSARIO = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="index.html">Observatório</a> &nbsp;/&nbsp; Glossário</p>
  <h1 class="h1" style="margin-top: 24px">Glossário</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Os termos que aparecem nesta plataforma, incluindo os que são propostos pelo Eixo 3 e ainda não são padrão em nenhuma base pública. Onde a distinção importa, ela está dita na própria entrada.</p>
  <ul class="glo-indice">{_glossario_indice()}</ul>
</section>

<section class="wrap section" style="padding-top: clamp(24px, 3vw, 40px)">
  {_glossario_corpo()}
  <p class="body" style="margin: clamp(34px, 4vw, 50px) 0 0; max-width: 74ch">Atualizada em {ATUALIZADO}. Sigla de órgão e denominação de entidade seguem a forma usada pela própria instituição. Onde um termo é proposta deste Eixo, e não padrão vigente, a entrada diz.</p>
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
        pagina("preservar.html", "Preservar evidências",
               "Como preservar prova de ato antissemita: os primeiros 60 minutos e o roteiro de cada tipo de ocorrencia.",
               "preservar.html", PRESERVAR),
        pagina("glossario.html", "Glossário",
               "Os termos usados nesta plataforma, com a distincao entre o que e padrao vigente e o que e proposta do Eixo 3.",
               "glossario.html", GLOSSARIO),
        pagina("contato.html", "Contato e errata",
               "Como apontar erro no que esta publicado. Este canal nao recebe denuncia: os canais que recebem estao na secao de denuncia.",
               "", CONTATO_PAG),
    ]
    print("paginas institucionais: " + ", ".join(feitos))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
