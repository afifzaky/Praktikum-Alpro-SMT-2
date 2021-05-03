'''
No 1 Jurnal

Kamu adalah seorang programmer terkenal di PT. JustCodeIt, Mr. Rizal
meminta mu untuk membuat sebuah program sederhana yang dapat
melakukan pendaftaran peserta, penghapusan, serta memperlihatkan
peserta yang hadir yang dapat di akses oleh user dalam bentuk “menu”.
(Program tidak akan berhenti sebelum user melakukan exit)
'''
nm = []
while True:
    print("""
    === JUST CODE IT ===
    1. Mendaftarkan Peserta
    2. Menghapus Peserta
    3. Mencetak Semua Peserta
    
    0. Exit
    """)

    pilihan = int(input("Masukkan Pilihan : "))
    if pilihan == 1:
        nm.append(input("Masukkan Nama Peserta : "))
    elif pilihan == 2:
        nm.remove(input("Masukkan Nama Peserta : "))
    elif pilihan == 3:
        print(nm)
    elif pilihan == 0:
        print("Selamat Anda Berhasil Keluar EAAAAAAAAAAAAAAAAAAAAAAAAAA")
        break
    else:
        print("WEEEEEEEEEEEEEEEEEEEEEEEEEE Inputnya Salah MAN")
        break