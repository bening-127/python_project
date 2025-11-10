# #data Int
# a=3
# print("haloow")
# print("tampilkan angka: ",(a))

# #data tuple
# b = 4,5
# print("tampilkan angka: ",(b))

# #data str
# nama = "sinta"
# print("tampilkan nama: ",(nama))

# #data list
# angka=[1,2,3,4,5]
# print((angka))
# angka.append(7)
# print(angka)

# # 1. Variabel dan Tipe Data
# int_var = 10
# float_var = 3.14
# str_var = "Hello"
# list_var = [1, 2, 3]

# print("Tipe data int_var:", (int_var))
# print("Tipe data float_var:", (float_var))
# print("Tipe data str_var:", (str_var))
# print("Tipe data list_var:", (list_var))

# print("="*40)

# #2. List dan Manipulasi
# belanja = ["beras", "minyak", "telur"]

# #Tambahkan gula dan kopi
# belanja.append("gula")
# belanja.append("kopi")

# #Tampilkan semua item dengan perulangan
# print("Daftar Belanja:")
# for item in belanja:
#     print("-", item)

# print("="*40)

# # 3. Dictionary
# harga_belanja = {
#     "beras": 12000,
#     "minyak": 17000,
#     "telur": 24000,
#     "gula": 15000,
#     "kopi": 20000
# }

# # Hitung total harga
# total = sum(harga_belanja.values())

# print("Daftar Harga Belanja:")
# for barang, harga in harga_belanja.items():
#     print(f"{barang} : Rp{harga}")

# print("Total harga belanja:", total)

# print("="*40)

# # 4. Fungsi
# import math

# def luas_keliling_lingkaran(r):
#     luas = math.pi * r**2
#     keliling = 2 * math.pi * r
#     return luas, keliling

# # Contoh penggunaan
# r = 7
# luas, keliling = luas_keliling_lingkaran(r)
# print(f"Luas lingkaran (r={r}) = {luas:.2f}")
# print(f"Keliling lingkaran (r={r}) = {keliling:.2f}")

# print("="*40)

# # 5. Percabangan
# while True:
#     usia = int(input("Masukkan usia (ketik -1 untuk keluar): "))

#     if usia == -1:
#         print("Program selesai. Terima kasih!")
#         break  

#     if 0 <= usia <= 13:
#         print("Anak-anak")
#     elif 14 <= usia <= 24:
#         print("Remaja")
#     elif 25 <= usia <= 49:
#         print("Dewasa")
#     elif usia > 50:
#         print("Lansia")
#     else:
#         print("Usia tidak valid")

#     print() 
