class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        n=len(nums)

        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%n]:
                count=count+1
        return count<=1
        

        