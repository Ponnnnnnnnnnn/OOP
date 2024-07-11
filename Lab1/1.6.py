name = ["Alice", "Bob", "..."]
age = [25, 30, 35]
city = ["NYC", "LA", "Chic"]

for name, age, city in zip(name, age, city):
    print(f"{name} is {age} y/o & lives in {city}")