from booking_parser import BookingParser

class Table:

    def __init__(self, booking=None):
        self.bookings = []
        if booking is not None:
            self.bookings.append(booking)

    def is_available_at(self, dt_pair):
        for booking in self.bookings:
            if BookingParser.is_overlap(booking, dt_pair):
                return False
        return True

    def add_booking(self, booking):
        if booking is not None:
            self.bookings.append(booking)
