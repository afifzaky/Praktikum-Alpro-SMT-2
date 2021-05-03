"""
No 3
Anas dan teman-temannya ingin mendapatkan seluruh SIM yang berlaku di
Indonesia, namun Anas tidak tahu syarat umur untuk setiap SIM. Kamu
sebagai programmer yang ahli diminta bantuan Anas untuk membuat program
yang bisa menerima input umur lalu menampilkan SIM apa saja yang bisa
didapatkan dengan ketentuan sebagai berikut:

SIM                                  Syarat Umur 
A                                    Umur >= 17
A UMUM                               Umur >= 20
B                                    Umur >= 23                                
C                                    Umur >= 17

u = umur
"""
u = int(input("Masukkan umur anda: "))

if u >=17 and u <20:
    print("Anda bisa membuat SIM A, SIM C")
elif u >= 20 and u <23:
    print("Anda bisa membuat SIM A, SIM A UMUM, SIM C")
elif u >= 23:
    print("Anda bisa membuat SIM A, SIM A UMUM, SIM B, SIM C")
else:
    print("Anda belum bisa membuat SIM")