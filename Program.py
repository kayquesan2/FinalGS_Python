import DatabaseConnection
import FunctionsDataBase

# Definição dos caminhos dos arquivos CSV
arquivo1 = "C:\\Users\\kayqu\\Documents\\ArquivosCSVPython\\1- producao-de-plastico-global.csv"
arquivo5 = "C:\\Users\\kayqu\\Documents\\ArquivosCSVPython\\5- poluicao-agua-cidades.csv"

# Estabelecer conexão com o banco de dados
conn, cursor = DatabaseConnection.DataBaseConnection()

# Chamada das funções para inserção de dados nos respectivos arquivos
FunctionsDataBase.inserir_dados_arquivo1(arquivo1, cursor)
FunctionsDataBase.inserir_dados_arquivo5(arquivo5, cursor)

while True:
    print('..:: Seja bem vindo ao nosso sistema de leitura de Tabelas ::..\n')
    print('Qual tabela você quer acessar?\n')
    print("1. Ler dados da tabela TB_PRODUCAO_PLASTICO")
    print("2. Ler dados da tabela TB_POLUICAO_AGUA_CIDADES")
    print("3. Sair")
    escolha = int(input('Digite o número da opção: '))

    if escolha == 1:
        FunctionsDataBase.ler_dados("TB_PRODUCAO_PLASTICO", cursor)
    elif escolha == 2:
        FunctionsDataBase.ler_dados("TB_POLUICAO_AGUA_CIDADES", cursor)
    elif escolha == 3:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Fechamento do cursor e da conexão
try:
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Erro ao fechar a conexão com o banco de dados: {e}")    