import unittest
from ddt import ddt, data, unpack

from datetime import datetime

from booking_parser import BookingParser

@ddt
class BookingParserTest(unittest.TestCase):

    @unpack
    @data(
        (('13:00','14:00'), (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0))),
        (('11:00','12:30'), (datetime(1900, 1, 1, 11, 0), datetime(1900, 1, 1, 12, 30)))
    )
    def test_convert_to_dt(self, input_val, expected):
        self.assertEqual(BookingParser.convert_to_dt(input_val), expected)


    @unpack
    @data(
        (
        [('13:30','14:30'),('13:00','14:00')],
        [(datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
        (datetime(1900, 1, 1, 13, 30), datetime(1900, 1, 1, 14, 30))]
        ),
        (
        [('13:30','14:30'),('13:00','14:00'),('11:00','12:00'),('18:30','19:00'),('09:30','10:00')],
            [
                (datetime(1900, 1, 1, 9, 30), datetime(1900, 1, 1, 10, 0)),
                (datetime(1900, 1, 1, 11, 0), datetime(1900, 1, 1, 12, 0)),
                (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
                (datetime(1900, 1, 1, 13, 30), datetime(1900, 1, 1, 14, 30)),
                (datetime(1900, 1, 1, 18, 30), datetime(1900, 1, 1, 19, 00))
            ]
        )
    )
    def test_convert_input_pairs(self, input_val, expected):
        self.assertEqual(BookingParser.convert_input_pairs(input_val), expected)


    @unpack
    @data(
        (
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
            (datetime(1900, 1, 1, 13, 30), datetime(1900, 1, 1, 14, 30)),
            True
        ),
        (
            (datetime(1900, 1, 1, 9, 0), datetime(1900, 1, 1, 12, 0)),
            (datetime(1900, 1, 1, 10, 30), datetime(1900, 1, 1, 11, 30)),
            True
        ),
        (
            (datetime(1900, 1, 1, 15, 0), datetime(1900, 1, 1, 16, 0)),
            (datetime(1900, 1, 1, 15, 30), datetime(1900, 1, 1, 16, 30)),
            True
        ),
        (
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
            (datetime(1900, 1, 1, 15, 30), datetime(1900, 1, 1, 16, 30)),
            False
        ),
        (
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
            (datetime(1900, 1, 1, 12, 30), datetime(1900, 1, 1, 16, 30)),
            True
        ),
        (
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 30)),
            True
        ),
        (
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
            True
        ),
        (
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
            (datetime(1900, 1, 1, 14, 0), datetime(1900, 1, 1, 15, 0)),
            False
        ),
        (
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 15, 0)),
            True
        ),
        (
            (datetime(1900, 1, 1, 13, 0), datetime(1900, 1, 1, 14, 0)),
            (datetime(1900, 1, 1, 12, 0), datetime(1900, 1, 1, 14, 0)),
            True
        )

    )
    def test_is_overlap(self, inp1, inp2, expected):
        self.assertEqual(BookingParser.is_overlap(inp1, inp2), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
