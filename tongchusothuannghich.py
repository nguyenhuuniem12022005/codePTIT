for t in range(int(input())):
    def dao(s):
        if len(s) <=1:
            return 'NO'
        return 'YES' if s==s[::-1] else 'NO'
    def tcs(n):
        s=0
        for i in n: s+=int(i)
        return dao(str(s))
    print(tcs(input()))