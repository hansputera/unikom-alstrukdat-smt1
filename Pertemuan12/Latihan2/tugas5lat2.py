# Program Operasi Array 2 Dimensi
# I.S: Pengguna akan memilih sebuah menu
# F.S: Program akan menampilkan pilihan menu

max_rows = 10
max_cols = 10

def selectionMenu():
    print()
    print('1. Penjumlahan Dua Matriks')
    print('2. Matriks Transpose')
    print('3. Perkalian Dua Matriks')
    print('0. Keluar')

    return int(input('Pilihan Anda? : '))

def matricesCreation(matrices: list[int]):
    for i in range(max_cols):
        matrices[i] = [0] * max_cols

def showMatrices(matrices: list, rows: int, cols: int):
    print('Matriks Berordo', rows, 'x', cols)
    print('-' * 30)
    for i in range(rows):
        for j in range(cols):
            print(matrices[i][j], '\t', end=" ")

def fillMatrices(matrices: list, rows: int, cols: int):
    print('Matriks Berordo', rows, 'x', cols)
    print('-' * 30)
    for i in range(rows):
        for j in range(cols):
            element = int(input('Indeks[{}][{}] : '.format(i, j)))
            matrices[i][j] = element


def countMatrices(matrices: list, secondMatrices: list, resultMatrices: list, rows: int, cols: int):
    print('Matriks Berordo', rows, 'x', cols)
    print('-' * 30)
    for i in range(rows):
        for j in range(cols):
            resultMatrices[i][j] = matrices[i][j] - secondMatrices[i][j]

def transposeMatrices(matrices: list, rows: int, cols: int):
    print('Matriks Setelah Transpose')
    for i in range(rows):
        for j in range(cols):
            print(matrices[i][j], '\t', end=" ")
        print()

def multiplyMatrices(matrices: list, secondMatrices: list, resultMatrices: list, rows: int, cols: int, colsM2: int):
    for i in range(rows):
        for k in range(colsM2):
            multiplyResult = 0
            for j in range(cols):
                multiplyResult = multiplyResult + matrices[i][j] * secondMatrices[i][j]
            resultMatrices[i][k] = multiplyResult

menu = selectionMenu()
while menu != 0:
    if menu == 1:
        print('Penjumlahan Dua Buah Matriks')

        A = [0] * max_rows
        B = [0] * max_rows
        C = [0] * max_rows # Result of +

        matricesCreation(A)
        matricesCreation(B)
        matricesCreation(C)

        count_rows = int(input('Banyak baris : '))
        count_cols = int(input('Banyak kolom : '))

        print('Mengisi Matriks A')
        fillMatrices(A, count_rows, count_cols)
        print()

        print('Mengisi Matriks B')
        fillMatrices(B, count_rows, count_cols)
        print()

        print('Matriks A')
        showMatrices(A, count_rows, count_cols)
        print()

        print('Matriks B')
        showMatrices(B, count_rows, count_cols)
        print()

        countMatrices(A, B, C, count_rows, count_cols)
        print('Matriks Hasil Penjumlahan')
        showMatrices(C, count_rows, count_cols)
    elif menu == 2:
        print('Matriks Transpose')

        A = [0] * max_rows
        matricesCreation(A)

        count_rows = int(input('Banyak baris : '))
        count_cols = int(input('Banyak kolom : '))

        print()
        print('Mengisi Matriks A')
        showMatrices(A, count_rows, count_cols)

        transposeMatrices(A, count_rows, count_cols)

    elif menu == 3:
        print('Perkalian Dua Buah Matriks')

        A = [0] * max_rows
        B = [0] * max_rows
        C = [0] * max_rows

        matricesCreation(A)
        matricesCreation(B)
        matricesCreation(C)

        count_rows = int(input('Banyak baris Matriks Pertama : '))
        count_cols = int(input('Banyak kolom Matriks Pertama : '))

        print('Banyak Baris Matriks Kedua ', count_cols)
        count_colsM2 = int(input('Banyak kolom Matriks Kedua : '))

        print('Mengisi Matriks A')
        fillMatrices(A, count_rows, count_cols)
        print()

        print('Mengisi Matriks B')
        showMatrices(B, count_cols, count_colsM2)
        print()

        print('Matriks A')
        showMatrices(A, count_rows, count_cols)
        print('Matriks B')
        showMatrices(B, count_cols, count_colsM2)
        print()

        multiplyMatrices(A, B, C, count_rows, count_cols, count_colsM2)
        print('Matriks Hasil Perkalian')
        showMatrices(C, count_rows, count_cols)


    else:
        print('Menu Pilihan Salah')

    menu = selectionMenu()


## NIM: 10125905
## Nama: HANIF DWY PUTRA S
## Kelas: IF-10K (Kelas Karyawan)
## Tanggal: 15 Januari 2026 (15/01/2026)