class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        array = []
        for i in range(N+1):
            array.append(i)
        return self.fibona(array,N)
    
    def fibona(self, array, N):
        if N <= 1:
            return N
        array[N] = self.fibona(array, N-1) + array[N-2]
        return array[N]