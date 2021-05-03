"""
No 5

Lauriel penasaran dengan BMI berat badannya. Namun, Lauriel bingung kategori
dari nilai BMI. Buatlah program python yang dapat mengetahui kategori BMI
ketika memasukan berat badan dan tinggi badan. Acuan rumus dan kategori
nilai BMI sebagai berikut.

Rumus Menghitung BMI

BMI = Berat badan / (Tinggi badan)^2

BMI          Kategori
< 18.5       Underweight
18.5 - 24.9  Normal
25 - 29.9    Overweight
30 - 34.9    Obese
35 - 39.9    Very Obese
> 40         Extermely Obese
b = berat     t = tinggi
"""

b = float(input("Masukkan berat badan dalam kg: "))
t = float(input("Masukkan tinggi badan dalam m: "))

bmi = b/(t**2)

if bmi < 18.5:
    print(bmi,"termasuk kategori Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print(bmi,"termasuk kategori Normal")
elif bmi >= 25 and bmi <= 29.9:
    print(bmi<"termasuk kategori Overweight")
elif bmi >= 30 and bmi <= 34.9:
    print(bmi,"termasuk kategori Obese")
elif bmi >= 35 and bmi <= 39.9:
    print(bmi,"termasuk kategori Very Obese")
elif bmi >= 40:
    print(bmi,"termasuk kategori Extremely Obese")
else:
    print("tidak termasuk kategori")