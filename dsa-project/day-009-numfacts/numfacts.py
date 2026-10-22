import sys
from math import gcd,lcm

def digit_count(n):
    return len(str(abs(n)))

def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))


def divisors(n):
    divs=[]
    for i in range(1,abs(n)+1):
        if n%i==0:
            divs.append(i)
    return divs

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_facts(n):
    print(f"Number: {n}")
    print(f"Number of digits: {digit_count(n)}")
    print(f"Sum of digits: {digit_sum(n)}")
    print(f"Divisors: {divisors(n)}")



def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: python numfacts.py <number> [number2]")
        sys.exit(1)

    try:
        numbers = [int(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("Please provide valid integers.")
        sys.exit(1)

    if any(n == 0 for n in numbers):
        print("Zero is not supported for divisor calculations.")
        sys.exit(1)

    for index, n in enumerate(numbers):
        if index > 0:
            print()
        print_facts(n)

    if len(numbers) == 2:
        a, b = numbers
        print(f"GCD: {gcd(a, b)}")
        print(f"LCM: {lcm(a, b)}")


if __name__ == "__main__":
    main()








    
