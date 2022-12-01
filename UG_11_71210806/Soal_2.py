print("Pemeriksa Kelipatan 9")
a=float(input("Masukan Kelipatan 9 yang ingin diperiksa:"))

def kelipatan_sembilan(a):
    k=a%9
    return k

if kelipatan_sembilan(a)==0:
    print("Benar")
else:
    print("Salah")
    print(a[1])
