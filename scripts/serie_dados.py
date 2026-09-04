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

PERFIS += [
 dict(n=5, id="sousa-mendes", nome="Aristides de Sousa Mendes",
   vida="morreu em 1954", nac="Português", bloco="Justos entre as Nações",
   chamada="Cônsul em Bordeaux que emitiu vistos em massa contra ordem expressa de Lisboa, e pagou por isso.",
   corpo=[
     "Diante da crise de refugiados após a ocupação da França, Portugal restringiu a entrada e, com a invasão da Bélgica e dos Países Baixos, proibiu novas travessias, sobretudo de judeus. Sousa Mendes decidiu desobedecer. Recebeu uma delegação de refugiados chefiada pelo rabino Haim Krieger e prometeu vistos de trânsito a todos os necessitados, gratuitos a quem não pudesse pagar a taxa.",
     "Montou escritório improvisado no consulado e trabalhou três dias e três noites, auxiliado por dois filhos. Entre 15 e 22 de junho de 1940 emitiu 1.575 vistos. Chamado de volta e escoltado, ao passar pelo consulado de Bayonne viu centenas de pessoas à porta, entrou e, apesar das objeções do cônsul local, ordenou a emissão imediata de vistos a todos.",
     "Em Lisboa foi submetido a conselho disciplinar e demitido do Ministério, ficando sem meios para sustentar treze filhos. Disse ao rabino Krieger: &ldquo;Se milhares de judeus sofrem por causa de um cristão, seguramente um cristão pode sofrer por tantos judeus.&rdquo; Morreu na indigência em 1954. A exoneração total só veio em 1988. Reconhecido Justo entre as Nações em 18 de outubro de 1966.",
   ],
   importa="É o caso em que a punição do funcionário está tão documentada quanto o ato de resgate, o que permite discutir o custo institucional da desobediência. Os 34 anos até a reabilitação medem a lentidão do reconhecimento estatal.",
   diverg="Yad Vashem informa 1.575 vistos, que é número de documentos e não de pessoas. Cifras muito superiores, na casa de dezenas de milhares de pessoas salvas, circulam em fontes secundárias e não constam da fonte primária. O ano de nascimento não foi confirmado.",
   fontes=[("Yad Vashem, história de Sousa Mendes","https://www.yadvashem.org/righteous/stories/mendes.html")]),

 dict(n=6, id="chiune-sugihara", nome="Chiune Sempo Sugihara",
   vida="anos de vida não confirmados", nac="Japonês", bloco="Justos entre as Nações",
   chamada="Cônsul do Japão em Kovno que emitiu vistos de trânsito depois de três negativas de Tóquio.",
   corpo=[
     "Enviado em novembro de 1939 a Kovno, então capital da Lituânia, com a atribuição de monitorar movimentos do Exército alemão. Cerca de 15 mil judeus poloneses tinham chegado à Lituânia ainda independente. Com a anexação à União Soviética, os diplomatas estrangeiros foram instados a deixar a cidade até o fim de agosto de 1940.",
     "Enquanto arrumava suas coisas, foi informado de que uma delegação judaica o aguardava, chefiada por Zerach Warhaftig, futuro ministro de Israel. Os refugiados haviam descoberto que Curaçao, colônia holandesa, não exigia visto de entrada; precisavam de vistos de trânsito japoneses para cruzar a União Soviética. Sugihara pediu autorização a Tóquio e, sem esperar, começou a emitir por iniciativa própria. Nove dias depois o ministério recusou e reiterou as condições. Ele continuou emitindo.",
     "Sua mulher, Yukiko, descreveu as filas de 200 a 300 pessoas de manhã à noite e o risco concreto de o marido perder o emprego. Removido para Königsberg e depois Bucareste, foi demitido do serviço diplomático japonês em 1946, o que entendeu como consequência da insubordinação. Reconhecido Justo entre as Nações em 4 de outubro de 1984.",
   ],
   importa="Documenta uma recusa reiterada por escrito e desobedecida três vezes, o que torna o caso raro em rastreabilidade: existe a ordem, existe a data, existe o descumprimento.",
   diverg="A página de Yad Vashem não informa número de vistos nem de pessoas. As cifras correntes, em torno de 2.139 vistos ou cerca de seis mil pessoas, não aparecem nessa fonte. A ausência é o registro.",
   fontes=[("Yad Vashem, história de Sugihara","https://www.yadvashem.org/righteous/stories/sugihara.html")]),

 dict(n=7, id="raoul-wallenberg", nome="Raoul Wallenberg",
   vida="1912 – provavelmente 1947", nac="Sueco", bloco="Justos entre as Nações",
   chamada="Diplomata que montou em Budapeste a maior operação de proteção documental do período, e desapareceu na custódia soviética.",
   corpo=[
     "De família aristocrática de banqueiros, estudou arquitetura nos Estados Unidos. Após a ocupação da Hungria em 19 de março de 1944, a legação sueca pediu um enviado especial para tratar de passaportes. Wallenberg foi nomeado secretário com privilégios diplomáticos plenos e chegou a Budapeste em 9 de julho de 1944 com uma lista de nomes e 650 passaportes protetores.",
     "Ampliou a operação: passou a emitir milhares de cartas de proteção e a comprar casas que colocava sob bandeira sueca, tornando-as extraterritoriais. Em outubro de 1944 a Cruz Flechada tomou o poder e instaurou o terror. Wallenberg recorreu a suborno e chantagem para financiar a operação, empregou cerca de 340 pessoas e manteve 32 prédios sob proteção sueca, com dois hospitais e uma cozinha comunitária. Com outras legações, montou o gueto internacional protegido pelos países neutros.",
     "Desapareceu na custódia soviética. Em 1956 os soviéticos declararam que morrera na prisão em 1947. Em 1989 seu passaporte diplomático e objetos pessoais foram encontrados no porão da sede da KGB em Moscou. O grupo de trabalho russo-sueco confirmou em 2000 que &ldquo;provavelmente&rdquo; morreu na prisão em 1947, sem conclusão definitiva. Reconhecido Justo entre as Nações em 26 de novembro de 1963. A mãe pediu que não se recebessem as honras em seu nome, acreditando que o filho voltaria; a árvore só foi plantada após a morte dela, em 1979.",
   ],
   importa="Documento de proteção como instrumento de sobrevivência, e o limite disso: a operação funcionou e o operador desapareceu. A recusa da mãe às honras é o registro de uma pendência que nunca se fechou.",
   diverg="Divergência dentro da mesma fonte. O corpo do texto de Yad Vashem afirma que cerca de 4.500 judeus tinham esses papéis. Na mesma página, a homenagem do congressista Tom Lantos, ele próprio salvo por Wallenberg, fala em dezenas de milhares. Duas ordens de grandeza no mesmo documento, registradas sem escolha entre elas.",
   fontes=[("Yad Vashem, história de Wallenberg","https://www.yadvashem.org/righteous/stories/wallenberg.html")]),

 dict(n=8, id="irena-sendler", nome="Irena Sendler",
   vida="morreu em 12 de maio de 2008", nac="Polonesa", bloco="Justos entre as Nações",
   chamada="Assistente social que dirigiu, com departamento e codinome, o resgate de crianças do gueto de Varsóvia.",
   corpo=[
     "Ao início da guerra era assistente social de 29 anos do Departamento de Bem-Estar da prefeitura de Varsóvia. Usou o cargo para ajudar judeus, o que se tornou quase impossível com o fechamento do gueto em novembro de 1940, onde cerca de 400 mil pessoas foram confinadas. Obteve da prefeitura autorização para entrar sob pretexto de inspecionar condições sanitárias.",
     "Lá dentro, fez contato com ativistas da organização judaica de bem-estar, ajudou a contrabandear pessoas para o lado ariano e a montar esconderijos. Tornou-se uma das principais ativistas do Żegota, o Conselho de Auxílio aos Judeus, criado no outono de 1942. Em setembro de 1943, quatro meses após a destruição completa do gueto, foi nomeada diretora do Departamento de Cuidado das Crianças Judias do Żegota. Sob o codinome Jolanta, usou contatos com orfanatos e instituições religiosas.",
     "Presa em 20 de outubro de 1943, conseguiu esconder as provas comprometedoras, entre elas os endereços codificados das crianças. Condenada à morte e enviada à prisão de Pawiak, foi libertada mediante suborno pela resistência em fevereiro de 1944. Continuou na clandestinidade, o que a impediu de ir ao enterro da mãe. Reconhecida Justa entre as Nações em 19 de outubro de 1965; a árvore em sua honra está na entrada da Avenida dos Justos.",
   ],
   importa="Mostra o resgate como operação organizada, com departamento, codinome e cadeia de custódia de informação, não como gesto isolado. O cuidado com os registros é o que permitiu depois devolver identidades.",
   diverg="A lacuna é declarada pela própria fonte. Yad Vashem afirma textualmente que o número exato de crianças salvas por Sendler e seus parceiros é desconhecido. A cifra de 2.500 crianças, de circulação corrente, não é endossada pela fonte primária. O ano de nascimento não foi confirmado.",
   fontes=[("Yad Vashem, história de Irena Sendler","https://www.yadvashem.org/righteous/stories/sendler.html")]),

 dict(n=9, id="verificacao-winton", nome="O limite da verificação: o caso Nicholas Winton",
   vida="Edição metodológica", nac="Sobre o método desta série", bloco="Método",
   chamada="Um fato de altíssima circulação que não se confirma na instituição que o concederia. Esta edição publica a lacuna, não o perfil.",
   corpo=[
     "Nicholas Winton organizou o transporte de crianças da Tchecoslováquia para o Reino Unido em 1939. É frequentemente descrito como Justo entre as Nações. <strong>Esta série não confirmou esse enquadramento.</strong>",
     "A evidência disponível é negativa. A nota de falecimento publicada por Yad Vashem em 2 de julho de 2015 o elogia sem lhe atribuir o título. O presidente do Conselho, Avner Shalev, afirma que Winton &ldquo;agiu incansavelmente, com coragem e integridade para salvar crianças e por isso merece nossa admiração&rdquo;, e relata tê-lo encontrado num evento com as crianças israelenses que resgatou. Em nenhum ponto o texto o chama de Justo entre as Nações.",
     "Entre fontes secundárias há divergência aberta: parte afirma que ele foi declarado Justo, parte afirma que Israel nunca o reconheceu como tal, com a explicação de que nasceu de pais judeus convertidos e batizados, e o título se destina a não judeus. A base consultável de Justos entre as Nações não foi consultada nesta rodada, e sem isso não há como afirmar nem negar.",
     "O que Winton fez não está em disputa. O que está em disputa é o título, e um observatório não deve atribuir reconhecimento institucional que não conseguiu verificar.",
   ],
   importa="Esta edição existe para tornar público o critério da série. Fato muito repetido não é fato verificado, e a diferença entre os dois é o trabalho. Publicar a lacuna é mais útil que preencher com o que circula.",
   diverg="Para fechar a questão, o passo é uma consulta direta à base de Justos entre as Nações, com registro do resultado. Enquanto isso não for feito, o enquadramento permanece não verificado.",
   fontes=[("Yad Vashem, nota de falecimento de 2 de julho de 2015","https://www.yadvashem.org/press-release/02-july-2015-15-13.html"),
           ("Base dos Justos entre as Nações, para consulta","https://collections.yadvashem.org/en/righteous")]),
]

PERFIS += [
 dict(n=10, id="primo-levi", nome="Primo Levi",
   vida="nasceu em 31 de julho de 1919", nac="Italiano", bloco="Sobreviventes e educadores",
   chamada="Químico e escritor. O relato de referência sobre Auschwitz, escrito por quem descreve o mecanismo e não apenas o sofrimento.",
   corpo=[
     "Nasceu em Turim, na mesma casa em que viveu toda a vida, de família de judeus piemonteses vindos da Espanha e da Provença. Matriculou-se em química na Universidade de Turim em 1937. Em 1938 registrou o efeito das leis raciais: &ldquo;a libertação da universidade coincidiu com o trauma de ouvir: cuidado, você não é como os outros, você vale menos que eles.&rdquo;",
     "Formou-se com louvor em 1941. <strong>O diploma traz a anotação &ldquo;de raça judaica&rdquo;.</strong> Aderiu ao clandestino Partito d'Azione e, após o armistício de setembro de 1943 e a ocupação alemã do norte e centro da Itália, entrou numa banda partigiana no Valle d'Aosta. Foi preso perto de Brusson e deportado para Monowitz, o Auschwitz III.",
     "Em 1945 passou meses num campo de trânsito soviético em Katowice, onde trabalhou como enfermeiro; a viagem de volta começou em junho e se arrastou até outubro. Publicou <em>Se questo è un uomo</em> em 1947, e disse tê-lo escrito &ldquo;sem nunca hesitar&rdquo;; a edição ampliada saiu em 1958. Sobre Auschwitz: &ldquo;Há Auschwitz, portanto não pode haver Deus. Não encontro solução para esse dilema. Eu a procuro, mas não a encontro.&rdquo;",
   ],
   importa="Fixa o padrão de testemunho que descreve o mecanismo, o que o torna utilizável como fonte e não só como memória. A anotação &ldquo;de raça judaica&rdquo; no diploma é a prova documental de que a classificação administrativa precede a perseguição, e é o argumento mais direto a favor de cuidar do que se registra na entrada de qualquer sistema.",
   diverg="O ano de morte não foi confirmado na fonte consultada.",
   fontes=[("Centro Internazionale di Studi Primo Levi, biografia","https://www.primolevi.it/en/biography")]),

 dict(n=11, id="elie-wiesel", nome="Elie Wiesel",
   vida="30 de setembro de 1928 – 2 de julho de 2016", nac="Romeno naturalizado norte-americano", bloco="Sobreviventes e educadores",
   chamada="Sobrevivente de Auschwitz e Buchenwald, Nobel da Paz de 1986, que nomeou a indiferença como o problema.",
   corpo=[
     "Nasceu em Sighet, na Romênia. Após a ocupação alemã da Hungria em 1944, a família foi deportada para Auschwitz. Na chegada, a mãe e a irmã mais nova foram assassinadas em câmara de gás. Wiesel e o pai foram selecionados para trabalho forçado pesado e submetidos deliberadamente a fome, frio e maus-tratos.",
     "No início de 1945 os dois foram forçados a uma marcha da morte até Buchenwald, onde o pai contraiu disenteria e morreu pouco depois da chegada, em 29 de janeiro. Nos meses seguintes os guardas matavam milhares de prisioneiros por dia. Aos dezessete anos, Wiesel ainda estava vivo quando os soldados aliados libertaram o campo em 11 de abril de 1945.",
     "Recebeu o Nobel da Paz de 1986, com a motivação de ser &ldquo;um mensageiro para a humanidade&rdquo;. Fez do testemunho a obra de sua vida. Considerava igualmente importante combater a indiferença e a atitude do &ldquo;não é problema meu&rdquo;: &ldquo;O oposto do amor não é o ódio, mas a indiferença.&rdquo;",
   ],
   importa="A frase sobre a indiferença é operacional para um observatório: define a omissão como objeto de monitoramento, e não apenas o ato hostil. Nomeia o público que assiste como parte do problema.",
   diverg="",
   fontes=[("Comitê Nobel, fatos do Nobel da Paz de 1986","https://www.nobelprize.org/prizes/peace/1986/wiesel/facts/")]),

 dict(n=12, id="viktor-frankl", nome="Viktor Emil Frankl",
   vida="26 de março de 1905 – 2 de setembro de 1997", nac="Austríaco", bloco="Sobreviventes e educadores",
   chamada="Neurologista que organizou atendimento psicológico dentro do campo e reconstruiu seu manuscrito com tifo.",
   corpo=[
     "Nasceu em Viena. Aos quinze anos fez sua primeira conferência pública, <em>Sobre o sentido da vida</em>. Em 1926 já usava o termo logoterapia. Entre 1928 e 1938 organizou centros de orientação para jovens em Viena.",
     "Em setembro de 1942 foi preso com a mulher, Tilly, e deportado junto com os pais para o gueto de Theresienstadt; após meio ano, o pai morreu de exaustão. Em Terezín, Frankl <strong>organizou uma equipe de primeiro atendimento psicológico</strong> para os recém-chegados em estado de choque e, no esforço de conter o risco de suicídio, teve como parceira a companheira de internamento Regina Jonas, a primeira mulher rabina do mundo.",
     "Em 1944 foi transportado para Auschwitz-Birkenau; a mãe foi assassinada de imediato na câmara de gás e Tilly transferida para Bergen-Belsen. Levado a Kaufering e depois Türkheim, subcampos de Dachau, contraiu tifo em 1945 e, para evitar colapso vascular fatal durante as noites, mantinha-se acordado reconstruindo o manuscrito de seu livro em tiras de papel furtadas do escritório do campo. O campo foi libertado em 27 de abril de 1945. Em poucos dias soube da morte da mulher, da mãe e do irmão.",
     "Em 1946 tornou-se diretor da Policlínica Neurológica de Viena, cargo que ocupou por 25 anos. A reconstrução de <em>Ärztliche Seelsorge</em>, com um capítulo novo sobre a psicologia do campo de concentração, foi um dos primeiríssimos livros publicados na Viena do pós-guerra. No mesmo ano, em nove dias, ditou o livro depois publicado como <em>Man's Search For Meaning</em>.",
   ],
   importa="Documenta assistência psicológica organizada dentro do campo, o que desloca o sobrevivente do papel de objeto para o de agente. A reconstrução do manuscrito sob tifo é o registro material da recusa em deixar o conhecimento morrer com o autor.",
   diverg="",
   fontes=[("Viktor Frankl Institut, biografia","https://www.viktorfrankl.org/biography.html")]),

 dict(n=13, id="simone-veil", nome="Simone Veil",
   vida="nasceu em 13 de julho de 1927", nac="Francesa", bloco="Sobreviventes e educadores",
   chamada="Sobrevivente de Auschwitz-Birkenau, magistrada e primeira presidente do Parlamento Europeu eleito por sufrágio direto.",
   corpo=[
     "Nasceu Simone Jacob em Nice, a mais nova de quatro filhos de uma família judia laica. Em março de 1944, aos dezesseis anos, foi presa pela Gestapo com a família e deportada para Auschwitz-Birkenau. O pai e o irmão foram deportados para a Lituânia e nunca voltaram; ela, a mãe e a irmã Madeleine foram enviadas ao campo. Sobreviveu ao trabalho forçado; a mãe morreu de tifo em Bergen-Belsen, antes da libertação.",
     "De volta à França, estudou direito na Universidade de Paris e seguiu carreira na magistratura, dedicando-se à reforma prisional e à situação dos detentos. <strong>Em 1976 falou de sua experiência como deportada num documentário de catorze minutos para a televisão francesa</strong>, num momento em que a negação do Holocausto começava a recuar.",
     "Em 1979 tornou-se a primeira presidente do Parlamento Europeu eleito por sufrágio direto, e a primeira mulher no cargo. Presidiu a Fondation pour la Mémoire de la Shoah. Em 2018 foi sepultada no Panthéon com o marido, Antoine, uma das poucas mulheres a receber a honra.",
   ],
   importa="O testemunho televisivo de 1976 é um marco de política pública de memória: colocou a experiência da deportação no espaço de audiência majoritária. A trajetória de sobrevivente a presidente de parlamento supranacional é o caso mais legível de vítima que passa a ocupar a instituição.",
   diverg="A data de morte não foi confirmada na fonte consultada, que a indica em 2017. Esta edição não trata da atuação legislativa de Veil em matéria de aborto, por integrar disputa política corrente e ser incompatível com a declaração de não emitir opinião editorial. Mantêm-se os fatos ligados ao Holocausto, à magistratura e às instituições europeias.",
   fontes=[("Liberation Route Europe, perfil de Simone Veil","https://www.liberationroute.com/en/stories/493/simone-veil")]),
]

PERFIS += [
 dict(n=14, id="raphael-lemkin", nome="Raphael Lemkin",
   vida="1900–1959", nac="Jurista polonês, radicado nos Estados Unidos", bloco="Juristas",
   chamada="Cunhou a palavra &ldquo;genocídio&rdquo; porque, sem categoria, o fato não podia ser contado nem julgado.",
   corpo=[
     "Nasceu numa pequena fazenda perto de Wolkowysk. Desde a infância interessou-se pela história da perseguição religiosa e étnica, e tinha consciência aguda dos pogroms antissemitas. Estudante de direito, tomou conhecimento da destruição dos armênios pelo Império Otomano durante a Primeira Guerra, o que consolidou sua convicção de que deveria existir uma lei internacional contra a destruição de grupos. Durante os anos 1930 tentou, sem sucesso, introduzir salvaguardas jurídicas para grupos étnicos, religiosos e sociais em fóruns internacionais.",
     "Com a invasão da Polônia, escapou da Europa e chegou aos Estados Unidos. Mudou-se para Washington em 1942 para integrar o Departamento de Guerra como analista e documentou as atrocidades nazistas em <em>Axis Rule in Occupied Europe</em>, de 1944, onde <strong>introduziu a palavra genocídio</strong>, formada do grego <em>genos</em> e do latim <em>cide</em>. Definiu-a como um plano coordenado de ações visando à destruição dos fundamentos essenciais da vida de grupos nacionais, dirigida contra o grupo como entidade e contra indivíduos não em sua capacidade individual, mas como membros do grupo.",
     "Integrou a equipe norte-americana que preparou os julgamentos de Nuremberg, onde conseguiu incluir a palavra na acusação contra a liderança nazista. Mas o genocídio ainda não era crime tipificado, e o veredito não cobria ataques a grupos em tempo de paz. Em Nuremberg soube da morte de 49 membros de sua família, entre eles os pais. Voltou determinado a inscrever o genocídio no direito internacional e fez campanha nas primeiras sessões da ONU. Em 9 de dezembro de 1948 a Convenção para a Prevenção e Punição do Genocídio foi aprovada. Morreu em 1959, empobrecido e exaurido.",
   ],
   importa="É o caso fundador de que <strong>sem categoria não há mensuração nem imputação</strong>: foi preciso criar a palavra para que o fato pudesse ser contado e julgado. Isso é diretamente aplicável à discussão de marcador estatístico e de tipificação na entrada de dados, que é o achado central deste Observatório.",
   diverg="",
   fontes=[("United States Holocaust Memorial Museum, a história de Raphael Lemkin","https://encyclopedia.ushmm.org/content/en/article/coining-a-word-and-championing-a-cause-the-story-of-raphael-lemkin")]),

 dict(n=15, id="simon-wiesenthal", nome="Simon Wiesenthal",
   vida="1908–2005", nac="Austríaco", bloco="Juristas",
   chamada="Sobrevivente que transformou a documentação de crimes em atividade permanente. É o antecedente institucional mais próximo de um observatório.",
   corpo=[
     "Nasceu em 31 de dezembro de 1908 em Buczacz. Recusado no Instituto Politécnico de Lvov por restrições de cota a estudantes judeus, formou-se em engenharia arquitetônica em Praga em 1932. Sob a ocupação soviética de Lvov, o padrasto morreu na prisão e o meio-irmão foi fuzilado. Sob os alemães, foi detido no campo de Janwska e depois no campo de trabalho forçado das oficinas da Ostbahn. Em agosto de 1942 a mãe foi enviada ao campo de extermínio de Belzec; até setembro, 89 membros das duas famílias estavam mortos.",
     "Sobreviveu ao percurso a oeste por Plaszow, Gross-Rosen e Buchenwald, terminando em Mauthausen, onde, pesando menos de 45 quilos, foi libertado em 5 de maio de 1945. Restabelecido, começou a reunir provas para a Seção de Crimes de Guerra do Exército dos Estados Unidos. Em 1947, com trinta voluntários, abriu o Centro de Documentação Histórica Judaica em Linz. Com o esfriamento do interesse na Guerra Fria, o escritório fechou em 1954 e os arquivos foram para Yad Vashem, <strong>exceto um: o dossiê de Adolf Eichmann</strong>.",
     "Em 1953 recebeu informação de que Eichmann estava na Argentina e a repassou a Israel. Eichmann foi capturado, julgado e executado em 31 de maio de 1961. Encorajado, Wiesenthal reabriu o Centro de Documentação em Viena, em 1961. Localizou em 1963 Karl Silberbauer, o oficial da Gestapo que prendeu Anne Frank, e obteve dele a confissão &ldquo;Sim, eu prendi Anne Frank&rdquo;, o que desarmou a campanha de negacionistas contra a autenticidade do diário. Após três anos de trabalho, localizou no Brasil Franz Stangl, comandante de Treblinka e Sobibor, remetido à Alemanha Ocidental em 1967 e condenado à prisão perpétua. Uma seção do escritório de Viena documentava a atividade de grupos de extrema direita e neonazistas.",
   ],
   importa="É o modelo institucional mais próximo do que um observatório faz: coleta, análise e guarda continuada de informação, sustentada por rede de colaboradores, com monitoramento explícito de grupos extremistas. O caso Silberbauer mostra a documentação servindo diretamente ao enfrentamento do negacionismo. O caso Stangl é ponto de contato direto com o Brasil.",
   diverg="A fonte informa que os arquivos alemães de criminosos de guerra continham mais de 90 mil nomes, a maioria de pessoas nunca julgadas. A cifra de 1.100 criminosos de guerra atribuída a ele circula em fontes secundárias e não consta da página institucional consultada. A data exata de morte não foi confirmada.",
   fontes=[("Simon Wiesenthal Center, sobre Simon Wiesenthal","https://wiesenthal.org/about/about-simon-wiesenthal")]),

 dict(n=16, id="fritz-bauer", nome="Fritz Bauer",
   vida="16 de julho de 1903 – 1º de julho de 1968", nac="Alemão", bloco="Juristas",
   chamada="Procurador-geral que tratou a persecução dos crimes nazistas como política de construção democrática, de dentro do aparato.",
   corpo=[
     "Nasceu em Stuttgart, em família de comerciante judeu. Estudou direito e economia em Heidelberg, Munique e Tübingen. Em 1930 foi nomeado juiz distrital em sua cidade, o mais jovem juiz da Alemanha. Filiou-se ao Partido Social-Democrata na juventude e chefiou o grupo local de Stuttgart do Reichsbanner Schwarz-Rot-Gold, liga de defesa da democracia parlamentar de Weimar.",
     "Poucas semanas após a chegada dos nacional-socialistas ao poder, foi demitido do cargo de juiz e detido por vários meses, por motivos políticos, no campo de concentração de Heuberg. Em 1936 fugiu para a Dinamarca e depois para a Suécia, onde sobreviveu à guerra. No ano da fundação da República Federal, voltou do exílio. Considerava a persecução judicial dos crimes nazistas <strong>fundamento de um sistema de justiça democrático</strong>, e fez disso o objetivo de seu trabalho.",
     "Em 1956 tornou-se procurador-geral em Frankfurt. Forneceu ao serviço secreto israelense a pista decisiva sobre o paradeiro de Adolf Eichmann, que levou à captura em 1960 e ao julgamento em Jerusalém em 1961. Iniciou o processo de Auschwitz, realizado em Frankfurt de dezembro de 1963 a agosto de 1965. Entendia os processos contra perpetradores nazistas como meio de autoesclarecimento e autodepuração da sociedade alemã-ocidental. Foi encontrado morto em seu apartamento em 1º de julho de 1968. Um processo contra participantes do programa de eutanásia, que havia preparado, não se realizou.",
   ],
   importa="É o caso em que a persecução penal dos crimes é tratada explicitamente como política de construção democrática, e não como vingança. Um Estado processando os próprios quadros é o teste mais duro de capacidade institucional, e Bauer conduziu isso de dentro.",
   diverg="",
   fontes=[("Fritz Bauer Institut, sobre Fritz Bauer","https://www.fritz-bauer-institut.de/en/fritz-bauer")]),
]

PENDENTES = [
 ("Hersch Lauterpacht", "Jurista que formulou o conceito de crimes contra a humanidade. "
  "Não entregue: as duas rotas testadas ao Lauterpacht Centre, em Cambridge, devolveram 404. "
  "Preferiu-se não publicar perfil sem fonte primária aberta."),
 ("Serge e Beate Klarsfeld", "Casal que documentou e localizou perpetradores na França. "
  "Não entregue por ausência de fonte institucional acessível na verificação."),
 ("Ministro Celso de Mello", "A atuação no HC 82.424/RS não foi verificada. O inteiro teor do acórdão "
  "e a página do processo no portal do STF não abriram. O placar e os três vencidos estão confirmados; "
  "os votos concorrentes que compõem a maioria não foram recuperados."),
]
