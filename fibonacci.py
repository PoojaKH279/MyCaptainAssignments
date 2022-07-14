a=0
b=1
n=int(input("enter no. of Fibonacci to be generated:"))
sum=0
if n<=0:
	print("enter number greater than 0:")
else:
	for I in range(0,n):
		print(sum,end=" ")
		a=b
		b=sum
		sum=a+b
		
