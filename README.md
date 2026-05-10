# Analise Inicial de Desempenho Academico

Projeto em Python para a primeira parte de uma analise exploratoria de dados sobre desempenho academico.

O foco e somente:

- preparacao dos dados;
- estatistica descritiva;
- visualizacoes iniciais.

Este projeto usa a base **Student Performance** da UCI Machine Learning Repository, com o arquivo `student-mat.csv`.

Fonte da base:

https://archive.ics.uci.edu/dataset/320/student+performance

## O que este projeto analisa

Variaveis usadas:

- `studytime`: tempo semanal de estudo;
- `G3`: nota final do aluno em Matematica.

O script nao faz correlacao, regressao linear, R2, analise preditiva ou grafico de dispersao.

## Estrutura

```text
.
├── analise_student.py
├── requirements.txt
├── data/
│   └── student-mat.csv
└── outputs/
```

## Como preparar a base

O arquivo `data/student-mat.csv` ja foi baixado da UCI para este projeto.

Caso precise baixar novamente:

1. Acesse:

```text
https://archive.ics.uci.edu/dataset/320/student+performance
```

2. Baixe o arquivo da base.
3. Extraia o arquivo `student-mat.csv`.
4. Coloque o arquivo neste caminho:

```text
data/student-mat.csv
```

## Como instalar as dependencias

```bash
pip install -r requirements.txt
```

## Como executar

```bash
python analise_student.py
```

## Saidas esperadas

No terminal, o script mostra:

- primeiras linhas do dataset;
- informacoes gerais;
- formato do dataset;
- valores nulos;
- tipos das colunas;
- estatistica descritiva;
- interpretacoes automaticas.

Na pasta `outputs/`, o script salva:

- `histograma_g3.png`;
- `boxplot_g3.png`;
- `barras_studytime.png`.

## Observacao

O projeto foi organizado para ser simples, limpo e apropriado para um trabalho de Probabilidade e Estatistica de faculdade.
