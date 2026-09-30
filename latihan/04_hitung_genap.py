# ==========================================
# 04_hitung_genap.py
# Contoh Kode: Menyaring dan Menjumlahkan Bilangan Genap
# ==========================================

print("=== PROGRAM HITUNG BILANGAN GENAP ===")

# 1. Validasi Input batas
batas = int(input("Masukkan batas akhir angka (> 0): "))
while batas <= 0:
    print(" [ERROR] Batas harus lebih dari 0!")
    batas = int(input("Masukkan batas akhir angka (> 0): "))

total_genap = 0
banyak_genap = 0

print(f"\nBilangan genap dari 1 hingga {batas}:")
# 2. Perulangan for dan filter if
for i in range(1, batas + 1):
    if i % 2 == 0:  # Cek sisa bagi dengan 2 adalah 0 (Genap)
        print(f"-> Angka genap: {i}")
        total_genap += i
        banyak_genap += 1

print("-" * 30)
print(f"Banyaknya bilangan genap : {banyak_genap}")
print(f"Total jumlah bilangan genap: {total_genap}")