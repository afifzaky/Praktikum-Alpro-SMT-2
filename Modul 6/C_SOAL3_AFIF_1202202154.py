'''
3. Buatlah sebuah list berisi 5 data bebas. Lalu buatlah sebuah fungsi bernama
getIndex yang akan mengembalikan data di index yang ditentukan oleh sebuah
input. Lalu buatlah exception ketika index yang diinputkan melebihi jumlah data
yang ada pada list. (Hint : Gunakan exception IndexError!)
'''

iniapa = ["Afif","Seorang","VVota","Ngidol","JKT48"]
def getIndex():
    yoo = int(input("Inputz Index : "))
    try:
        print("Data Index Ke-", yoo, "Adalah", iniapa[yoo])
    except IndexError:
        print("Index Tidak Ditemukan zzz")

getIndex()