x=int(input('Enter your number here:-'))
num=1
tot=0
for i in range(2,x+1):
    num*=i
while num>9:
    z=num%10
    tot+=z
    num=num//10
tot+=num
print(tot)
    
    

