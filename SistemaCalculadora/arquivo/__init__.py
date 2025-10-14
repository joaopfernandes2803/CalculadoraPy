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
    """Limpa o histórico atual da memória."""
    lista.clear()
    print('Histórico limpo!')




