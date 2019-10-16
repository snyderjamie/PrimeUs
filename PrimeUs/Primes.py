

class Primes():
    def __init__(self):
        pass

    def prime_check(self, n):
        # make sure n is valid
        try:
            assert isinstance(n, int)
            assert n > 1
        except AssertionError:
            raise Exception('Input: ' + str(n) + ' is not a positive integer > 1')

        # simple checks
        if n <= 3:
            return True

        # quick way to eliminate a lot of numbers
        if n % 2 == 0 or n % 3 == 0:
            return False

        # weed out the rest - kinda brute force for the moment
        i = 5
        while i**2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 1

        return True
