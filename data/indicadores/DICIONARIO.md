# Dicionário de campos e procedência

**Protótipo do Observatório do Antissemitismo no Brasil — Eixo 3 (Segurança e Monitoramento).**
Versão de trabalho, sem caráter oficial. Última revisão em 4 de setembro de 2026.

> **Nota de data.** A versão anterior deste arquivo declarava revisão em 30 de agosto de
> 2026. A data estava errada: o relógio do ambiente de trabalho estava quatro dias
> atrasado, e o desvio foi herdado pelos carimbos de vários arquivos deste acervo. A data
> real daquela revisão é 3 de setembro de 2026. O desvio está documentado na auditoria do
> Eixo 3.

Nenhum dado aqui é produzido pelo Observatório. Todos vêm de relatórios publicados
por terceiros. A autoridade é sempre a publicação de origem, citada no campo `fonte`.

Fonte primária da série brasileira, pública e conferida na íntegra:
<https://combateaoantissemitismo.org.br/wp-content/uploads/2026/04/Relatorio_Antissemitismo-no-Brasil-2025-FULL-PORT_vOK3_web.pdf>

Não há, em nenhum arquivo, dado pessoal, denúncia individualizada, identificação de
vítima, denunciante ou investigado, nem informação sob sigilo. Todos os valores são
agregados.

## Ficha da fonte

Cinco campos, na forma padrão do gênero. Os dois primeiros já existiam como campo nos
arquivos; os três últimos passaram a ser declarados aqui e na página de indicadores.

### Série brasileira — CONIB, FISESP e Departamento de Segurança Comunitária

| Campo | Valor |
|---|---|
| Procedência | `conferido`. Checado contra o Relatório de Antissemitismo no Brasil 2025, integral e público, linkado acima. |
| Base de cálculo | Declarada por recorte no campo `base_de_calculo`, quando há percentual. |
| Método de coleta | Denúncia recebida em canal próprio das entidades, com triagem e validação posterior por equipe. Mede denúncia recebida, e não incidência: não há busca ativa nem varredura automatizada. |
| Cobertura | Nacional, com localização declarada por quem denuncia. Em 2025, 462 dos 989 casos validados (46,7%) não trazem estado informado. |
| Data de extração | 3 de setembro de 2026. |

### Resposta institucional — SaferNet, MPF, e referência internacional

| Campo | Valor |
|---|---|
| Procedência | `citado`. Publicação primária não consultada nesta versão. |
| Base de cálculo | Declarada quando há percentual. |
| Método de coleta | **Não declarado.** O levantamento de origem não descreve como a apuração foi feita. |
| Cobertura | **Não declarada.** Nenhum recorte tem categoria específica de antissemitismo; o neonazismo é o proxy mais próximo. |
| Data de extração | Agosto de 2026, do levantamento reunido para o Eixo 3. |

Onde o campo não é conhecido, esta ficha declara que não é, em vez de omitir a linha.
Ficha que só mostra o que se sabe induz a supor que o resto foi apurado.

## Campo `procedencia`

Presente em todos os arquivos. Declara o grau de verificação do valor.

| Valor | Significado |
|---|---|
| `conferido` | Número conferido contra o documento de origem. Para a série brasileira, contra o Relatório CONIB 2025 integral, público e linkado acima. |
| `citado` | Fonte declarada, publicação primária não consultada nesta versão. Usar com a ressalva. |
| `inferido` | Resíduo calculado a partir de valores publicados, não transcrito da fonte. |

## Campo `base_de_calculo`

Quando presente, informa o denominador sobre o qual o percentual foi apurado.
Percentual sem base declarada não deve ser reutilizado.

## `serie_anual.csv`

Ocorrências validadas por ano, com separação entre ambiente digital e físico.

| Campo | Descrição |
|---|---|
| `ano` | Ano de referência. |
| `ocorrencias_validadas` | Registros que passaram na triagem e foram classificados como antissemitismo. Não é o total de registros recebidos. |
| `online` / `offline` | Decomposição por ambiente da ocorrência. |
| `pct_online` | Participação do ambiente digital no total do ano. |

**Ressalva.** O total de 2023 aparece como 1.410 no Relatório de 2024 e como 1.412 no
Relatório de 2025. Adotou-se o valor revisado, de 1.412.

## `serie_mensal.csv`

Denúncias mês a mês, de janeiro de 2022 a dezembro de 2024.

| Campo | Descrição |
|---|---|
| `ano`, `mes_numero`, `mes` | Período de referência. |
| `denuncias` | Registros do mês. |

**Ressalva.** A série mensal de 2025 não consta do Sumário Executivo e não foi incluída.
A soma da série mensal de 2023 é 1.410, valor da edição de 2024 do relatório.

## `distribuicao_2025.csv`

Três recortes do ano de 2025: destino do registro na triagem, distribuição geográfica
e plataforma da ocorrência digital.

**Nota sobre a triagem.** A taxa de descarte em 2025 foi de 30,74%. Em 2024 o canal
recebeu 3.167 denúncias brutas e descartou 43,55% delas. A queda no volume validado de
2025 decorre em parte disso, e não apenas de variação do fenômeno.

**Ressalvas.**

1. A distribuição geográfica de 2025 **não é comparável** com a de 2024. Em 2024, São
   Paulo respondia por 900 ocorrências (50,3%) e o grupo sem definição por 132 (7,4%).
   Em 2025 a proporção se inverte. A causa é mudança na forma de captar a localização,
   e não migração do fenômeno.
2. As plataformas de 2025 são calculadas sobre as 800 ocorrências online. Em 2024, o
   relatório apurou 48% para o X e 37% para o Instagram sobre uma base de 846 casos
   classificados em redes sociais, e não sobre as 1.310 ocorrências online do ano.
   A troca de liderança entre as duas plataformas é real; a magnitude não é comparável.

## `resposta_institucional.csv`

Indicadores de resposta institucional e referência internacional. Único recorte de
desfecho disponível de forma pública.

**Ressalvas.**

1. Todos os valores estão marcados como `citado`. Constam do levantamento reunido para
   o Eixo 3 em agosto de 2026, e a publicação primária não foi consultada nesta versão.
2. Nenhum recorte tem categoria específica de antissemitismo. O neonazismo é o proxy
   mais próximo. A categoria de intolerância religiosa absorve o antissemitismo sem
   distingui-lo, que é precisamente a lacuna documentada pelo Eixo 3.
3. Os identificadores administrativos e números de processo indicados no levantamento
   de origem não foram confirmados e por isso não estão transcritos.

## Licença

Conteúdo e código sob licença MIT. A reutilização é livre, com citação da fonte
primária. Citar este protótipo como origem do dado seria incorreto.
