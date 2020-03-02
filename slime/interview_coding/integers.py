
# ######################################################################### #
# Integer operations, such as base conversion, are represented here.        #
# ######################################################################### #

def change_base_16(i, base):
    """
    This will take a string i that represents an integer of base 'base' and
    converts it to a hexadevimal string.

    | :param str i: The integer to convert
    | :param int base: The base of the integer to convert
    | :return: str representation of i in base 16
    """
    return str(hex(int(i, base))).split('x')[-1]


def find_primes(start, end):
    """
    Find a list of prime numbers between start and end, return the list
    in ascending order.

    | :param int start: The starting integer
    | :param int end: The highest possible number to check if it is prime
    | :return: A sorted list of prime number where start <= prime <= end
    """
    primes = []
    # generate all possible cadidates for testing
    candidates = [x for x in range(start, end + 1, 1)]

    # loop over candidates
    for c in candidates:
        # check if it is a prime
        # This can be a bit confusing. The check uses the fact that True = 1 and False = 0.
        # Using list comprehension, it checks the mod for every integer between 2 and c - 1.
        # The sum of which will be 0 (a list of nothing but False results), indicating that c
        # is indeed a prime. f this is still confusing, I have included a more step by step
        # version below.
        if sum([int(c % j == 0) for j in range(2, c, 1)]) == 0:
            primes.append(c)
    return sorted(primes)


def find_primes2(start, end):
    """
    This is the longer, less efficient way to frind primes. See above for the
    Pythonic way of doing it.

    :param start: The starting integer
    :param end: The highest possible number to check if it is prime
    :return: A sorted list of prime number where start <= prime <= end
    """
    primes = []

    # generate all possible cadidates for testing
    candidates = [x for x in range(start, end + 1, 1)]

    # loop over candidates
    for c in candidates:
        # create a list to hold the cadidate tests
        c_results = []
        # for each candidate, you have to loop over a range of 2 to (c - 1)
        for j in range(1, c - 1, 1):
            # Test if c % j gives us remainder, if it does, the result is True
            # otherwise, the result is False. Cast the result to an int and
            # append it to a new list
            if c % j == 0:
                c_results.append(int(True))
            else:
                c_results.append(int(False))
        # now if the sum of the list is 0 (got a False for every modulous)
        # then it is prime
        if sum(c_results) == 0:
            primes.append(c)
    # now return a numerically sorted list of the primes
    return sorted(primes)
