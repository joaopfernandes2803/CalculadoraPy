import os

def salvar_historico(lista, nome_arquivo='lista.txt'):
    """Salva o histórico em um arquivo de texto."""
    with open(nome_arquivo, 'w') as arquivo:
        for valor in lista:
            arquivo.write(str(valor) + '\n')
    print('Histórico salvo em', nome_arquivo)

def ler_historico(nome_arquivo='lista.txt'):
    """Lê e exibe o conteúdo do histórico salvo."""
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        print('Histórico do arquivo:')
        print(conteudo)
    except FileNotFoundError:
        print('Nenhum histórico salvo ainda.')

def limpar_historico(lista):
    lista.clear()
    print('Histórico em memória limpo!')

def limpar_arquivo(nome_arquivo='lista.txt'):
    """Apaga o arquivo de histórico se ele existir."""
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print(f'Arquivo {nome_arquivo} apagado com sucesso!')
    else:
        print(f'Nenhum arquivo {nome_arquivo} encontrado.')

def limpar_tudo(lista, nome_arquivo='lista.txt'):
    """Limpa tanto o histórico em memória quanto o arquivo físico."""
    limpar_historico(lista)
    limpar_arquivo(nome_arquivo)
    print('Histórico  limpo!')


