class TicketProcess:
    def __init__(self, tickets):
        self.tickets = tickets

    def validate_input(self, ticket_name, quantity):
        if ticket_name not in self.tickets:
            raise ValueError("Nama tiket tidak valid.")
        if quantity <= 0:
            raise ValueError("Jumlah tiket harus lebih dari 0.")

    def calculate_total(self, ticket_name, quantity):
        return self.tickets[ticket_name] * quantity