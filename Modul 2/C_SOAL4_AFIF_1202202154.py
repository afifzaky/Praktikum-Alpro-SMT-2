"""
No 4

Namamu adalah Pras, kamu memiliki adik bernama Setyo yang masih duduk di
bangku TK, Setyo ingin mengenal nama-nama hari dalam satu minggu sesuai
urutannya, kamu sebagai kakak yang baik, kamu pasti akan membantu adikmu.
Buatlah program untuk membantu adikmu belajar nama nama hari dalam 1
minggu, seperti hari ke 1 adalah hari Senin, hari ke 2 adalah hari selasa, dan
seterusnya hingga hari minggu. karena hari hanya ada 7 maka hari ke 8 dan
seterusnya dianggap tidak ada.
"""
hari = int(input("Masukkan nomor hari : "))

if hari == 1:
    print("Hari ke-",hari,"adalah hari senin")
elif hari == 2:
    print("Hari ke-",hari,"adalah hari selasa")
elif hari == 3:
    print("Hari ke-",hari,"adalah hari rabu")
elif hari == 4:
    print("Hari ke-",hari,"adalah hari kamis")
elif hari == 5:
    print("Hari ke-",hari,"adalah hari jum'at")
elif hari == 6:
    print("Hari ke-",hari,"adalah hari sabtu")
elif hari == 7:
    print("Hari ke-",hari,"adalah hari minggu")
else:
    print("Tidak ada hari ke-",hari)