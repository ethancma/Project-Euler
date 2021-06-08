"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumSquareNatural(n):
    return sum(i**2 for i in range(1,n+1))

def sumSquare(n):
    return sum(i for i in range(1,n+1))**2

def main():
    print(sumSquare(100)-sumSquareNatural(100))

if __name__=='__main__':
    main()

