num=1
n=3
while True:
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        num+=1
    if num==10001:
        print(n)
        break
    n+=1
       
