# Observatório do Antissemitismo no Brasil — protótipo

> **Versão de trabalho, sem caráter oficial.** Protótipo em elaboração no Eixo 3 — Segurança e Monitoramento, ainda não apreciado pelo Eixo nem pela reunião de coordenadores. Não representa posição do CDESS, da Presidência da República ou de qualquer órgão citado no conteúdo. A página traz faixa permanente com essa marcação e está fora de indexação (`noindex` e `robots.txt`).

> Monitoramento de incidentes, indicadores, orientação jurídica, canais de denúncia e preservação de evidências para o enfrentamento ao antissemitismo no Brasil.

## Sobre

Este protótipo demonstra o desenho de uma plataforma pública de monitoramento, orientação jurídica e proteção de direitos. É uma proposta em elaboração no **Eixo 3 — Segurança e Monitoramento** da **Iniciativa de Enfrentamento ao Antissemitismo**. Os canais de denúncia listados são oficiais e funcionam de forma independente deste protótipo.

### Definição Adotada

Este Observatório adota a definição de antissemitismo estabelecida pelo **Supremo Tribunal Federal** no julgamento do **HC 82.424/RS (Caso Ellwanger, 2003)**, que qualificou o antissemitismo como racismo — crime inafiançável e imprescritível nos termos do art. 5º, XLII, da Constituição Federal.

## Funcionalidades

- 📊 **Indicadores e KPIs** — Página própria, em duas camadas: as séries que hoje são mensuráveis a partir de fontes secundárias, e o painel das vinte lacunas que nenhuma base preenche, com o motivo de cada uma
- 📰 **Painel de notícias** — Agregação automática de 21 fontes públicas, atualizada a cada trinta minutos, com link para a publicação de origem e declaração de quantas fontes responderam em cada coleta
- 📡 **Fita ao vivo** — Duas faixas em movimento, No Brasil e No mundo, com as manchetes mais recentes
- 📚 **Biblioteca de referência** — Marcos conceituais internacionais, legislação brasileira, leading cases (STF, TEDH, SCOTUS) e centros de pesquisa, em página própria
- 📋 **Canais de Denúncia** — Links diretos para CONIB, FISESP, SaferNet, Disque 100, MPF, Polícia Federal e órgãos estaduais
- 🔒 **Preservar Evidências** — Guia prático de preservação de provas digitais com cadeia de custódia, e uma ferramenta de apoio que calcula o resumo SHA-256 dos arquivos **no próprio navegador**
- 🕯️ **Série: quem enfrentou o antissemitismo** — Dezesseis perfis, um por semana, com fonte pública conferida em cada um. Começa pelos brasileiros. Onde a fonte primária não confirma um dado de ampla circulação, a divergência fica registrada em bloco próprio, em vez de resolvida por escolha
- 🏛️ **Acervos e memória** — Catálogo de acervos, memoriais e material de referência, com endereço verificado. Registra também o que foi examinado e não recomendado, com o motivo
- 📬 **Boletim semanal** — Uma edição por semana ISO, gerada do histórico do painel, com feed RSS próprio
- ⚖️ **Linha do Tempo** — Legislação, jurisprudência e normativos de enfrentamento ao antissemitismo

## Roadmap

Situação verificada em 04/09/2026 contra a página publicada. O quadro completo,
com o método de verificação, está em
`EIXO3/01_ESTADO/PENDENCIAS_Site_2026-09-04.md` no repositório da Iniciativa.

### Concluído

- [x] MVP: Ticker + Denúncias + Preservação + Timeline
- [x] Marcação de protótipo e retirada da atribuição institucional
- [x] Área de indicadores e KPIs, com painel de lacunas e dados abertos
- [x] Persistir instantâneos do painel (instantâneo diário + índice acumulado)
- [x] Boletim semanal gerado do histórico, com feed RSS próprio em `boletim/feed.xml`
- [x] **Cadência do deploy decidida e branch de dados confirmado.** Ativo desde 04/09/2026: doze coletas diárias, gravação em `dados`
- [x] Metodologia e taxonomia como páginas próprias e citáveis
- [x] Política de privacidade e termos de uso publicados
- [x] Série editorial semanal, com dezesseis perfis de endereço próprio
- [x] Página de acervos e memória, com a curadoria declarada
- [x] Natureza e grau de verificação de cada número, no modelo ODIHR
- [x] Cabeçalho e rodapé unificados numa fonte de verdade única, com conferência de links, âncoras, ativos e menu
- [x] Canal de contato e procedimento de errata

### Aberto: decisões de coordenação

- [ ] **Situação institucional e endereço definitivo.** Trava divulgação, indexação, `sitemap.xml`, bilinguismo e lista institucional de boletim
- [ ] **Envio do boletim por e-mail:** serviço externo, lista institucional ou apenas RSS. O bloqueio anterior caiu com a publicação da política de privacidade

### Aberto: conteúdo

- [ ] Glossário. A fonte está pronta em `EIXO3/00_CONFIG/CONVENCOES_E_GLOSSARIO.md`
- [ ] Agenda de datas
- [ ] Confirmar com CONIB e FISESP o endereço dos canais dedicados de denúncia
- [ ] Conferir no Relatório CONIB 2025 integral os valores hoje extraídos do Sumário Executivo
- [ ] Verificar na publicação primária os números da SaferNet, do MPF, da ADL e da FRA
- [ ] Ficha de fonte por indicador: faltam método de coleta, cobertura e data de extração como campos próprios
- [ ] Série versionada com caminho fixo por edição e resumo SHA-256 por edição

### Aberto: técnico

- [ ] Busca e filtro por período no painel. Implementável desde que o histórico passou a acumular
- [ ] Estado dos filtros refletido na URL, para que um recorte seja compartilhável
- [ ] Resolver o redirecionamento dos itens do radar até a URL final do veículo
- [ ] Migração incremental para páginas em pastas (`/preservar/`, `/denunciar/`)
- [ ] Auditoria de acessibilidade por ferramenta e por leitor de tela
- [ ] Bilinguismo (PT/EN). Depende do endereço definitivo
- [ ] `sitemap.xml` e dados estruturados JSON-LD. Só fazem sentido depois de a página sair do `noindex`

### Frentes da página de preservação, na ordem sugerida

- [ ] Seletor de tipo de incidente, com o roteiro correspondente. Não recolhe dado
- [ ] Checklist de medidas de emergência dos primeiros 60 minutos. Não recolhe dado
- [ ] Formulário de qualificação da notícia-crime. Recolhe dado, e por isso é decisão à parte
- [ ] Geração e exportação de dossiê preliminar. Mesmo caso

## Navegação e conferência

### Uma fonte de verdade

`scripts/layout.py` declara a faixa de protótipo, o menu, o cabeçalho e o rodapé. Todos os
geradores o importam. Antes dele havia cinco definições independentes de navegação, e a
consequência foi um defeito no ar: oito itens de menu apontando para âncoras que não
existiam nas páginas onde estavam, mais rodapés que divergiam entre si, de modo que da
página de acervos não se alcançava a série.

Os destinos são declarados **relativos à raiz** do sítio. A função `caminho()` os reescreve
relativos ao diretório da página que está sendo gerada, o que resolve num só lugar os três
casos que antes eram feitos à mão em cada gerador: página na raiz, página em subdiretório e
link para a própria página ou para um vizinho no mesmo subdiretório. Tem autoteste:

```bash
python3 scripts/layout.py     # 14 casos de caminho
```

### As duas páginas mantidas à mão

`index.html` e `biblioteca.html` não são geradas. Para que não voltem a divergir:

```bash
python3 scripts/sincroniza_navegacao.py             # aplica a navegação canônica
python3 scripts/sincroniza_navegacao.py --conferir  # só verifica, não escreve
```

O script substitui no lugar apenas três blocos, o menu do cabeçalho e os dois `<nav>` do
rodapé. É idempotente: rodar duas vezes não muda nada na segunda.

### Antes de publicar

```bash
python3 scripts/verifica_sitio.py
```

Quatro conferências sobre todas as páginas: todo link local resolve em arquivo existente,
toda âncora existe na página de destino, todo ativo referenciado existe, e o menu principal
tem os mesmos rótulos na mesma ordem em toda parte. Devolve 1 na primeira falha, nomeando o
arquivo e o alvo.

Não está ligado ao deploy. Os passos do workflow são tolerantes a erro de propósito, para
que uma falha de coleta não derrube a publicação, e transformar a conferência em portão de
publicação é decisão de coordenação, não detalhe de implementação.

## Tecnologia

- HTML5 + CSS3 + JavaScript (vanilla)
- GitHub Pages (hospedagem estática)
- Sem dependências externas de código
- Tipografia: Libre Caslon Display, Work Sans e Space Mono (Google Fonts)
- Responsivo (mobile-first)
- LGPD: apenas armazenamento local para preferências de exibição

## Acessibilidade

O protótipo **não declara conformidade com a WCAG 2.1**, porque ela não foi auditada.
O que está atendido, e verificado no código:

- `prefers-reduced-motion` dispensa a abertura e desliga as animações da fita;
- link de salto para o conteúdo em todas as páginas, visível ao receber foco;
- `:focus-visible` com contorno em todos os elementos interativos;
- filtros do painel como botões com `aria-pressed`, ligados por `aria-controls` à região que atualizam, que é `aria-live` e `aria-busy`;
- gráficos com tabela equivalente em `<details>`, alcançável por teclado, e `<title>` em cada marca;
- links externos avisam que abrem em nova aba por texto oculto dentro do próprio link;
- `noscript` no painel de notícias.

Pendente: auditoria por ferramenta e por leitor de tela, revisão de contraste em toda
a paleta de interface e teste de navegação completa por teclado.

## Estrutura

```
├── index.html                    # Página principal (mantida à mão)
├── indicadores.html              # Indicadores e KPIs (gerado por script)
├── boletim/                      # Edições semanais e feed RSS (geradas por script)
├── serie/                        # Série semanal de perfis (gerada por script)
├── acervo.html                   # Acervos e memória (gerado por script)
├── contato.html                  # Contato e errata (gerado por script)
├── biblioteca.html               # Biblioteca de referência (mantida à mão)
├── BIBLIOTECA.md                 # Mesma biblioteca em Markdown
├── css/main.css                  # Estilos e tokens de design
├── css/indicadores.css           # Estilos da página de indicadores
├── js/app.js                     # Abertura, fita ao vivo, painel, filtros e LGPD
├── js/indicadores.js             # Leitura por ponteiro e teclado nos gráficos
├── scripts/layout.py             # Fonte de verdade única do cabeçalho e do rodapé
├── scripts/agregar.py            # Coleta dos feeds, roda no build
├── scripts/gerar_paginas.py      # Páginas institucionais, inclusive contato
├── scripts/gerar_indicadores.py  # Gera indicadores.html a partir das séries
├── scripts/gerar_serie.py        # Gera a série de perfis
├── scripts/gerar_acervo.py       # Gera a página de acervos
├── scripts/historico.py          # Instantâneo diário e índice acumulado
├── scripts/gerar_boletim.py      # Gera as edições semanais e o feed
├── scripts/sincroniza_navegacao.py  # Aplica a navegação canônica nas duas páginas à mão
├── scripts/verifica_sitio.py     # Confere links, âncoras, ativos e menu
├── img/                          # Imagem de abertura (1200 / 1800 / 2400 px)
├── data/feeds.json               # Catálogo das fontes a agregar
├── data/biblioteca.json          # Biblioteca em formato estruturado
├── data/indicadores/             # Séries em CSV e dicionário de campos
├── data/historico/               # Instantâneos diários e índice (branch `dados`)
├── data/noticias.json            # Resultado da coleta, gerado no build
├── robots.txt                    # Bloqueio de indexação enquanto for protótipo
├── LICENSE                       # MIT
├── .github/workflows/            # Deploy automático
└── README.md
```

## Ferramenta de integridade probatória

`js/preservar.js` calcula o resumo SHA-256 dos arquivos escolhidos pela pessoa, usando
`crypto.subtle.digest`. É a única parte do sítio que recebe entrada do usuário, e por isso
tem uma regra de projeto explícita: **nada sai do navegador.**

O arquivo não contém, e não pode conter, nenhuma chamada de rede: sem `fetch`, sem
`XMLHttpRequest`, sem `sendBeacon`, sem `WebSocket`, sem `<form action>`. Também não usa
`localStorage`, `sessionStorage` nem IndexedDB — aparelho compartilhado ou apreendido
transforma persistência em passivo, não em conveniência. O conteúdo do arquivo é lido
apenas para o cálculo do resumo, não é retido nem exibido, e fechar a página descarta tudo.

Conferência, que deve não retornar nada:

```
grep -nE 'fetch\(|XMLHttpRequest|sendBeacon|WebSocket|localStorage|sessionStorage|indexedDB|<form' js/preservar.js
```

`crypto.subtle` só existe em contexto seguro. Em `https` funciona; ao abrir a página direto
do disco, não. O painel detecta e se retira, exibindo no lugar os comandos de terminal
equivalentes. O guia de quatro etapas continua valendo por si.

O resultado foi conferido contra `sha256sum`: mesmo arquivo, mesmo valor.

## Série e acervos

`scripts/serie_dados.py` guarda os dezesseis perfis; `scripts/gerar_serie.py` emite o índice
e uma página por perfil, com endereço próprio para citação isolada.
`scripts/gerar_acervo.py` emite o catálogo de acervos.

Duas regras editoriais que os dois observam:

**Fato muito repetido não é fato verificado.** Cada perfil declara as fontes conferidas.
Onde a fonte primária não confirma um dado de circulação corrente, a divergência é
publicada. Números de pessoas salvas variam muito: em um caso as duas cifras divergem *na
mesma página* da mesma instituição; em outro, a própria fonte declara que o número exato é
desconhecido. A semana 9 é inteiramente dedicada a um fato de altíssima circulação que não
se confirma na instituição que o concederia.

**Código 200 não é garantia de conteúdo.** Quatro endereços examinados para o catálogo
respondiam normalmente e não serviam o que o título prometia. Nenhum entrou como remissão.

Nenhum perfil de pessoa cuja atuação seja objeto de disputa política corrente no Brasil. Em
dois casos o escopo foi recortado por essa razão, e a página diz isso.

## Persistência e boletim

`data/noticias.json` é regerado a cada execução do deploy e sobrescreve o anterior.
Sem persistência nada do que o Observatório observa sobrevive ao ciclo seguinte, e
série própria nunca se forma.

`scripts/historico.py` grava um instantâneo por dia em `data/historico/AAAA-MM-DD.json`
e mantém `indice.json` com contagem por dia e por semana ISO. A granularidade é diária,
não por execução: a execução do dia sobrescreve o arquivo do dia, acumulando itens novos
e deduplicando por URL normalizada. Dias anteriores nunca são tocados. A retenção é de
400 dias.

**O que o histórico mede.** Manchetes agregadas por dia, não incidentes. É indicador de
cobertura de imprensa e de alcance das fontes monitoradas, não de incidência do fenômeno.
O `indice.json` carrega esse aviso no próprio arquivo.

`scripts/gerar_boletim.py` monta uma edição por semana ISO em `boletim/`, com índice e
feed RSS. A seleção é por data, sem juízo editorial: não cabe a este protótipo escolher
o que é mais relevante. Cada item remete à publicação de origem.

### O branch de dados

**O problema.** GitHub Pages publica um artefato efêmero. O que o build gera existe
enquanto o site está no ar e desaparece na publicação seguinte. Um sítio estático não tem
banco. Sem um lugar durável, cada coleta apagaria a anterior e série própria nunca se
formaria.

**A solução, e por que é um branch.** O histórico vive em `dados`, um **branch órfão** —
não tem ancestral comum com `main`, não contém código, não aparece em diff de código e
não interfere no histórico do projeto. Guarda só `data/historico/`.

Por que não em `main`: doze coletas por dia gerariam doze commits automáticos diários no
mesmo histórico onde ficam as mudanças de código. Em uma semana, o log ficaria ilegível e
qualquer revisão de código teria que garimpar entre commits de robô. Separando, `main`
continua sendo o registro do que pessoas decidiram, e `dados` é o registro do que a
máquina observou.

Por que não um banco externo: exigiria servidor, credencial e custo, para guardar
40 KB por dia de dado público que já é, ele mesmo, aberto.

**O ciclo, a cada execução:**

```
1. recupera data/historico/ do branch dados        (git restore --source)
2. coleta as 21 fontes                             (agregar.py)
3. acumula no arquivo do dia, deduplicando         (historico.py)
4. gera as edições do boletim                      (gerar_boletim.py)
5. publica o site, já com o histórico dentro       (deploy-pages)
6. devolve data/historico/ ao branch dados         (clone em diretório separado)
```

O passo 6 roda **depois** do deploy e monta o branch por clone em diretório temporário.
Fazer isso na árvore de trabalho destruiria os arquivos do sítio antes da publicação.

**Reversibilidade.** Desativar é uma linha: `if: false` no passo 6. O branch permanece e
nada se perde. Apagar o branch `dados` não afeta o sítio nem o código; só interrompe a
série.

### A cadência

**Doze coletas por dia**, de duas em duas horas. Era de trinta em trinta minutos.

A redução não custa nada à série, e a razão é o desenho da persistência. A granularidade
do histórico é **diária**: a coleta do dia abre o arquivo do dia, acrescenta o que ainda
não viu e deduplica por URL normalizada. Não sobrescreve. Então o que importa não é a
frequência, é a cobertura — e uma matéria publicada às 9h continua no feed da fonte às
10h, às 11h e no dia seguinte. Doze passagens cobrem o ciclo noticioso com folga.

O que a frequência alta custava: 48 publicações diárias do sítio inteiro, cada uma
consumindo minutos de Actions e produzindo uma entrada no histórico de deploys, para
atualizar um arquivo de 40 KB.

Para adensar em período de crise, uma linha: `cron: '0 * * * *'` dá uma coleta por hora.

**O que a série mede, e o que não mede.** Manchetes agregadas por dia, não incidentes. É
indicador de cobertura de imprensa e de alcance das fontes monitoradas. O aviso está
dentro do próprio `indice.json`, para que ninguém o perca ao reutilizar o arquivo.

### O boletim por e-mail

O envio automático por e-mail exige guardar uma lista de assinantes, o que um sítio
estático não faz. Depende de serviço externo ou de lista institucional. O protótipo **não
coleta endereço de e-mail** e a assinatura é pelo feed RSS, que funciona em qualquer
leitor e em vários clientes de e-mail, sem que este protótipo guarde endereço de ninguém.

## Série versionada do boletim

Cada edição tem três coisas ao lado do texto, para poder ser citada e conferida:

| | |
|---|---|
| **Endereço permanente** | `boletim/<semana-ISO>.html`, que não muda |
| **Planilha** | `boletim/<semana-ISO>.csv`, com a edição inteira e não apenas as manchetes exibidas |
| **Resumo SHA-256** | do conteúdo da edição, na forma canônica descrita abaixo |

A página mostra as dez manchetes mais recentes de cada recorte; o CSV traz todas as da
semana. É o CSV que é a base do resumo.

### A forma canônica, e por que não é o hash do HTML

O resumo **não** é do arquivo HTML. Seria inútil: o HTML carrega cabeçalho, menu e rodapé,
que mudam quando um item novo entra na navegação, e o resumo mudaria sem que a edição
tivesse mudado. O resumo é do conteúdo.

A forma canônica é esta:

1. Um registro por manchete, com os campos `escopo`, `publicado_em`, `fonte`, `via`,
   `titulo`, `link`, nessa ordem, separados por tabulação. Campo vazio entra vazio.
2. Os registros em ordem alfabética crescente, o que torna o resumo independente da
   ordem em que a coleta encontrou os itens.
3. Os registros unidos por `\n`, com um `\n` ao final.
4. `SHA-256` desse texto em UTF-8.

### Como conferir

Da planilha publicada, sem depender deste repositório:

```bash
python3 - <<'EOF'
import csv, hashlib
with open("2026-S36.csv", encoding="utf-8", newline="") as f:
    r = csv.reader(f); next(r)
    linhas = ["\t".join(x) for x in r]
print(hashlib.sha256(("\n".join(sorted(linhas)) + "\n").encode("utf-8")).hexdigest())
EOF
```

O valor deve bater com o publicado na própria edição. Resumo que ninguém consegue
reproduzir não serve de nada, e é por isso que a regra está escrita aqui e não só no
código.

## Página de indicadores

`indicadores.html` **não é editada à mão**: é gerada por `scripts/gerar_indicadores.py`,
onde as séries ficam declaradas em estruturas Python e a geometria dos gráficos é
calculada. Para atualizar um número, altere a série no script e rode:

```
python3 scripts/gerar_indicadores.py
```

Os gráficos são SVG embutido, sem dependência externa de código. Cada figura traz
tabela equivalente em `<details>`, de modo que nenhum valor dependa do ponteiro.
A paleta de duas cores (`#1f5fae` e `#c2531f`) foi validada para daltonismo e para
contraste de 3:1 sobre o papel do site.

### Natureza do dado

Cada número carrega, além do selo de procedência, uma **marca de natureza**: contagem de
fonte comunitária, registro oficial agregado, monitoramento de imprensa, pesquisa de
percepção ou apuração de outra jurisdição.

**Números de naturezas diferentes não são somados nem comparados diretamente.** A prática
vem do ODIHR, organismo da OSCE que mantém dois acervos separados e nunca os junta: o que
vem do Estado é registrado como crime, o que vem da sociedade civil como incidente, com a
razão declarada de que não se consegue verificar se o segundo grupo se qualifica como
crime.

A razão de adotar aqui é prática. Como nenhuma base estatal brasileira tem categoria
autônoma de antissemitismo, misturar a contagem comunitária da CONIB com dado policial do
Anuário do FBSP, ou com a apuração da ADL em outro país, produziria número sem
denominador. A marca torna a ausência de marcador estatal informação declarada, em vez de
constrangimento silencioso.

### Grau de verificação

A página declara o grau de verificação de cada bloco: **conferido no acervo**, para
número checado contra o documento de origem, e **citado, primária não consultada**,
para número cuja fonte está declarada mas cuja publicação não foi aberta. Nenhum
identificador administrativo ou número de processo não confirmado foi transcrito.

## Identidade visual

O desenho da página segue o **modelo D** dos quatro estudos tipográficos produzidos para o Observatório: Libre Caslon Display nos títulos, Work Sans no texto corrido e Space Mono nos rótulos e metadados. A abertura cinematográfica cita o HC 82.424/RS e roda uma vez por visita, com controle para pular.

## Como o painel funciona

`scripts/agregar.py` lê `data/feeds.json`, consulta as 21 fontes em paralelo, filtra por termo, deduplica por URL normalizada e por título, ordena por data e escreve `data/noticias.json`. Usa apenas a biblioteca padrão do Python.

A coleta roda **dentro do job de deploy**, não em um workflow que faz commit. O arquivo entra somente no artefato publicado e é ignorado pelo Git, de modo que o histórico do repositório não recebe commits automáticos. Para que o painel não congele na última publicação, `pages.yml` ganhou um agendamento de trinta em trinta minutos — o que reintroduz o deploy periódico removido em 28/08. Para reduzir a cadência, basta alterar o `cron` do workflow.

Se a coleta falhar por inteiro, o passo é tolerante e o site sobe assim mesmo: a página exibe o estado "painel em implantação", com os cartões em esqueleto e a fita oculta. São três estados desenhados — carregando, no ar e indisponível — e há um `noscript` para quem navega sem JavaScript.

O filtro por termo se aplica a todas as fontes menos as sete do radar, que já são consultas por palavra-chave, e o feed do Combat Antisemitism Movement, dedicado ao tema. O recorte de termos acompanha o nome do Observatório: além do antissemitismo, alcança racismo religioso, intolerância religiosa e crimes de ódio.

## Fontes e biblioteca

`data/feeds.json` registra 21 feeds públicos, agrupados em cinco categorias, com idioma, escopo e foco de cobertura. Os endereços foram reconferidos por requisição HTTP em 30/08/2026 e todos responderam 200 na bancada. **Isso não garante que respondam no build:** a coleta de 30/08 às 07h59 registrou falha de The Times of Israel, cujo endereço responde 200 em requisição local. A causa provável é bloqueio ao IP do runner, e não endereço inválido. Por isso a página passou a declarar quantas fontes responderam em cada coleta, com a lista das que faltaram.

Quatorze são feeds de veículos e instituições. Os outros sete são o radar por palavras-chave — buscas permanentes no Google Notícias em português, inglês, espanhol e francês, com a expressão booleana registrada ao lado da URL e os atributos `tipo: radar_de_busca` e `exige_resolucao_de_url: true`. Esses sete não são veículos: cada item traz `<source url="...">` com o nome do veículo, mas o `<link>` é um endereço de redirecionamento em `news.google.com`. O agregador exibe o nome do veículo e marca o item com o rótulo **via Google Notícias**, para que o leitor saiba que o clique passa por um intermediário. Resolver o redirecionamento até a URL final está no roadmap.

`BIBLIOTECA.md` e `data/biblioteca.json` trazem os mesmos 29 verbetes da página `biblioteca.html`. Nove verbetes carregam nota no corpo da página.

Seis são notas de revisão, onde a leitura do texto de origem divergiu da entrega de pesquisa:

- **Marco Civil da Internet** — o art. 19 não é base de remoção célere, e seu regime foi alterado pelo STF em 26/06/2025;
- **Resolução CNJ nº 492/2023** — o protocolo é de perspectiva de gênero; a dimensão racial e étnica aparece no dever de formação;
- **Virginia v. Black** — a Corte estadunidense manteve a proibição da queima de cruz com intenção de intimidar, mas derrubou o dispositivo que presumia essa intenção a partir do ato;
- **CC 146.983/RJ** — a entrega indicava `/AC` e 10/08/2016, e invertia a tese: o acórdão amplia a competência federal, não a restringe;
- **REsp 2.134.594** — a entrega descrevia agravo regimental de 21/05/2024 sem número; o julgado é recurso especial de 21/10/2024;
- **Kantor Center** — a entrega inverteu o nome do centro e afirmou publicação ininterrupta desde 1994, o que não foi confirmado.

Uma é nota de acréscimo, em **CC 163.420/PR**: acórdão ausente da entrega, incluído por ser o caso do STJ que trata especificamente de antissemitismo em rede social.

Uma é nota de inferência, no verbete do **Tema 987 do STF**: o enquadramento de conteúdo antissemita no rol de condutas com dever de cuidado decorre do HC 82.424/RS, não de menção expressa na tese fixada.

A última é nota de lacuna, no verbete do **Ministério Público Federal**: os quatro identificadores administrativos indicados na entrega não foram confirmados e por isso não estão transcritos.

Duas lacunas seguem registradas: dois acórdãos citados na entrega não foram localizados na verificação (CC 175.525/SP e AgRg no AREsp 1.331.345/SP) e os identificadores administrativos do MPF.

Os quatro indicadores da página inicial têm fonte declarada: o Relatório de Antissemitismo no Brasil 2024, da CONIB, da FISESP e do Departamento de Segurança Comunitária, publicado em abril de 2025.

## Contribuições

Contribuições são bem-vindas. Abra uma issue para sugestões ou envie um pull request.

## Licença

Este projeto é de interesse público. Conteúdo editorial e código sob [MIT License](LICENSE).

## Referências

- [HC 82.424/RS — Caso Ellwanger (STF, 2003)](https://portal.stf.jus.br/)
- [Lei 7.716/1989 — Lei Caó](https://www.planalto.gov.br/ccivil_03/leis/l7716.htm)
- [Lei 14.532/2023](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/L14532.htm)
- [CONIB — Relatório do Antissemitismo no Brasil](https://conib.org.br)
- [Panorama do enfrentamento penal ao antissemitismo (Conjur)](https://conjur.com.br/2024-fev-01/panorama-do-enfrentamento-penal-ao-antissemitismo-no-brasil/)
- [Biblioteca de referência completa](BIBLIOTECA.md)

---

*Iniciativa de Enfrentamento ao Antissemitismo — CDESS / Presidência da República*
