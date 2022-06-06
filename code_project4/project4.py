from words import words
import random
import os
from time import sleep

# limpa tela
clear = lambda: os.system('clear')


def imprime_boneco(tentativas):
    if tentativas == 7:
        print("""\033[1;96m
                    O  
                   /|\\
                    |
                   / \\
                            \033[m""")
    elif tentativas == 6:
        print("""\033[1;96m
                    O  
                   /|\\
                    |
                   / 
                            \033[m""")
        
    elif tentativas == 5:
        print("""\033[1;96m
                    O  
                   /|\\
                    |

                            \033[m""")
    elif tentativas == 4:
        print("""\033[1;96m
                    O  
                   /|\\
                    

                            \033[m""")
    elif tentativas == 3:
        print("""\033[1;96m
                    O  
                   /|
                    

                            \033[m""") 
    elif tentativas == 2:
        print("""\033[1;96m
                    O  
                    |
                    

                            \033[m""")
        
    else:
        print("""\033[1;96m
                    O  
                   
                    

                            \033[m""")
                               
            
    
    
def palavras_aleatorias(words):
    palavra = random.choice(words)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(words)
    return palavra.upper()

def menu():
    tentativas = 7
    print('=-'*18)
    print('          |JOGO DA FORCA|')
    imprime_boneco(tentativas)
    print('Digite [1] para jogar')
    print('Digite [2] para sair')
    op = input('Digite sua opção: ')
    if op == 1:
        pass
    else:
        pass
    print('=-'*18)
    
    
def jogo_forca(palavra):
    #print(palavra)
    acertos = 0
    tam_word = len(palavra)
    tentativas = 7
    simbolos = list()
    letras = list(palavra)
    print(f'A PALAVRA TEM {tam_word} LETRAS!')
    print(f'NÚMERO DE TENTATIVAS: {tentativas}')
    sleep(1)
    #print('     \033[1;91m__  \033[m'*tam_word)
    for _ in range(tam_word):
        simbolos.append('\033[1;91m__\033[m')
    t = ' '.join(simbolos)      
    while tentativas > 0:
        print(t)
        imprime_boneco(tentativas)
        letra = input('Digite uma letra: ').upper()               
        letras.append(letra)
        if letra in palavra:    # fazer função checa letra
            for i in range(tam_word):
                if letra == letras[i]:
                    simbolos[i] = letras[i]
                    t = ' '.join(simbolos)
                    print(t)
                    acertos += 1
        else:
            tentativas -= 1
        clear()                   
                    
            
            
            
if __name__ == '__main__':
    palavra = palavras_aleatorias(words)
    menu()
    clear()
    jogo_forca(palavra)
            