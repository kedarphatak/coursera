def binary_search(arr, element):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if element < arr[mid]:
            right = mid - 1
        elif element > arr[mid]:
            left = mid + 1
        else:
            return True
    return False


def find_times_rotation(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        if arr[left] <= arr[right]:
            return left
        mid = (left + right) // 2
        next = (mid + 1) % n
        prev = (mid + n - 1) % n
        if arr[mid] <= arr[next] and arr[mid] < arr[prev]:
            return mid
        elif arr[mid] <= arr[right]:
            right = mid - 1
        elif arr[mid] >= arr[left]:
            left = mid + 1
    return -1

  def searchFirstOrLast(M, value):
    start = 0
    end = len(M)
    while start <= end:
        import pdb; pdb.set_trace()
        mid = (start+end) // 2
        if value == M[mid]:
            first = last = mid
            while first - 1 >= 0:
                if M[first] == M [first-1]:
                    first -= 1
                else:
                    break
            while last + 1 < len(M):
                if M[last] == M [last+1]:
                    last += 1
                else:
                    break
            return [first,last]
        elif value > M[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return [-1,-1]

def main():
    arr = [1,2,3,4,5,6,7,8,9]
    print "Input: ", arr
    print "Output: ", binary_search(arr,10)
    print "Output: ", binary_search(arr,2)
    arr = [6,7,8, 1,2,3,4,5]
    print "Input: ", arr
    print "Output: ", find_times_rotation(arr)
    arr = [ 1, 2, 6, 9, 9 ]
    element = 2
    print "Input: ", arr, element
    print "Output: ", searchFirstOrLast(arr, element)

if __name__ == "__main__":
    main()
