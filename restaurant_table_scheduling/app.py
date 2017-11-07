from table import Table
from booking_parser import BookingParser

def print_tables_schd(tables):
    print('##########')
    print('Table List:')
    print('##########')
    for idx, table in enumerate(tables):
        print('Table {} bookings:'.format(idx+1))
        for booking in table.bookings:
            start, end = booking
            print('From {} to {}'.format(start.time(), end.time()))
        print('========')
    print('##########')

def number_table_required(pairs):
    tables = []
    bookings = BookingParser.convert_input_pairs(pairs)
    for booking in bookings:
        if len(tables) == 0:
            tables.append(Table(booking))
        else:
            found_table = False
            for table in tables:
                if table.is_available_at(booking):
                    found_table = True
                    table.add_booking(booking)
                    break
            if not found_table:
                tables.append(Table(booking))
    print_tables_schd(tables)
    return len(tables)

if __name__ == '__main__':
    pairs = [
        ('13:30','14:30'),
        ('13:00','14:00'),
        ('09:00','10:00'),
        ('09:15','10:30'),
        ('09:15','10:30'),
        ('12:00','13:00'),
        ('12:00','13:00'),
        ('12:00','13:00'),
        ('12:30','13:30'),
        ('12:00','13:00')
        ]
    print('Number of table required: {}'.format(number_table_required(pairs)))
