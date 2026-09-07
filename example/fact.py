def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

n = int(input())
print(factorial(n))



def ord():
    n=int(input())
    if n%2==0:
        print("odd num")
    else:
        print("even num")
ord()