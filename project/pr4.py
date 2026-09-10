def input_data():
    print("\nSelect Array Type:")
    print("1. 1D Array")
    print("2. 2D Array")
    ch = input("Enter choice (1 or 2): ")

    if ch == '1':
        raw_input = input("space separated ")
        data = [int(x) for x in raw_input.split()]
        print(data)
        print("data stored")
        return "1D", data

    elif ch == '2':
        rows = int(input("\nEnter number of rows: "))
        cols = int(input("Enter number of columns: "))
        matrix = []
        for i in range(rows):
            row_input = input("space separated): ")
            matrix.append([int(x) for x in row_input.split()])
        return "2D", matrix

    else:
        print("Invalid choice!")
        return []

# 2.  SUMMARY 

def display_summary(dtype, data):
    if dtype == "1D":
        total_len = len(data)
        min_v = min(data)
        max_v = max(data)
        sum_v = sum(data)
    
    elif dtype == "2D":
       
        for row in data:
            print(row)
            
        
        total_len = 0
        sum_v = 0
        min_v = data[0][0]
        max_v = data[0][0]

        for row in data:
            for val in row:
                total_len += 1
                sum_v += val
                if val < min_v:
                    min_v = val
                if val > max_v:
                    max_v = val

    avg_v = round(sum_v / total_len, 2)

    print("\nData Summary:")
    print(f"- Total elements: {total_len}")
    print(f"- Minimum value: {min_v}")
    print(f"- Maximum value: {max_v}")
    print(f"- Sum of all values: {sum_v}")
    print(f"- Average value: {avg_v}")

    # 3. RECURSION FACTORIAL
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 5. short
def sort_data(dtype, data, choice):
    if dtype == "1D":
        temp = data.copy()
        temp.sort(reverse=(choice == 2))
        print("\nSorted 1D Data:", temp)
        
    elif dtype == "2D":
        print("\nSorted 2D Matrix (Row-wise):")
        for row in data:
            sorted_row = sorted(row, reverse=(choice == 2))
            print(sorted_row)




dtype, current_data = input_data()  
display_summary(dtype, current_data)

num = int(input("\nEnter number for factorial: "))
fact = factorial(num)
print(f"Factorial of {num} is: {fact}")



print("\nChoose Sorting Order:")
print("1. Ascending")
print("2. Descending")
s_choice = int(input("Enter choice (1 or 2): "))

sort_data(dtype, current_data, s_choice)




