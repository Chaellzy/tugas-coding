data = ""
nilai = 0
hasil = 0

while True:
    data = input("Input nilai: ")

    if data == "":
        break

    elif data in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'E']:
        if data == 'A':
            hasil += 4.00
            print('Nilai = 4.00')
        elif data == 'A-':
            hasil += 3.75
            print('Nilai = 3.75')
        elif data == 'B+':
            hasil += 3.50
            print('Nilai = 3.50')
        elif data == 'B':
            hasil += 3.00
            print('Nilai = 3.00')
        elif data == 'B-':
            hasil += 2.75
            print('Nilai = 2.75')
        elif data == 'C+':
            hasil += 2.50
            print('Nilai = 2.50')
        elif data == 'C':
            hasil += 2.00
            print('Nilai = 2.00')
        elif data == 'C-':
            hasil += 1.75
            print('Nilai = 1.75')
        elif data == 'D':
            hasil += 1.50
            print('Nilai = 1.50')
        elif data == 'E':
            hasil += 1.25
            print('Nilai = 1.25')
        
        nilai += 1 
    else:
        print("Nilai invalid!")

if nilai > 0:
    avg = hasil / nilai
    print(f'Rata-rata nilai: {avg:.2f}')
else:
    print("Tidak ada nilai yang valid dimasukkan.")

