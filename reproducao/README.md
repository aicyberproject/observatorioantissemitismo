# Reproduza o achado: script de referência do Disque 100

Este script refaz, no seu computador, os 25 totais que o relatório preliminar conjunto do Eixo 3 (versão 2.0, Anexo E, item E.11) calculou a partir dos microdados abertos do Disque 100. Ele compara cada total com o valor do relatório e diz se confere, se diverge ou se faltou informação.

Se um total não fechar, o achado correspondente está em xeque, e o relatório quer saber.

## O que o script faz e o que não faz

- Lê os arquivos CSV que você baixou do MDHC e calcula **apenas totais**.
- **Nunca** imprime, exporta ou grava linha da base. Mensagens de erro citam o arquivo, nunca o conteúdo.
- Não usa a internet. Tudo roda no seu computador.
- Os arquivos de dados e as saídas ficam fora do repositório, pelo `.gitignore`.

## Passo a passo para quem não programa

### 1. Instale o Python

Baixe o Python 3.12 em <https://www.python.org/downloads/>. No Windows, marque a opção **"Add python.exe to PATH"** durante a instalação.

### 2. Baixe este repositório

Na página do repositório no GitHub, clique em **Code** e depois em **Download ZIP**. Descompacte o arquivo. A pasta deste kit é `reproducao/`.

### 3. Baixe os microdados

No portal de dados abertos do MDHC, baixe os arquivos do Disque 100 de cada semestre: 1º e 2º semestres de 2023, 2024 e 2025 e 1º semestre de 2026. Ponha todos numa pasta só, por exemplo `reproducao/dados/`.

Os nomes precisam seguir o padrão do MDHC: `disque100-primeiro-semestre-2024.csv` ou `disque100-segundo-semestre-2024.csv`. Os arquivos podem continuar comprimidos (`.csv.bz2` ou `.csv.gz`). Confira se o tamanho de cada arquivo coincide com o informado no portal.

Não ponha dois arquivos do mesmo semestre na pasta, por exemplo a versão comprimida e a descomprimida. O script recusa a pasta nesse caso.

### 4. Abra o terminal na pasta do kit

- **Windows:** abra a pasta `reproducao` no Explorador de Arquivos, clique na barra de endereço, digite `powershell` e tecle Enter.
- **macOS ou Linux:** abra o Terminal e digite `cd` seguido do caminho da pasta `reproducao`.

### 5. Instale as bibliotecas

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

No macOS e no Linux, a segunda linha é `source .venv/bin/activate`, e o comando pode se chamar `python3`.

### 6. Inspecione as colunas

A base não tem dicionário de dados. Por isso, o primeiro passo descreve as colunas sem mostrar nenhuma linha:

```
python reproduza_disque100.py inspecionar dados
```

O resultado vai para `saida/inspecao.md`. Para cada arquivo, ele traz o número de linhas, o tamanho, o SHA-256 e, para cada coluna, o tipo e o número de valores distintos. Os valores aparecem só nas colunas com até 200 valores distintos. Colunas de identificador nunca têm valores listados. Com milhões de linhas, a inspeção demora alguns minutos por arquivo.

### 7. Prepare o mapa de colunas

Copie `colunas.exemplo.json` para `colunas.json`. O exemplo já traz os nomes encontrados nos arquivos de 2023 a 2025. Confira cada nome contra o `inspecao.md`. Se o MDHC tiver renomeado alguma coluna, corrija o nome no `colunas.json`.

Se alguma coluna não existir ou não for identificável, **não invente**. O script para e registra a lacuna em `saida/lacunas.md`. A lacuna é resultado, e não falha.

### 8. Reproduza os totais

```
python reproduza_disque100.py reproduzir dados
```

O script grava:

- `saida/resultado_conferencia.csv`: cada total, com as colunas `id;calculado;esperado;situacao`. A situação é `confere`, `diverge` ou `lacuna`.
- `saida/execucao.md`: versões do Python e das bibliotecas, SHA-256 e tamanho de cada arquivo, mapa de colunas, definições aplicadas, data e hora.
- `saida/lacunas.md`, se algum período ou coluna faltar.

Depois, digite os valores no conferidor da página **Agenda futura** do sítio, ou compare com o arquivo `data/relatorio-v2/disque100_reproducao.csv`.

## Definições

As definições estão declaradas no início do script, em `DEFINICOES`, antes de qualquer execução. Não se ajusta definição até o número bater. Quando há ambiguidade, o script calcula as variantes e reporta todas, com a principal indicada.

- **Linha.** Cada linha do arquivo combina denúncia, vítima, suspeito e violação.
- **Denúncia.** O identificador de denúncia (`hash`) contado uma vez no período. As contagens de semestres não se somam: conta-se a união do período.
- **Período.** A atribuição principal usa a data de cadastro. Os totais de linhas do arquivo usam o semestre do arquivo. A outra atribuição aparece como variante, com o sufixo `-data` ou `-arquivo`.
- **Ramo "Liberdade de religião ou crença".** A árvore de violações não tem categoria chamada intolerância religiosa. O recorte é esse ramo, com os subtipos de crença, de culto e não crença.
- **Vítima de religião judaísmo.** Denúncia com ao menos uma linha com religião da vítima igual a judaísmo.
- **c18.** A principal conta as denúncias com vítima judia sem nenhuma linha no ramo. A variante `-L` conta as que não têm linha que combine, na mesma linha, vítima judia e ramo.
- **Preenchimento da religião da vítima.** A principal (A) conta as denúncias com ao menos uma linha com religião preenchida, sobre as denúncias do período. A variante `-B` conta as linhas preenchidas sobre as linhas do período. Os rótulos tratados como ausência estão no mapa, em `religiao_ausente`: `NULL` e `NÃO SABE`, porque "não sabe" não informa a religião (critério adotado pelo Eixo em 05/10/2026, e usado nos totais esperados do kit). As variantes `-N` e `-BN` repetem o cálculo tratando como ausência só `NULL` e o vazio, e mostram quanto o resultado depende dessa escolha.
- **Ramo na base.** A coluna `violacao` é hierárquica, como em `LIBERDADE>DE RELIGIÃO ou CRENÇA>DE CULTO`. O ramo são os dois primeiros níveis, e o subtipo é o terceiro.
- **Comparação.** Inteiros por igualdade exata. Percentuais com duas casas decimais.

Linhas com `ctl` no `id` são controles do item E.11.9: denúncias com motivação "em razão da religião" no 1º e no 2º semestre de 2023 (502 e 140) e a data do último registro (31/08/2023).

## Como ler uma divergência

A divergência não refuta o achado por si só. Confira a versão dos arquivos, pelo SHA-256 e pelo tamanho, o filtro e a unidade. O MDHC pode republicar um arquivo com correções. Se a divergência persistir, registre-a e avise: é exatamente o que o kit existe para revelar.

## Testes

```
python -m pytest tests
```

Os testes usam dados sintéticos gerados no próprio teste. Nenhum dado real entra neles. Um dos testes falha se qualquer identificador aparecer na saída padrão, na saída de erro ou nos arquivos gerados.
