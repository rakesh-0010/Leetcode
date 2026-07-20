class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        if x < 0:
            return False

        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10

        return x == rev