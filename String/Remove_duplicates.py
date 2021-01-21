def remove_duplicates(s):
    #char_list = s.split()
    char_list_set = set(s)
    t = ""
    for i in s:
        if i in t:
            pass
        else:
            t = t+i
            
    return t

s = 'geeks'
print(remove_duplicates(s))
