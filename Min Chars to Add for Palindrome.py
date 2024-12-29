def minCharsToAdd(s: str) -> int:
    rev_s = s[::-1]
    concat = s + "#" + rev_s
    n = len(concat)
    lps = [0] * n 
    for i in range(1, n):
        j = lps[i - 1]
        while j > 0 and concat[i] != concat[j]:
            j = lps[j - 1]
        if concat[i] == concat[j]:
            j += 1
        lps[i] = j
    longest_palindromic_suffix_len = lps[-1]
    return len(s) - longest_palindromic_suffix_len
print(minCharsToAdd("abc")) 
print(minCharsToAdd("aacecaaaa")) 
