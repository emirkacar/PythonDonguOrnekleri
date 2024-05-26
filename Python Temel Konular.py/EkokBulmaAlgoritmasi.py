sayi1 = int(input("Bir sayi giriniz: "))
sayi2=int(input("Ikinci sayiyi giriniz: "))

while(True):
    if (sayi1 == sayi2):
        ekok = sayi1
    elif ( sayi1 > sayi2):
        i = sayi1
        while(True):
            if(i % sayi1 ==0 and i %sayi2 ==0):
                ekok = i
                break
            i+=1
            
        break
    else:
        i=sayi2
        while(True):
            if(i % sayi1 ==0 and i%sayi2 == 0):
                ekok=i
                break
            i+=1
        break
    break
print(f"Iki sayinin ekoku = {ekok} ")
