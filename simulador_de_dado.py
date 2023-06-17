# Simulador de Dado
# Simular o uso de um dado gerando um valor aleatório de 1 a 6
import random
import PySimpleGUI as sg




class simulador_dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #layout interface
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]
       

    def Iniciar(self):
#criar uma janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
 #ler os dados na tela
        self.eventos, self.valores = self.janela.Read()
#fazer algo com os valores
        

        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.valor_do_dado()
                print(self.valor_do_dado)
            elif self.eventos =='não' or self.eventos == 'n':
                print('Obrigado por sua participação')
            else:
                print('favor digitar sim ou não')
        except:
            print('ocorreu um erro ao receber sua resposta')


    def valor_do_dado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = simulador_dado()
simulador.Iniciar()