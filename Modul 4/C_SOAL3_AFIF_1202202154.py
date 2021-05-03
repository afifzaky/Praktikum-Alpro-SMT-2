'''
No 3
Meldi saat ini sedang jomblo, namun ia ingin mempunyai sebuah program yang
memanfaatkan OOP di Python yang bisa menampilkan sifat-sifat dari keluarganya
Meldi suatu saat nanti, dengan ketentuan sifat dari Meldi sebagai orang tua akan
pasti dimiliki oleh anak dari Meldi. Meldi berencana ikut KB jadi ia akan mempunyai 2
anak saja, satu laki-laki dan satu perempuan. Sifat-sifat dari Meldi adalah sebagai
berikut, penyayang, penyabar, pemaaf, dan susah move on, lalu sifat dari anak
laki-laki Meldi adalah pemberani, dan dermawan, dan sifat dari anak perempuan
Meldi adalah pemalu, dan setia. Namun ternyata Meldi tidak bisa pemrograman
lalu ia meminta bantuan kamu untuk membuatkan program nya.
'''
class orang:

    def Penyayang(self):
        print("I Love You")
    def Penyabar(self):
        print("Saya Tidak Marah Kok")
    def Pemaaf(self):
        print("Saya Maafkan Kamu")
    def SusahMoveOn(self):
        print("Kembalilah Padaku")

class LakiLaki(orang):
    def Pemberani(self):
        print("Saya Tidak Takut")
    def Dermawan(self):
        print("Ini Saya Ada Rezeki Buat Kamu")

class Perempuan(orang):
    def Pemalu(self):
        print("Haduh Saya Jadi Malu")
    def Setia(self):
        print("Akumah Cukup Kamu Aja")

print("<<< Contoh Laki - Laki >>>")
lk1 = LakiLaki()
lk1.Penyayang()
lk1.Penyabar()
lk1.Pemaaf()
lk1.SusahMoveOn()
lk1.Pemberani()
lk1.Dermawan()
print()

print("<<< Contoh Perempuan >>>")
pr1 = Perempuan()
pr1.Penyayang()
pr1.Penyabar()
pr1.Pemaaf()
pr1.SusahMoveOn()
pr1.Pemalu()
pr1.Setia()
print()