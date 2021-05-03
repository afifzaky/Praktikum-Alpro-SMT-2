'''
No 4
Setiap hari minggu kuturut ayah ke gunung naik naga istimewa kududuk dimuka,
namun karena sering duduk dimuka celanaku sering berlubang-lubang karena
terbakar api naga, beruntungnya di gunung ada mesin pembuat celana otomatis
yang dapat menerima input dari user berupa bahan yang ingin digunakan untuk
celana, namun bahan-bahan ini hanya terbatas yang ada di hutan saja tetapi mesin
ini bukan sembarang mesin karena berdasarkan jenis bahan yang dimasukkan akan
memberikan efek yang berbeda-beda seperti bahan Abaka akan menghasilkan
efek berupa celana tahan air, bahan Pandan akan menghasilkan efek harum,
dan bahan Batu akan menghasilkan efek perlindungan maksimal. Buatkanlah
sebuah program yang bisa mengeluarkan efek berdasarkan dari input yang dimasukkan
'''


bc = input("Masukkan Bahan : ")

def Katok(bc):
    if bc == "Abaka":
        print("Keluarlah Celana Tahan Air")
        return
    elif bc == "Pandan":
        print("Keluarlah Celana Berbau Harum")
        return
    elif bc == "Batu":
        print("Keluarlah Celana Yang Menghasilkan Efek Perlindungan Maksimal")
        return
    else :
        print(f"Bahan {bc} Tidak Diketahui")
        return
Katok(bc)