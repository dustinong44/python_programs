input_list = []

while True:
    try:
        input_num = float(input("Enter your numbers (Enter a non-numeric value to proceed):"))
        
        input_list.append(input_num)
    except ValueError:
        break
if input_num in input_list:
            print("Duplicate")
else:
       print("Unique")

print("All numbers entered:", input_list)