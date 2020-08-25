# Create a list and attach it to another name
list_a = ['dog', 'cat', 'frog']
list_b = list_a

# Change the first item in the list
list_b[0] = 'ferret'

# Note that both variables are affected
print(list_a)
print(list_b)

# Note that both variables share the same ID
print(id(list_a) == id(list_b))


# Therefore, Use .copy() in order to avoid updating both names
list_c = ['owl', 'dog', 'beaver']
list_d = list_c.copy()

# Change the first item in the list
list_d[0] = 'dolphin'

# Note that only list_d is affected
print(list_c)
print(list_d)

# Note that each list now has a unique ID
print(id(list_c) == id(list_d))