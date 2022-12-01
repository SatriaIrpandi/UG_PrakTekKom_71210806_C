print("Operasi Matematika")
print("1. Jumlah [+}")
print("2. Kurang [-}")
print("3. Kali   [*}")
print("4. Bagi   [/}")
p=int(input("Pilih Operasi (1/2/3/4) :"))
a=int(input("Masukan bilangan pertama :"))
b=int(input("Masukan bilangan kedua :"))

#rumus
def penjumlahan(a,b):
    tambah=a+b
    return tambah
def pengurangan(a,b):
    kurang=a-b
    return kurang
def perkalian(a,b):
    perkalian=a*b
    return perkalian
def pembagian(a,b):
    bagi=a/b
    return bagi

if p==1:
    print("Hasil operasi dari",a,"+",b,"=",penjumlahan(a,b))
elif p==2:
    print("Hasil operasi dari",a,"-",b,"=",pengurangan(a,b))
elif p==3:
    print("Hasil operasi dari",a,"*",b,"=",perkalian(a,b))
else:
    print("Hasil operasi dari",a,"/",b,"=",pembagian(a,b))

