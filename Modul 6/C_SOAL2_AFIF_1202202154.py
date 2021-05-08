'''
2. Sebagai seorang programmer buatlah sebuah program yang dapat membagi kedua
operasi dengan menggunakan handling atau program yang dapat menangani error
apabila membagi bilangan dengan angka 0!
'''
print("===Operasi Pembagian===")
try:
    nomeeeeeeeeeer1 = int(input("Inpoet Angka Pertama   : "))
    nomeeeeeeeeeer2 = int(input("Inpoet Angka Kedua     : "))
    penghasil = (nomeeeeeeeeeer1  / nomeeeeeeeeeer2) 
except ZeroDivisionError:
    print("Broo, Anda Tidak dapat membagi Dengan angka 0")
else:
    print(f"Hasil Akhir Dari Bagi  : {penghasil}")