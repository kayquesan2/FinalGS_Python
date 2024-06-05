import DatabaseConnection  # Importa o módulo Database para usar a função de conexão com o Banco de Dados
import csv

# Função para inserir dados do arquivo1 na tabela TB_PRODUCAO_PLASTICO
def inserir_dados_arquivo1(caminho_arquivo, cursor):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            next(file)  # Ignora o cabeçalho
            for line in file:
                Entidade, Ano, Producao = line.strip().split(',')
                Ano = int(Ano)
                Producao = float(Producao)
                cursor.execute("INSERT INTO TB_PRODUCAO_PLASTICO (ENTIDADE, ANO, PRODUCAO) VALUES (:1, :2, :3)", (Entidade, Ano, Producao))
        cursor.connection.commit()
    except Exception as e:
         print(f"Erro ao inserir dados do arquivo {caminho_arquivo}: {e}")

# Função para inserir dados do arquivo5 na tabela TB_POLUICAO_AGUA_CIDADES
def inserir_dados_arquivo5(caminho_arquivo, cursor):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Ignora o cabeçalho
            for row in reader:
                cursor.execute("INSERT INTO TB_POLUICAO_AGUA_CIDADES (CIDADE, REGIAO, ENTIDADE, QUALIDADE_AR, POLUICAO) VALUES (:1, :2, :3, :4, :5)", row)
        cursor.connection.commit()
    except Exception as e:
        print(f"Erro ao inserir dados do arquivo {caminho_arquivo}: {e}")

# Função para ler todos os dados de qualquer tabela
def ler_dados(tabela, cursor):
    try:
        cursor.execute(f"SELECT * FROM {tabela}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Erro ao ler dados da tabela {tabela}: {e}")

# Função para ler uma linha específica de qualquer tabela
def ler_linha_tabela(tabela, id, cursor):
    try:
        cursor.execute(f"SELECT * FROM {tabela} WHERE ID = {id}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Erro ao ler dados da tabela {tabela}: {e}")