import pyautogui
from time import sleep
import sys




m = pyautogui.prompt('Qual numero O.S?')
if m is None:  
    pyautogui.alert('Operação cancelada.')
    sys.exit()

n = pyautogui.prompt('Qual a empresa?')
if n is None:
    pyautogui.alert('Operação cancelada.')
    sys.exit()

e = pyautogui.prompt('Qual o cliente?')
if e is None:
    pyautogui.alert('Operação cancelada.')
    sys.exit()

a = pyautogui.prompt('Qual o endereço?')
if a is None:
    pyautogui.alert('Operação cancelada.')
    sys.exit()

b = pyautogui.prompt('Qual o serviço?')
if b is None:
    pyautogui.alert('Operação cancelada.')
    sys.exit()

d = pyautogui.prompt('Qual a previa?')
if d is None:
    pyautogui.alert('Operação cancelada.')
    sys.exit()

msg = """OS:{}
    Empresa:{}
    Cliente:{} 
    Endereco:{} 
    Servico:{} 
    Previa: {}""".format(m, n, e, a, b, d)

if msg:
    pyautogui.alert(msg)

proseguir = pyautogui.confirm('Deseja prosseguir com o envio?', buttons=['Continuar', 'Cancelar'])

if proseguir == 'Cancelar':
    pyautogui.alert('Operação cancelada.') 
    sys.exit()


confirmacao = pyautogui.confirm('Enviando Serviço', buttons=['Enviar','Cancelar'])  

if confirmacao == 'Cancelar':
    sys.exit()
  
sleep(5) 
pyautogui.confirm.buttons=pyautogui.write(msg)

pyautogui.press('enter')

 
pyautogui.alert('Serviço Enviado!')
