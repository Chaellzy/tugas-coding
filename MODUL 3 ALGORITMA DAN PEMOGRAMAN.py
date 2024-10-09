import math

# Input nilai dari pengguna
nilai1 = int(input("Masukan Nilai A = "))
nilai2 = int(input("Masukan Nilai B = "))
nilai3 = int(input("Masukan Nilai C = "))

# Memeriksa apakah ini persamaan kuadrat
if nilai1 == 0:
    print("Bukan merupakan Persamaan Kuadrat")
else:
    # Menghitung determinan
    D = (nilai2**2) - (4*nilai1*nilai3)
    
    # Menentukan jenis akarnya berdasarkan nilai D (determinannya)
    if D > 0:
        x1 = (-nilai2 + math.sqrt(D)) / (2 * nilai1)
        x2 = (-nilai2 - math.sqrt(D)) / (2 * nilai1)
        print("Persamaan kuadrat:", nilai1, "x^2 +", nilai2, "x +", nilai3)
        print("Determinan =", D)
        print("Akar x1 =", x1)
        print("Akar x2 =", x2)
        print("Dua akar berbeda")
        
    elif D == 0:
        x1 = (-nilai2) / (2 * nilai1)
        print("Persamaan kuadrat:", nilai1, "x^2 +", nilai2, "x +", nilai3)
        print("Determinan =", D)
        print("Akar =", x1)
        print("Dua akar sama")
        
    else:
        real_part = -nilai2 / (2 * nilai1)
        imag_part = math.sqrt(abs(D)) / (2 * nilai1)
        print("Persamaan kuadrat:", nilai1, "x^2 +", nilai2, "x +", nilai3)
        print("Determinan =", D)
        print(f"Akar x1 = {real_part} + {imag_part}i")
        print(f"Akar x2 = {real_part} - {imag_part}i")
        print("Akar imajiner, tidak punya akar real")
