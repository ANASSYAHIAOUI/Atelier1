x=int(input('Entrer un nombre: '))
n=int(input('Entrer une puissance : '))

def puissance(X,n):
    r= 1
    for i in range(n):
        r*=X
    return r 
print(puissance(x,n))
