"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def primeFactors(n):
    copy = n
    L = []
    while copy % 2 == 0:
        copy /= 2
        L.append(2)
    for i in range(3,int(math.sqrt(copy)),2):
        while copy % i == 0:
            copy /= i
            L.append(i)
    if copy > 2: L.append(copy)
    return L

def main():
    print(max(primeFactors(600851475143)))
# end

if __name__=='__main__':
    main()
# end
