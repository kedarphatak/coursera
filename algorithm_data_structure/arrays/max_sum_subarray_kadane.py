def find_max_sum_subarray(arr):
    """
    Python implementation of Kadane's algorithm.
    Time complexity is O(n), Space complexity O(1)

    """
    max_so_far = 0
    max_ending_here = 0
    start = end = s = 0
    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return max_so_far, start, end


def main():
    arr = [4, -3, -2, 2, 3, 1, -2, -3, 4, 2, -6, -3, -1, 3, 1, 2]
    print "Input: {}".format(arr)
    print "Output: {}".format(find_max_sum_subarray(arr))


if __name__ == '__main__':
    main()
