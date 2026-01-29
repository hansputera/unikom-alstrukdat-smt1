#Program Selection_Sort_Min
#I.S: menginisiasi variabel test cases
#F.S: menampilkan hasil pengurutan berdasar min selection sort

## Nama: HANIF DWY PUTRA S.
## NIM: 10125905
## Tgl pengerjaan: 28 Januari 2026
## Mata Kuliah: Algoritma dan Struktur Data 1

def selection_sort_min(data):
    n = len(data)
    for i in range(n - 1):
        imin = i
        for j in range(i + 1, n):
            if data[j] < data[imin]:
                imin = j
        data[i], data[imin] = data[imin], data[i]

    return data

test_cases = [
    [47, 22, 34, 18, 56, 43, 15],
    [3, 1, 4, 1, 5, 9, 2, 6, 5],
    [21, 11, 48, 34, 19, 27, 33],
    [8, 5, 2, 9, 5, 6, 3, 7, 4, 5],
    [30, 20, 50, 40, 10, 60, 70]
]

for test_case in test_cases:
    print(selection_sort_min(test_case))