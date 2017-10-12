def move(n,a='A',b='B',c='C'):
	if n==1:
		print('%s>>%s'%(a,c))
	else:
		move(n-1,a,b,c)
		print('%s>>%s'%(a,b))
		z=a
		a=c
		c=z
		move(n-1,a,b,c)
		print('%s>>%s'%(b,a))
		z=a
		a=c
		c=z
		move(n-1,a,b,c)