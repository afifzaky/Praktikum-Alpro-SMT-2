'''
No 5
Lab DASPRO ingin kamu membuat program voting untuk asprak terimut, di program
tersebut kamu diminta mengisi nama pemilih baru memilih. Program tersebut
memiliki fungsi khusus yaitu dapat melihat nama pemilih, dan asprak yang dipilih,
tapi demi keselamatan bangsa dan negara maka jika ingin mengakses fungsi
tersebut user harus memasukkan token yang diberikan oleh admin.
'''
voting = []
database = []

while True:
    print("""
    === DASPRO VOTING === 
    1. Voting 
    2. Database 
    
    0. Exit 
    """)
    pilihan = int(input("Masukan Pilihan Anda : "))
    if pilihan == 1:
        nm = input("Masukkan Nama Anda : ")
        database.append(nm)
        print("""
        === KANDIDAT ASPRAK TERUwU ===
        1. XAX
        2. ADV
        3. NOP
        4. HAS
        5. IAN 
        """)
        kandidat = int(input("Masukkan Pilihan Anda (1/2/3/4) : ? "))
        if kandidat == 1:
            voting.append("XAX")
        elif kandidat == 2:
            voting.append("ADV")
        elif kandidat == 3:
            voting.append("NOP")
        elif kandidat == 4:
            voting.append ("HAS")
        elif kandidat == 5:
            voting.append("IAN")
        print(f"{nm} Terima Kasih Udah Memilih Semoga Berkah")
    elif pilihan == 2:
        ps = input("Masukkan Token : ")
        if ps == "d4spr0":
            for k in range(len(database)):
                print(database[k] + "\tpilih\t" + voting [k])
        else:
            print("YAH TOKEN SALAH YAAAAAAAAAAAAAAAAAAAA!!")
    elif pilihan == 0:
        print("Akhirnya Keluar Juga")
        break