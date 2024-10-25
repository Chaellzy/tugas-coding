print("=====SELAMAT DATANG DI KEBUN BINATANG TRISAKTI=====")
umur = int(input("masukkan umur : "))
total = 0

if umur == 1:
  print("Gratis")
  total = 0

elif umur >= 10 and umur <= 19:
  print("Harga $ 14")
  total = 14

elif umur >= 20 and umur <= 69:
  print("Harga $ 23")
  total = 23

elif umur >= 70:
  print("Harga $ 18")
  total = 18

print("Running total : $",total)

while True:
  umur = input("masukkan umur : ")
  if umur == "":
    break
  umur = int(umur)
  if umur >= 10 and umur <= 19:
    print("Harga $ 14")
    total += 14

  elif umur >= 20 and umur <= 69:
    print("Harga $ 23")
    total += 23

  elif umur >= 70:
    print("Harga $ 18")
    total += 18
  print("Running total : $",total)
uang = int(input("masukkan jumlah uang: "))
kembalian = uang - total
print("Running Kembalian: $",kembalian)
print("=====TERIMAKASIH=====")


