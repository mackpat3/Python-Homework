foods=("Apple", "Banana", "Orange", "Mango", "Strawberry", "Grape", "Mandarin", "Strawberry")
calories=("52", "96", "62", "605", "33", "68", "50", "33")

#print (foods)
#print (calories)

foods_list=list(foods)
calories_list=list(calories)

print(f"The fifth food is a {foods_list[4]} containing a total of {calories_list[4]} calories.")
print(f"The second to last food is a {foods_list[-2]} containing a total of {calories_list[-2]} calories.")

unique_foods=list(set(foods_list))
print("Unique foods: ", unique_foods)

food_dict={}
for i in range(len(foods)):
    food_dict[foods[i]]=calories[i]
print("Food Dictionary: ", food_dict)


