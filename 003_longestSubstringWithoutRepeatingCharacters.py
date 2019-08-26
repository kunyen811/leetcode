class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        char = set()
        res = 0
        
        while left < len(s) and right < len(s):
            if s[right] in char:
                if s[left] in char:
                    char.remove(s[left])
                left+=1
            else:
                char.add(s[right])
                right+=1
                res = max(res, len(char))
        return res        
        