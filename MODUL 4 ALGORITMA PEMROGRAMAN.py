while True:
    bulan = int(input("Masukkan nomor bulan (1-12) atau -1 untuk berhenti: "))
    
    if bulan == -1:
        print("Program dihentikan. Terima kasih!")
        break

    tahun = int(input("Masukkan tahun: "))
    
    if bulan < 1 or bulan > 12:
        print("Bulan yang dimasukkan tidak valid! Harap masukkan bulan antara 1-12.")
    else:
        jumlah_hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if bulan == 2:
            if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
                print(f"Bulan {bulan} pada tahun {tahun} memiliki 29 hari (tahun kabisat).")
            else:
                print(f"Bulan {bulan} pada tahun {tahun} memiliki 28 hari.")
        else:
            print(f"Bulan {bulan} pada tahun {tahun} memiliki {jumlah_hari[bulan - 1]} hari.")
