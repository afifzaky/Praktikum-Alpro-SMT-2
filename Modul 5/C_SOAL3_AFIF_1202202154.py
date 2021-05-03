'''
No 3
Udin adalah seorang mahasiswa baru Telkom University yang ingin mendata setiap
nama teman yang baru ditemuinya. Ia ingin membuat sebuah program dimana dia
dapat menginput nama-nama tersebut ke dalam sebuah program, dan ia dapat
menginput “selesai” apabila ia telah selesai menginput nama sehingga program
akan berhenti dan akan menampilkan daftar nama teman baru yang ia temui hari ini.
Bantulah Udin mencapai tujuan tersebut! (Hint : Gunakan List dan Perulangan
While)
'''

print("\t\tNOTES TEMAN BARU ")

tmn = []

while True:
    nm = input("Masukkan Nama Teman Baru : ")
    if nm == "selesai":
        break
    else:
        tmn.append(nm)
print("\t\t\t Teman-Teman Baru!")
print(tmn)