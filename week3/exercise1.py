# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""
from __future__ import division
from __future__ import print_function


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    my_list = []
    for x in xrange(start, stop, step):
        my_list.append(x)

    return my_list


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    return(range(start, stop, step))
    pass


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    my_list = []
    for x in xrange(start, stop, 2):
        my_list.append(x)

    return my_list
    pass


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """

    new_list = [start]
    is_odd = False
    incr = start
    while incr <= stop:
        if is_odd and incr + odd_step < stop:
            incr += odd_step
            new_list.append(incr)
            is_odd = False
        elif not is_odd and incr + even_step < stop:
            incr += even_step
            new_list.append(incr)
            is_odd = True
        else:
            return new_list
    return new_list
    print(new_list)


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    Question = "Enter a number between "
    my_number = int(raw_input("%s%s and %s :" % (Question, low, high)))

    while not low <= my_number <= high:
        my_number = int(raw_input("%s%s and %s :" % (Question, low, high)))
    return(my_number)


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    Test = False
    Question = message
    Test2 = 0
    while Test is False:
        try:
            my_number = raw_input("%s" % (Question))
            Test2 = int(my_number)
            Test = True
            return(Test2)
        except ValueError:
            print("That isn't a number!")


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    Test = False
    my_num = "Test"
    Test2 = 0
    Question = "Enter a number between "

    while Test is False:
        try:
            my_num = 2
            Test2 = int(my_num)
            Test = True
            my_num = int(raw_input("%s%s and %s:" % (Question, low, high)))
            while not low <= my_num <= high:
                my_num = int(raw_input("%s%s and %s:" % (Question, low, high)))
        except ValueError:
            print("That isn't a number!")
            Test = False
    return(str(Test2))


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    # inside Atom, you need to run them from the terminal. E.g.:
    # ben@um:~/projects/git/code1161base$ python week3/exercise1.py

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Give me a number:")
    print("\nsuper_asker")
    super_asker(33, 42)
