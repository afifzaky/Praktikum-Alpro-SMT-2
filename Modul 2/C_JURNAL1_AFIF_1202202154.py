"""
No 1 Jurnal 

Althaf adalah seorang mahasiswa Sistem Informasi pada saat semester 2, dia
mendapatkan tugas dari dosen alpronya untuk membuat suatu program
python tentang pengelompokan status berdasarkan usia. Terdapat 5
kondisi pada program ini berikut adalah tabel kondisinya:

No              Usia                   Keterangan
1               0 - 5                  "Balita"
2               6 - 13                 "Anak Anak"
3               13 - 17                "Remaja"
4               18 - 59                "Dewasa"
5               >60                    "Lansia"

Sebagai seorang programmer yang ahli bantulah Althaf dalam mengerjakan
tugas dari dosennya untuk membuat sebuah program yang sesuai dengan
keterangan output yang diinginkan.

u = umur
"""
u = int(input("Masukkan umur = "))

if u >= 0 and u <= 5:
    print("Balita")
elif u >= 6 and u <= 13:
    print("Anak-anak")
elif u >= 13 and u <= 17:
    print("Remaja")
elif u >= 18 and u <= 59:
    print("Dewasa")
elif u >= 60:
    print("Lansia")
else:
    print("Inputan Salah")