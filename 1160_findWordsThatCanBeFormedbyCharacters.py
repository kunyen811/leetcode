class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        from collections import Counter
        
        target_count = Counter(chars)
        
        res = 0
        
        for word in words:
            word_count = Counter(word)
            decision = True
            for key in word_count:
                if not (key in target_count and target_count[key] >= word_count[key]):
                    decision = False
                    break
            if decision:
                res += len(word)
        return res