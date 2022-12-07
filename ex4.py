
n=int(input(entrer un nombre))
def DecimalToBinary(n):
    if n == 0:
        return 0
    else:
        re = ""
        while(n>0):
            r=n%2
            re = str(r)+re
            n//= 2
        return int(re)
print(DecimalToBinary(n))
