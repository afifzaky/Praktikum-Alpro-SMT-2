'''
Jurnal No 2
Dokter Bruno adalah seorang dokter umum. Ia ingin memeriksa suhu seorang
pasien yang sedang demam tinggi, dokter Bruno pun mengambil termometer
untuk memeriksa suhu pasien tersebut. Tetapi termometer itu hanya dapat
mengkonversi suhu menjadi reamur. Sebagai seorang Programmer professional
kamu ingin membantu dokter Bruno untuk membuat sebuah aplikasi yang dapat
mengkonversi suhu reamur menjadi celcius, fahrenheit, dan kelvin. Buatlah
program python3 untuk membantu Dokter Bruno!
'''
print("=== Program Konversi Suhu ===")
suhu_reamur = int(input("Masukkan Suhu Reamur: "))

celcius = suhu_reamur * 5/4
fahrenheit = suhu_reamur * 9/4 + 32
kelvin = suhu_reamur * 5/4 + 273

print(suhu_reamur,"Reamur ke Celcius= ",celcius)
print(suhu_reamur,"Reamur ke Fahrenheit= ",fahrenheit)
print(suhu_reamur,"Reamur ke Kelvin= ",kelvin)