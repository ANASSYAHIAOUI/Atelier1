def puissance(X,n):
    r= 1
    for i in range(n):
        r*=X
    return r 
print(puissance(3,2))