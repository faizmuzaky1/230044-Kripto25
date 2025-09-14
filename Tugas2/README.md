# Tugas 2 Kriptografi - Program Hill Cipher

**Nama:** Muhamad Faiz Muzaki
**NPM:** 140810230044

## Penjelasan Alur Program

Program ini adalah implementasi dari algoritma Hill Cipher yang memiliki tiga fitur utama: enkripsi, dekripsi, dan pencarian kunci (known-plaintext attack).

1.  **Enkripsi**: Program meminta input berupa plaintext dan matriks kunci 2x2. Teks akan diubah menjadi angka, lalu dikalikan dengan matriks kunci dalam modulo 26 untuk menghasilkan ciphertext.
2.  **Dekripsi**: Program meminta ciphertext dan matriks kunci. Program akan terlebih dahulu mencari matriks invers dari kunci tersebut (termasuk mencari invers modular dari determinan). Kemudian, ciphertext dikalikan dengan matriks invers untuk mengembalikan plaintext asli.
3.  **Pencarian Kunci**: Pengguna memasukkan 4 karakter plaintext dan 4 karakter ciphertext yang bersesuaian. Program akan membentuk matriks P (dari plaintext) dan C (dari ciphertext), lalu menghitung kunci K dengan rumus `K = C * P⁻¹ mod 26`.

## Screenshot Running Program

Berikut adalah screenshot dari setiap fungsionalitas program:

**1. Tampilan Menu Utama**
![Menu Utama](https://github.com/faizmuzaky1/230044-Kripto25/blob/main/Tugas2/screenshot/Hasil_Cari_kunci.png?raw=true)

**2. Contoh Proses Enkripsi**
![Proses Enkripsi](link-ke-gambar-enkripsi.png)

**3. Contoh Proses Dekripsi**
![Proses Dekripsi](link-ke-gambar-dekripsi.png)

**4. Contoh Proses Pencarian Kunci**
![Pencarian Kunci](link-ke-gambar-cari-kunci.png)
