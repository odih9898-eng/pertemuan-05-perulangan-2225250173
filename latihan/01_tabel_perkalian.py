# ==========================================
# 01_tabel_perkalian.py
# Contoh Kode: Menampilkan Tabel Perkalian
# ==========================================

print("=== PROGRAM TABEL PERKALIAN ===")

# Input dari user
angka = int(input("Masukkan angka perkalian: "))
batas = int(input("Masukkan batas perkalian: "))

print(f"\nTabel Perkalian {angka}:")
print("-" * 20)

# Perulangan for
for i in range(1, batas + 1):
    hasil = angka * i
    print(f"{angka} x {i:<2} = {hasil}")

print("-" * 20)