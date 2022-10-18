#simulador de dado
#simular o uso de dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self) -> None:
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
        
        #layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]    
        
    def Iniciar(self) :
        
         #criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        #ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        
        try:
            if self.eventos == 'sim':
                self.GerarValorDoDado()
            elif self.eventos == 'não':
                print('Então vai dormir !')
            else:
                print('Valor inválido!')
        except:
            print('Ocorreu algum erro !')
            
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        
simulador = SimuladorDeDado()
simulador.Iniciar()