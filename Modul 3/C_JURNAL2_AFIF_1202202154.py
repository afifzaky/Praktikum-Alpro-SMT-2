'''
Jurnal No 2

Sebuah butik menjual 3 jenis barang yaitu:
- Kaos = Rp 25.000
- Kemeja = Rp 50.000
- Jas = Rp 100.000
Buat program yang dapat menerima inputan barang mana yang akan dibeli
lalu ketika user selesai membeli barang program akan menampilkan total
harga yang harus dibayar user

k = keseluruhan
o = opsi
h = harga

'''
print("=== SELAMAT DATANG DI PROGRAM BUTIK ===")
print("1. KAOS")
print("2. KEMEJA")
print("3. JAS")
print("4. SELESAI")


k = 0

'''
Jurnal No 2

Sebuah butik menjual 3 jenis barang yaitu:
- Kaos = Rp 25.000
- Kemeja = Rp 50.000
- Jas = Rp 100.000
Buat program yang dapat menerima inputan barang mana yang akan dibeli
lalu ketika user selesai membeli barang program akan menampilkan total
harga yang harus dibayar user

k = keseluruhan
o = opsi
h = harga

'''
print("=== SELAMAT DATANG DI PROGRAM BUTIK ===")
print("1. KAOS")
print("2. KEMEJA")
print("3. JAS")
print("4. SELESAI")

k = 0

o = (input("Masukkan barang yang ingin dibeli (1/2/3/4) : "))
while o != 4:
    if o == 1 or o == "Kaos":
        h = int(25000)
        print("Kaos telah ditambahkan")
        print()
        k += h
        o = int(input("Masukkan barang yang ingin dibeli (1/2/3/4) : "))
    elif o == 2 or o == "Kemeja":
        h = int(50000)
        print("Kemeja telah ditambahkan")
        print()
        k += h
        o = int(input("Masukkan barang yang ingin dibeli (1/2/3/4) : "))
    elif o == 3 or o == "Jas":
        h = int(100000)
        print("Jas telah ditambahkan")
        print()
        k += h
        o = int(input("Masukkan barang yang ingin dibeli (1/2/3/4) : "))
    else:
        break
print("Total: ",k)