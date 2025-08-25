s1={3,5,6,3,6,9,49,69,93,0,3,3,5}
s2={5,8,3,7,9,94,4,769,68,69}

print(s1.union(s2))
print(s1.intersection(s2))


# A U B = R1 + R2 + R3
# A n B = R2
# A delta(triangle) B = R1 + R3  # i.e A delta(triangle) B = A U B - A n B 