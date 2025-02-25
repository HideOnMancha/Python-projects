import pyautogui as p
import time

m=p.prompt('Qual OS?')
print(p.alert('Sua OS:{}'.format(m)))


n=p.prompt('Qual Empresa?')
print(p.alert('Empresa:{}'.format(n)))

e=p.prompt('Qual Cliente?')
print(p.alert('Cliente:{}'.format(e)))

a=p.prompt('Qual Endereço?')
print(p.alert('Endereço:{}'.format(a)))

b=p.prompt('Qual Serviço?')
print(p.alert('Serviço:{}'.format(b)))

d=p.prompt('Qual Previa?')
print(p.alert('Previa:{}'.format(d)))




#quit with 
p.click=exit
p.click(1)


msg='OS:{}','Empresa:{}','Cliente:{}','Endereço:{}','Serviço:{}','Previa:{}'.format(m,n,e,a,b,d)

print(p.alert(msg))



print(p.alert('Previa {}'.format(d)))

print(p.alert('Serviço {}'.format(b)))

print(p.alert('Endereço {}'.format(a)))

print(p.alert('Cliente {}'.format(e)))

print(p.alert('Empresa {}'.format(n)))

print(p.alert('sua os {}'.format(m)))


