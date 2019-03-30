class main():
    def func(self):
        S = []
        S = input().split()
        N = len(S)
        for i in range (0,N):
            if i<N-1:
                print (S[i][::-1],end=" ")
            else:
                print (S[i][::-1],end="")
ob = main()
ob.func()
