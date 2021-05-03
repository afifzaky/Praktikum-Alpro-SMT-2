'''
No 4
Farras merupakan pemilik toko buah alpukat. Harga per-kilo untuk buah alpukat
yang dijual adalah Rp.8000. Toko buah alpukat Farras selalu dibanjiri oleh
pembeli karena ia memberikan diskon sebesar 15% untuk pembelian buah
alpukat tanpa minimal pembelian. Bantulah Farras membuat program dengan
inputan user yang dapat menghitung harga total pembelian buah alpukat
sebelum dan setelah diskon!
'''

harga_per_kilo = int(8000)
berat = int(input("Masukkan berat buah : "))

harga_normal = harga_per_kilo*berat
print ("Harga sebelum diskon :",harga_normal)
harga_diskon = harga_normal*0.85
print ("Harga setelah diskon :",harga_diskon)