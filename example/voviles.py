def vovels(txt):
    count=0
    for i in txt:
        if i  in "aeiou":
            count+=1
            
        return count
print(vovels(input()))