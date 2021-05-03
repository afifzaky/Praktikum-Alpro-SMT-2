'''
Jurnal No 1

Kamu adalah seorang mahasiswa. Karena kamu penasaran mengenai nilai
kalkulus kamu selama 3 kali quiz, maka kamu ingin membuat sebuah program
yang dapat menghitung nilai dari rata-rata quiz tersebut. Buatlah sebuah program
python3 yang dapat menghitung rata-rata quiz, dengan inputan berupa
nama, kelas, nim, dan nilainya!
'''

nama = str(input("Nama: "))
kelas = str(input("Kelas: "))
nim = str(input("NIM: "))

k1 = float(input("Masukkan nilai Kuis 1: "))
k2 = float(input("Masukkan nilai Kuis 2: "))
k3 = float(input("Masukkan nilai Kuis 3: "))

rata_rata = (k1+k2+k3)/3
print("Rata - rata Kuis: ",float(rata_rata))