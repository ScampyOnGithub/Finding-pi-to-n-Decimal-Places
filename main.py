from math import factorial, log10
from decimal import Decimal, getcontext

def find_pi_to_n_digits(n: int) -> Decimal:
    # Uses the Chudnovsky algorithm to find pi to n decimal places
    # The time complexity is O(n(logn)**3)
    # https://en.wikipedia.org/wiki/Chudnovsky_algorithm

    numerator = Decimal(0)
    denominator = Decimal(0)
    pi = Decimal(0)

    # prevents DivisionByZero error
    if n < 1:
        n = 1

    n_iterations = int(n+1/(log10(640320 ** 3)/24*6*2*6))

    getcontext().prec = n + 1

    for k in range(n_iterations):
        numerator = (-1)**k * factorial(6*k) * (545140134 * k + 13591409)
        denominator = factorial(3 * k) * factorial(k) ** 3 * (640320) ** (3 * k)
        pi += Decimal(numerator) / Decimal(denominator)

    pi = (Decimal(12) * pi)/(Decimal(640320 ** Decimal(1.5)))
    pi = 1/pi

    return pi

def main() -> None:
    while True:
        precision = input("How many decimal places would you like to find pi to? ").strip()
        try:
            output = find_pi_to_n_digits(int(precision))
            print(str(output))
            print(len(str(output)))
        except ValueError:
            print("Please enter an integer.")
    return

if __name__ == '__main__':
    main()
