class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        j=0
        for i in sentences:
            j=max(j,len(i.split()))

        return j
