def longest_substring(s, k):
    if not s:
        return 0
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    less_than_k_chars = [char for char, count in char_count.items() if count < k]
    if not less_than_k_chars:
        return len(s)
    parts = []
    start = 0
    for end, char in enumerate(s):
        if char in less_than_k_chars:
            if end > start:
                parts.append(s[start:end])
            start = end + 1
    if start < len(s):
        parts.append(s[start:])
    if not parts:
        return 0
    max_length = 0
    for part in parts:
        max_length = max(max_length, longest_substring(part, k))
    return max_length
s = "aaabb"
k = 3
result = longest_substring(s, k)
print(result)
