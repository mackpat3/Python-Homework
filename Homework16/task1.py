def merge_lists(list1, list2):
    return list(zip(list1, list2))

car_names=("Mustang", "Camaro", "Challenger")
car_horsepower=(450, 455, 485)

combined_list=merge_lists(car_names, car_horsepower)

print ("Here are a list of American Muscle cars and their horsepower: ")
print(combined_list)

