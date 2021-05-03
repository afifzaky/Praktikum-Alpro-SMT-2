'''
No 2 Jurnal

Kamu memiliki seorang crush yang sama-sama sedang mempelajari
Algoritma dan Pemrograman. Kamu ingin membuat sebuah program dimana
kamu ataupun dia dapat memasukkan input sifat yang kamu miliki. Input sifat
kamu akan selesai ketika kamu memasukkan input “selesai”. Program
dilanjutkan dengan input sifat yang dia miliki dan menggunakan input “selesai”
juga untuk menghentikan perulangannya. Setelahnya, program akan
menampilkan sifat-sifat yang sama dari kamu dan dia. Buatlah program
tersebut dan berikan kepadanya! (Hint : Gunakan set dan syntax bawaan
python)

'''

sk = set([])
sd = set([])

while True:
    km = str(input ("Masukkan Sifat Kamu : "))
    sk.add(km)
    if km == "selesai":
        sk.remove("selesai")
        break
while True:
    dia = str(input ("Masukkan Sifat Dia : "))
    sd.add(dia)
    if dia == "selesai":
        sd.remove("selesai")
        break

print(f"\t\tSIFAT KAMU\n{sk}")
print(f"\t\tSIFAT DIA\n{sd}")
print("\tPersamaan Dari Sifat Kamu dan Dia")
print(sd.intersection(sk))