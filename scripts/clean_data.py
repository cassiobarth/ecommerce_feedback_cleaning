import pandas as pd
import numpy as np

# Definindo o caminho dos arquivos
INPUT_FILE = '../data/raw_feedback.csv'
OUTPUT_FILE = '../data/clean_data.csv'

def clean_data(df):
    """
    Realiza a limpeza do DataFrame.
    
    Args:
        df (pd.DataFrame): O DataFrame a ser limpo.
        
    Returns:
        pd.DataFrame: O DataFrame limpo.
    """
    print("Iniciando a limpeza dos dados...")

    # 1. Tratando valores ausentes
    # Preenche valores ausentes na coluna 'nome_cliente' com 'Desconhecido'
    df['nome_cliente'].fillna('Desconhecido', inplace=True)
    
    # Preenche valores ausentes na coluna 'valor_total' com a mediana
    median_valor_total = df['valor_total'].median()
    df['valor_total'].fillna(median_valor_total, inplace=True)
    
    # 2. Padronizando a coluna 'status'
    # Converte todos os valores para minúsculas
    df['status'] = df['status'].str.lower()
    
    # 3. Tratando a coluna 'regiao'
    # Remove espaços em branco no início e fim
    df['regiao'] = df['regiao'].str.strip()
    
    # 4. Convertendo tipos de dados
    # Garante que 'data_venda' seja do tipo datetime
    df['data_venda'] = pd.to_datetime(df['data_venda'])
    
    print("Limpeza concluída com sucesso.")
    return df

def main():
    """
    Função principal para executar o fluxo de trabalho de limpeza de dados.
    """
    try:
        # Lendo o arquivo CSV com um parâmetro para pular linhas com erro
        df = pd.read_csv(INPUT_FILE, on_bad_lines='skip')
        
        # Chamando a função de limpeza
        df_cleaned = clean_data(df)
        
        # Salvando o DataFrame limpo em um novo arquivo
        df_cleaned.to_csv(OUTPUT_FILE, index=False)
        print(f"Dados limpos salvos em: {OUTPUT_FILE}")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo {INPUT_FILE} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()