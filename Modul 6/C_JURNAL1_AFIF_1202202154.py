'''
1. Buatlah sebuah program yang hanya dapat menerima sebuah inputan angka, dan
jika program diinputkan dengan string maka program akan menangkap error
tersebut!
'''
try:
    aeee = int(input("Masukkan Sebuah Angka : "))
except ValueError:
    print("Hanya Menerima Angka")
else:
    print(aeee)