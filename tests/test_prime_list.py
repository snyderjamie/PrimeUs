from PrimeUs.Primes import Primes


def test_init():
    primes = Primes()
    assert type(primes) is Primes
    assert type(primes.prime_cache) is list
    assert primes.prime_cache == [2, 3]


def test_get_prime_list():
    primes = Primes()

    chk_list = primes.get_prime_list(10)
    assert chk_list == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_get_prime_list_max():
    primes = Primes()

    chk_list = primes.get_prime_list(1000)
    assert len(chk_list) == 100


def test_check_cache():
    primes = Primes()

    assert primes.check_prime_cache(2) is True
    assert primes.check_prime_cache(5) is False

