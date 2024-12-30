def areRotations(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1
if __name__ == "__main__":
    s1 = "aab"
    s2 = "aba"
    print("true" if areRotations(s1, s2) else "false")
