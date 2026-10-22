
# Number Facts CLI

A command-line tool that calculates digit count, digit sum,
divisors, primality, GCD, and LCM.

## Requirements

- Python 3
- Node.js for the JavaScript version

## Usage

```bash
python numfacts.py 360
python numfacts.py 84 36
```

## Functions and Time Complexity

Let n be the input number and d be its number of digits.

| Function | Time Complexity | Space Complexity |
|---|---|---|
| digit_count | O(d) | O(d) |
| digit_sum | O(d) | O(d) |
| divisors | O(n) | O(n) |
| is_prime | O(sqrt(n)) | O(1) |
| gcd | O(log(min(a, b))) | O(1) |
| lcm | O(log(min(a, b))) | O(1) |

## Features

- Count digits
- Calculate digit sum
- List all positive divisors
- Check whether a number is prime
- Calculate GCD and LCM for two numbers

## Testing

Test with 360, 84 36, 17, 12, and 97.

## JavaScript

The same functionality is implemented in numfacts.js
using Node.js, with matching output.
