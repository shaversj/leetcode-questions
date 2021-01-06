import math
import timeit


def count_primes_brute_force(n):
    def is_prime_brute_force(num):
        if num < 2:
            return False

        for numb in range(2, math.floor(math.sqrt(num)) + 1):
            if num % numb == 0:
                return False

        return True

    count = 0
    for number in range(2, n):
        if is_prime_brute_force(number):
            count += 1

    return count


# n = 1500000
# 114155
# 8.770894518999999

start = timeit.default_timer()
# print(is_prime(10))

print(count_primes_brute_force(1500000))

end = timeit.default_timer()
print(end - start)