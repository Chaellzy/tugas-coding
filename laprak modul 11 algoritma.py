class Data:
    def __init__(self):
        self._nama = None
        self._nilai = None

    def get_nama(self):
        return self._nama

    def set_nama(self, nama):
        self._nama = nama

    def get_nilai(self):
        return self._nilai

    def set_nilai(self, nilai):
        self._nilai = nilai


def menu():
    print("\n===== Program OOP =====")
    print("1. Mendeklarasikan Objek")
    print("2. Menampilkan Objek")
    print("3. Merubah Nilai Objek")
    print("4. Menghapus Objek")
    print("5. Keluar Dari Program")
    pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4/5): ")
    return pilihan


data = Data()

while True:
    pilihan = menu()
    
    if pilihan == '1':
        nama = input("Masukkan Nama: ")
        nilai = input("Masukkan Nilai: ")
        data.set_nama(nama)
        data.set_nilai(nilai)
        print("Data Berhasil Ditambahkan")
    
    elif pilihan == '2':
        nama = data.get_nama()
        nilai = data.get_nilai()
        print("\nNama:", nama if nama else "None")
        print("Nilai:", nilai if nilai else "None")
    
    elif pilihan == '3':
        atribut = input("Apa yang ingin diubah (Nama/Nilai): ").lower()
        if atribut == "nama":
            nama_baru = input("Masukkan Nama Baru: ")
            data.set_nama(nama_baru)
            print("Data Nama Berhasil Dirubah")
        elif atribut == "nilai":
            nilai_baru = input("Masukkan Nilai Baru: ")
            data.set_nilai(nilai_baru)
            print("Data Nilai Berhasil Dirubah")
        else:
            print("Atribut tidak valid. Silakan pilih Nama atau Nilai.")
    
    elif pilihan == '4':
        data.set_nama(None)
        data.set_nilai(None)
        print("Data Berhasil Dihapus")
    
    elif pilihan == '5':
        print("Terima Kasih Sudah Menggunakan Program Saya")
        break
    
    else:
        print("Pilihan tidak valid. Silakan masukkan angka antara 1-5.")
