while True:
    print ("Good Day!!")
    first_num = float (input ("Please enter your dividend:"))
    second_num = float (input ("Please enter your divisor:"))

    quotient_num = first_num / second_num

    print ("The quotient of the two numbers is", quotient_num)

    decision = input ("Do you want to input another pair of number? (yes/no):")
    if decision != "yes":
        print  ("Thank you")
        break 
