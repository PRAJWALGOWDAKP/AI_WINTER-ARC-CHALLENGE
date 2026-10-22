class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=min(nums)
        b=max(nums)
        gcd=0
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                gcd=i
        return gcd
        