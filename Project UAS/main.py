from class_data.ticket_data import TicketData
from class_process.ticket_process import TicketProcess
from class_view.ticket_view import TicketView

def main():
    # Inisialisasi kelas
    data = TicketData()
    view = TicketView()
    process = TicketProcess(data.get_tickets())

    try:
        # Tampilkan daftar tiket
        view.display_tickets(data.get_tickets())

        # Input pengguna
        ticket_name = input("Masukkan nama tiket yang ingin dibeli: ")
        quantity = int(input("Masukkan jumlah tiket: "))

        # Validasi input
        process.validate_input(ticket_name, quantity)

        # Hitung total harga
        total = process.calculate_total(ticket_name, quantity)
        summary = {
            "Nama Tiket": ticket_name,
            "Jumlah Tiket": quantity,
            "Total Harga": f"Rp {total}"
        }

        # Tampilkan ringkasan pembelian
        view.display_summary(summary)

    except ValueError as e:
        view.display_message(f"Error: {e}")
    except Exception as e:
        view.display_message(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
