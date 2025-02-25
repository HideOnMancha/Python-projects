from tkinter import *
from tkinter import messagebox

class MinhaGUI:
 def __init__(self):
  # Criamos a janela principal
  self.janela_principal = Tk()
  
  # Criando o botão
  self.botao = Button(self.janela_principal, text='Clique aqui', command=self.hello_world)
  
  # Empacotando o botão na janela principal
  self.botao.pack()
  
  # Rodando
  mainloop()

  
 def hello_world(self):
  messagebox.showinfo('Adoro a Apostila Python Progressivo!')


gui = MinhaGUI()


# outro ex

from tkinter import *

dia = {1:'domingo',2:'segunda',3:'terça',4:'quarta',5:'quinta',6:'sexta',7:'sabado'}

i = len(dia)

menu = Tk()
menu.title("Exemplo - Função Exibir Botão")
menu.geometry("500x250+150+150")


def exbir_dia(valor):    
    print(valor)


def exbir_botao(i, valor):    
    botao = Button(menu, text=dia.get(i), command = lambda: exbir_dia(valor))    
    botao.grid()


while i > 0:

    valor = dia.get(i)

    exbir_botao(i, valor)

    i -= 1 

menu.mainloop()





t1 = pyautogui.confirm('Está correto? ',buttons=['Sim','Não'])

if t1 == 'Sim':
    running = True
else:
    quit()
