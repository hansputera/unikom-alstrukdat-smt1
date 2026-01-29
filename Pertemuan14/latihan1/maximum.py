#Program Selection_Sort_Max
#I.S: menginisiasi variabel test cases
#F.S: menampilkan hasil pengurutan berdasar max selection sort

## Nama: HANIF DWY PUTRA S.
## NIM: 10125905
## Tgl pengerjaan: 28 Januari 2026
## Mata Kuliah: Algoritma dan Struktur Data 1

def selection_sort_max(data):
    n = len(data)
    for i in range(n - 1, 0, -1):
        imaks = 0
        for j in range(1, i + 1):
            if data[j] > data[imaks]:
                imaks = j
        data[i], data[imaks] = data[imaks], data[i]

    return data

test_cases = [
    [34, 19, 42, 17, 23, 28],
    [5, 1, 8, 3, 2, 6, 4, 7],
    [55, 67, 12, 95, 32, 45, 78],
    [21, 43, 11, 89, 54, 36, 20, 72],
    [9, 14, 3, 7, 21, 5, 18]
]

for test_case in test_cases:
    print(selection_sort_max(test_case))