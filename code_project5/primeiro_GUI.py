from tkinter import *



def limpa_tela():
    caixa_montante.delete(0, END)
    caixa_porcentagem.delete(0, END)
    caixa_tempo.delete(0, END)
    caixa_juros.delete(0, END)

def calcula_juros():
    montante = int(caixa_montante.get())
    porcentagem = float(caixa_porcentagem.get())
    tempo = int(caixa_tempo.get())
    JurosCompostos =  montante*(1+(porcentagem/100))**tempo
    caixa_juros.insert(10, JurosCompostos)

if __name__ == '__main__':
    
    janela = Tk()
    janela.title('Calculadora de juros compostos')
    montante_principal = Label(janela, text='Montante principal:', background='red').grid(column=0, row=0, padx=5, pady=10)
    porcentagem = Label(janela, text='porcentagem(%):', background='red').grid(column=0, row=1, padx=5, pady=10)
    tempo = Label(janela, text='Tempo(anos):', background='red').grid(column=0, row=2, padx=5, pady=10)
    caixa_montante = Entry(janela).grid(column=1, row=0)
    caixa_porcentagem = Entry(janela).grid(column=1, row=1)
    caixa_tempo = Entry(janela).grid(column=1, row=2)
    botao_enviar = Button(janela, text='Enviar', background= 'red', command=calcula_juros).grid(column=1, row=3)
    juros_compostos = Label(janela, text='Juros compostos:', background='red').grid(column=0, row=4, padx=5, pady=10)
    caixa_juros = Entry(janela).grid(column=1, row=4)
    limpa_telaa = Button(janela, text='Limpar', background='red', command=limpa_tela).grid(column=1, row=5)
    

    janela.mainloop()