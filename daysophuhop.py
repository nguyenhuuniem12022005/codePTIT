for t in range(int(input())):
    def c(a,b):
        for i in range(len(a)):
            if a[i]>b[i]:return 'NO'
        return 'YES'
    n,a,b=int(input()),list(map(int,input().split())),list(map(int,input().split()))    
    print(c(sorted(a),sorted(b)))