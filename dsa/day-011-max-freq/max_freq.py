class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for n in nums:
          freq[n]=freq.get(n,0)+1
        max_freq=max(freq.values())
        total=0
        for count in freq.values():
         if count==max_freq:
            total=total+count
        return total


        