from ex2 import factorielle

n=int(input(entrer un nombre))
def sommeSerie(n):
    if(n<=0):
        return "le nombre doit être strictement positif"
    else:
        sum = 0
        for i in range(1,n+1):
            sum = 0
        for i in range(1,n+1):
            sum += factorielle(i-1)
        return sum
print(sommeSerie(n))
