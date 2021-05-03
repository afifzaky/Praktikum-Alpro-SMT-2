'''
Jurnal No 1

Buatlah sebuah program login yang menampilkan inputan dari username
dan password, dengan username "alpro", dan password "daspro123".
Jika inputan username atau password salah maka akan menampilkan
"Login gagal. Sisa percobaan login sebanyak n" dan program akan
mengulang sampai username dan password benar, namun batas
percobaan login ditentukan sebanyak 3 kali. Dan jika inputan username
dan password benar maka akan menampilkan "Selamat anda berhasil
login!"

k = Kesempatan
c = coba
l = login
u = username
p = password
'''

k = 3
c = 0
l = False

for i in range(k):
    u = str(input("Masukkan username anda : "))
    p = str(input("Masukkan password anda : "))
    if u == "alpro" and p == "daspro123":
        l = True
        print("Selamat, anda berhasil login!")
        break
    else:
        c+= 1
        if k - c!= 0:
            print("Login gagal. Sisa percobaan login sebanyak",k - c)
if l == False and k == c:
    print("Yah Salah 3 kali ya gan, hehe kasian, pal pale pale")