start=int(input("enter the start of range: "))
end=int(input("enter the end of range: "))
for i in range (start,end+1):
	if i>=0:
		print("positive numbers in a range",start,"and",end,"is:",i)
