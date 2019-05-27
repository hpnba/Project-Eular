count=8
for a in range(2):
    for b in range(4):
        for c in range(10):
            for d in range(20):
                for e in range(40):
                    for f in range(100):
                        for g in range(200):
                            num=100*a+50*b+20*c+10*d+5*e+2*f+g
                            if num>200:
                                break
                            if num==200:
                                count+=1
                                
print(count)
