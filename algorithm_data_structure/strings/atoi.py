ef is_digit(s):
    if ord('0') <= ord(s) <= ord('9'):
        return True
    return False


def is_space(s):
    if ord(" ") == ord(s):
        return True
    return False

def my_atoi(str):
    """
    :type str: str
    :rtype: int
    """
    if len(str) < 1:
        return 0
    res = 0
    sign = 1
    digit_found = False
    sign_flag = False
    for s in str:
        # Handle space
        if ord(" ") == ord(s):
            # After digits
            if digit_found or sign_flag:
                break
            continue
        elif ord(s) == ord("-"):
            if digit_found or sign_flag:
                break
            sign_flag = True
            sign = -1
            continue
        elif ord(s) == ord("+"):
            if digit_found or sign_flag:
                break
            sign_flag = True
            continue
        elif ord('0') <= ord(s) <= ord('9'):
            digit_found = True
            res = res * 10 + (ord(s) - ord('0'))
            if res >= 2147483648:
                if sign == 1:
                    return 2147483647
                return -2147483648
        else:
            break
    return sign * res
  

def main():
    strings = ["    43", "-43-34", 'We want 43', '43 we want', "+-43", '-2147483649', '2147483648', "", "0"]
    for s in strings:
        print "Input:{}".format(s)
        print "Output:{}".format(my_atoi(s))


if __name__ == "__main__":
    main()
