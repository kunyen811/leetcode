class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l = 0
        h = len(S)
        ans = []
        for i in S:
            if i == "I":
                ans.append(l)
                l+=1
            if i == "D":
                ans.append(h)
                h-=1
        ans.append(h)
        return ans