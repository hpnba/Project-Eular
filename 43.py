import time
st=time.time()

tot=0
number=0
num=[0 for a in range(10)]

res=[0 for a in range(10)]
def clone(x):
    copy=x[:]
    return copy

for a in range(1):
    num=[0,1,2,3,4,5,6,7,8,9]
    res[0]=num[a]
    num.remove(num[a])
    num1=clone(num)
    
    for b in range(1):
        num=clone(num1)
        res[1]=num[b]
        num.remove(num[b])
        num2=clone(num)

        for c in range(1):
            num=clone(num2)
            res[2]=num[c]
            num.remove(num[c])
            num3=clone(num)


            for d in range(1):
                num=clone(num3)
                res[3]=num[d]
                num.remove(num[d])
                num4=clone(num)

                if (res[2]*100+res[3]*10+res[4])%2==0:
                    

                    for e in range(1):
                        num=clone(num4)
                        res[4]=num[e]
                        num.remove(num[e])
                        num5=clone(num)

                        if (res[3]*100+res[4]*10+res[5])%3==0:
                            

                            for f in range(1):
                                num=clone(num5)
                                res[5]=num[f]
                                num.remove(num[f])
                                num6=clone(num)

                                if (res[4]*100+res[5]*10+res[6])%5==0:
                                    

                                    for g in range(1):
                                        num=clone(num6)
                                        res[6]=num[g]
                                        num.remove(num[g])
                                        num7=clone(num)

                                        if (res[5]*100+res[6]*10+res[7])%7==0:
                                            

                                            for h in range(1):
                                                num=clone(num7)
                                                res[7]=num[h]
                                                num.remove(num[h])
                                                num8=clone(num)

                                                if (res[6]*100+res[7]*10+res[8])%11==0:
                                                    

                                                    for i in range(1):
                                                        num=clone(num8)
                                                        res[8]=num[i]

                                                        if (res[7]*100+res[8]*10+res[9])%13==0:
                                                            
                                                            num.remove(num[i])
                                                            res[9]=num[0]
                                                            if (res[8]*100+res[9]*10+res[10])%17==0:
                                                                for i in range(10):
                                                                    number+=res[i]*10**(9-i)
                                                                    tot+=number
                                                                    print(number)
                    
print(tot)

et=time.time()
print(et-st)
