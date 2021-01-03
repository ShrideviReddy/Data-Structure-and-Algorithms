from collections import Counter
def maxoccurence():
    test_str = "Geeks"
    res = Counter(test_str)
    res = max(res, key = res.get)
    print("Max occuring character is:", res)
maxoccurence()
