def two_sum(arr, target):
    sum_dict = {}
    for i in range(len(arr)):
        if target-arr[i] not in sum_dict:
            sum_dict[arr[i]] = i
        else:
            return i, sum_dict[target-arr[i]]
    return 0

def main():
    arr = [2,7,11,15,-5]
    target = 10
    print "Input: ", arr, target
    print "Output:", two_sum(arr,target)

if __name__ == '__main__':
    main()
