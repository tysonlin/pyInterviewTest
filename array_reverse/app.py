#! python3

def array_reverse(array):
    '''Come up with an algorithm to reverse the array as fast as possible
    >>> array_reverse([1, 2, 3, 4, 5, 6])
    [6, 5, 4, 3, 2, 1]
    >>> array_reverse([2, 4, 6])
    [6, 4, 2]
    >>> array_reverse([1])
    [1]
    '''
    front_idx = 0
    back_idx = len(array) - 1
    while front_idx < back_idx:
        temp = array[front_idx]
        array[front_idx] = array[back_idx]
        array[back_idx] = temp
        front_idx += 1
        back_idx -= 1
    return array

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
