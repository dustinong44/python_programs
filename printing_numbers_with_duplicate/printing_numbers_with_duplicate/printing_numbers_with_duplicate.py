input_list = []

while True:
    try:
        input_num = float(input("Enter your numbers (Enter a non-numeric value to proceed):"))
        input_list.append(input_num)
    except ValueError:
        print("Proceeding to the next step.")
        break
