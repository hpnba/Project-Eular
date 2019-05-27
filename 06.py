n1=n2=0
for i in range(1,101):
    n1+=i*i
    n2+=i
n2=n2**2
dif=n2-n1
print(dif)
