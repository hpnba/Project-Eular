mx=0
cm=0
t=0

for a in range(1,1000000):
    count=1
    x=a
    while x>1:
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
        count+=1
    if count>cm:
        cm=count
        mx=a
    
    
print(mx)
