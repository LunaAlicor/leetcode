class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        non_alpha = ""
        for i_sym in s:
            if i_sym.isalpha():
                non_alpha += i_sym.lower()
            else:
                try:
                    rofl = int(i_sym)
                    non_alpha += str(rofl)
                except:
                    pass
            
        if non_alpha == non_alpha[::-1]:
            return True
        else:
            return False