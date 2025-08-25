a="yogesh"
b="singh"
print(a+b) # this is concatination
c='1'
d='1'
print(c+d) # this is concatination


# INPUT FUNCTION:

x=input("Enter Number 1: ")
y=input("Enter number 2: ")

print("Number 1 is: ", x)
print("Number 2 is: ", y)

print(x+y) #this is also concatination

print(float(x)+float(y))

u=int(x)
v=int(y)

print(type(u))
print(type(y))

z=print(u+v)
print(type(z)) #here we will get none type data because its the side effect of operating inside print function

f=u+v
print(type(f)) # here we will recieve int data type as we have calculated outside print function 

print(type(print())) # here we can clearly see the data type of print function



print(complex(u))
