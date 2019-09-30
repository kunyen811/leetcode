class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        counter = Counter(nums).most_common()
        return [counter[i][0] for i in range(k)]