numbers = [1,2,3,4,5,3,6,7,3,1]
remove_num = 3

while remove_num in numbers:
    numbers.remove(remove_num)
    
print("Numbers after removal", numbers)
print("Sum of remaining numbers:", sum(numbers))
print("Count number list:", numbers.count(1))