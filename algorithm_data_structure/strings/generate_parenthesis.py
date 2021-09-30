def helper(n,string, pos, lc, rc):
    if rc>=n and lc>=n:
        for i in string:
            print i
        print ""
    else:
        if lc > rc:
            string[pos] = ')'
            helper(n,string,pos+1,lc,rc+1)
        if lc < n:
            string[pos] = '('
            helper(n,string,pos+1, lc +  1,rc)

def generateParenthesis(n):
    helper(n,arr,0,0)

def main():
    n = 4
    generateParenthesis(n)
    print para

if __name__ == "__main__":
    main()
