n=input()
b=0
c=0
d=n.lower()
e=n.upper()
for i in n:
    if i.isupper():
        b+=1
for i in n:
    if i.islower():
        c+=1
if c>=b:
    print(d)
else:
    print(e)    