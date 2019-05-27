x=int(input('Enter your last number here:-'))
tot=0
for i in range(1,x):
    if (i%3==0 or i%5==0):
        tot=i
print(tot)
