def n_ext(d, num):
    # lista dezenas
    l = ['', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa',]
    # lista centenas
    l2 = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos',
          'oitocentos', 'novecentos']
    decimal = []    # lista que vai conter o número digitado separado em unidade, dezena e centena
    dezenas = {}
    centenas = {}
    for i in num:   # laço for para separar o número digitado em digitos únicos
        decimal.append(int(i))
    if 0 < int(num) < 20:   # para números abaixo de vinte é so escrever o nome que ja tem no dicionario d
        print(d[int(num)])
    if 20 <= int(num) < 100:    # se estiver entre 20 e 100, vais passar as dezenas para o dicionário dezenas
        # laço for para criar um dicionário com as dezenas em extenso
        for x in range(0, 10):
            dezenas[x] = l[x]
        if decimal[1] != 0:
            print('{} e {}'.format(dezenas[decimal[0]], d[decimal[1]]))
        else:
            print('{}'.format(dezenas[decimal[0]]))
    if 100 < int(num) < 1000:
        # laço for para criar um dicionário com as dezenas em extenso
        for x in range(0, 10):
            dezenas[x] = l[x]
            # laço for para criar um dicionário com as centenas em extenso
        for j in range(0, 10):
            centenas[j] = l2[j]
        if decimal[1] != 0:
            print('{} e {} {}'.format(centenas[decimal[0]], dezenas[decimal[1]], d[decimal[2]]))
        else:
            print('{} e {}'.format(centenas[decimal[0]], d[decimal[2]]))
    elif int(num) == 100:
        print('cem')
    elif int(num) == 0:
        print('zero')

def new_func(decimal):
    return decimal[2] != 0


if __name__ == '__main__':
    d1 = {0: '', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito',
          9: 'nove', 10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis',
          17: 'dezessete', 18: 'dezoito', 19: 'dezenove'}
    n = str(input('Digite um número: '))
    n_ext(d1, n)
