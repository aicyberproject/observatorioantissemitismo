#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera acervo.html: catalogo de acervos, memoriais e material de referencia.

Cada item traz endereco conferido por requisicao em 04/09/2026. O Observatorio
remete, nao republica: nenhum conteudo de terceiro e reproduzido aqui.

Regra de curadoria que a pagina declara: codigo HTTP 200 nao e garantia de
conteudo. Quatro itens examinados respondiam 200 e nao serviam o que o titulo
prometia. Ficam registrados como ressalva, e nao como remissao.
"""
import html
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from gerar_paginas import pagina, ATUALIZADO  # noqa: E402

E = lambda s: html.escape(str(s or ""), quote=True)

# nome, url, oferta, idioma, nota
BRASIL = [
 ("Museu do Holocausto de Curitiba &mdash; materiais educativos",
  "https://museudoholocausto.org.br/educacao/materiais-educativos/",
  "Quatorze cadernos em PDF, de download direto", "Português, acesso livre",
  "Entre eles <em>Arte Degenerada</em>, <em>Nossa Luta: a perseguição aos negros durante o Holocausto</em>, "
  "<em>Tudo está em chamas: os 80 anos da Noite dos Cristais</em> e <em>Jan Karski e os Justos Entre as Nações</em>.", True),
 ("Museu do Holocausto &mdash; exposição &ldquo;O Caminho para o Holocausto&rdquo;",
  "https://museudoholocausto.org.br/memoria/exposicoes/o-caminho-para-o-holocausto/",
  "Exposição virtual em seis módulos", "Português, acesso livre",
  "Tem módulo próprio sobre o Brasil diante da ascensão do nazismo, entre resistência e normalização. "
  "O próprio texto declara que não é exposição sobre o Holocausto, mas sobre suas condições de possibilidade.", True),
 ("Museu do Holocausto &mdash; os Justos entre as Nações e o Brasil",
  "https://museudoholocausto.org.br/memoria/o-holocausto/os-justos-entre-as-nacoes-e-o-brasil/",
  "Texto de referência", "Português, acesso livre",
  "Sobre os dois brasileiros reconhecidos por Yad Vashem: Aracy de Carvalho Guimarães Rosa e "
  "Luiz Martins de Souza Dantas. É a contraface da política de vistos do Estado Novo.", True),
 ("Museu do Holocausto &mdash; depoimentos de sobreviventes",
  "https://museudoholocausto.org.br/memoria/o-holocausto/depoimentos/",
  "Testemunhos audiovisuais", "Português, acesso livre",
  "Amostra da USC Shoah Foundation, com uso educativo autorizado ao Museu. A coleta brasileira, "
  "coordenada por Anita Pinkuss, produziu mais de 800 entrevistas. É a alternativa realista ao "
  "Visual History Archive, cujo acesso é institucional.", True),
 ("Travessias &mdash; Arqshoah, Arquivo Virtual do Holocausto e do Antissemitismo",
  "https://travessias.arqshoah.com/",
  "Arquivos, hemeroteca, iconografia, testemunhos e seção de Justos e Salvadores",
  "Português, acesso parcialmente livre",
  "Curadoria universitária, ligada ao LEER da USP. Único arquivo virtual brasileiro dedicado ao Holocausto "
  "<strong>e ao antissemitismo</strong>, com postura antinegacionista declarada. Documentos pessoais exigem "
  "termo de autorização assinado pelo entrevistado.", True),
 ("Museu Judaico de São Paulo &mdash; área do pesquisador",
  "https://museujudaicosp.org.br/area-do-pesquisador/",
  "Acervo arquivístico, museológico e bibliográfico, com catálogo em linha",
  "Português e inglês, acesso livre",
  "Mais de 500 coleções e fundos, mais de 500 depoimentos de história oral, cerca de 2.500 itens "
  "museológicos e mais de 11 mil volumes. <strong>É o destino de quem procura o Arquivo Histórico Judaico "
  "Brasileiro:</strong> o acervo do AHJB foi incorporado a este museu, e o domínio antigo não resolve mais.", True),
 ("Museu Judaico do Rio de Janeiro &mdash; documentos históricos",
  "https://museujudaico.org.br/documentos-historicos/",
  "Fonte primária digitalizada e fundos de consulta presencial",
  "Português e inglês, acesso livre à página",
  "Nove cartas de Alfred Dreyfus em visualização integral, traduzidas. Mantém o Fundo Werner Nehab, "
  "com documentação sobre nazismo, fascismo, antissemitismo e integralismo no Brasil, de interesse "
  "direto para um observatório.", True),
 ("Instituto Cultural Judaico Marc Chagall",
  "https://chagall.org.br/acervo/",
  "Sete núcleos: documental, iconográfico, história oral, audiovisual, biblioteca, periódicos e acervo digital",
  "Português e inglês, acesso livre",
  "Foco na história judaica no Rio Grande do Sul e no Brasil.", True),
 ("Centro de Estudos Judaicos da USP",
  "https://cej.fflch.usp.br/",
  "Acervo, publicações, periódicos e congresso", "Português, acesso livre",
  "Vinculado ao Departamento de Letras Orientais da FFLCH.", True),
 ("Hemeroteca Digital Brasileira &mdash; Biblioteca Nacional",
  "https://memoria.bn.gov.br/hdb/periodico.aspx",
  "Coleção digital de jornais e revistas", "Português, acesso livre, sem cadastro",
  "Instrumento indispensável para pesquisar imprensa e imigração judaica no Brasil, inclusive no Estado Novo. "
  "<strong>Ressalva técnica:</strong> o servidor apresenta cadeia de certificação incompleta. Navegadores "
  "costumam abrir; clientes rigorosos recusam a conexão.", True),
 ("Arquivo Nacional &mdash; bases de dados e instrumentos de pesquisa",
  "https://www.gov.br/arquivonacional/pt-br/servicos/atendimento/bases-de-dados-e-instrumentos-de-pesquisa",
  "Ponto de entrada para o catálogo arquivístico", "Português, acesso livre",
  "O sistema de consulta exige atravessar verificação antibot, que impede conferência automatizada. "
  "Em navegador, o acesso é normal.", True),
]

INTERNACIONAL = [
 ("Enciclopédia do Holocausto &mdash; United States Holocaust Memorial Museum",
  "https://encyclopedia.ushmm.org/pt-br",
  "Enciclopédia integral, linha cronológica, banco de imagens e carteiras de identidade de vítimas",
  "Português do Brasil, acesso livre, sem cadastro",
  "É o material didático mais completo em português de todo este catálogo, e a porta de entrada natural "
  "para leitor não especializado.", True),
 ("Yad Vashem &mdash; Escola Internacional, seção em português",
  "https://www.yadvashem.org/education/other-languages/portuguese.html",
  "Lições educacionais, filmes de testemunho com plano de aula e artigos",
  "Português, acesso livre",
  "O caminho intuitivo não funciona: <code>yadvashem.org/pt</code> devolve 404. O conteúdo em português "
  "existe apenas sob este endereço.", True),
 ("Yad Vashem &mdash; base dos Justos entre as Nações",
  "https://collections.yadvashem.org/en/righteous",
  "Base nominal pesquisável", "Inglês, acesso livre, sem cadastro",
  "Permite chegar ao registro primário de cada reconhecimento. O endereço antigo "
  "<code>righteous.yadvashem.org</code> hoje redireciona para cá.", True),
 ("Yad Vashem &mdash; Base Central de Nomes das Vítimas da Shoá",
  "https://collections.yadvashem.org/en/names",
  "Base nominal de vítimas", "Inglês, acesso livre", "", True),
 ("USHMM &mdash; coleções",
  "https://collections.ushmm.org/search/",
  "Catálogo unificado de documentos, fotografias, objetos, testemunhos orais e filmes",
  "Inglês, busca de acesso livre", "", True),
 ("USC Shoah Foundation &mdash; Visual History Archive",
  "https://sfi.usc.edu/what-we-do/collections",
  "60.394 testemunhos em vídeo, em 45 idiomas e 69 países",
  "Inglês; exige cadastro ou vínculo institucional",
  "Os 204 pontos de acesso no mundo indicam modelo de assinatura institucional, e não acesso livre. "
  "Há mais de 800 entrevistas coletadas no Brasil, com amostra disponível pelo Museu do Holocausto de Curitiba.", True),
 ("Mémorial de la Shoah",
  "https://www.memorialdelashoah.org/",
  "Museu e centro de documentação, com biblioteca, fototeca e centro de ensino",
  "Francês, sem versão em português", "Tem seção sobre outros genocídios do século XX.", True),
 ("Anne Frank House",
  "https://www.annefrank.org/en/",
  "Material biográfico, o Anexo Secreto e seção educacional",
  "Inglês, neerlandês e alemão; <strong>sem versão em português</strong>",
  "Ao contrário do que se costuma supor, não há edição em português: os caminhos em "
  "<code>/pt</code> redirecionam ao inglês ou devolvem 404.", True),
 ("Memorial e Museu Auschwitz-Birkenau",
  "https://www.auschwitz.org/en/",
  "Panorama fotográfico navegável, galeria e lições em linha",
  "Inglês e polonês; <strong>sem versão em português</strong>",
  "<code>auschwitz.org/pt</code> devolve 404.", True),
]

DIVULGACAO = [
 ("Canais institucionais dos acervos brasileiros",
  "https://www.youtube.com/@museudoholocausto",
  "Webinars, séries próprias, mesas de festival literário e vídeos de acervo",
  "Português, acesso livre",
  "Autoria institucional identificável. Além do Museu do Holocausto de Curitiba, mantêm canal o "
  "Museu Judaico de São Paulo, o Instituto Marc Chagall e o Arqshoah. É a divulgação em vídeo de "
  "melhor lastro disponível em português.", True),
 ("História FM",
  "https://leituraobrigahistoria.com/historia-fm/",
  "Podcast em formato de entrevista com historiadores acadêmicos",
  "Português, acesso livre",
  "Apresentado por historiador com formação na área. O episódio 124 trata da Alemanha nazista, das "
  "origens do nazismo ao fim da guerra. <strong>Produção privada:</strong> a curadoria vem da escolha de "
  "convidados, não de tutela de acervo. Indicado por episódio, não em bloco.", True),
 ("Na Trilha da História &mdash; EBC, Rádio Nacional",
  "https://radios.ebc.com.br/na-trilha-da-historia/2019/01/na-trilha-da-historia-conta-os-horrores-do-holocausto",
  "Programa de radiodifusão pública, com episódio dedicado ao Holocausto",
  "Português, acesso livre", "Autoria e responsabilidade editorial institucionais.", True),
]

REPROVADOS = [
 ("Superinteressante",
  "O acervo sobre o tema existe, mas o registro editorial predominante é de curiosidade e de gancho "
  "cinematográfico. Entre os títulos listados na própria página do tema: &ldquo;'Toy Story 3' é uma metáfora "
  "sobre o holocausto judeu?&rdquo;, &ldquo;E se Hitler tivesse vencido a 2ª Guerra Mundial?&rdquo; e "
  "&ldquo;Álbum da Alemanha nazista foi feito com pele de vítimas do Holocausto&rdquo;. Há peças defensáveis "
  "no mesmo acervo, sobre Nuremberg e a fundação do direito internacional, mas a mistura impede recomendar "
  "o veículo em bloco numa seção de referência."),
 ("Guia dos Curiosos",
  "A busca por &ldquo;holocausto&rdquo; devolve um único resultado, e ele é alheio ao tema. "
  "<strong>Não há material sobre Holocausto, antissemitismo ou história judaica a indicar.</strong> "
  "A exclusão não é juízo de gosto: é ausência de acervo."),
 ("History Channel Brasil",
  "O endereço brasileiro do canal não estabelece conexão, em HTTP e em HTTPS, embora o domínio resolva. "
  "Não há endereço estável a que remeter."),
 ("Casa Stefan Zweig",
  "O endereço responde, mas o sítio está degradado: a página inicial é servida em alemão, o seletor de "
  "idioma devolve 404, as páginas internas só existem como espelho estático sem corpo de conteúdo, e o "
  "material mais recente é de 2020. Não há acervo digital, exposição virtual nem material didático a "
  "indicar. Fica registrada como endereço institucional em Petrópolis, com a limitação declarada."),
]


def bloco(itens):
    saida = []
    for nome, url, oferta, idioma, nota, _ in itens:
        saida.append(
            f'<article class="acv-item"><div class="acv-id">'
            f'<h3 class="acv-nome">{nome}</h3>'
            f'<p class="acv-oferta">{oferta}</p></div>'
            f'<div><p class="acv-idioma">{idioma}</p>'
            + (f'<p class="body">{nota}</p>' if nota else "")
            + f'<p class="tl-src"><a href="{E(url)}" target="_blank" rel="noopener">Acessar &rarr;</a></p>'
            f'</div></article>')
    return f'<div class="acv-lista">{"".join(saida)}</div>'


CORPO = f"""<section class="wrap" id="topo" style="padding-top: clamp(44px, 6vw, 80px); padding-bottom: clamp(10px, 2vw, 20px)">
  <p class="crumb"><a href="index.html">Observat&oacute;rio</a> &nbsp;/&nbsp; Acervos</p>
  <h1 class="h1" style="margin-top: 24px">Acervos e mem&oacute;ria</h1>
  <p class="lead" style="margin: 26px 0 0; max-width: 70ch">Onde encontrar fonte prim&aacute;ria, testemunho, material did&aacute;tico e exposi&ccedil;&atilde;o sobre hist&oacute;ria judaica, Holocausto e antissemitismo. Come&ccedil;a pelo que existe no Brasil e em portugu&ecirc;s.</p>
  <p class="body" style="margin: 18px 0 0; max-width: 70ch">Cada endere&ccedil;o foi conferido por requisi&ccedil;&atilde;o em {ATUALIZADO}. O Observat&oacute;rio remete, n&atilde;o republica: nada do conte&uacute;do de terceiros &eacute; reproduzido aqui.</p>
</section>

<section class="band"><div class="wrap section">
  <p class="eyebrow">Regra de curadoria</p>
  <h2 class="h2" style="max-width: 34ch">Responder n&atilde;o &eacute; o mesmo que servir</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">Quatro dos endere&ccedil;os examinados respondiam normalmente e <strong>n&atilde;o serviam o que o t&iacute;tulo prometia</strong>: p&aacute;ginas marcadas &ldquo;em breve&rdquo;, telas de bloqueio no lugar do acervo, espelho est&aacute;tico sem corpo de conte&uacute;do. Nenhum deles entrou como remiss&atilde;o.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Tr&ecirc;s dom&iacute;nios respondem com recusa consistente a acesso automatizado, compat&iacute;vel com bloqueio a endere&ccedil;o de <em>datacenter</em> e n&atilde;o com aus&ecirc;ncia de p&aacute;gina. Em navegador comum devem abrir, e por isso constam com a ressalva.</p>
  <p class="body" style="margin: 14px 0 0; max-width: 74ch">Publicamos sempre o endere&ccedil;o final da cadeia de redirecionamentos. Endere&ccedil;o antigo cria depend&ecirc;ncia de um redirecionamento que pode ser desligado, e foi assim que boa parte do acervo hist&oacute;rico de outra institui&ccedil;&atilde;o examinada acabou inalcan&ccedil;&aacute;vel.</p>
</div></section>

<section class="wrap section">
  <p class="eyebrow">Brasil</p>
  <h2 class="h2" style="max-width: 30ch">Acervos brasileiros</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">A prioridade &eacute; o que existe no pa&iacute;s e em portugu&ecirc;s. Um caso merece registro: o <strong>Arquivo Hist&oacute;rico Judaico Brasileiro</strong> n&atilde;o existe mais como s&iacute;tio aut&ocirc;nomo, e seu dom&iacute;nio n&atilde;o resolve. O acervo foi incorporado ao Museu Judaico de S&atilde;o Paulo, que &eacute; o destino correto de quem o procura.</p>
  {bloco(BRASIL)}
</section>

<section class="band"><div class="wrap section">
  <p class="eyebrow">Internacional</p>
  <h2 class="h2" style="max-width: 30ch">Institui&ccedil;&otilde;es de refer&ecirc;ncia</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Duas suposi&ccedil;&otilde;es correntes n&atilde;o se confirmaram na verifica&ccedil;&atilde;o: nem a Anne Frank House nem o memorial de Auschwitz-Birkenau mant&ecirc;m vers&atilde;o em portugu&ecirc;s. Yad Vashem mant&eacute;m, mas n&atilde;o no caminho que se esperaria.</p>
  {bloco(INTERNACIONAL)}
</div></section>

<section class="wrap section">
  <p class="eyebrow">Divulga&ccedil;&atilde;o</p>
  <h2 class="h2" style="max-width: 30ch">Material de divulga&ccedil;&atilde;o em portugu&ecirc;s</h2>
  <p class="body" style="margin: 18px 0 0; max-width: 74ch">Esta se&ccedil;&atilde;o &eacute; curta por decis&atilde;o, e n&atilde;o por falta de busca. Divulga&ccedil;&atilde;o popular sobre Holocausto carrega risco de imprecis&atilde;o e de sensacionalismo, e a curadoria institucional foi preferida.</p>
  {bloco(DIVULGACAO)}
</section>

<section class="band"><div class="wrap section">
  <p class="eyebrow">Transpar&ecirc;ncia de curadoria</p>
  <h2 class="h2" style="max-width: 32ch">O que foi examinado e n&atilde;o recomendado</h2>
  <p class="body" style="margin: 20px 0 0; max-width: 74ch">Registrar o que n&atilde;o entrou &eacute; parte da fun&ccedil;&atilde;o. Quatro ve&iacute;culos e institui&ccedil;&otilde;es foram examinados e ficaram fora, com o motivo declarado.</p>
  <div class="repr-lista">{''.join(
    f'<div class="repr-item"><h3 class="repr-nome">{n}</h3><p class="body">{m}</p></div>'
    for n, m in REPROVADOS)}</div>
  <p class="fonte" style="margin-top: 24px">A aus&ecirc;ncia de recomenda&ccedil;&atilde;o n&atilde;o &eacute; ju&iacute;zo sobre o ve&iacute;culo em geral. &Eacute; avalia&ccedil;&atilde;o do material dispon&iacute;vel <strong>sobre este tema</strong>, para uso em se&ccedil;&atilde;o de refer&ecirc;ncia de &oacute;rg&atilde;o p&uacute;blico. Corre&ccedil;&otilde;es s&atilde;o bem-vindas pelo canal registrado em <a href="sobre.html">Sobre</a>.</p>
</div></section>
"""


def main():
    arq = pagina("acervo.html", "Acervos e mem&oacute;ria",
                 "Onde encontrar fonte primaria, testemunho e material didatico sobre historia judaica, "
                 "Holocausto e antissemitismo. Prioridade ao que existe no Brasil e em portugues.",
                 "acervo.html", CORPO)
    print("acervo:", arq)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
