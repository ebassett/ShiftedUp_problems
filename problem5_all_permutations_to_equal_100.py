#!/usr/bin/env python

# EJB 2015-10-25
# https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
#   Problem 5
#   Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100.
#   For example: 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100.


from __future__ import print_function


def build_equations(digit_str, operator, branch_list):
    '''
    Takes all partial equations in the given branch (addition, subtraction, concatenation) and
    updates them (into a new list),
    *prepending* the current digit and operator
    (as we walk back up the recursion stack)
    '''
    return [digit_str + operator + partial_equation for partial_equation in branch_list]


def compute_sums(number, target, remaining_inputs):
    '''
    See https://www.shiftedup.com/2015/05/08/solution-to-problem-5-and-some-other-thoughts-about-this-type-of-questions
    for the thinking behind this algorithm

    # doctest
    >>> compute_sums(1, 100, [2, 3, 4, 5, 6, 7, 8, 9])
    ['1 + 2 + 3 - 4 + 5 + 6 + 78 + 9', '1 + 2 + 34 - 5 + 67 - 8 + 9', '1 + 23 - 4 + 5 + 6 + 78 - 9', '1 + 23 - 4 + 56 + 7 + 8 + 9', '12 + 3 + 4 + 5 - 6 - 7 + 89', '12 + 3 - 4 + 5 + 67 + 8 + 9', '12 - 3 - 4 + 5 - 6 + 7 + 89', '123 + 4 - 5 + 67 - 89', '123 + 45 - 67 + 8 - 9', '123 - 4 - 5 - 6 - 7 + 8 - 9', '123 - 45 - 67 + 89']
    '''

    # We build the equation string one digit at a time, from right to left, even if we are concatenating
    digit_str = str(abs(number) % 10)

    if len(remaining_inputs) == 0:  # Base case: end of inputs: we finally have a complete good equation, or not
        if number == target:
            return list(digit_str)
        else:
            return list()

    # We have to handle the three cases (addition, subtraction, concatenation) separately.
    # Each branch returns a list of successful (partial) equations.
    addition_branch = compute_sums(remaining_inputs[0], target - number, remaining_inputs[1:])
    # Add the negative of the number (otherwise you have to worry about flipping signs through the rest of the equation)
    subtraction_branch = compute_sums(-1 * remaining_inputs[0], target - number, remaining_inputs[1:])
    # Maintain correct sign and value of number while concatenating
    concat_number = 10 * number + remaining_inputs[0]  if number >= 0  else 10 * number - remaining_inputs[0]
    concatenation_branch = compute_sums(concat_number, target, remaining_inputs[1:])

    results = []
    if addition_branch:
        results.extend(build_equations(digit_str, ' + ', addition_branch))
    if subtraction_branch:
        results.extend(build_equations(digit_str, ' - ', subtraction_branch))
    if concatenation_branch:
        results.extend(build_equations(digit_str, '', concatenation_branch))

    return results



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print()

    INPUTS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    TARGET = 100
    results = compute_sums(INPUTS[0], TARGET, INPUTS[1:])
    print('Inputs:', INPUTS)
    print('Target sum:', TARGET)
    print(len(results), 'solutions.')
    for equation in results:
        print(equation)

