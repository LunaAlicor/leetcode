class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        def check(prefix_to_check, list_to_check):
            flag = 0
            for i_elem in list_to_check:
                if prefix_to_check not in i_elem:
                    flag += 1
                    break
                else:
                    if i_elem.startswith(prefix_to_check):
                        pass
                    else:
                        flag += 1
                        break
            if flag == 0:
                return True
            else:
                return False

        prefix = ''
        lastPrefix = prefix
        for i_elem in strs:
            if i_elem != '' and len(strs) != 1:
                for j_char in i_elem:
                    lastPrefix = prefix
                    prefix += j_char
                    if check(prefix, strs):
                        continue
                    else:
                        return lastPrefix
            else:
                return i_elem
