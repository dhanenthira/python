def p (text):
    rev=text[::-1]
    if text==rev:
        print("palindrom")
    else:
        print("not palindrom")
p(input("enter the words :"))
    
def rev():
    n=input("enter the word of Reverse:")
    print(n[::-1])
rev()