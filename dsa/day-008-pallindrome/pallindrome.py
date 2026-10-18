class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        rev=0
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        return rev==temp
        