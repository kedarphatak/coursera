def reverse_array(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    print "Input: ", arr
    print "Output: ", reverse_array(arr)


if __name__ == '__main__':
    main()
