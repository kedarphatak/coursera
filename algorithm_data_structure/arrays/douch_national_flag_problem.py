def douch_national_flag_problem(arr):
    n = len(arr)
    low = mid = 0
    high = n - 1
    while mid < high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr


def main():
    arr = [0, 1, 1, 2, 0, 1, 1, 0, 2, 1, 0, 0, 1, 1, 0, 2]
    print "Input: ", arr
    print "Output: ", douch_national_flag_problem(arr)


if __name__ == '__main__':
    main()
