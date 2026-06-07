class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = 0
        count = 0

        for j in g:
            while i < len(s) and s[i] < j:
                i += 1

            if i < len(s) and s[i] >= j:
                count += 1
                i += 1

        return count