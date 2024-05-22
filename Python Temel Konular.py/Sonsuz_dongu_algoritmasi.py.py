#SONSUZ DONGU ALGORİTMASI
toplam=0 

while(True):
    sayi=input("Bir sayi giriniz:")
    if(sayi=='q'):
        break
    toplam+=int(sayi)
print("Toplam sonucu = {}".format(toplam))

