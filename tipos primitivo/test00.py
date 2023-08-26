n1=int(input('Digite um número ?'))
n2=int(input('Digite outro número ?'))
a=n1+n2
print('Número {} mais {} é igual a {}' .format(n1,n2,a))

n=input('Digite algo:')
print('O tipo primitivo desse valor',type(n))
print('É um número :',n.isnumeric())
print('É letra :',n.isalpha())
print('É alfa númerico:',n.isalnum())
