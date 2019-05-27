x=int(input('Enter your number here:-'))
tot=0
num=2**x
while num>9:
    z=num%10
    tot+=z
    num=num//10
tot+=num
print(tot)
    
    

