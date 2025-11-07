import random as r
sz = "kalapács"
n = len(sz)

for db in range(0,5,1):
    szam =  r.randint(0,n-1)
    print(sz[szam],end=" ")


 