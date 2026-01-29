# Program Array

## Deklarasi
max_numbers = 10
numbers: list[int] = []


def selectionMenu():
    print("Menu Pilihan")
    print("-" * 10)

    print("1. Isi Larik Angka")
    print("2. Tampil Larik Angka")
    print("3. Tambah Elemen Larik Angka")
    print("4. Sisip Elemen Larik Angka")
    print("5. Hapus Elemen Larik Angka")
    print("6. Angka Tertinggi dan Terendah")
    print("0. Keluar")

    return int(input("Pilihan Anda?: "))


def numberCreation(numbers: list[int]):
    for _ in range(max_numbers):
        el = 0
        numbers.append(el)


def showNumber(numbers: list[int], muchData: int):
    print("Menampilkan elemen array angka")
    print("-" * 20)
    print("! Indeks Ke- ! Elemen Array !")
    print("-" * 20)
    for i in range(muchData):
        print(f"!     {i:2}     !      {numbers[i]:3}      !")
    print("-" * 20)


def fillNumber(numbers: list[int], muchData: int):
    for i in range(muchData):
        newNumber = int(input("Masukan Angka Ke-{} : ".format(i + 1)))
        numbers[i] = newNumber


def addNumber(numbers: list[int], muchData: int, newNumber: int):
    if muchData < max_numbers:
        numbers[muchData] = newNumber
    else:
        print("Array numbers sudah penuh")


def insertNumber(numbers: list[int], muchData: int, position: int, newNumber: int):
    if muchData < max_numbers:
        position = position - 1
        if position >= 0 and position <= (muchData - 1):
            i = muchData - 1
            while i >= position:
                numbers[i + 1] = numbers[i]
                i = i - 1

            numbers[position] = newNumber
        else:
            print("Posisi Sisip Tidak Valid")
    else:
        print("Array numbers sudah penuh")


def removeNumber(numbers: list[int], muchData: int, position: int):
    if muchData > 0:
        position = position - 1
        if position >= 0 and position <= muchData:
            i = position + 1
            while i <= (muchData - 1):
                numbers[i - 1] = numbers[i]
                i = i + 1
            numbers[i - 1] = 0
        else:
            print("Posisi Hapus Tidak Valid")
    else:
        print("Array numbers kosong")


# Badan Program Utama
# Proses Penciptaan Array Angka
# numberCreation(numbers)

numbers = [0] * max_numbers
showNumber(numbers, max_numbers)

muchData = 0
print()

menu = selectionMenu()
while menu != 0:
    if menu == 1:
        print("Menu 1 - Isi Elemen Array")
        print()

        muchData = int(input("Banyak data : "))
        while muchData < 1 or muchData > max_numbers:
            print("Tidak boleh lebih dari", max_numbers, "ulangi!")
            muchData = int(input("Banyak data : "))

        fillNumber(numbers, muchData)
    elif menu == 2:
        print("Menu 2 - Tampil Elemen Array")
        showNumber(numbers, max_numbers)
    elif menu == 3:
        print("Menu 3 - Tambah Elemen Array")
        newNumber = int(input("Masukan sebuah elemen angka baru : "))
        addNumber(numbers, muchData, newNumber)

        if muchData <= max_numbers:
            muchData = muchData + 1
    elif menu == 4:
        print("Menu 4 - Sisip Elemen Array")
        newNumber = int(input("Masukan sebuah element angka baru : "))
        position = int(input("Angka tersebut akan disisipkan diposisi ke : "))

        insertNumber(numbers, muchData, position, newNumber)
        if muchData <= max_numbers:
            muchData = muchData + 1
    elif menu == 5:
        print("Menu 5 - Hapus elemen array")
        position = int(input("Posisi elemen angka yang akan dihapus : "))
        removeNumber(numbers, muchData, position)
        muchData = muchData - 1
    elif menu == 6:
        print("Menu 6")

        print("Tertinggi: ", max(numbers))
        print("Terendah: ", min(numbers))
    else:
        print("Pilihan menu tidak ada")

    menu = selectionMenu()


## NIM: 10125905
## Nama: HANIF DWY PUTRA S.
## Kelas: IF-10K (Kelas Karyawan)
## Tanggal: 15 Januari 2026 (15/01/2026)
