#!/usr/bin/env python
import argparse
import sys
sys.path.append('.')
sys.path.append('..')

from PrimeUs.Multiply import Multiply
from PrimeUs.Primes import Primes

# Get args
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--size', help='the size of the prime table')
args = parser.parse_args()

if args.size is None or int(args.size) < 1:
    parser.print_usage()
    exit()

primes = Primes()
multiply = Multiply()
primes_list = primes.get_prime_list(int(args.size))
prime_table = multiply.two_lists(primes_list, primes_list)
print(multiply.format_table(prime_table))


