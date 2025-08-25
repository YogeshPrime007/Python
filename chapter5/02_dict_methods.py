d={} # empty dict
print(type(d))


marks={
    "Harry": 100,
    "Subham": 84,
    "Rohan": 897,
    97: "ieh"
}

print(marks.items())
print(marks.keys()) # left hand side wala (key)
print(marks.values()) # right hand side wala (value)

marks.update({"Harry": 98, "Yogesh": 102, "": "pass", "check": "false"}) # "" ie. space can also become key of key value pair
print(marks)

marks["test"]=marks.pop("check")
print(marks)

marks["Shyam"]=marks.pop('Rohan')
print(marks)

print(marks.get("shiva"))
print(marks.get("yogesh"))
print(marks.get("Yogesh"))

print(marks.get("Yogesh"))
print(marks["Yogesh"])
print(marks.get("Yogesh2"))
# print(marks["Yogesh2"]) # it gives error 

# the difference between fetching values from dictonary using "get" and "[]" is if value not present, get will output in "none" whereas [] willl output in "error"

print(type(marks.get("Yogesh")))
print(type(marks["Yogesh"]))

print(marks.clear())
print(type(marks.clear()))

print(len(marks))