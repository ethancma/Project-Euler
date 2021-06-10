"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math

def primeGen():
    # Generator Object for Prime Numbers
    yield 2
    k = 3
    while True:
        prime = True
        for i in range(2,math.floor(math.sqrt(k))+1):
            if k % i == 0:
                prime = False
                break
        if prime: yield k
        k += 2
# end

def main():
    a = primeGen()
    for i in range(10001): val = next(a)
    print(val)

if __name__=='__main__':
    main()

