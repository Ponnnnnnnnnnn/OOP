list = [1, 2, 4, 3, 5]
list_extend = [55,66]

list.append(6)
print("List after append:", list)

list.extend(list_extend)
print("List after extend:", list)

list.insert(1,20)
print("List after insert[1]: 20:", list)

list.remove(20)
print("List after remove 20:", list)

pop_data = list.pop()
print("List after pop:", list)
print("Pop value:", pop_data)

print("Value 4 in index:", list.index(4))

print("List after count(2):", list.count(2))

list.sort()
print("List after Sort:", list)

list.reverse()
print("List after Reverse:", list)
