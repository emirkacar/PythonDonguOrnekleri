metin=input("Yazdirilacak metini giriniz.")
adet=int(input("Metini kac kere yazdirmak istiyorsunuz?"))

for i in range(adet):
    print(metin)




for i in range(1,6):
    print("*" * i)



"""    *
      ***
     *****
    *******
   ********* ÖRNEK 1"""

n=5

for i in range (1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

""" ÖRNEK 2
      ****
      ****
      ****
      ****
            """
n=4

for i in range (1,n+1):
    for j in range (1,n+1):
        print("*",end="")
    print()




""" ORNEK 3
       *
       **
       ***
       ****
       *****
       """

n = 5
for i in range(1,n+1):
    print("*" * i)





"""ORNEK 3
   *
  **
 ***
****
"""

n=4
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()






"""ORNEK 4
*****
****
***
**
*
"""

n=5

for i in range (n,0,-1):
    print("*" ,end=" ")
    for j in range(i-1):
        print("*",end=" ")
    print() #Alt satıra gec demek.

    
        
        

