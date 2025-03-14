input_list = []

while True:
    try:
        input_num = float(input("Enter your numbers (Enter a non-numeric value to proceed):"))
        input_list.append(input_num)
    except ValueError:
        break

highest_number = max (input_list)

print ("The highest number among the inputs is", highest_number)


