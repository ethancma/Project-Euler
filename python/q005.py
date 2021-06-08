"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def divisibleTo20(n):
    # Return True if divisible by numbers 1-20, else false
    for i in range(11,21):
        if n % i != 0:
            return False
    return True
# end

def main():
    i = 2
    while divisibleTo20(i) == False:
        i += 2
    print(i)

if __name__=='__main__':
    main()
