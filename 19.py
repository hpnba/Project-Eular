d=31*7+30*4+29
d=d%7

d1=[31,28,31,30,31,30,31,31,30,31,30,31]
d2=[31,29,31,30,31,30,31,31,30,31,30,31]

num=0
day=d
if d==0:
    num=1
sun=0
for i in range(1901,2001):
    for j in range(0,12):
        if i%4==0 and i%400!=0:
            day+=d2[j]
        else:
            day+=d1[j]
        n=(day)%7
        if n==0:
            num+=1
if day%7==0:
    num-=1
print(num)


    
