total = 0
input_list = []
display_list = []

for i in range(10):
    user_input = float(input("Enter your numbers: "))
    input_list.append(user_input)
    total += user_input

for num in input_list:
    if input_list.count(num) > 1:
        
        if num not in display_list:
            display_list.append(num)
    else:
        
        display_list.append(num)

print("Numbers to display (duplicates only show the first entry):", display_list)

