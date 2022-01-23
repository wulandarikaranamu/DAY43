nilai = int(input("masukkan panjang list :"))
lst = []
print("list awal : {}")

for i in range(nilai):
    hasil = int(input("masukkan nilai list pada indeks ke-" + str(i) + ":"))
    lst.insert(i,hasil)

print(lst)
