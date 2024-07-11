per = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
print(per['name'])

per['age'] = 31
print(per["age"])

for key, value in per.items():
    print(f"{key}: {value}")