class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = 0
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if len(stack) == 0:
                    flag += 1
                else:
                    opening = stack.pop()
                    if (opening == "(" and char != ")") or (opening == "[" and char != "]") or (
                            opening == "{" and char != "}"):
                        flag += 1
            elif char == chr(ord(char) + 2):
                flag += 1

        if len(stack) != 0:
            flag += 1

        if flag == 0:
            return True
        else:
            return False