#! python3

def string_to_int(str):
    '''Return combined number amount from integer in the string, ignoring the letters
    >>> string_to_int('123')
    123
    >>> string_to_int('123d456')
    123456
    >>> string_to_int('a12b34')
    1234
    '''
    amount = 0
    for char in str:
        if not char.isalpha():
            amount = (amount*10) + int(char)
    return amount

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
