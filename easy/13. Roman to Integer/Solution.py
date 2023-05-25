class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_dict = {'I': 1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summ = 0
        position = 0

        for i_elem in range(position, len(s)):
            if position != 0:
                position = 0
                continue
            try:
                if symbol_dict[s[i_elem]] == symbol_dict[s[i_elem+1]]:
                    summ += symbol_dict[s[i_elem]]
                elif symbol_dict[s[i_elem]] < symbol_dict[s[i_elem+1]]:
                    summ += symbol_dict[s[i_elem+1]] - symbol_dict[s[i_elem]]
                    position += 1

                else:
                    summ += symbol_dict[s[i_elem]]
            except:
                summ += symbol_dict[s[i_elem]]

        return summ