class TicketData:
    def __init__(self):
        self.tickets = {
            "VIP": 500000,
            "Regular": 200000,
            "Economy": 100000
        }

    def get_tickets(self):
        return self.tickets