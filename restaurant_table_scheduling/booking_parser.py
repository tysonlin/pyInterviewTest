from datetime import datetime

class BookingParser:
    @staticmethod
    def convert_to_dt(pair):
        start, end = pair
        start_dt = datetime.strptime(start, '%H:%M')
        end_dt = datetime.strptime(end, '%H:%M')
        return (start_dt, end_dt)

    @staticmethod
    def convert_input_pairs(pairs):
        result = []
        for pair in pairs:
            result.append(BookingParser.convert_to_dt(pair))
        result.sort()
        return result

    @staticmethod
    def is_overlap(base_pair, comp_pair):
        base_start, base_end = base_pair
        comp_start, comp_end = comp_pair
        if base_start < comp_start and base_end > comp_start: # comp start time is in range of base time
            return True
        elif base_end > comp_end and base_start < comp_end: # comp end time is in range of base time
            return True
        elif base_start <= comp_start and base_end >= comp_end: # comp range is within base range
            return True
        elif base_start >= comp_start and base_end <= comp_end: # comp range spans over base range
            return True
        else:
            return False

if __name__ == '__main__':
    pass
