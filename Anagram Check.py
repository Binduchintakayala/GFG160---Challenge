def areAnagrams(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2
s1 = "geeks"
s2 = "kseeg"
print("true" if areAnagrams(s1, s2) else "false")