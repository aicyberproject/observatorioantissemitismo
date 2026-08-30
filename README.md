# Observatório do Antissemitismo no Brasil

> Monitoramento contínuo de incidentes, orientação jurídica, canais de denúncia e preservação de evidências para o enfrentamento ao antissemitismo no Brasil.

## Sobre

O Observatório do Antissemitismo no Brasil é uma plataforma pública de monitoramento, orientação jurídica e proteção de direitos, proposta pelo **Eixo 3 — Segurança e Monitoramento** da **Iniciativa de Enfrentamento ao Antissemitismo**, instituída pelo Conselho de Desenvolvimento Econômico, Social e Sustentável (CDESS) da Presidência da República.

### Definição Adotada

Este Observatório adota a definição de antissemitismo estabelecida pelo **Supremo Tribunal Federal** no julgamento do **HC 82.424/RS (Caso Ellwanger, 2003)**, que qualificou o antissemitismo como racismo — crime inafiançável e imprescritível nos termos do art. 5º, XLII, da Constituição Federal.

## Funcionalidades (MVP)

- 📰 **Painel de notícias** — Área reservada para a agregação automática (Brasil e mundo). O serviço agregador ainda não está no ar; a seção declara essa pendência de forma explícita
- 📋 **Canais de Denúncia** — Links diretos para CONIB, FISESP, SaferNet, Disque 100, MPF, Polícia Federal e órgãos estaduais
- 🔒 **Preservar Evidências** — Guia prático de preservação de provas digitais com cadeia de custódia
- ⚖️ **Linha do Tempo** — Legislação, jurisprudência e normativos de enfrentamento ao antissemitismo

## Roadmap

- [ ] MVP: Ticker + Denúncias + Preservação + Timeline
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
├── index.html          # Página principal
├── css/main.css        # Estilos e tokens de design
├── js/app.js           # Abertura, filtros e aviso de LGPD
├── img/                # Imagem de abertura (1200 / 1800 / 2400 px)
├── data/feeds.json     # Dados de exemplo, ainda não consumidos pela página
├── .github/workflows/  # Deploy automático
└── README.md
```

## Identidade visual

O desenho da página segue o **modelo D** dos quatro estudos tipográficos produzidos para o Observatório: Libre Caslon Display nos títulos, Work Sans no texto corrido e Space Mono nos rótulos e metadados. A abertura cinematográfica cita o HC 82.424/RS e roda uma vez por visita, com controle para pular.

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

---

*Iniciativa de Enfrentamento ao Antissemitismo — CDESS / Presidência da República*
