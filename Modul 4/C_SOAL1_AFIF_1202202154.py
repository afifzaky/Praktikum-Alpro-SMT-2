'''
No 1
Ananda menginginkan sebuah program sederhana untuk membantu dia
mengerjakan soal matematika. Buatlah sebuah program menggunakan User Input
dan Fungsi pengembalian nilai yang dapat menghitung perkalian 3 bilangan bulat.
'''



def pertambahan(a,b,c):
    return a + b + c 
def perkurangan(x,y,z):
    return a - b - c 
def perkalian(x,y,z):
    return a * b * c 
def pembagian(x,y,z):
    return a / b / c

a = int(input("Masukan Bil 1 : "))
b = int(input("Masukan Bil 2 : "))
c = int(input("Masukan Bil 3 : "))

print("Hasil Pertambahan Ketiga Bilangan Bulat Adalah",pertambahan(a,b,c))
print("Hasil Perkurangan Ketiga Bilangan Bulat Adalah",perkurangan(a,b,c))
print("Hasil Perkalian Ketiga Bilangan Bulat Adalah",perkalian(a,b,c))
print("Hasil Pembagian Ketiga Bilangan Bulat Adalah",pembagian(a,b,c))