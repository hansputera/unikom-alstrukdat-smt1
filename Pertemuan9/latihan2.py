#Program Tahun_Kabisat
#I.S: menerima input tahun kabisat
#F.S: mengeluarkan apakah tahun tersebut kabisat

def kabisat(tahun: int):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

tahun = int(input("Tahun : "))
print(kabisat(tahun))

## Created by HANIF DWY PUTRA S. (NIM: 10125905)
