from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. Configuracoes iniciais
# ============================================================

CAMINHO_DADOS = Path("data") / "student-mat.csv"
PASTA_SAIDA = Path("outputs")

ROTULOS_STUDYTIME = {
    1: "1 - menos de 2 horas",
    2: "2 - de 2 a 5 horas",
    3: "3 - de 5 a 10 horas",
    4: "4 - mais de 10 horas",
}


# ============================================================
# 2. Carregamento dos dados
# ============================================================

def carregar_dados(caminho: Path) -> pd.DataFrame:
    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo nao encontrado: {caminho}\n"
            "Baixe a base Student Performance da UCI e coloque o arquivo "
            "student-mat.csv dentro da pasta data/."
        )

    return pd.read_csv(caminho, sep=";")


def mostrar_informacoes_iniciais(dados: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("INFORMACOES INICIAIS DO DATASET")
    print("=" * 60)

    print("\nPrimeiras linhas:")
    print(dados.head())

    print("\nInformacoes gerais:")
    dados.info()

    print("\nFormato do dataset:")
    print(f"Linhas: {dados.shape[0]}")
    print(f"Colunas: {dados.shape[1]}")


# ============================================================
# 3. Selecao e verificacao das variaveis
# ============================================================

def selecionar_variaveis(dados: pd.DataFrame) -> pd.DataFrame:
    colunas_necessarias = ["studytime", "G3"]
    colunas_ausentes = [coluna for coluna in colunas_necessarias if coluna not in dados.columns]

    if colunas_ausentes:
        raise ValueError(f"Colunas ausentes no dataset: {colunas_ausentes}")

    return dados[colunas_necessarias].copy()


def verificar_dados(dados: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("VERIFICACAO DAS VARIAVEIS SELECIONADAS")
    print("=" * 60)

    print("\nValores nulos por coluna:")
    print(dados.isnull().sum())

    print("\nTipos das colunas:")
    print(dados.dtypes)


def limpar_dados(dados: pd.DataFrame) -> pd.DataFrame:
    linhas_antes = len(dados)
    dados_limpos = dados.dropna().copy()
    linhas_depois = len(dados_limpos)

    print("\n" + "=" * 60)
    print("LIMPEZA BASICA")
    print("=" * 60)
    print(f"Linhas antes da limpeza: {linhas_antes}")
    print(f"Linhas depois da limpeza: {linhas_depois}")
    print(f"Linhas removidas: {linhas_antes - linhas_depois}")

    return dados_limpos


# ============================================================
# 4. Estatistica descritiva
# ============================================================

def calcular_estatisticas(dados: pd.DataFrame) -> pd.DataFrame:
    estatisticas = pd.DataFrame(
        {
            "media": dados.mean(numeric_only=True),
            "mediana": dados.median(numeric_only=True),
            "moda": dados.mode().iloc[0],
            "variancia": dados.var(numeric_only=True),
            "desvio_padrao": dados.std(numeric_only=True),
            "q1": dados.quantile(0.25, numeric_only=True),
            "q2": dados.quantile(0.50, numeric_only=True),
            "q3": dados.quantile(0.75, numeric_only=True),
            "amplitude": dados.apply(lambda coluna: np.ptp(coluna.to_numpy())),
        }
    )

    return estatisticas


def mostrar_estatisticas(estatisticas: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("ESTATISTICA DESCRITIVA")
    print("=" * 60)
    print(estatisticas.round(2))


# ============================================================
# 5. Visualizacoes iniciais
# ============================================================

def criar_visualizacoes(dados: pd.DataFrame) -> None:
    PASTA_SAIDA.mkdir(exist_ok=True)
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.histplot(dados["G3"], bins=10, kde=False, color="#3a7ca5")
    plt.title("Distribuicao das notas finais (G3)")
    plt.xlabel("Nota final (G3)")
    plt.ylabel("Quantidade de alunos")
    plt.tight_layout()
    plt.savefig(PASTA_SAIDA / "histograma_g3.png", dpi=150)
    plt.show()

    plt.figure(figsize=(7, 4))
    sns.boxplot(x=dados["G3"], color="#81b29a")
    plt.title("Boxplot das notas finais (G3)")
    plt.xlabel("Nota final (G3)")
    plt.tight_layout()
    plt.savefig(PASTA_SAIDA / "boxplot_g3.png", dpi=150)
    plt.show()

    contagem_studytime = (
        dados["studytime"]
        .map(ROTULOS_STUDYTIME)
        .value_counts()
        .reindex(ROTULOS_STUDYTIME.values(), fill_value=0)
    )

    plt.figure(figsize=(9, 5))
    sns.barplot(x=contagem_studytime.index, y=contagem_studytime.values, color="#f2cc8f")
    plt.title("Distribuicao do tempo semanal de estudo")
    plt.xlabel("Categoria de tempo de estudo")
    plt.ylabel("Quantidade de alunos")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(PASTA_SAIDA / "barras_studytime.png", dpi=150)
    plt.show()

    print("\nGraficos salvos na pasta outputs/:")
    print("- histograma_g3.png")
    print("- boxplot_g3.png")
    print("- barras_studytime.png")


# ============================================================
# 6. Interpretacoes automaticas
# ============================================================

def identificar_faixa_mais_comum(notas: pd.Series) -> str:
    faixas = pd.cut(
        notas,
        bins=[-0.1, 4, 9, 14, 20],
        labels=["0 a 4", "5 a 9", "10 a 14", "15 a 20"],
    )
    return str(faixas.value_counts().idxmax())


def mostrar_interpretacoes(dados: pd.DataFrame) -> None:
    media_g3 = dados["G3"].mean()
    faixa_mais_comum = identificar_faixa_mais_comum(dados["G3"])
    studytime_mais_frequente = dados["studytime"].mode().iloc[0]
    rotulo_studytime = ROTULOS_STUDYTIME.get(studytime_mais_frequente, "categoria desconhecida")

    print("\n" + "=" * 60)
    print("INTERPRETACOES AUTOMATICAS")
    print("=" * 60)
    print(f"Media das notas finais (G3): {media_g3:.2f}")
    print(f"Faixa de notas mais comum: {faixa_mais_comum}")
    print(f"Categoria de tempo de estudo mais frequente: {rotulo_studytime}")


# ============================================================
# 7. Execucao principal
# ============================================================

def main() -> None:
    dados = carregar_dados(CAMINHO_DADOS)
    mostrar_informacoes_iniciais(dados)

    dados_selecionados = selecionar_variaveis(dados)
    verificar_dados(dados_selecionados)

    dados_limpos = limpar_dados(dados_selecionados)
    estatisticas = calcular_estatisticas(dados_limpos)

    mostrar_estatisticas(estatisticas)
    criar_visualizacoes(dados_limpos)
    mostrar_interpretacoes(dados_limpos)


if __name__ == "__main__":
    main()
