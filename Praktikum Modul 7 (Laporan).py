print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
    number = int(input("masukkan angka: "))
    
    if number == 0:
        print("terima kasih telah menggunakan program saya")
        break
    
    if number % 10 == 1 and number % 100 != 11:
        suffix = 'st'
    elif number % 10 == 2 and number % 100 != 12:
        suffix = 'nd'
    elif number % 10 == 3 and number % 100 != 13:
        suffix = 'rd'
    else:
        suffix = 'th'
    
    print(f"({number}, '{suffix}')")
