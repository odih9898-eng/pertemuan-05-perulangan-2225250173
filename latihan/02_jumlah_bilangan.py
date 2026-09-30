# ==========================================
# 02_jumlah_bilangan.py
# Contoh Kode: Menjumlahkan Deret Bilangan 1 sampai N
# ==========================================

print("=== PROGRAM JUMLAH BILANGAN ===")

n = int(input("Masukkan banyak bilangan (N): "))

# Variabel penampung akumulasi (inisialisasi di luar loop)
total = 0

print("\nProses Penjumlahan:")
for i in range(1, n + 1):
    total += i
    # Menampilkan jalannya proses akumulasi per langkah
    print(f"Iterasi ke-{i}: total sementara = {total}")

print("-" * 30)
print(f"Total akhir jumlah 1 sampai {n} = {total}")