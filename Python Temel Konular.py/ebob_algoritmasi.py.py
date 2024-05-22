#EBOB BULMA ORNEGİ

x=int(input("Ilk sayiyi giriniz: "))
y=int(input("Ikinci sayiyi giriniz"))

if(x>y):
    if(x%y==0):
        ebob=y
    else:
        i=y
        while(i>0):
            
            if(x%i==0 and y%i==0):
                ebob=i
                break
            i-=1
            
            
elif(y>x):
    if(y%x==0):
        ebob=x
    else:
        i=2
        while(i>0):
            
            if(y%i==0 and x%i==0):
                ebob=i
                break
            i-=1
else:
    ebob=x

print(ebob)





