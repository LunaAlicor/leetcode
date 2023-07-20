class Solution(object):
    def generate(self, numRows):
        if numRows <= 0:
            return []
        output = [[1]]
        for i in range(1, numRows):
            current_row = [1]
            for j in range(len(output[i - 1]) - 1):
                current_row.append(output[i - 1][j] + output[i - 1][j + 1])
            current_row.append(1)
            output.append(current_row)
        print(output)
        return output
