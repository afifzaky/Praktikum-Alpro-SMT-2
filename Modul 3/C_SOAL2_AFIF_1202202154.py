'''
Latihan Soal No 2

Naynay ingin membuat sebuah countdown yang simple menggunakan while
Python. Ketika countdown mencapai angka 1, maka yang ditampilkan adalah
"It's enough.". Input user harus lebih dari angka 1. Buatlah program tersebut
bersama Naynay dan gunakan konsep For Loop atau While Loop!

c = countdown
'''

print("== COUNTDOWN SIMPLE ==")
c = 5
while (c >= 0):
    print(c)
    c = c - 1
    if c == 1:
        print("It's enough")
        break