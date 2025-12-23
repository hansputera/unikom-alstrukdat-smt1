##Algoritma StudiKasus2
##I.S: menerima input opsi untuk memilih operasi
##F.S: menampilkan hasil operasi sesuai opsi yang dipilih

def fibo():
    n = int(input("Masukan Jumlah Suku : "))

    a, b = 1, 1
    print(f"Barisan fibonacci sebanyak {n} suku : ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

def m_kali_n():
    m = int(input("Masukan suatu bilangan bulat : "))
    n = int(input("Masukan bilangan pengali : "))

    print(f"{m} X {n} = {m * n}")

print("-" * 30)
print("1. Barisan  Fibonacci")
print("2. M kali N")
print("0. Keluar")

selection = int(input("Masukan Menu : "))
if selection == 1:
    fibo()
elif selection == 2:
    m_kali_n()
else:
    pass

## Created by HANIF DWY PUTRA S. - 10125905 (IF-10K)
