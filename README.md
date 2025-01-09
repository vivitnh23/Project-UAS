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

# Kode Program 
```python
from class_data.ticket_data import TicketData
from class_process.ticket_process import TicketProcess
from class_view.ticket_view import TicketView


def main():
    data = TicketData()
    view = TicketView()
    process = TicketProcess(data.get_tickets())
    running = True

    while running:
        print("\n=== Program Pembelian Tiket ===")
        print("1. Input Data")
        print("2. Tampilkan Data Tiket")
        print("3. Cari Data Tiket")
        print("4. Keluar Program")
        choice = input("Pilih menu: ")

        if choice == "1":  # Input Data
            try:
                view.display_tickets(data.get_tickets())
                ticket_name = input("Masukkan nama tiket yang ingin dibeli: ")
                quantity = int(input("Masukkan jumlah tiket: "))
                process.validate_input(ticket_name, quantity)
                total = process.calculate_total(ticket_name, quantity)
                summary = {
                    "Nama Tiket": ticket_name,
                    "Jumlah Tiket": quantity,
                    "Total Harga": f"Rp {total}"
                }
                view.display_summary(summary)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

        elif choice == "2":  # Tampilkan Data Tiket
            print("\n=== Daftar Harga Tiket ===")
            view.display_tickets(data.get_tickets())

        elif choice == "3":  # Cari Data Tiket
            try:
                search_ticket = input("Masukkan nama tiket yang ingin dicari: ")
                tickets = data.get_tickets()
                if search_ticket in tickets:
                    print(f"Tiket '{search_ticket}' ditemukan dengan harga Rp {tickets[search_ticket]}")
                else:
                    print(f"Tiket '{search_ticket}' tidak ditemukan.")
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

        elif choice == "4":  # Keluar Program
            print("Keluar dari program. Terima kasih!")
            running = False

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
```

# Output Program 
````
=== Program Pembelian Tiket ===
1. Input Data
2. Tampilkan Data Tiket
3. Cari Data Tiket
4. Keluar Program
Pilih menu: 1

Daftar Tiket yang Tersedia:
------------------------------
VIP: Rp 500000
Regular: Rp 200000
Economy: Rp 100000
------------------------------
Masukkan nama tiket yang ingin dibeli: VIP
Masukkan jumlah tiket: 3

Ringkasan Pembelian:
------------------------------
Nama Tiket: VIP
Jumlah Tiket: 3
Total Harga: Rp 1500000
------------------------------

=== Program Pembelian Tiket ===
1. Input Data
2. Tampilkan Data Tiket
3. Cari Data Tiket
4. Keluar Program
Pilih menu: 2

=== Daftar Harga Tiket ===

Daftar Tiket yang Tersedia:
------------------------------
VIP: Rp 500000
Pilih menu: 2

=== Daftar Harga Tiket ===

Daftar Tiket yang Tersedia:
------------------------------
VIP: Rp 500000
=== Daftar Harga Tiket ===

Daftar Tiket yang Tersedia:
------------------------------
VIP: Rp 500000

Daftar Tiket yang Tersedia:
------------------------------
VIP: Rp 500000
Daftar Tiket yang Tersedia:
------------------------------
VIP: Rp 500000
------------------------------
VIP: Rp 500000
VIP: Rp 500000
Regular: Rp 200000
Economy: Rp 100000
Regular: Rp 200000
Economy: Rp 100000
Economy: Rp 100000
------------------------------
------------------------------

=== Program Pembelian Tiket ===
1. Input Data
2. Tampilkan Data Tiket
3. Cari Data Tiket
4. Keluar Program
Pilih menu: 3
Masukkan nama tiket yang ingin dicari: VIP
Tiket 'VIP' ditemukan dengan harga Rp 500000

=== Program Pembelian Tiket ===
1. Input Data
2. Tampilkan Data Tiket
3. Cari Data Tiket
4. Keluar Program
Pilih menu: 4
Keluar dari program. Terima kasih!
PS C:\Users\hp\Documents\Lab praktikum\Project UAS>
````

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
