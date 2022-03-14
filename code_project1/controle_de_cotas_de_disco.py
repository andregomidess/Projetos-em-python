# Função que vai converter Bytes para MegaBytes, e retornar o total de memória utilizado
def bytes_to_mb(l):
    j = 0
    total = 0
    while j < len(l):
        b = round(int(l[j][1])/1048576, 2)
        total += b
        l[j][1] = b
        j += 1
    return total


# Função que vai trocar ponto por vírgula
def custom_to_string(num):
    return '{:.2f}'.format(num).replace('.', ',')


# Função que vai calcular o porcentual de uso de cada funcionário
def percentual(total, l):
    j = 0
    while j < len(l):
        perc = (l[j][1] * 100)/total
        l[j].append(round(perc, 2))
        j += 1


if __name__ == '__main__':
    cont = 0
    with open('usuarios.txt') as arq:   # abertura do arquivo contendo os dados
        lista = []
        for linha in arq:   # laço for para adicionar dados em uma lista
            dados = linha.split()
            lista.append(dados)
        utilizado = bytes_to_mb(lista)
        percentual(utilizado, lista)
    with open('relatorio.txt', 'w') as f:   # abertura e escrita no arquivo relatorio
        f.write('ACME Inc.           Uso do espaço em disco pelos usuários\n')
        f.write('-----------------------------------------------------------\n')
        f.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
        for i in range(0, len(lista)):
            f.write('{:<4} {:<14} {:>7} MB           {:>6}%\n'.format(i+1, lista[i][0], custom_to_string(lista[i][1]),
                                                                      custom_to_string(lista[i][2])))
            cont += 1
        f.write('\nEspaço total ocupado: {} MB\n'.format(utilizado))
        f.write('Espaço médio ocupado: {} MB'.format(custom_to_string(utilizado/cont)))
        