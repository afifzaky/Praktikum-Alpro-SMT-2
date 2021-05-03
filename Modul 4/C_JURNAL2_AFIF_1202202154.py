class Bangunruang:
    def K1(self,sisi1):
        v = sisi1 * sisi1 * sisi1
        l = 6 * sisi1 * sisi1
        k = 12 * sisi1
        print("==================================")
        print("Kubus 1")
        print(f"volume          : {v} cm^3 ")
        print(f"Luas Permukaan  : {l} cm^2 ")
        print(f"Keliling        : {k} cm")

    def K2(self,sisi2):
        v = sisi2 * sisi2 * sisi2
        l = 6 * sisi2 * sisi2
        k = 12 * sisi2
        print("==================================")
        print("Kubus 2")
        print(f"volume          : {v} cm^3 ")
        print(f"Luas Permukaan  : {l} cm^2 ")
        print(f"Keliling        : {k} cm ")
        print("==================================")
        
print("================================")
sisi1 = int(input("Masukan sisi Kubus 1 : "))
sisi2 = int(input("Masukan Sisi Kubus 2 : "))

B = Bangunruang()
B.K1(sisi1)
B.K2(sisi2)