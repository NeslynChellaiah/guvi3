a = int(input())
l = [int(x) for x in input().split()]
l = sorted(l)
for i in range (0,len(l)-1):
	if i%2 == 0:
		print (max(l),end=" ")
		l.remove(max(l))
	else:	
		print (min(l),end=" ")
		l.remove(min(l))
print (l[len(l)-1],end="")
