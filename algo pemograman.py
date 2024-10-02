import math

# input user
lat1 = float(input("masukan lintang kota 1:"))
lon1 = float(input("masukan bujur kota 1:"))
lat2 = float(input("masukan lintang kota 2:"))
lon2 = float(input("masukan bujur kota 2:"))

# mengonversi derajat ke radian
lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

# jari - jari bumi dalam kilometer
R = 6371.0

# menghitung perbedaan lintang dan bujur
dlat = lat2 - lat1
dlon = lon2 - lon1

# menggunakan rumus haversine
a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# menghitung jarak
jarak = R * c

# menampilkan hasil jarak
print(f"jarak antara kedua titik tersebut adalah {jarak:.2f} kilometer.")