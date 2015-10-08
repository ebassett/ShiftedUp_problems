#!/usr/bin/env python

# EJB 2015-10-07
# Problem 1 from:
# https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour


def recursive_sum(num_list):
    ''' # doctest
    >>> recursive_sum([1,2,3,4,5,6])
    21
    '''

    sum = 0
    if num_list:
        return num_list[0] + recursive_sum(num_list[1:])
    else:
        return sum


def tail_recursive_sum(accumulator, num_list):
    ''' # doctest
    >>> tail_recursive_sum(0, [1,2,3,4,5,6])
    21
    '''

    if num_list:
        return tail_recursive_sum(accumulator + num_list[0], num_list[1:])
        #print 'tail_recursive_sum({}, {})'.format(accumulator + num_list[0], num_list[1:])
    else:
        return accumulator


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

