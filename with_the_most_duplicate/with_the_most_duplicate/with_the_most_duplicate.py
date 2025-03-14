input_list = []

while True:
    try:
        input_num = float(input("Enter your numbers (Enter a non-numeric value to proceed):"))
        input_list.append(input_num)
    except ValueError:
        break

max_count = 0
most_duplicated_number = None



