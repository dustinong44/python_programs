input_list = []

while True:
    try:
        input_num = float(input("Enter your numbers (Enter a non-numeric value to proceed):"))
        input_list.append(input_num)
    except ValueError:
        break

max_count = 0
most_duplicated_number = None

for num in input_list:
    count = input_list.count(num)
    if count > max_count:
        max_count = count
        most_duplicated_number = num

if max_count > 1:
    print(f"The number with the most duplicates is: {most_duplicated_number} (appears {max_count} times).")
else:
    print("No duplicates found.")

