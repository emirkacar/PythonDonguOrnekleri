#SONSUZ DONGU ALGORİTMASI
toplam=0 

while(True):
    sayi=int(input("Bir sayi giriniz:"))
    toplam+=sayi
    if(sayi=='q'):
        break
print("Toplam sonucu = {}".format(toplam))

