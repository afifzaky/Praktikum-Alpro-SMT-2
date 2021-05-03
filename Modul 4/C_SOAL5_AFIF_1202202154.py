'''
No 5
Alice merupakan sebuah mahasiswa magang di sebuah startup. Ia diminta untuk
membuat sebuah program untuk login dan logout menggunakan Class dan Fungsi.
Program tersebut akan mengecek apabila username dan password yang diinputkan
telah benar maka user bisa login. Apabila user memilih logout tanpa melakukan login,
program akan menampilkan pesan bahwa harus melakukan login terlebih dahulu.
'''
class aplikasi:

    def masuk(self):
        usr = input("Username : ")
        pw = input("Password : ")

        if usr == "alpro" and pw == "daspro":
            print("""
            Login Success
            Welcome To My App !
            """)
    def keluar(self):
        print("You're successfully logged out. Thank You For Using Me")

if __name__ == "__main__":
    apip = False
    while True:
        print("""
        User Testing Application
        1.login
        2.logout
        """)
        input_pengguna = int(input("Choose Menu ? : "))

        if input_pengguna == 1:
            app = aplikasi()
            app.masuk()
            apip = True
            print()
        elif input_pengguna == 2 and apip == False:
            print("""
            !!! Login First !!!
            """)
        elif input_pengguna == 2 and apip == True:
            app.keluar()
            break
        else:
            print("!! No Option !!")