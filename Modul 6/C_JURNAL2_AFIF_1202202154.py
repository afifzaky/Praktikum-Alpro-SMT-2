'''
Buatlah sebuah program dimana program tersebut akan file .txt ini dan akan
mencetak informasi yang ada di dalamnya
'''
a = open("LOVE ALPRO.txt","r")

b = a.read()
print(b)
a.close()