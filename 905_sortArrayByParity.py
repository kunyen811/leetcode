class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        res1 = []
        for i in A:
            if i % 2 == 0:
                res.append(i)
        for i in A:
            if i % 2 != 0:
                res1.append(i)
        res2 = res + res1
        return res2