class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first=second=third=float('-inf')

        for num in nums:
            if num in (first,second,third):
                continue
            elif num>first:
                first,second,third=num,first,second
            elif num>second:
                second,third=num,second
            elif num>third:
                third=num

        return first if third==float('-inf') else third