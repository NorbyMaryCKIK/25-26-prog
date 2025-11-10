import random as r
#generaljon ki 10 db veletlen szamot!
#írassa ki a szamok osszege

osszeg= 0
for a in range(1,11,1):
    velszam = r.randint(1,9)
    osszeg += velszam
    print(velszam,end=" ")
print()
print(osszeg)

#hany darab paros veletle szamot generalt ki
#melyik a legnagyobbvéletlen szám