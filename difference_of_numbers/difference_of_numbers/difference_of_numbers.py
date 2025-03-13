
while True:
    print ("Good Day!!")
    first_num = float(input ("Please enter your subtrahend:"))
    second_num = float(input ("Please enter your minuend:"))

    difference_of_num = first_num  - second_num

    print ("The total of the two numbers is", difference_of_num)

    decision = input ("Do you want to input another pair of number? (yes/no):")
    if decision != "yes":
        print  ("Thank you")
        break 

