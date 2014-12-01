def findTheNeedle(haystack, needle):
"""takes in an array of strings haystack and a string needle and checks if needle is in the haystack"""
    if needle not in haystack:
        return -1
    else:
        i = 0
        for i in range(len(haystack)):
            if haystack[i] == needle:
                return i
            
