n1=int(input('Digite um número ?'))
n2=int(input('Digite outro número ?'))
a=n1+n2
s=n1-n2
m=n1*n2
d=n1/n2
p=n1**n2
di=n1//n2
rd=n1%n2
print('A soma {}, a subtração {}, A multiplicação {} e a Divisão {:.3f}'.format(a,s,m,d), end ='')
print(' potência {}, divisão inteira {}, resto da divisão {}'.format(p,di,rd))