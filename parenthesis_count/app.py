#! python3

import re

def parenthesisCount(str):
    '''return number of parenthesis pairs in string
    >>> parenthesisCount('(a)(b)()c')
    3
    >>> parenthesisCount('(a(b(c)d))')
    3
    >>> parenthesisCount('oauaoeuu')
    0
    >>> parenthesisCount('o(aua())(oeuu')
    -1
    >>> parenthesisCount('o)(auaoeuu')
    -1
    >>> parenthesisCount('o)(auao(euu')
    -1
    >>> parenthesisCount('o(auao()asd(()))euu')
    4
    '''
    front_cnt = 0
    back_cnt = 0
    nest = 0

    for s in str:
        if s == '(':
            front_cnt += 1
            nest += 1
        elif s == ')':
            back_cnt += 1
            nest -= 1

        if nest < 0: # cannot close paren ')' before open '('
            return -1

    if nest == 0 and front_cnt == back_cnt:
        return back_cnt
    else:
        return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # str_in = input('\nEnter string: ')
    # if str_in == 'utest':
    #     import doctest
    #     doctest.testmod(verbose=True)
    # else:
    #     print(parenthesisCount(str_in))
