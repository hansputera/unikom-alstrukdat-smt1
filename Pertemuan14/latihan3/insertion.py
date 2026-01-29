#Program Insertion_Sort
#I.S: menginisiasi variabel test cases
#F.S: menampilkan hasil pengurutan berdasarkan insertion sort

## Nama: HANIF DWY PUTRA S.
## NIM: 10125905
## Tgl pengerjaan: 28 Januari 2026
## Mata Kuliah: Algoritma dan Struktur Data 1

def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        y = data[i]
        j = i - 1
        while j >= 0 and data[j] > y:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = y
    return data

test_cases = [
    [29, 20, 73, 34, 64, 14, 59],
    [8, 4, 3, 7, 6, 2, 5, 1],
    [45, 22, 12, 33, 67, 89, 41, 56, 23],
    [5, 9, 1, 3, 7, 4, 6, 2, 8],
    [21, 55, 39, 12, 19, 43, 31, 74, 58]
]

for test_case in test_cases:
    print(insertion_sort(test_case))