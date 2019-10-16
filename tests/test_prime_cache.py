from PrimeUs.Primes import Primes


def test_init():
    primes = Primes()
    assert type(primes) is Primes
    assert type(primes.prime_cache) is list
    assert primes.prime_cache == [2, 3]


def test_add_prime():
    primes = Primes()

    assert 5 not in primes.prime_cache
    primes.add_prime_to_cache(5)
    assert 5 in primes.prime_cache


def test_check_cache():
    primes = Primes()

    assert primes.check_prime_cache(2) is True
    assert primes.check_prime_cache(5) is False

