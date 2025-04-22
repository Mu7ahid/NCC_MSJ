k,n,w=map(int,input().split())
sum=0
for i in range(w):
    sum+=w*k
    w-=1
if sum > n:
    print(sum-n)
else:
    print(0)