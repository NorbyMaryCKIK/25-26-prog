import random as r
sz = "kalapács"
n = len(sz)

for db in range(0,5,1):
    szam =  r.randint(0,n-1)
    print(sz[szam],end=" ")
print()


ujszoveg = ""

for index in range(-1, -n-1, -1):
      ujszoveg += sz[index]
print(ujszoveg)






 