class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        L = len(A)
        res = [0]*L
        even, odd = 0, 1
        for a in A:
            if a % 2 == 1:
                res[odd] = a
                odd+=2
            else:
                res[even] = a
                even+=2
        return res
        