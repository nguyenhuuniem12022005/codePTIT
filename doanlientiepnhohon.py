for t in range(int(input())):
    n,a=int(input()),list(map(int,input().split()))
    st=[]
    for i in range(n):
        a[i]=(a[i],i)
        while (len(st)>0) and (st[len(st)-1][0]<=a[i][0]):
            a[i]=(a[i][0],st[len(st)-1][1])
            st.pop()
        st.append(a[i])
    for i in range(n):
        print(i-a[i][1]+1,end=' ') 
    print('')           