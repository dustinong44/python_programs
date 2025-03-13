while True:
    print ("Good Day!!")
    first_num = float (input ("Please enter your First Number:"))
    second_num = float (input ("Please enter your Second Number:"))

    remainder_num = first_num % second_num

    print ("The remainder of the two numbers is", remainder_num)

    decision = input ("Do you want to input another pair of number? (yes/no):")
    if decision != "yes":
        print  ("Thank you")
        break 


