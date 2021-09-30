import sys


def bubble_sort(arr):
    """
    Sort elements of array using bubble sort.
    Time complexity: O(n^2)
    :param arr:
    :return:
    """
    for p in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

  def merge_sort(arr):
    """
    Sort elements of array using merge sort.
    Time complexity: O(nlogn)
    Space complexity: O(n)
    :param arr:
    :return:
    """

    def _merge(left, right, array):
        """
        Merge left partition and right partition into array in sorted fashion

        :param left: array
        :param right: array
        :param array: array
        :return: array:
        """
        nL = len(left)
        nR = len(right)
        i = j = k = 0
        # Loop over right and left part of array and merge elements based on order.
        while i < nL and j < nR:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        # Copy remaining elements of left part
        while i < nL:
            array[k] = left[i]
            i += 1
            k += 1
        # Copy remaining elements of right part
        while j < nR:
            array[k] = right[j]
            j += 1
            k += 1

        return array

    n = len(arr)
    # If only one element then already sorted so return
    if n < 2:
        return arr
    mid = n / 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    _merge(left, right, arr)
    return arr
  
def selection_sort(arr):
    """
    Sort elements of array using selection sort.
    Time complexity: O(n^2)
    :param arr:
    :return:
    """
    for fixed in range(len(arr)):
        for var in range(fixed + 1, len(arr)):
            if arr[fixed] > arr[var]:
                arr[fixed], arr[var] = arr[var], arr[fixed]
    return arr


def quick_sort(arr):
    """
    Sort elements of array using quick sort.

    Time complexity in average case is O(nlogn)
    Time complexity in worst case is O(n^2)
    Space complexity is O(1)
    :param arr:
    :return
    """

    def partition(a, start, end):
        pivot = a[(start + end) / 2]
        while start <= end:
            while a[start] < pivot:
                start += 1
            while a[end] > pivot:
                end -= 1
            if start <= end:
                a[start], a[end] = a[end], a[start]
                start += 1
                end -= 1
        return end

    def quick_sort_helper(a, start, end):
        p = partition(a, start, end)
        if start < p - 1:
            quick_sort_helper(a, start, p - 1)
        if p < end:
            quick_sort_helper(a, p, end)

    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr
  
  def heap_sort(arr):
    def heapify(array, n, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < n and array[largest] < array[left]:
            largest = left
        if right < n and array[largest] < array[right]:
            largest = right
        if largest != index:
            array[largest], array[index] = array[index], array[largest]
            heapify(array, n, largest)

    # Create a heap for given array
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        # print arr[i-1]
        heapify(arr, i, 0)
    return arr


def main():
    arr = [9, 8, 7, 6, 4, 5, 3, 2, 1, 0]
    # arr = [10, 7, 8, 9, 1, 5]
    method = sys.argv[1]
    print "Input: ", arr
    if method == 'bubble':
        print "Output: ", bubble_sort(arr)
    elif method == 'merge':
        print "Output: ", merge_sort(arr)
    elif method == 'selection':
        print "Output: ", selection_sort(arr)
    elif method == 'quick':
        print "Output: ", quick_sort(arr)
    elif method == 'heap':
        print "Output:", heap_sort(arr)
    elif method == 'insertion':
        print "Output:", insertion_sort(arr)
    else:
        print "not a valid method for sorting"


if __name__ == '__main__':
    print main()
