def buat_file(nama_file):
    with open(nama_file, 'w') as file:
        file.write(input("Masukkan Namamu: ") + "\n")
        file.write(input("Masukkan NIM kamu: ") + "\n")
        file.write(input("Masukkan tahun angkatanmu: ") + "\n")
    print("File Berhasil Dibuat")

def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File tidak ditemukan.")

def tambah_text(nama_file):
    try:
        with open(nama_file, 'a') as file:
            file.write(input("Masukkan teks tambahan: ") + "\n")
        print("Data Berhasil Ditambahkan")
    except FileNotFoundError:
        print("File tidak ditemukan.")

while True:
    print("\n===== Program File Handling =====")
    print("1. Membuat dan Menulis File")
    print("2. Membaca File")
    print("3. Menambahkan Text Pada File")
    print("4. Keluar Dari Program")
    
    pilihan = input("Masukkan Pilihan (1/2/3/4): ")
    if pilihan == '1':
        buat_file(input("Masukkan Nama File: "))
    elif pilihan == '2':
        baca_file(input("Masukkan Nama File: "))
    elif pilihan == '3':
        tambah_text(input("Masukkan Nama File: "))
    elif pilihan == '4':
        print("Terima Kasih!")
        break
    else:
        print("Pilihan tidak valid.")
