"""
No 2

Buatlah program python yang dapat mengetahui hasil campuran dari warna
RGB. Ketika warna merah dicampur dengan warna biru maka akan
menghasilkan warna ungu. Ketika warna merah dicampur dengan warna hijau
akan menghasilkan warna kuning. Ketika warna hijau dicampur dengan warna
biru maka akan menghasilkan warna cyan.
"""
print("===PROGRAM MIX COLOR RGB===")
w1 = str(input("Masukkan warna pertama: "))
w2 = str(input("Masukkan warna kedua: "))

if w1 == "merah" and w2 == "biru" or w1 == "biru" and w2 == "merah":
    print("campuran warna",w1,"dan",w2,"menghasilkan warna ungu")
elif w1 == "merah" and w2 == "hijau" or w1 == "hujai" and w2 == "merah":
    print("campuran warna",w1,"dan",w2,"menghasilkan warna kuning")
elif w1 == "hijau" and w2 == "biru" or w1 == "biru" and w2 == "hijau":
    print("campuran warna",w1,"dan",w2,"menghasilkan warna cyan")
else:
     print("PROGRAM MIX COLOR ERROR")
     print("Mix hanya bisa untuk warna merah/hijau/biru.")
