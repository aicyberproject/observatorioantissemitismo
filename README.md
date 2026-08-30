# Observatório do Antissemitismo no Brasil

> Monitoramento contínuo de incidentes, orientação jurídica, canais de denúncia e preservação de evidências para o enfrentamento ao antissemitismo no Brasil.

## Sobre

O Observatório do Antissemitismo no Brasil é uma plataforma pública de monitoramento, orientação jurídica e proteção de direitos, proposta pelo **Eixo 3 — Segurança e Monitoramento** da **Iniciativa de Enfrentamento ao Antissemitismo**, instituída pelo Conselho de Desenvolvimento Econômico, Social e Sustentável (CDESS) da Presidência da República.

### Definição Adotada

Este Observatório adota a definição de antissemitismo estabelecida pelo **Supremo Tribunal Federal** no julgamento do **HC 82.424/RS (Caso Ellwanger, 2003)**, que qualificou o antissemitismo como racismo — crime inafiançável e imprescritível nos termos do art. 5º, XLII, da Constituição Federal.

## Funcionalidades (MVP)

- 📰 **Painel de notícias** — Catálogo de 14 fontes públicas registradas e verificadas, exibido na própria página. O serviço que lê esses feeds e preenche os cartões ainda não está no ar; a seção declara essa pendência de forma explícita
- 📚 **Biblioteca de referência** — Marcos conceituais internacionais, legislação brasileira, leading cases (STF, TEDH, SCOTUS) e centros de pesquisa, em página própria
- 📋 **Canais de Denúncia** — Links diretos para CONIB, FISESP, SaferNet, Disque 100, MPF, Polícia Federal e órgãos estaduais
- 🔒 **Preservar Evidências** — Guia prático de preservação de provas digitais com cadeia de custódia
- ⚖️ **Linha do Tempo** — Legislação, jurisprudência e normativos de enfrentamento ao antissemitismo

## Roadmap

- [ ] MVP: Ticker + Denúncias + Preservação + Timeline
- [ ] Serviço agregador que leia os feeds de `data/feeds.json` e preencha o painel
- [ ] Radar por palavras-chave: obter as expressões de busca e as URLs (lacuna registrada)
- [ ] Dashboard estatístico (dados CONIB, ADL, SaferNet)
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
- Acessível (WCAG 2.1)
- LGPD compliance

## Estrutura

```
├── index.html            # Página principal
├── biblioteca.html       # Biblioteca de referência
├── BIBLIOTECA.md         # Mesma biblioteca em Markdown
├── css/main.css          # Estilos e tokens de design
├── js/app.js             # Abertura, filtros e aviso de LGPD
├── img/                  # Imagem de abertura (1200 / 1800 / 2400 px)
├── data/feeds.json       # Catálogo das fontes a agregar (não contém notícias)
├── data/biblioteca.json  # Biblioteca em formato estruturado
├── .github/workflows/    # Deploy automático
└── README.md
```

## Identidade visual

O desenho da página segue o **modelo D** dos quatro estudos tipográficos produzidos para o Observatório: Libre Caslon Display nos títulos, Work Sans no texto corrido e Space Mono nos rótulos e metadados. A abertura cinematográfica cita o HC 82.424/RS e roda uma vez por visita, com controle para pular.

## Fontes e biblioteca

`data/feeds.json` registra 14 feeds RSS públicos, agrupados em quatro categorias, com idioma, escopo e foco de cobertura. Os endereços foram reconferidos por requisição HTTP em 30/08/2026. O arquivo **não contém notícias**: é o catálogo do que será agregado quando o serviço entrar em operação.

A entrega de pesquisa que originou o catálogo descreve ainda uma quinta categoria — radar por palavras-chave, nos recortes Brasil, Iberoamérica, França/Europa e global — e informa um total de 21 feeds, mas fornece endereço apenas para os 14 registrados. A diferença está consignada como lacuna no próprio arquivo e na página, não reconstruída por suposição.

`BIBLIOTECA.md` e `data/biblioteca.json` trazem os mesmos 22 verbetes da página `biblioteca.html`. Quatro verbetes carregam nota no corpo da página.

Três são notas de revisão, onde a leitura do texto de origem divergiu da entrega de pesquisa:

- **Marco Civil da Internet** — o art. 19 não é base de remoção célere, e seu regime foi alterado pelo STF em 26/06/2025;
- **Resolução CNJ nº 492/2023** — o protocolo é de perspectiva de gênero; a dimensão racial e étnica aparece no dever de formação;
- **Virginia v. Black** — a Corte estadunidense manteve a proibição da queima de cruz com intenção de intimidar, mas derrubou o dispositivo que presumia essa intenção a partir do ato.

A quarta é nota de inferência, no verbete do **Tema 987 do STF**: o enquadramento de conteúdo antissemita no rol de condutas com dever de cuidado decorre do HC 82.424/RS, não de menção expressa na tese fixada.

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
