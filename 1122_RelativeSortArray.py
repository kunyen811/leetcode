class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        arr1_map = Counter(arr1)
                
        res = []
        notinarr2=[]
        
        for i in arr2:
            if i in arr1_map:
                res+=[i]*arr1_map[i]
        
        for i in arr1:
            if i not in arr2 and i not in notinarr2:
                notinarr2+=[i]*arr1_map[i]
        
        res2 = sorted(notinarr2)
        
        return res+res2