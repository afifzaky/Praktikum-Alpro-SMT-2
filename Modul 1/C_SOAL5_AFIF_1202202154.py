'''
No 5
Seorang pasien datang ke rumah sakit untuk menimbang berat badannya selama
3 minggu berturut-turut. Pasien pertama bernama Popol dengan jenis kelamin
Laki-laki dan umurnya 15 tahun, ia memiliki berat badan 53 kg (minggu ke-1),
58,5 kg (minggu ke-2), dan 50 kg (minggu ke-3). Pasien kedua bernama
Esmeralda dengan jenis kelamin Perempuan dan umurnya 30 tahun, ia memiliki
berat badan 45 kg (minggu ke-1), 48 kg (minggu ke-2), dan 55,2kg (minggu
ke-3). Sebagai seorang ahli gizi kamu ingin mengetahui rata-rata berat badan
dari kedua pasien tersebut. Buatlah program Python3 untuk menghitung rata-rata
berat badan pasien dengan menggunakan user input dan tipe data!
'''

#Pasien 1
nama = str(input("Nama: "))
jk = str(input("Jenis Kelamin: "))
umur = str(input("Umur: "))

bm1 = float(input("Masukkan Berat Badan Minggu ke-1: "))
bm2 = float(input("Masukkan Berat Badan Minggu ke-2: "))
bm3 = float(input("Masukkan Berat Badan Minggu ke-3: "))

rata_rata = (bm1+bm2+bm3)/3
print("Rata-Rata Berat Badan",nama,":",int(rata_rata),"Kg")

print()

#Pasien 2
nama = str(input("Nama: "))
jk = str(input("Jenis Kelamin: "))
umur = str(input("Umur: "))

bm1 = float(input("Masukkan Berat Badan Minggu ke-1: "))
bm2 = float(input("Masukkan Berat Badan Minggu ke-2: "))
bm3 = float(input("Masukkan Berat Badan Minggu ke-3: "))

rata_rata = (bm1+bm2+bm3)/3
print("Rata-Rata Berat Badan",nama,":",int(rata_rata),"Kg")