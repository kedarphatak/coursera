def remove_duplicate(arr):
    """Remove elements from array.
    This algorithm has time complexity of O(n)
    and space complexity of O(1)
    """
    j = 0
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            arr[j] = arr[i]
            j += 1
    arr[j] = arr[len(arr) - 1]
    return arr[:j + 1]


def main():
    arr = [0, 2, 2, 2, 2, 2, 2, 2, 3]
    print "Input: ", arr
    print "Output: ", remove_duplicate(arr)


if __name__ == '__main__':
    main()
