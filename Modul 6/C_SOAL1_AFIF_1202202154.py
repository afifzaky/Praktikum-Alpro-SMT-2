'''
1. Buatlah program Multi Except yang dapat menangani beberapa error secara
bersamaan. Error yang dapat ditangkap oleh program adalah kesalahan tipe data,
dan kesalahan jika membagi operasi dengan nol (0)!
'''
try:
    numbahhhhhh1 = float(input("Invut Angka Pertama  : "))
    numbahhhhhh2 = float(input("Invut Angka Kedua    : "))
    soedahhhh = (numbahhhhhh1 / numbahhhhhh2) or (numbahhhhhh2 / numbahhhhhh1)
except ValueError:
    print("GIMANA MAS BRO DATA NYA GA SESUAI")
except ZeroDivisionError:
    print("Mana Bisa Dibagi Sama Angka 0 BROOOO")
else:
    print(f"Ini Hasilnya : {soedahhhh}")