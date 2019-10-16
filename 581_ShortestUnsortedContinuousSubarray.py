class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens, numss = len(nums), sorted(nums)
        if nums == numss:
            return 0
        l = min(i for i in range(lens) if nums[i] != numss[i])
        r = max(i for i in range(lens) if nums[i] != numss[i])
        
        return r-l+1