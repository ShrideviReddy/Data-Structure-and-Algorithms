from collections import Counter
def string_compress(s):
    count_dict = Counter(s)
    compress_string = []
    for i,v in count_dict.items():
        compress_string.append(i)
        compress_string.append(str(v))
    return ''.join(compress_string)

s = 'aabbcc'

print(string_compress(s))
