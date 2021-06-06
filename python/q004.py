"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(n):
    return str(n) == str(n)[::-1]
    

def main():
    L = 123456654321
    print(isPalindrome(L))

if __name__=='__main__':
    main()
# end
