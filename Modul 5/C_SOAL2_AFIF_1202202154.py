'''
no 2
Kamu adalah seorang mahasiswa yang mulai terjun ke dunia wirausaha. Dalam
menjalankan bisnis ini, kamu ingin mengetahui berapa pembelian terbanyak yang
dilakukan oleh pelanggan dalam satu hari ini. Karena kamu sekarang sedang belajar
python, kamu berinisiatif untuk membuat program tersebut agar memudahkanmu.
Buatlah program tersebut dengan menggunakan python3! (Hint : Gunakan List dan
syntax bawaan python)
'''
print("\t\tPorsi Terbanyak ?")

mkn = []
while True:
    jmp = input('Masukkan Jumlah Porsi ("stop" untuk berhenti) : ')
    if jmp == "stop":
        break
    else:
        mkn.append(int(jmp))
print(f"Penjualan Terbanyak Dari Satu Pelanggan Hari Ini Adalah: {max(mkn)}")