n=int(input())
for i in range(n):
    b=input()
    if len(b)>10:
        print(f"{b[0]}{len(b[1:-1])}{b[-1]}")
    else:
        print(b)