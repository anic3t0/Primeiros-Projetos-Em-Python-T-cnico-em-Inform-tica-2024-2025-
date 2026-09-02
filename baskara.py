import math
a=float(input("digite o valor de A:"))
b=float(input("digite o valor de B:")
delta=b**2-4*a*c
print(delta)
if delta>0:
 x1=(-b+(sqtr(delta))/(2*a))
x2=(-b-(sqtr(delta))/(2*a))
print(x1,x2)
print('possui duas raizes')
if delta==0:
  x1=(-b+(sqtr(delta))/(2*a))
  x2=(-b-(sqtr(delta))/(2*a))
  print(x1,x2)
  print('Já que o delta é igual a zero, as raizes são iguais')

if delta<0:
  print('Já que delta e menor que zero, não existe raízes')
