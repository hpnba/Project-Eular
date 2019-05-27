x=int(input('Enter your number here:-'))
m=0
for i in range(2,x+1):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        if(x%i==0):
            m=i
            x=x/i
            if x==1:
                print(m)
                break
#    print(i)

            
