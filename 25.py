y=2
a=1
b=1
d=10**999
while True:
    c=a+b
    y+=1
    if c>d:
        print(y)
        break
    a=b
    b=c
