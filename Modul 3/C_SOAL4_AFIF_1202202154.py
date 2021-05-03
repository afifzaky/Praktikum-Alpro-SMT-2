'''
Latihan Soal No 4

Gina sebagai seorang kasir ingin membuat program untuk membantunya
dalam menghitung total belanjaan pembelinya. Program ini membutuhkan
banyak barang belanjaan pembeli dan harganya. Jika total belanjaan
pembeli lebih dari 75000, maka pembeli akan mendapatkan diskon 20%.
Gunakan konsep While Loop!
'''

barang = int(input("Masukkan banyak barang belanjaan : "))
harga = 0
keseluruhan = 0
x = 0
while x < barang:
    harga = int(input("Masukkan harga barang : "))
    keseluruhan += harga
    x += 1
if keseluruhan > 75000:
    diskon = keseluruhan * 0.80
    print(f"Total belanjaan sebelum diskon Rp.{keseluruhan}\n Total belanjaan setelah diskon Rp.{diskon}")
else:
    print(f"Total belanjaan yang harus dibayar Rp.{keseluruhan}")