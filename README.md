# Nama : Vivit Nurul Hidayah
# NIM : 312410110
# Kelas : TI.24.A1
# Mata Kuliah : Bahasa Pemrograman (Project-UAS)

# Program Pembelian Tiket Konser
# Deskripsi Program 
Program ini adalah aplikasi berbasis terminal yang digunakan untuk membeli tiket. Program ini menggunakan pendekatan berbasis kelas dengan tiga komponen utama:

- TicketData: Berfungsi untuk mengelola data tiket yang tersedia.
- TicketProcess: Bertanggung jawab atas validasi input pengguna dan perhitungan total harga tiket.
- TicketView: Menangani semua output, seperti menampilkan daftar tiket, pesan error, dan ringkasan pembelian.

# Cara Kerja Program 
1. Inisialisasi Kelas
- Program memulai dengan menginisialisasi tiga kelas utama:
    - TicketData: Menyediakan data tiket yang tersedia.
    - TicketProcess: Digunakan untuk memproses input pengguna.
    - TicketView: Digunakan untuk menampilkan data atau pesan kepada pengguna.

2. Menampilkan Daftar Tiket
- Program memanggil metode display_tickets dari kelas TicketView untuk menampilkan daftar tiket yang tersedia beserta detailnya, seperti nama dan harga tiket.

3. Input Pengguna
- Program meminta pengguna memasukkan:
    - Nama tiket: Nama tiket yang ingin dibeli.
    - Jumlah tiket: Jumlah tiket yang ingin dibeli.

4. Validasi Input
- Validasi Nama Tiket:
    - Program memeriksa apakah nama tiket yang dimasukkan oleh pengguna sesuai dengan daftar tiket yang tersedia.
    - Jika tiket tidak ditemukan, program akan menampilkan pesan error.
- Validasi Jumlah Tiket:
    - Program memeriksa apakah jumlah tiket yang dimasukkan valid (misalnya, jumlah positif dan tidak melebihi batas yang ditentukan).

5. Perhitungan Total Harga
- Jika validasi berhasil, program akan menghitung total harga tiket menggunakan metode calculate_total dari kelas TicketProcess.

6. Pembuatan Ringkasan Pembelian
- Program membuat ringkasan pembelian dalam bentuk dictionary, mencakup:
    - Nama tiket.
    - Jumlah tiket.
    - Total harga.

7. Menampilkan Ringkasan Pembelian
- Program memanggil metode display_summary dari kelas TicketView untuk menampilkan ringkasan pembelian kepada pengguna.

8. Penanganan Kesalahan
- Jika terjadi kesalahan selama proses (seperti input yang tidak valid atau nama tiket tidak ditemukan), program akan menangkapnya melalui blok try-except dan menampilkan pesan error menggunakan metode display_message.

9. Mengakhiri Program
- Setelah semua langkah selesai, program mengakhiri eksekusi.
