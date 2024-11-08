def kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

def hitung_hari(bulan, tahun):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if kabisat(tahun):
            return 29
        else:
            return 28
    else:
        return None

def running_program():
    while True:
        tahun = int(input("Masukkan tahun (atau ketik 0 untuk keluar): "))
        if tahun == 0:
            print("Program selesai. Terimakasih telah menggunakan.")
            break

        bulan = int(input("Masukkan nomor bulan (1-12): "))
        hari = hitung_hari(bulan, tahun)

        if hari:
            print(f"Jumlah hari pada bulan {bulan} tahun {tahun} adalah {hari} hari.\n")
        else:
            print("Input bulan tidak valid. Harap masukkan bulan antara 1 dan 12.\n")

running_program()