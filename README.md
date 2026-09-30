# Pertemuan 05 Perulangan Python

**Nama:** Odih Hidayat  
**NIM:** 2225250173  
**Kelas:** Pendidikan Matematika  
**Mata Kuliah:** Algoritma dan Pemrograman  
**Dosen Pengampu:** [Dr. Aan Hendrayana, S.Si., M.Pd.]  

---

## Tujuan
Menggunakan `for` dan `while` untuk menyelesaikan masalah iteratif.

---

## Penjelasan Program & Kode Lengkap

### 1. Folder Latihan (`latihan/`)

Folder ini berisi skrip latihan dasar perulangan:

* **`01_tabel_perkalian.py`**
  * **Penjelasan:** Menampilkan tabel perkalian dari suatu angka berdasarkan batas perkalian yang ditentukan.
  * **Kode Program:**
    ```python
    print("--- Latihan 1: Tabel Perkalian ---")
    angka = int(input("Masukkan angka: "))
    batas = int(input("Masukkan batas perkalian: "))

    print(f"\nTabel Perkalian {angka}:")
    for i in range(1, batas + 1):
        print(f"{angka} x {i} = {angka * i}")
    ```

* **`02_jumlah_bilangan.py`**
  * **Penjelasan:** Menhitung akumulasi total penjumlahan deret angka dari 1 sampai N.
  * **Kode Program:**
    ```python
    print("--- Latihan 2: Jumlah Bilangan 1 sampai N ---")
    n = int(input("Masukkan nilai N: "))
    total = 0

    for i in range(1, n + 1):
        total += i

    print(f"Jumlah akumulasi dari 1 hingga {n} adalah: {total}")
    ```

* **`03_validasi_input.py`**
  * **Penjelasan:** Memvalidasi input agar bernilai positif (N > 0) menggunakan perulangan `while`.
  * **Kode Program:**
    ```python
    print("--- Latihan 3: Validasi Input ---")
    n = int(input("Masukkan nilai n positif (n > 0): "))

    while n <= 0:
        print("Input tidak valid! Nilai n harus lebih besar dari 0.")
        n = int(input("Masukkan kembali nilai n: "))

    print(f"Input valid diterima: n = {n}")
    ```

* **`04_hitung_genap.py`**
  * **Penjelasan:** Menyaring dan menjumlahkan seluruh angka genap dari rentang 1 sampai N.
  * **Kode Program:**
    ```python
    print("--- Latihan 4: Hitung Bilangan Genap ---")
    batas_akhir = int(input("Masukkan batas akhir angka: "))
    total_genap = 0

    print("Bilangan genap yang ditemukan:")
    for i in range(1, batas_akhir + 1):
        if i % 2 == 0:
            print(i, end=" ")
            total_genap += i

    print(f"\nTotal penjumlahan bilangan genap = {total_genap}")
    ```

---

### 2. Folder Kuis (`kuis/`)

* **`kuis2_deret_aritmetika.py`**
  * **Penjelasan:** Meminta input suku pertama (`a`), beda (`d`), dan banyak suku (`n`). Memvalidasi `n > 0`, lalu menghitung serta menampilkan tiap suku beserta total jumlah deretnya secara iteratif.
  * **Kode Program:**
    ```python
    print("Deret Aritmetika")

    a = float(input("Suku pertama a: "))
    d = float(input("Beda d: "))
    n = int(input("Banyak suku n: "))

    while n <= 0:
        print("Jumlah suku harus positif (n > 0)!")
        n = int(input("Banyak suku n: "))

    total = 0.0
    print("\nSuku-suku deret:")
    for i in range(n):
        suku = a + i * d
        total += suku
        print(f"Suku ke-{i + 1}: {suku}")

    print(f"\nJumlah seluruh suku = {total:.2f}")
    ```

---

## Algoritma Kuis 2
1. Menerima input suku pertama (`a`) dan beda (`d`) sebagai bilangan riil (`float`).
2. Menerima input banyak suku (`n`) sebagai bilangan bulat (`int`).
3. Memeriksa nilai `n`. Jika `n <= 0`, program melakukan perulangan `while` untuk meminta pengguna memasukkan ulang nilai `n` hingga bernilai positif (`n > 0`).
4. Menginisialisasi variabel `total = 0.0` untuk menampung jumlah akumulasi seluruh suku.
5. Melakukan perulangan `for` sebanyak `n` kali (dari `i = 0` sampai `n - 1`).
6. Di dalam perulangan `for`, menghitung nilai suku dengan rumus `suku = a + i * d`, mencetak nilai suku tersebut, dan menambahkan nilainya ke variabel `total`.
7. Setelah perulangan `for` selesai, mencetak hasil penjumlahan akhir (`total`) dengan format dua angka di belakang koma (`.2f`).

---

## Hasil Pengujian

| Test Case | Input (a, d, n) | Keluaran Diharapkan | Keluaran Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Test Case 1** | a = 2, d = 3, n = 5 | Suku: 2, 5, 8, 11, 14<br>Jumlah: 40 | Suku ke-1: 2.0<br>Suku ke-2: 5.0<br>Suku ke-3: 8.0<br>Suku ke-4: 11.0<br>Suku ke-5: 14.0<br>Jumlah seluruh suku = 40.00 | Sesuai |
| **Test Case 2** | a = 10, d = -2, n = 4 | Suku: 10, 8, 6, 4<br>Jumlah: 28 | Suku ke-1: 10.0<br>Suku ke-2: 8.0<br>Suku ke-3: 6.0<br>Suku ke-4: 4.0<br>Jumlah seluruh suku = 28.00 | Sesuai |
| **Test Case 3** | a = 1.5, d = 0.5, n = 3 | Suku: 1.5, 2.0, 2.5<br>Jumlah: 6.0 | Suku ke-1: 1.5<br>Suku ke-2: 2.0<br>Suku ke-3: 2.5<br>Jumlah seluruh suku = 6.00 | Sesuai |
| **Validasi Input** | n = -2, lalu n = 0, lalu n = 3 | Menolak n <= 0, meminta input kembali sampai n > 0 | Menampilkan pesan error dan meminta input n kembali hingga valid | Sesuai |

---

## Refleksi Teknis
- **Bagian penentu jumlah iterasi:** Variabel `n` yang dimasukkan ke dalam `range(n)` pada perulangan `for i in range(n)`.
- **Inisialisasi total sebelum loop:** Variabel `total` diinisialisasi sebelum perulangan agar akumulasi penjumlahan suku dapat terus bertambah bertahap dari iterasi pertama hingga terakhir. Jika diletakkan di dalam loop, nilai `total` akan selalu tereset menjadi `0` di setiap iterasi.
- **Validasi `n` menggunakan `while`:** Perulangan `while` lebih sesuai untuk validasi input karena jumlah kesalahan input pengguna tidak dapat diprediksi secara pasti sampai pengguna memasukkan nilai yang valid (`n > 0`).
- **Bukti loop berhenti tepat:** Fungsi `range(n)` secara pasti berjalan dari indeks `i = 0` hingga `i = n - 1`, sehingga eksekusi pernyataan di dalam perulangan terjadi tepat sebanyak `n` kali.