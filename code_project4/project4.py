from words import words
import random
import os
from time import sleep

# limpa tela
clear = lambda: os.system('clear')


def imprime_boneco(tentativas):
    if tentativas == 7:
        print("""\033[1;96m
              _______
                    |
                     
                   
                
                   
                            \033[m""")
    elif tentativas == 6:
        print("""\033[1;96m
              _______
                    |
                    O  
                   
                
                   
                            \033[m""")
        
    elif tentativas == 5:
        print("""\033[1;96m
              _______
                    |
                    O  
                    |
                    
                   
                            \033[m""")
    elif tentativas == 4:
        print("""\033[1;96m
              _______
                    |
                    O  
                    |
                    |
                   
                            \033[m""")
    elif tentativas == 3:
        print("""\033[1;96m
              _______
                    |
                    O  
                   /|
                    |
                   
                            \033[m""")
    elif tentativas == 2:
        print("""\033[1;96m
              _______
                    |
                    O  
                   /|\\
                    |
                   
                            \033[m""")
        
    elif tentativas == 1:
        print("""\033[1;96m
              _______
                    |
                    O  
                   /|\\
                    |
                   / 
                            \033[m""")
        
    else:
        print("""\033[1;96m
              _______
                    |
                    O  
                   /|\\
                    |
                   / \\
                            \033[m""")    
                               
            
    
    
def palavras_aleatorias(words):
    palavra = random.choice(words)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(words)
    return palavra.upper()

def menu():
    palavra = palavras_aleatorias(words)
    tentativas = 0
    print('=-'*18)
    print('          |JOGO DA FORCA|')
    imprime_boneco(tentativas)
    print('Digite [1] para jogar')
    print('Digite [2] para sair')
    op = int(input('Digite sua opção: '))
    if op == 1:
        clear()
        jogo_forca(palavra)
    else:
        return
    print('=-'*18)
    
    
def jogo_forca(palavra):
    print(palavra)
    tam_word = len(palavra)
    tentativas = 7
    simbolos = list()
    letras_palavra = list(palavra)
    letras_digitadas = []
    for _ in range(tam_word):
        simbolos.append('\033[1;91m__\033[m')
    t = ' '.join(simbolos)      
    while tentativas > 0:
        if simbolos == letras_palavra:
            break 
        print(f'A PALAVRA TEM {tam_word} LETRAS!')
        print(f'NÚMERO DE TENTATIVAS: {tentativas}')
        lixo = ' '.join(letras_digitadas)
        print(f'Letras digitadas: {lixo}')
        print(t)
        imprime_boneco(tentativas)
        letra = input('Digite uma letra: ').upper()
        while len(letra) > 1:
            print('\033[1;31mDIGITE APENAS UMA LETRA!\033[m')
            letra = input('Digite uma letra: ').upper()               
        while letra in letras_digitadas:
            print('\033[1;31mLETRA JÁ DIGITADA!\033[m')
            letra = input('Digite outra letra: ').upper()
        letras_digitadas.append(letra)
        if letra in palavra:    # fazer função checa letra
            for i in range(tam_word):
                if letra == letras_palavra[i]:
                    simbolos[i] = letras_palavra[i]
                    t = ' '.join(simbolos)
                    print(t)       
        else:
            tentativas -= 1
        clear()
        
    if simbolos == letras_palavra:
        print(t)
        imprime_boneco(tentativas)
        print('\033[1;92mPARABÉNS VOCÊ GANHOU!\033[m\n')
    
    else:
        print(t)
        imprime_boneco(tentativas)
        print('\033[1;31mQUE PENA, VOCÊ PERDEU!\033[m\n')
        print(f'A palavra era: \033[1;96m{palavra}\033[m')
    
    escolha = None
    while escolha != 'S' or escolha != 'N':
        print('\033[1;33mDIGITE ''N'' OU ''S''\033[m')   
        escolha = input(str('Você deseja jogar novamente?[S/N] ')).upper()
        if escolha == 'S':
            clear()
            menu()
        else:
            break
    return               
        
                           
                    
            
            
            
if __name__ == '__main__':
    menu()
            