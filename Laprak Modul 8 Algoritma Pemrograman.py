def perpangkatan(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / perpangkatan(base, -power)
    return base * perpangkatan(base, power - 1)

print("Ini merupakan program perpangkatan negatif dan positif.")
while True:
    try:
        base = input("Masukkan Angka: ")
        if base == "":
            print("Program Selesai")
            break
        base = float(base)
        power = int(input("Masukkan Pangkatnya: "))
        hasil = perpangkatan(base, power)
        print(f"Hasilnya adalah: {hasil}")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")