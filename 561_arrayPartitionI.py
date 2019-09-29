class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_nums = sorted(nums)
        
        sum_ans = sum(n_nums[::2])
        
        return sum_ans