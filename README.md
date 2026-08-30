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
- 🔒 **Preservar Evidências** — Guia prático de preservação de provas digitais com cadeia de custódia
- ⚖️ **Linha do Tempo** — Legislação, jurisprudência e normativos de enfrentamento ao antissemitismo

## Roadmap

- [x] MVP: Ticker + Denúncias + Preservação + Timeline
- [x] Marcação de protótipo e retirada da atribuição institucional
- [x] Área de indicadores e KPIs, com painel de lacunas e dados abertos
- [ ] **Persistir instantâneos do painel.** Item com prazo: `data/noticias.json` é regerado a cada trinta minutos e sobrescreve o anterior. Enquanto não houver persistência, o Observatório não poderá produzir série própria do que monitora, e cada ciclo apaga o anterior
- [ ] Confirmar com CONIB e FISESP o endereço dos canais dedicados de denúncia
- [ ] Conferir no Relatório CONIB 2025 integral os valores hoje extraídos do Sumário Executivo
- [ ] Verificar na publicação primária os números da SaferNet, do MPF, da ADL e da FRA
- [ ] Resolver o redirecionamento dos itens do radar até a URL final do veículo
- [ ] Busca e filtro por período no painel
- [ ] Página de metodologia autônoma, política de privacidade e canal de errata
- [ ] Migração incremental para páginas em pastas (`/preservar/`, `/denunciar/`)
- [ ] Feed RSS próprio
- [ ] Newsletter semanal
- [ ] Glossário
- [ ] Agenda de eventos
- [ ] Bilinguismo (PT/EN)

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
├── index.html                    # Página principal
├── indicadores.html              # Indicadores e KPIs (gerado por script)
├── biblioteca.html               # Biblioteca de referência
├── BIBLIOTECA.md                 # Mesma biblioteca em Markdown
├── css/main.css                  # Estilos e tokens de design
├── css/indicadores.css           # Estilos da página de indicadores
├── js/app.js                     # Abertura, fita ao vivo, painel, filtros e LGPD
├── js/indicadores.js             # Leitura por ponteiro e teclado nos gráficos
├── scripts/agregar.py            # Coleta dos feeds, roda no build
├── scripts/gerar_indicadores.py  # Gera indicadores.html a partir das séries
├── img/                          # Imagem de abertura (1200 / 1800 / 2400 px)
├── data/feeds.json               # Catálogo das fontes a agregar
├── data/biblioteca.json          # Biblioteca em formato estruturado
├── data/indicadores/             # Séries em CSV e dicionário de campos
├── data/noticias.json            # Resultado da coleta, gerado no build
├── robots.txt                    # Bloqueio de indexação enquanto for protótipo
├── LICENSE                       # MIT
├── .github/workflows/            # Deploy automático
└── README.md
```

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
