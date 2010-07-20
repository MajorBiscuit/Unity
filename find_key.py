# Author = Andreas Theodosiou
# A function that returns the dictionary key in which a value belongs

entity = {'speed': ['m/s', 'km'], 'length': ['m', 'in']}
def find_key(dic, val):
    return [k for k, v in dic.items() if val in v][0]

key = find_key(entity, 'm')
print(key)

