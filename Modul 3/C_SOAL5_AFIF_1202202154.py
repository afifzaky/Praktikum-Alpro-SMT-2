'''
Latihan Soal No 5

Tami dan Boi akan melakukan pertandingan suit Batu, Gunting, Kertas (B/G/K).
Disini mereka bisa memasukkan banyak ronde mereka bermain. Dan diakhir
akan ditampilkan siapa yang menang dan berapa banyak ronde yang
dimenangkan. Gunakan konsep For Loop atau While Loop!
'''
r = int(input("Banyak Ronde ? "))

tami_menang = 0
boi_menang = 0

for i in range(r):
    tami = input("Tami pilih apa? (B/G/K) ")
    boi  = input("Boi pilih apa? (B/G/K) ")
    if tami == "B" and boi == "G":
        tami_menang += 1 
        print()
    elif tami == "G" and boi == "K":
        tami_menang += 1
        print()
    elif tami == "K" and boi == "B":
        tami_menang += 1
        print()
    elif tami == boi:
        continue
    else:
        boi_menang += 1
        print()
if tami_menang > boi_menang:
    print("Selamat tami menang sebanyak",tami_menang,"ronde")
elif tami_menang == boi_menang:
    print("SERI")
else:
    print("Selamat boi menang sebanyak",boi_menang,"ronde")