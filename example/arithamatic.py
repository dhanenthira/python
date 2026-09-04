def cal(a,b,op):
    if op=="+":
        return a + b
    if op=="-":
        return a - b
    if op=="*":
        return a * b
    if op=="/":
        return a/b
    else:
        return "Invalid operation"
a=int(input("enter the a :"))
b=int(input("enter the b :"))
op=input("enter the operations")
    
print(cal( a,b,op))
    