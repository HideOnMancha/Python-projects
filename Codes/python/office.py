import pyautogui as p
cancelar = exit
click = p.press

p.alert('instalação Office')


p.confirm('deseja continuar?')


a1 = p.confirm('enter', buttons=['Office 2014', 'Office 2019'])

p.prompt('Qual seu usuario?')

p.password('Digite sua senha:')

p.alert('Sucesso no Login ')

p.alert('Instalando {}'.format(a1))
