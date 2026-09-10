print("Welcome to the Interactive Personal Data Collector")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))
fav_num = int(input("Enter your favourite number: "))

birth_year = 2026 - age

print("\nPersonal Information")

print(f"Name : {name}")
print(f"Age : {age}")
print(f"Height : {height}")
print(f"Favourite Number : {fav_num}")
print(f"Approximate Birth Year : {birth_year}")

print("\n Data Types and Memory")

print(f"Name  Value: {name}, Type: {type(name)}, ID: {id(name)}")
print(f"Age  Value: {age}, Type: {type(age)}, ID: {id(age)}")
print(f"Height  Value: {height}, Type: {type(height)}, ID: {id(height)}")
print(f"Favourite Number  Value: {fav_num}, Type: {type(fav_num)}, ID: {id(fav_num)}")

print("\nThank you for using the Personal Data Collector!")