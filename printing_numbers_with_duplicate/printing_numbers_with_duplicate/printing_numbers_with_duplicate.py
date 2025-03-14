total = 0
input_list = []


for i in range(10):
    user_input = int(input("Enter number: "))
    input_list.append(user_input)
    total += user_input

duplicates = []
for num in input_list:
    if input_list.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Numbers with duplicates:", duplicates if duplicates else "No duplicates found")