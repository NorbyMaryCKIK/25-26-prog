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

def ciklusokfor1():
    for elem in range(1,11,1):
        print(elem,end=" ")

    print("")

def ciklusokfor2():
    for elem in range(0,19,2):
        print(elem)

def ciklusokfor3():
    szoveg = "kalapács"
    print(szoveg)

    for karakter in szoveg[:-1]:
        print(karakter, end=",")
    print(szoveg[-1])

    






def main():
    ciklusokfor1()
    # ciklusokfor2()
    ciklusokfor3()
    
main()