t=0
for b in range(1,1000):
    for a in range(1,b):
        c=(a**2+b**2)**(1/2)
        print(a,b)
        if (a+b+c==1000):
            print(a*b*c)
            t=1
            break
    if t==1:
        break
