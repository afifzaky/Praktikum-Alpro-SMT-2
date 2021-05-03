"""
No 2

Alfian akan bertanding dengan Nopal untuk sebuah pertandingan suit tingkat
dunia. Suit mempunyai ketentuan seperti:
    a. Jempol lawan Telunjuk, menang Jempol.
    b. Kelingking lawan Telunjuk, menang Telunjuk.
    c. Kelingking lawan Jempol, menang Kelingking.
    d. Apabila sama, maka seri

Dalam kejuaraan ini suit hanya akan dilakukan sebanyak 1 ronde, siapapun
yang menang maka dinyatakan sebagai pemenangnya. Buatlah sebuah
program untuk mewadahi kejuaraan suit ini agar pertandingan berjalan
dengan adil.
"""
alfian = str(input("Alfian, Masukkan jagoan anda : "))
nopal = str(input("Nopal, Masukan jagoan anda : "))

if alfian == "jempol" and nopal == "telunjuk":
    print("ALFIAN MENANG")
elif nopal == "jempol" and alfian == "telunjuk":
    print("NOPAL MENANG")
elif alfian == "telunjuk" and nopal == "kelingking":
    print("ALFIAN MENANG")
elif nopal == "telunjuk" and alfian == "kelingking":
    print("NOPAL MENANG")
elif alfian == "kelingking" and nopal == "jempol":
    print("ALFIAN MENANG")
elif nopal == "kelingking" and alfian == "jempol":
    print("NOPAL MENANG")
elif alfian == "jempol" and nopal == "jempol" or alfian == "telunjuk" and nopal == "telunjuk" or alfian == "kelingking" and nopal == "kelingking":
    print("Pertandingan Seri")
else:
    print("pengampunten, hanya bisa menginputkan telunjuk, jempol, kelingking")