class main():
    def func(self):
        a = int(input())
        l = []
        l = input().split()
        for i in range (0,a):
            b = int(l[i])
            if (i==b) and (i<a-1):
                print (b,end=' ')
            elif (i==b) and (i==a-1):
                print (b,end='')

ob = main()
ob.func()
