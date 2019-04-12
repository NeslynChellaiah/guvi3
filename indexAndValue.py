class main():
    def func(self):
        a = int(input())
        l = []
        z = []
        l = [int(x) for x in input().split()]
        count = 0
        for i in range (0,a):
            b = int(l[i])
            if (i==b) and (i<a):
                z.append(b)
            else:
                count+=1

        lz = len(z)
        for i in range (0,lz):
            if (i<lz-1):
                print (z[i],end=' ')
            elif (i==lz-1):
                print (z[i],end='')
        if (count == a):
            print (-1)

ob = main()
ob.func()
