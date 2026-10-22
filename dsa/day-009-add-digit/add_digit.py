class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        s=0
        while num>0:
            rem=num%10
            s=s+rem
            num=num//10
        return self.addDigits(s)
        