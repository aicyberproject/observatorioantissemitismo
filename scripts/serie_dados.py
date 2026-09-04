#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dados da serie editorial semanal: quem enfrentou o antissemitismo.

Cada perfil declara as fontes com o codigo HTTP obtido na verificacao, e o grau
de verificacao campo a campo. Onde a fonte primaria nao confirma um dado muito
citado, a divergencia fica registrada em vez de resolvida por escolha.

Regra editorial: nenhum perfil de pessoa viva cuja atuacao seja objeto de disputa
politica corrente no Brasil. O Observatorio declara nao emitir opiniao editorial
nem carregar posicao politico-partidaria, e a serie observa isso.
"""

# semana, id, nome, vida, nacionalidade, chamada, corpo, importa, divergencia, fontes, bloco
PERFIS = [
 dict(n=1, id="souza-dantas", nome="Luiz Martins de Souza Dantas",
   vida="1876–1954", nac="Brasileiro", bloco="Brasil",
   chamada="Embaixador do Brasil na França que concedeu vistos a judeus perseguidos, contra ordens expressas do Estado Novo.",
   corpo=[
     "Chefiou a representação brasileira na França durante a ocupação nazista. Em 1940 pediu e obteve autorização do chanceler brasileiro para emitir vistos de imigração a um número limitado de cidadãos franceses. Apesar da proibição brasileira de imigração de judeus, concedeu vistos diplomáticos a centenas de judeus que fugiam do regime de Vichy, cuidando de encobrir qualquer indício de judeidade nos documentos e antedatando as datas de emissão para antes da proibição.",
     "Em 1941 interveio para salvar o navio <em>Alsina</em>, retido quatro meses pelo bloqueio naval britânico e forçado a atracar em Casablanca: obteve a renovação dos vistos vencidos e os passageiros chegaram ao Rio de Janeiro. Chamado ao Brasil para processo disciplinar, escapou do julgamento por uma tecnicalidade, sua condição de aposentado no período em que falsificou os vistos.",
     "Reconhecido Justo entre as Nações em 10 de dezembro de 2003.",
   ],
   importa="Mostra que a política oficial de um Estado e a conduta de seus agentes podem divergir, e que o registro documental permite estabelecer qual foi qual. É o caso brasileiro em que a desobediência administrativa está mais bem documentada.",
   diverg="Yad Vashem registra apenas &ldquo;centenas&rdquo; de vistos. Cifras mais altas circulam atribuídas à pesquisa do historiador Fabio Koifman; essa obra não foi consultada e o número não está confirmado.",
   fontes=[("Yad Vashem, história de Souza Dantas","https://www.yadvashem.org/righteous/stories/dantas.html"),
           ("Museu do Holocausto de Curitiba, os Justos e o Brasil","https://museudoholocausto.org.br/memoria/o-holocausto/os-justos-entre-as-nacoes-e-o-brasil/")]),

 dict(n=2, id="aracy-carvalho", nome="Aracy de Carvalho Guimarães Rosa",
   vida="1908–2011", nac="Brasileira", bloco="Brasil",
   chamada="Funcionária do setor de vistos do consulado brasileiro em Hamburgo, chamada &ldquo;Anjo de Hamburgo&rdquo;.",
   corpo=[
     "Responsável pela seção de vistos do consulado do Brasil em Hamburgo, onde atuava como secretária em 1938. Ajudou judeus alemães a obter vistos para o Brasil e a superar dificuldades financeiras antes da partida, omitindo o &ldquo;J&rdquo; de identificação nos documentos.",
     "Durante o pogrom da Noite dos Cristais, em 9 e 10 de novembro de 1938, abrigou Margarethe Bertel-Levy e o marido em sua própria casa. Yad Vashem nomeia outras pessoas por ela assistidas: Albert Feis, Grethe Jacobsberg, Tuch e Kazenstein.",
     "Casou-se com o cônsul e escritor João Guimarães Rosa em 1940. Trabalharam juntos no consulado até a ruptura das relações entre Brasil e Alemanha, em meados de 1942. Günther Heilborn, um dos resgatados, deu à filha nascida no Brasil o nome Aracy. Morreu em São Paulo em março de 2011, aos 102 anos. Na exposição &ldquo;Vistos para a Vida&rdquo;, sobre diplomatas que salvaram judeus, é a única mulher.",
   ],
   importa="Deslocada a atenção do chefe de posto para o quadro funcional, aparece o servidor de carreira como ponto onde a decisão efetivamente se dá. É o registro de que a margem de ação existe fora do topo da hierarquia.",
   diverg="Yad Vashem data o reconhecimento em 3 de junho de 1982. Fontes brasileiras de ampla circulação informam 8 de julho de 1982. As duas datas não foram conciliadas: prevalece aqui a da instituição que concede o título. Yad Vashem não fornece número de pessoas assistidas.",
   fontes=[("Yad Vashem, história de Aracy de Carvalho","https://www.yadvashem.org/righteous/stories/carvalho.html"),
           ("Museu do Holocausto de Curitiba, os Justos e o Brasil","https://museudoholocausto.org.br/memoria/o-holocausto/os-justos-entre-as-nacoes-e-o-brasil/")]),

 dict(n=3, id="hc-82424", nome="A decisão que fez do antissemitismo racismo",
   vida="Julgado em 2003", nac="Supremo Tribunal Federal", bloco="Brasil",
   chamada="HC 82.424/RS, o Caso Ellwanger. A tese fundante do enquadramento jurídico do antissemitismo no Brasil, e ela não veio do relator.",
   corpo=[
     "Na sessão de 12 de dezembro de 2002, o relator, ministro Moreira Alves, votou por conceder o habeas corpus ao editor Siegfried Ellwanger: entendeu que judeus não podem ser considerados uma raça e que, logo, a condenação não configurava racismo, estando prescrita.",
     "O ministro Maurício Corrêa abriu divergência. Questionou a interpretação semântica restrita do art. 5º, XLII, da Constituição, por considerar que o conceito de racismo é mais amplo que a definição de tipos raciais, e pediu vista.",
     "O julgamento foi concluído em 17 de setembro de 2003. Por sete votos a três, o Plenário negou o habeas corpus e manteve a condenação imposta pelo Tribunal de Justiça do Rio Grande do Sul. Vencidos os ministros Moreira Alves, Marco Aurélio e Carlos Ayres Britto, os dois primeiros por prescrição e Ayres Britto por falta de provas. Prevaleceu a tese de que a prática de racismo abrange a discriminação contra judeus e é, portanto, imprescritível.",
     "Maurício José Corrêa nasceu em São João do Manhuaçu, em Minas Gerais, em 9 de maio de 1934. Foi senador pelo Distrito Federal, atuou na Assembleia Nacional Constituinte, foi Ministro da Justiça entre 1992 e 1994, tomou posse no Supremo em 15 de dezembro de 1994 e presidiu o Tribunal entre junho de 2003 e maio de 2004. Morreu em Brasília em 17 de fevereiro de 2012.",
   ],
   importa="É a decisão que dá base jurídica interna para tratar o antissemitismo como racismo, e não como mera ofensa. Fixa também que a definição do bem jurídico protegido não se resolve por biologia, mas por função da norma. Esta série o registra como decisão, com os ministros nomeados como autores factuais de votos.",
   diverg="A atuação do ministro Celso de Mello neste caso não foi verificada. As duas rotas para os votos individuais falharam: o inteiro teor do acórdão e a página do processo no portal do STF não abriram. Estão confirmados o placar e a identidade dos três vencidos; os votos concorrentes que compõem a maioria não foram recuperados. A lacuna fica registrada em vez de se atribuir autoria não conferida.",
   fontes=[("STF, notícia do julgamento concluído","https://noticias.stf.jus.br/postsnoticias/stf-nega-habeas-corpus-a-editor-de-livros-condenado-por-racismo-contra-judeus/"),
           ("STF, notícia da sessão de 2002","https://noticias.stf.jus.br/postsnoticias/stf-julga-habeas-corpus-de-editor-acusado-de-divulgar-ideias-anti-semitas/"),
           ("Agência Senado, morte de Maurício Corrêa","https://www12.senado.leg.br/noticias/materias/2012/02/17/morre-o-ex-senador-e-ex-presidente-do-supremo-mauricio-correa")]),

 dict(n=4, id="alberto-dines", nome="Alberto Dines",
   vida="1932–2018", nac="Brasileiro", bloco="Brasil",
   chamada="Jornalista e crítico de mídia que documentou a perseguição a judeus no mundo luso-brasileiro.",
   corpo=[
     "Natural do Rio de Janeiro, começou em 1952 como crítico de cinema. Foi por doze anos editor-chefe do <em>Jornal do Brasil</em>. Preso uma vez em 1968, sob a ditadura militar. Em setembro de 1973, contra ordem do regime de não noticiar a morte de Salvador Allende, publicou na primeira página um longo texto sem manchete; foi demitido três meses depois.",
     "Em 1975 criou na <em>Folha de S.Paulo</em> a coluna <em>Jornal dos jornais</em>, precursora da função de ombudsman no país. Em 1980 mudou-se para Lisboa e escreveu <em>Morte no Paraíso: a tragédia de Stefan Zweig</em>, de 1981, sobre o escritor que veio ao Brasil no início dos anos 1940 fugindo do nazismo.",
     "Viveu em Portugal entre 1988 e 1995, pesquisando na Torre do Tombo, e publicou <em>Vínculos do fogo: Antônio José da Silva, o Judeu, e outras histórias da Inquisição em Portugal e no Brasil</em>, de 1992, sobre o dramaturgo brasileiro executado pela Inquisição portuguesa em 1739 e sobre a experiência de sua família como cristãos-novos.",
     "Fundou o Observatório da Imprensa em 1996, um dos primeiros veículos jornalísticos exclusivamente em internet no Brasil. Morreu em 22 de maio de 2018, aos 86 anos.",
   ],
   importa="Junta duas competências que um observatório precisa: a crítica sistemática de mídia e a documentação histórica da perseguição antijudaica. O modelo do Observatório da Imprensa é o antecedente nacional mais próximo de monitoramento público de discurso.",
   diverg="Não foi localizada documentação de atuação militante de Dines contra o antissemitismo como causa organizada. O vínculo verificável é de obra: a biografia de Zweig e o estudo da Inquisição. A relevância é historiográfica e de crítica de mídia, e a série não a infla em ativismo.",
   fontes=[("Revista Pesquisa FAPESP, trajetória de Alberto Dines","https://revistapesquisa.fapesp.br/a-trajetoria-abrangente-e-a-influencia-de-alberto-dines/")]),
]
