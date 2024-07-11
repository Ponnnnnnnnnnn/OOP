cities = {
    'NYC': [32,25,30,45,34],
    'LA': [45,67,34,78,67],
    "Chic": [34,23,56,76,43]
}

avg = {city:sum(temps)/ len(temps) for city,temps in cities.items()}
print(avg)