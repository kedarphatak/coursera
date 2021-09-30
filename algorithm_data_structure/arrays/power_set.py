def get_power_set(arr):
    n = len(arr)
    number_of_sets = 2 ** n
    pow_set = []
    for i in range(number_of_sets):
        bn = format(i,'0{}b'.format(n))
        l = [arr[i] for i in range(len(bn)) if int(bn[i]) > 0]
        pow_set.append(l)
    return pow_set

def main():
    arr = range(4)
    pow_set = get_power_set(arr)
    print arr
    print pow_set

if __name__ == "__main__":
    main()
