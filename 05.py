num=11
n=[11,13,14,16,17,18,19,20]
while True:
    for i in range(0,8):
        if num%n[i]!=0:
            break
    else:
        print(num)
        break
    num+=1
