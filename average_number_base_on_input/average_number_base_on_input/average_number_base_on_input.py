data_list = []

while True:
    try:
       data_num = float(input(("Enter your data (Please enter a non integer data to calculate for average):")))
       data_list.append(data_num)
    except ValueError:
        break

average_result = sum(data_list) / len(data_list)
print ("The average of the data is:", average_result)