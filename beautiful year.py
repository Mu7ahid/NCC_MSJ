n=int(input())
n+=1
b=str(n)
while len(b)!=(len(set(b))):
    b=int(b)+1
    b=str(b)
print(b)    
   
    
    
    