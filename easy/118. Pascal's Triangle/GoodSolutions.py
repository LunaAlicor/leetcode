class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            output = self.generate(numRows-1)
            prev = output[-1]
            curr = [1]
            j = 1
            while(j < len(prev)):
                curr.append(prev[j-1] + prev[j])
                j+=1
            curr.append(1)
            output.append(curr)
            return output


def generate(numRows):
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    else:
        output = generate(numRows-1)
        prev = output[-1]
        curr = [1]
        j = 1
        while j < len(prev):
            curr.append(prev[j-1] + prev[j])
            j += 1
        curr.append(1)
        output.append(curr)
        return output


rows = int(input("Введите кол-во этажей пирамидки: "))
test = generate(rows)
for i_list in range(len(test)):
    print(' '*(len(test) - i_list - 1), end='')
    for j_elem in test[i_list]:
        print(j_elem, end=' ')
    print()
