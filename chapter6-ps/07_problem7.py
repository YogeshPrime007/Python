dict={}

n1=input("Enter name of friend 1: ")
l1=input("Enter their fav. language: ")
dict.update({n1:l1})

n2=input("Enter name of friend 2: ")
l2=input("Enter their fav. language: ")
dict.update({n2:l2})

n3=input("Enter name of friend 3: ")
l3=input("Enter their fav. language: ")
dict.update({n3:l3})

n4=input("Enter name of friend 4: ")
l4=input("Enter their fav. language: ")
dict.update({n4:l4})

print(dict)

# key:value
# values can be repeated for different keys
# but we we repeat keys, old values are overwritten by new values, hence only one key for all repeated keys is printed

# also, in keys, case sensitivity is followed