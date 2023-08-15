class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = [x for x in s.split(' ') if x != '']
        #print(s)
        #print(len(s[-1]))
        return len(s[-1])