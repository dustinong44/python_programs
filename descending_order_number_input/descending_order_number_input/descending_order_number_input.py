input_list = []

while True: 
    try:
        input_num = float(input("Enter your numbers: "))
        input_list.append(input_num)
    except ValueError:
        break

input_list.sort(reverse=True)
print(input_list)





























































