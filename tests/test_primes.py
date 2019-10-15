import pytest
from PrimeUs.Primes import Primes


def test_init():
    primes = Primes()
    assert type(primes) == Primes


def test_prime_check():
    primes = Primes()
    assert primes.prime_check() is True
