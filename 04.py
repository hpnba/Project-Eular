t=0
for a in range(9,0,-1):
    for b in range(9,-1,-1):
        for c in range(9,-1,-1):
            num=100000*a+10000*b+1000*c+100*c+10*b+a
            for i in range(999,0,-1):
                if num%i==0:
                    n=num/i
                    if n<1000:
                        print(num)
                        t=1
                        break
            if t==1:
                break
        if t==1:
            break
    if t==1:
        break
    
    
