#Program Hitung_Luas_Keliling
#I.S: menerima input pilihan, radius/panjang/lebar/sisi
#F.S: menampilkan luas dan keliling

import math
import sys

luas = 0
keliling = 0

def lingkaran():
    global luas
    global keliling
    print("Perhitungan Luas dan Keliling Lingkaran")
    print("-" * 30)

    radius = int(input("Radius : "))
    luas = math.pi * (radius ** 2)
    keliling = 2 * math.pi * radius

def bujursangkar():
    global luas
    global keliling
    print("Perhitungan Luas dan Keliling Bujursangkar")
    print("-" * 30)

    sisi = int(input("Sisi : "))
    luas = sisi ** 2
    keliling = 4 * sisi

def persegipanjang():
    global luas
    global keliling
    print("Perhitungan Luas dan Keliling Persegi Panjang")
    print("-" * 30)

    panjang = int(input("Panjang : "))
    lebar = int(input("Lebar : "))

    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

def segitiga():
    global keliling
    global luas
    print("Perhitungan Luas dan Keliling Seigitga")
    print("-" * 30)

    alas = int(input("Alas : "))
    tinggi = int(input("Tinggi : "))
    samping = int(input("Samping : "))

    luas = 0.5 * alas * tinggi
    keliling = 2 * samping

print("Aplikasi Perhitungan Luas dan Keliling")
print("-" * 30)
print("1. Lingkaran\n2. Bujursangkar\n3. Persegipanjang\n4. Segitiga\n0. Keluar")
print("-" * 30)

pilihan = int(input("Pilihan anda ? "))
if pilihan == 1:
    lingkaran()
elif pilihan == 2:
    bujursangkar()
elif pilihan == 3:
    persegipanjang()
elif pilihan == 4:
    segitiga()
elif pilihan == 0:
    print("Terimakasih")
    sys.exit(0)
else:
    print("Invalid pilihan")
    sys.exit(0)

print(f"Luas : {luas:.2f}")
print(f"Keliling : {keliling:.2f}")

