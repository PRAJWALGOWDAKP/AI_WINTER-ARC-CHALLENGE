class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        for i in range(2,n):
            is_prime=True

            for j in range(2,i):
                if i%j==0:
                    is_prime=False
                    break
            if is_prime:
                count+=1
        return count

        