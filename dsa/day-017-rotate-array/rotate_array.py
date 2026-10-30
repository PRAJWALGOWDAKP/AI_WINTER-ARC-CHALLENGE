class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)

        if n==0:
            return

        if k>n:
            k=k%n

        def reverse(i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i=i+1
                j=j-1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)



        

        