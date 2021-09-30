def segregate_array_by_sign(arr):
    """
    Time complexity is O(n) and space complexity O(1)
    :param arr:
    :return:
    """
    length = len(arr)
    i = 0
    j = length-1
    while True:
        while arr[i]<0 and i<j:
            i +=1
        while arr[j]>=0 and i< j:
            j -=1
        if i <j:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i]= temp
        else:
            break
    return arr

def main():
    a = [-1, 1 , 3 , -2, 4, -3, 5, 6 , -4]
    print "Input:{}".format(a)
    print "output:{}".format(segregate_array_by_sign(a))

if __name__ == '__main__':
    main()
