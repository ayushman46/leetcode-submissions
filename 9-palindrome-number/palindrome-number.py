class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Rule: Negative numbers are not palindromes
        if x < 0:
            return False
            
        # Initialize variables
        rev = 0
        a = x  # Use 'a' to preserve the original 'x' for comparison
        
        # Logic: Reverse the number
        while a > 0:
            rev = rev * 10 + a % 10
            a = a // 10
            
        # Comparison
        return rev == x