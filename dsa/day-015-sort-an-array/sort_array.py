class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left_half=nums[:mid]
        right_half=nums[mid:]
        left=self.sortArray(left_half)
        right=self.sortArray(right_half)
        return self.merge_array(left,right)
    def merge_array(self,left,right):
        res=[]
        i,j=0,0
        n,m=len(left),len(right)

        while i<n and j<m:
            if left[i]<=right[j]:
                res.append(left[i])
                i=i+1
            else:
                res.append(right[j])
                j=j+1
        if i<n:
            while i<n:
                res.append(left[i])
                i=i+1
        if j<m:
            while j<m:
                res.append(right[j])
                j=j+1
        return res
        