# ==========================================
# 03_validasi_input.py
# Contoh Kode: Validasi Input Menggunakan While
# ==========================================

print("=== PROGRAM VALIDASI INPUT N ===")

# Input awal
n = int(input("Masukkan nilai N (harus positif N > 0): "))

# Perulangan while akan terus berjalan jika n <= 0
while n <= 0:
    print(" [ERROR] Input tidak valid! Nilai N harus lebih besar dari 0.")
    n = int(input("Masukkan kembali nilai N (N > 0): "))

print(f"\n[SUCCESS] Input valid diterima: N = {n}")

# Lanjutkan dengan hitung jumlah seperti di Latihan 2
total = 0
for i in range(1, n + 1):
    total += i

print(f"Hasil penjumlahan 1 sampai {n} = {total}")