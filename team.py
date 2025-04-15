n=int(input())
count=0
for i in range(n):
   o,p,q=map(int,input().split())
   if o+p+q>=2:
       count+=1
print(count)       