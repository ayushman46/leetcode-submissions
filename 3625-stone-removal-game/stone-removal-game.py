class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #.   19-10 = 9. odd - false
        a = n - 10

        if a < 0:
            return False

        remove = 9
        moves = 1

        while a >= remove:
            a -= remove
            remove -= 1
            moves += 1

        return moves % 2 == 1