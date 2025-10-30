def first_non_repeating(s):
    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    for i in range(len(s)):
        if counts[s[i]] == 1:
            return i
    a=counts
    print(a)
    return -1

# Example:
print(first_non_repeating("leetcode"))       # → 0
print(first_non_repeating("loveleetcode"))   # → 2
print(first_non_repeating("aabbc"))           # → -1