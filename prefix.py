def prefix(L, pre):
"""takes in a list of string L and a string prefix; returns list of strings from L that start with prefix"""
    if L == []:
        return []
    elif pre == '':
        return []
    else:
        i = 0
        j = 0
        goodString = []
        for i in range(len(L)):
            if L[i][0:len(pre)] == pre:
                goodString.append(L[i])
        return goodString
