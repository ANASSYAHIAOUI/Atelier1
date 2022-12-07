n=int(input(entrer un nombre))
def sumOfNumbers(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
print(sumOfNumbers(n))
