class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        arr_map = Counter(arr)
        arr_unique = set(arr)
        arr_res = set()
        
        for i in arr_map:
            arr_res.add(arr_map[i])
        
        return len(arr_res) == len(arr_unique)