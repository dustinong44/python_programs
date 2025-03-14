input_list = []

while True:
    try:
        input_num = float(input("Enter your numbers (Enter a non-numeric value to proceed):"))
        input_list.append(input_num)
    except ValueError:
        break

lowest_number = min (input_list)

print ("The lowest number among the inputs is", lowest_number)


