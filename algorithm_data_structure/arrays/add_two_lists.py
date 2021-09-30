def addTwoNumbers(l1, l2):
    i = j = c = 0
    nl1 = len(l1)
    nl2 = len(l2)
    new_list = []
    while i < nl1 and j < nl2:
        sum = l1[i] + l2[j] + c
        k = sum % 10
        c = sum / 10
        i += 1
        j += 1
        new_list.append(k)
    while i<nl1:
        sum = l1[i] + c
        k = sum % 10
        c = sum / 10
        i += 1
        new_list.append(k)
    while j<nl2:
        sum = l2[j] + c
        k = sum % 10
        c = sum / 10
        j += 1
        new_list.append(k)
    if c:
        new_list.append(c)
    return list(reversed(new_list))

def main():
    l1 = [1,1,1,1,1]
    l2 = [9,9,9, 9, 9]
    print "Input: ", l1, l2
    print "Output: ", addTwoNumbers(l1,l2)

if __name__ == "__main__":
    main()
