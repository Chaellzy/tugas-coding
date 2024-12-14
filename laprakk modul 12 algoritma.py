import pandas as pd

data = {
    "Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil", "Rusia", "Mesir", "Aljazair", "Inggris"],
    "Ibu Kota": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brasilia", "Moskow", "Kairo", "Aljir", "London"],
    "Benua": ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika", "Asia", "Afrika", "Afrika", "Eropa"],
    "Luas": [1905, 377, 3287, 9597, 9834, 8516, 1709, 1001, 2381, 242],
    "Populasi": [264, 127, 1357, 1393, 327, 210, 144, 98, 43, 66]
}

df = pd.DataFrame(data)

mean_df = df.groupby("Benua")[["Luas", "Populasi"]].mean().reset_index()
mean_df.columns = ["Benua", "Mean Luas", "Mean Populasi"]

std_df = df.groupby("Benua")[["Luas", "Populasi"]].std().reset_index()
std_df.columns = ["Benua", "Std Luas", "Std Populasi"]

mean_df.to_csv("NegaraMean.csv", index=False)
std_df.to_csv("NegaraStandarDeviasi.csv", index=False)

print("File CSV berhasil dibuat:")
print("1. NegaraMean.csv")
print("2. NegaraStandarDeviasi.csv")
