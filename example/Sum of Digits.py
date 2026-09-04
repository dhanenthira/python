a = int(input())
sum = 0

while a > 0:
    dig = a % 10
    sum += dig
    a //= 10

print(sum)