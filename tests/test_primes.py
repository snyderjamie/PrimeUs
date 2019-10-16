import pytest

from PrimeUs.Primes import Primes


def test_init():
    primes = Primes()
    assert type(primes) == Primes


def test_prime_check():
    primes = Primes()

    assert primes.prime_check(2) is True
    assert primes.prime_check(3) is True
    assert primes.prime_check(4) is False
    assert primes.prime_check(5) is True
    assert primes.prime_check(6) is False
    assert primes.prime_check(7) is True
    assert primes.prime_check(8) is False
    assert primes.prime_check(9) is False
    assert primes.prime_check(10) is False
    assert primes.prime_check(11) is True
    assert primes.prime_check(12) is False
    assert primes.prime_check(13) is True
    assert primes.prime_check(14) is False
    assert primes.prime_check(15) is False
    assert primes.prime_check(16) is False
    assert primes.prime_check(17) is True
    assert primes.prime_check(18) is False
    assert primes.prime_check(19) is True
    assert primes.prime_check(20) is False
    assert primes.prime_check(21) is False
    assert primes.prime_check(22) is False
    assert primes.prime_check(23) is True
    assert primes.prime_check(24) is False
    assert primes.prime_check(25) is False
    assert primes.prime_check(26) is False
    assert primes.prime_check(27) is False
    assert primes.prime_check(28) is False
    assert primes.prime_check(29) is True
    assert primes.prime_check(30) is False
    assert primes.prime_check(31) is True
    assert primes.prime_check(32) is False
    assert primes.prime_check(33) is False
    assert primes.prime_check(34) is False
    assert primes.prime_check(35) is False
    assert primes.prime_check(36) is False
    assert primes.prime_check(37) is True
    assert primes.prime_check(38) is False
    assert primes.prime_check(39) is False
    assert primes.prime_check(40) is False
    assert primes.prime_check(41) is True
    assert primes.prime_check(42) is False
    assert primes.prime_check(43) is True
    assert primes.prime_check(44) is False
    assert primes.prime_check(45) is False
    assert primes.prime_check(46) is False
    assert primes.prime_check(47) is True
    assert primes.prime_check(48) is False
    assert primes.prime_check(49) is False
    assert primes.prime_check(50) is False
    # assert primes.prime_check(25) is False


def test_prime_check_larger(datadir):
    'read in a list of primes and make sure they all check out'
    primes = Primes()

    i = 0
    with open(datadir.join('primes'), 'r') as f:
        for line in f:
            assert primes.prime_check(int(line)) is True
            i = i + 1

    # make sure we got all of the numbers in the file
    assert i == 168


def test_prime_check_neg():
    primes = Primes()

    with pytest.raises(Exception, match=r'Input: -3 is not a positive integer'):
        primes.prime_check(-3)

    with pytest.raises(Exception, match=r'Input: x is not a positive integer'):
        primes.prime_check('x')

    with pytest.raises(Exception, match=r'Input: 3.14 is not a positive integer'):
        primes.prime_check(3.14)

    with pytest.raises(Exception, match=r'Input: 1 is not a positive integer > 1'):
        primes.prime_check(1)
