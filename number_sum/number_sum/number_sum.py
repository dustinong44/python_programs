
while True:
    print ("Good Day!!")
    first_num = float(input ("Please enter your first addends:"))
    second_num = float(input ("Please enter your second addends:"))

    sum_num = first_num + second_num

    print ("The total of the two numbers is", sum_num)

    decision = input ("Do you want to input another pair of number? (yes/no):")
    if decision != "yes":
        print  ("Thank you")
        break 