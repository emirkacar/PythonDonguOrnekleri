#Tuple,Dizi ve Donguleri kullanarak yapilan algoritmalar.

#Liste icindeki tekrar eden elemanlari bulma

liste=[1,2,3,1,1,2,2,3,6,5,8,5]
tekrarEdenElemanlar = []
gorulenElemanlar = []

for i in liste:
    if i in gorulenElemanlar and i not in tekrarEdenElemanlar:
        tekrarEdenElemanlar.append(i)
    if i not in gorulenElemanlar:
        gorulenElemanlar.append(i)
print("Tekrar eden elemanlar:")
print(tekrarEdenElemanlar)

#Tuple icindeki en buyuk ve en kucuk elemani bulma

demet = (50,60,75,12,94,5,1,60,78,80,14,8590,100)
maximum = demet[0]
minimum= demet[0]
i=0

while (i < len(demet)):
    if(maximum<demet[i]):
        maximum=demet[i]
    if(minimum>demet[i]):
        minimum=demet[i]
    i+=1
print("En buyuk eleman : %d" % (maximum))
print("En kucuk eleman : %d" % (minimum))


#Listedeki tek ve cift sayilari baska bir tuple'a atma

orijinal = [10,20,13,19,20,30,15]
tekSayilar= []
ciftSayilar = []

for i in range(len(orijinal)):
    if(orijinal[i]%2==0):
        ciftSayilar.append(orijinal[i])
    else:
        tekSayilar.append(orijinal[i])

print(ciftSayilar)
print(tekSayilar)


          
          

