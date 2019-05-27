z=int(input("Enter your number here:-"))
w=z+1
sq=[[0 for x in range(w)]for y in range(w)]
for i in range(w):
    sq[i][0]=1
    sq[0][i]=1
for i in range(1,w):
    for j in range(1,w):
        sq[i][j]=sq[i-1][j]+sq[i][j-1]
print(sq[z][z])
