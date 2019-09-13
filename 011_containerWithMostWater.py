class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r :
            water = min(height[l],height[r])*(r-l)
            
            if water > ans:
                ans = water
            
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return ans