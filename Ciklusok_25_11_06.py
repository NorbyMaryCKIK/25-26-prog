"""
Ciklusok- ismétlés - Loop

számlálós - For ciklus
Végig megy a megadott elemeken vagy intervallumon!

for elem in range(mettol, meddig, hányasával):
    Ismétlendő folyamat

    for karakter


Tesztelős -While

"""
#HF


for elem in range(1,11,1):
    print(elem,end=" ")

    print("")

for elem in range(0,19,2):
    print(elem)


szoveg = "kalapács"
   
for karakter in szoveg:
        print(karakter, end=",")
print()
    
for index in range(0,len(szoveg)-1,1):
        print(szoveg[index]+",",end="")
print(szoveg[-1])

print("")


for i in range(10,0,-1):
        print(i,end=" ")
print()



for i in range(30,50):
        if(i%4==0):
            print(i)

for index in range(len(szoveg)-1,-1,-1):
    print(szoveg[index],end="")
print()

n = len(szoveg)
for index in range(0, len(szoveg),1):
    
    print(szoveg[n-index-1],end="")








        
   
    
