class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        for i in range(l):
            if A[i] > A[i+1]:
                return i
        