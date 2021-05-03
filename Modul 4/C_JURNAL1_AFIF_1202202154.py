class pelajar:

    def __init__(self,nama,nim,kelas,alamat):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.alamat = alamat

    def tampilan(self):
        print("Nama     : "+self.nama)
        print("NIM      : "+self.nim)
        print("Kelas    : "+self.kelas)
        print("Alamat   : "+self.alamat)

print("Mahasiswa 1")
p1 = pelajar("Ananda","1202190008","SI-43-02","Palangka Raya")
p1.tampilan()
print()
print("Mahasiswa 2")
p2 = pelajar("Xaximi","12021902937","SI-42-04","Bogor")
p2.tampilan()
print()
print("Mahasiswa 3")
p3 = pelajar("Rizal","1202128729","SI-43-01","Bandung")
p3.tampilan()