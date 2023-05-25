class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        buffer_x = ''
        for i_char in reversed(str(x)):
            buffer_x += i_char
        print(buffer_x)
        if buffer_x == str(x):
            return True
        else:
            return False