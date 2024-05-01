Nama : Rido' Ul Ambari
NIM : SI20230030

#Daftar barang beserta harganya
daftar_barang = {
    "keyboard": 100000,
    "mouse" : 90000,
    "hardisk": 120000,
    "flashdisk" : 40000,
    "microphone" : 50000,
    "speaker" : 65000,
    "proyektor" : 700000
}

#Menampilkan daftar barang
print("---------------")
print("Daftar barang : ")
print("---------------")
for barang, harga in daftar_barang.items():
    print(f"{barang}: Rp{harga}")
print("-------------------")

#Input jumlah barang yang dibeli
total_belanja = 0
jumlah_barang = int(input("\nMasukan jumlah barang yang dibeli : "))

#Menghitung total belanjaan 
for i in range(jumlah_barang) :
    barang = input(f"Masukan nama barang ke-{i+1} : ")
    if barang in daftar_barang:
        total_belanja += daftar_barang[barang]
    else :
        print(f"{barang} tidak ada dalam daftar")
        
#Menampilkan total belanjaan
print("---------------------")
print(f"Total belanjaan anda = Rp{total_belanja}")
bayar = int(input("\nBayar : Rp "))
kembali = bayar-total_belanja
if bayar > total_belanja :
    print(f"Kembalian = Rp {kembali}")
    print("\nTerima kasih :)")
elif bayar == total_belanja :
    print("\nUangnya pas yaa")
    print("Terima kasih :)")
else :
    print("\nUangnya tidak cukup silahkan kembali dengan membawa uang!!")
