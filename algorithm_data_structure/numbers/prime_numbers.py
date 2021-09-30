import math
def get_prime_numbers(n):
    arr = range(n+1)
    n_sqrt = int(math.sqrt(n))
    for j in range(2,n_sqrt+1):
        for i in range(1,len(arr)):
            if arr[i] != "NP" and arr[i] != j:
                if arr[i]%j == 0:
                    arr[i]="NP"
    return arr

def main():
    print get_prime_numbers(50)

if __name__ == "__main__":
    main()
