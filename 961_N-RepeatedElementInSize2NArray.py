class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)/2
        for i in A:
            if A.count(i) == N:
                return i