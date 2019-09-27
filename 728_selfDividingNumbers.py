class Solution(object):  
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left, right+1):
            if self.self_dividing(i):
                ans.append(i)
        return ans        
    
    def self_dividing(self,i):
        D = str(i)
        for d in D:
            if d == '0' or i % int(d) > 0:
                return False
        return True