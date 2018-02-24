print "\n 2048 start\n------------------\n"
a=[[0 for i in range(4)]for j in range(4)]
s=0
def check(a,x,s):
	if x=='w':
		for j in range(4):
			for i in range(3):
				if a[i][j]==0:
					for k in range(i,3):
						a[k][j]=a[k+1][j]
					a[3][j]=0
				if a[i][j]==a[i+1][j]:
					a[i][j]=2*a[i+1][j]
					s+=a[i][j]
					for k in range(i+1,3):
						a[k][j]=a[k+1][j]
					a[3][j]=0
					
					
	elif x=='s':
		for j in range(4):
			for i in range(3,-1,-1):
				if a[i][j]==0:
					for k in range(i-1,-1,-1):
						a[k+1][j]=a[k][j]
					a[0][j]=0
				if a[i][j]==a[i-1][j]:
					a[i][j]=2*a[i][j]
					s+=a[i][j]
					for k in range(i-1,0,-1):
						a[k][j]=a[k-1][j]
					a[0][j]=0					
					
	elif x=='d':
		for i in range(4):
			for j in range(3,-1,-1):
				if a[i][j]==0:
					for k in range(j-1,-1,-1):
						a[i][k+1]=a[i][k]
					a[i][0]=0
				if a[i][j]==a[i][j-1]:
					a[i][j]=2*a[i][j]
					s+=a[i][j]
					for k in range(j-1,0,-1):
						a[i][k]=a[i][k-1]
					a[i][0]=0					
				
	
	elif x=='a':
		for i in range(4):
			for j in range(3):
				if a[i][j]==0:
					for k in range(j,3):
						a[i][k]=a[i][k+1]
					a[i][3]=0	
				if a[i][j]==a[i][j+1]:
					a[i][j]=2*a[i][j]
					s+=a[i][j]
					for k in range(j+1,3):
						a[i][k]=a[i][k+1]
					a[i][3]=0
		
	
	else:
		exit()
	return s	
			
def display(a,s):
	print '\n\n2048 -- current score :',s,'\n\n'
	for i in range(4):
		for j in range(4):
			print a[i][j],
		print '\n'	
			
			
def add(a):
	for i in range(4):
		for j in range(4):
			if a[i][j]==0:
				a[i][j]=2
				return 0
			if(i==3 and j==3):
				 return 1
				


a[2][3]=2;
display(a,s)
while(1):
	y=raw_input("\n\n\nEnter w,a,s,d [and any key to quit] : ")
	for i in range(6):
		s=check(a,y,s)
	'''display(a,s)
	print '---------'
	#add(a)'''
	if(add(a)!=0):
		print 'game over'
		exit()#break
	display(a,s)	
	for i in range(4):
		for j in range(4):
			if a[i][j]==2048:
				print "\n\tYou win\n"
				exit()#break
		
		
		
