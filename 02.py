a=1
b=1
tot=0
while b<4000000:
    if b%2==0:
        tot+=b
        print(b)
    c=a+b
    a=b
    b=c
print(tot)
