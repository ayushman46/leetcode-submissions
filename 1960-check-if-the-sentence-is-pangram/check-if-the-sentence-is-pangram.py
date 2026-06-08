class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        string="abcdefghijklmnopqrstuvwxyz"
        if "".join(sorted(set(sentence)))=="".join(sorted(string)):
            return True
        else:
            return False
       