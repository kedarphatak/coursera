def kmp_pre_processing(pattern):
    """Calculate partial match table"""
    # Initialize list/array
    arr = [0]
    # Iterate over pattern from index 1 to length -1
    for i in range(1, len(pattern_len)):
        j = arr[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = arr[j - 1]
        arr.append(j + 1 if pattern[j] == pattern[i] else j)
    return arr


def kmp_search(text, pattern):
    arr = kmp_pre_processing(pattern)
