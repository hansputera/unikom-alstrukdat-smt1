#Algoritma StudiKasus1
#I.S: menerima input opsi untuk memilih operasi
#F.S: menampilkan hasil operasi sesuai opsi yang dipilih

def pangkat():
    n = int(input("Masukan suatu bilangan bulat : "))
    a = int(input("Masukan pangkat yang diinginkan : "))

    for i in range(a):
        i = i + 1
        print(f"Hasil {n} pangkat {i} adalah {n**i}")

def hitung_deret():
    n = int(input("Masukan jumlah N : "))
    a, b = 1, 1
    result = a / b

    for i in range(n-1):
        a2 = a + b
        b2 = a2 + b

        if i % 2 == 0:
            result -= a2 / b2
        else:
            result += a2 / b2

        a, b = a2, b2

    print(result)

print("1. A pangkat B")
print("2. Hitung 1 - 2/3 + 3/5 - 5/8 + ...")
print("0. Keluar")

selection = int(input("Masukan Menu : "))
if selection == 1:
    pangkat()
elif selection == 2:
    hitung_deret()

## Created by HANIF DWY PUTRA S. - 10125905 (IF-10K)
