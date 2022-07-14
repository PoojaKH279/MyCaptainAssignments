fileName=input("write the file name")

file_extns=fileName.split(".")

print("the extenstion is"+repr(file_extns[-1]))

radius=float(input("enter the radius of the circle:"))
area=3.142*radius*radius
print("area of the circle is:",area)

