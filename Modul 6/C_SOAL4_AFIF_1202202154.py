'''
4. Buatlah sebuah program python 3 yang menerima input nama gen dan jumlah
anggota gen tersebut. Program tersebut menggunakan penegasan (assert) bahwa
panjang nama gen minimal 5 huruf dan jumlah anggota yang dimasukkan tidak
boleh 0.
'''
try:
    sukx = input("Inpoetz Nama Gen (Pastikan Tidak Kurang Dari 5) : ")
    assert any(sukx for x in sukx if not len(sukx) < 5)
    j = int(input(f"Invutz Jumlah Gen {sukx} (Ihh Ngaak Boleh 0 yaa): "))
    assert j != 0
except AssertionError:
    print("Loh Isi Sesuai Ketentuan Dumsss")
finally:
    print("Percobaan Pemrogramannya Telah Dinyatakan Selesai")