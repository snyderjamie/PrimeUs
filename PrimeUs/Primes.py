

class Primes():
    def __init__(self):
        self.prime_cache = [2, 3]


    def prime_check(self, n):
        'check if value is a prime number - return True if prime'

        # make sure n is valid
        try:
            assert isinstance(n, int)
            assert n > 1
        except AssertionError:
            raise Exception('Input: ' + str(n) + ' is not a positive integer > 1')

        # simple checks
        if n <= 3:
            return True

        # maybe we already checked this prime
        if self.check_prime_cache(n):
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


    def get_prime_list(self, num=0):
        prime_list = []
        if num > 100:
            num = 100

        i = 1
        num_primes = 0
        while num_primes < num:
            i = i + 1
            if self.prime_check(i):
                prime_list.append(i)
                num_primes = num_primes + 1

        return prime_list


    def add_prime_to_cache(self, prime):
        if self.check_prime_cache(prime) is not True:
            self.prime_cache.append(prime)


    def check_prime_cache(self, prime):
        chk = False

        if prime in self.prime_cache:
            chk = True

        return chk

