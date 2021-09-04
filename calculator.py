def cong(a,b):
    return a+b

def tru(a,b):
    return a-b

def nhan(a,b):
    return a*b

def chia(a,b):
    return a/b

n1 = int(input('input number A: '))
option = input("Enter the operation +, -, *, / :")
n2 = int(input('input number B: '))

if option == '+':
    print(n1 ,option, n2,'=', cong(n1,n2))
elif option == '-':
    print(n1 ,option, n2,'=', tru(n1,n2))
elif option == '*':
    print(n1 ,option, n2,'=', nhan(n1,n2))
elif option == '/':
    print(n1 ,option, n2,'=', chia(n1,n2))
else:
    print('Invalid input!!!')