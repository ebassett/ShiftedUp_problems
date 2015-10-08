#!/usr/bin/env python

# EJB 2015-10-07
# https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
#   Problem 4
#   Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.


# APPROACH 1
def concat_largest_number(lst):
    ''' # doctest
    >>> concat_largest_number([9, 5, 90, 50, 92, 900])
    '99290900550'
    >>> concat_largest_number([90, 9])
    '990'
    >>> concat_largest_number([420, 42, 423])
    '42423420'
    >>> concat_largest_number([8, 87, 88, 89])
    '8988887'
    '''

    # TODO: guarantee list is non-empty and consists solely of ints (or int-strings)
    lst = [str(x) for x in lst]  # Stringify
    #print lst
    concatenated_number = ''
    for digit in '9876543210':
        leading_digit_lst = []
        max_len = 0
        for x in lst:
            if x.startswith(digit):
                leading_digit_lst.append(x)
                length = len(x)
                if length > max_len:
                    max_len = length
        #print leading_digit_lst
        # I'm not sure how I came up with this insight, but if we right-pad all the numbers with the leading digit to a
        # common length, then they will sort correctly.
        # I'm using the padded numbers as tuple keys, with the original numbers as the values so that we can
        # sort on the former but still get the latter back. Basically the decorate-use-undecorate pattern.
        # (Originally I used a dictionary, but that can lead to collisions.)
        decorated_lst = []
        for x in leading_digit_lst:
            padded = x + digit * (max_len - len(x))
            _tuple = (padded, x)
            decorated_lst.append(_tuple)
        #print sorted(decorated_lst, reverse=True)
        concatenation_for_digit = ''
        for key, value in sorted(decorated_lst, reverse= True):
            concatenation_for_digit += value
        #print concatenation_for_digit
        concatenated_number += concatenation_for_digit
    #print concatenated_number
    return concatenated_number  # TODO?: convert back to int


# APPROACH 2
def concat_largest_number_2(lst):
    ''' # doctest
    >>> concat_largest_number_2([9, 5, 90, 50, 92, 900])
    '99290900550'
    >>> concat_largest_number_2([90, 9])
    '990'
    >>> concat_largest_number_2([420, 42, 423])
    '42423420'
    >>> concat_largest_number_2([8, 87, 88, 89])
    '8988887'
    '''

    # TODO: guarantee list is non-empty and consists solely of ints (or int-strings)
    lst = [str(x) for x in lst]  # Stringify
    #print lst
    lst = sorted(lst, cmp = lambda a,b: cmp(a+b, b+a), reverse=True)
    #print lst
    concatenated_number = ''.join(lst)
    #print concatenated_number
    return concatenated_number  # TODO?: convert back to int




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

