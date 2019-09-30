class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_heights = sorted(heights)
        res = 0
        for v1,v2 in zip(heights,sorted_heights):
            if v1 != v2: 
                res+=1
        return res