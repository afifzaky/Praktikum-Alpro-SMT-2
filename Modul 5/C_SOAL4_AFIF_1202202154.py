'''
No 4
Ximi Store sedang melakukan edukasi untuk para anak TK mengenai matematika
ilmu yang menyenangkan ~~, kamu adalah seorang programmer handal dari JCI,
buatlah program yang menerima inputan berupa angka bulat yang banyak
angkanya telah ditentukan (counted loop) sebelumnya, lalu pada saat angka di
keluarkan, setiap angka yang sama hanya akan di print satu kali.
'''

k = int(input("Masukkan Jumlah angka : "))
numbah = set()

for j in range(1,k+1):
    l = int(input(f'Masukkan angka ke-{j} : '))
    numbah.add(l)
print(numbah)