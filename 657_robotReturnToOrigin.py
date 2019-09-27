class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for move in moves:
            if move == "U":
                y += 1
            if move == "D":
                y -= 1
            if move == "L":
                x -= 1
            if move == "R":
                x += 1
        if x == y and  y == 0:
            return True
        else:
            return False