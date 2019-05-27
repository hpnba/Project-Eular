n1=[0,3,3,5,4,4,3,5,5,4]#one,two,...,nine
m2=[3,6,6,8,8,7,7,9,8,8]#ten,eleven,twelve,..,nineteen
n2=[6,6,5,5,5,7,6,6]#twenty,thirty,forty,..,ninety
n3=10#hundred and
n4=8#thousand
count=0
for i in range(0,10):
    count+=n1[i]

for i in range(0,10):
    count+=m2[i]

for i in range(0,8):
    for j in range(0,10):
        count+=n2[i]+n1[j]

for p in range(1,10):
    for i in range(0,10):
        count+=n1[p]+n3+n1[i]
    count-=3
    for i in range(0,10):
        count+=n1[p]+n3+m2[i]
    for i in range(0,8):
        for j in range(0,10):
            count+=n1[p]+n3+n2[i]+n1[j]
count+=n4+3
print(count)
