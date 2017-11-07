import copy

def init_table(n):
    '''
    Generate n*n table filled with zeros
    >>> init_table(2)
    [[0, 0], [0, 0]]
    >>> init_table(3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    '''
    table = []
    inner_table = []
    for i in range(n):
        inner_table.append(0)
    for i in range(n):
        table.append(copy.copy(inner_table))
    return table

def diag_table(n):
    '''
    Generate diagonal table
    where 1 is at top-right and n*n is at bottom-left
    e.g.
    >>> diag_table(2)
    [[2, 1], [4, 3]]
    >>> diag_table(3)
    [[4, 2, 1], [7, 5, 3], [9, 8, 6]]
    >>> diag_table(5)
    [[11, 7, 4, 2, 1], [16, 12, 8, 5, 3], [20, 17, 13, 9, 6], [23, 21, 18, 14, 10], [25, 24, 22, 19, 15]]
    '''
    table = init_table(n)
    r, c = start_seq = (0, n-1)
    # print('Start seq: {}, {}'.format(r,c))
    for i in range(n*n):
        # print('Ite {} of {}: '.format(i+1, n*n))
        if r >= n or c >= n:
            # print('ERROR! NOT SUPPOSED TO HAPPEN! r={} or c={} is more than or equal to n={}, both will be now set to n-1={}'.format(r,c,n,n-1))
            r, c = n-1, n-1
        # print('table[{}][{}] = {}'.format(r,c,i+1))
        table[r][c] = i+1
        if i == (n*n)-1:
            # print('Alreadt put last number => END OF METHOD')
            break
        r += 1
        c += 1
        if r == n or c == n:
            # print('Hit wall where r({}) or c({}) = n({})'.format(r,c,n))
            nr, nc = start_seq
            if nc == 0:
                nr += 1
                # print('c==0 :({}) => increment r to ({})'.format(nc,nr))
            else:
                nc -= 1
                # print('c!=0 :({}) => decrement c to ({})'.format(nc+1,nc))
            r, c = start_seq = (nr, nc)
            # print('New start seq: {}, {}'.format(r,c))

    return table

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
