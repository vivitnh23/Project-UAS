class TicketView:
    @staticmethod
    def display_tickets(tickets):
        print("\nDaftar Tiket yang Tersedia:")
        print("-" * 30)
        for name, price in tickets.items():
            print(f"{name}: Rp {price}")
        print("-" * 30)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_summary(summary):
        print("\nRingkasan Pembelian:")
        print("-" * 30)
        for key, value in summary.items():
            print(f"{key}: {value}")
        print("-" * 30)