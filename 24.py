from time import time
st=time()

n=0
t=0
number=0
num=[0 for a in range(10)]

res=[0 for a in range(10)]
def clone(x):
    copy=x[:]
    return copy

for a in range(10):
    num=[0,1,2,3,4,5,6,7,8,9]
    res[0]=num[a]
    num.remove(num[a])
    num1=clone(num)
    
    for b in range(9):
        num=clone(num1)
        res[1]=num[b]
        num.remove(num[b])
        num2=clone(num)

        for c in range(8):
            num=clone(num2)
            res[2]=num[c]
            num.remove(num[c])
            num3=clone(num)

            for d in range(7):
                num=clone(num3)
                res[3]=num[d]
                num.remove(num[d])
                num4=clone(num)

                for e in range(6):
                    num=clone(num4)
                    res[4]=num[e]
                    num.remove(num[e])
                    num5=clone(num)

                    for f in range(5):
                        num=clone(num5)
                        res[5]=num[f]
                        num.remove(num[f])
                        num6=clone(num)

                        for g in range(4):
                            num=clone(num6)
                            res[6]=num[g]
                            num.remove(num[g])
                            num7=clone(num)

                            for h in range(3):
                                num=clone(num7)
                                res[7]=num[h]
                                num.remove(num[h])
                                num8=clone(num)

                                for i in range(2):
                                    num=clone(num8)
                                    res[8]=num[i]
                                    num.remove(num[i])
                                    res[9]=num[0]
                                    n+=1
                                    if n==1000000:
                                        t=1
                                        break
                                if t==1:
                                    break
                            if t==1:
                                break
                        if t==1:
                            break
                    if t==1:
                        break
                if t==1:
                    break
            if t==1:
                break
        if t==1:
            break
    if t==1:
        break

for i in range(10):
    number+=res[i]*10**(9-i)


print(number)
print(time()-st)
        
        


