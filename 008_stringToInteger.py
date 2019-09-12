class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # Leading whitepsace are removed
        stripString = str.strip()
        
        if stripString == "" or stripString == "-" or stripString == "+":
            return 0
        
        s1 = re.match('[^\d]+', (stripString.lstrip("-")).lstrip("+"))
        
        if s1 != None:
            return 0
        else:
            s1 = re.search('\-*\+*\d+', stripString).group()
        
        if s1[0:2] == "--" or s1[0:2] == "-+" or s1[0:2] == "++":
            return 0
        
        res = int(s1)
        
        if res > 0:
            return 2147483647 if res > 2147483647 else res
        else:
            return -2147483648 if res < -2147483648 else res