class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = list(map(str,digits))
        digits = str(int("".join(digits))+1)
        new_string = ""
        for i_char in digits:
            new_string += i_char+" "
        return list(map(int,new_string.split()))