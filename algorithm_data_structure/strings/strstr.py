def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    nn = len(needle)
    hn = len(haystack)
    if nn > hn:
        return -1
    for i in range(hn):
        mismatch = False
        if haystack[i] == needle[0]:
            op = i
            j = 1
            k = i + 1
            while j < nn and k < hn:
                if haystack[k] != needle[j]:
                    mismatch = True
                    break
                k += 1
                j += 1
            if mismatch:
                continue
            return op
    return -1

def main():
    haystack = "mississippi"
    needle = "issip"
    print "Input: ",haystack ,needle
    print "Output: ", strStr(haystack,needle)

if __name__ == "__main__":
    main()
