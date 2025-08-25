# can u change the value inside a list which is contained in set S??

# s={8,7,12,"Harry", [1,2]}  #

# R1: we can not include list in a set, as all element inside set should be immutuable and hashable

# even if we don't use list in set, still elements inside set can not be changed
# but we can remove old elements and add new elements

S={3,5,4,6,7,3,6,7,3}
print(S)
S.remove(4)
print(S)
S.add(46)
print(S)