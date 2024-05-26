#Ebob hesaplama

sayi1 = int(input("Sayiyi giriniz : "))
sayi2= int(input("Ikinci sayiyi giriniz: "))

while (True):
    if ( sayi1 == sayi2):
        ebob = sayi1
        break
    elif ( sayi1 > sayi2):
        i=sayi2
        while(i!=0):
            if(sayi1 % i==0 and sayi2%i == 0):
                ebob = i
                break
            i-=1
        break
    else :
        i=sayi1
        while ( i!=0):
            if(sayi2 % i == 0 and sayi1 % i ==0):
                ebob = i
                break
            i-=1
        break
        
    break
    
    
print(f"Iki sayinin ebobu = {ebob} ")

