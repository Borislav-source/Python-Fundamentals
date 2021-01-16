import math


def divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n // i])
    return divs


n = int(input())
if sum(divisors(n)) == n:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


