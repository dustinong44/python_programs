while True:
    print ("Good Day!!")
    first_num = float(input ("Please enter your First Number:"))
    second_num = float(input ("Please enter your Second Number:"))

    result_num = first_num ** second_num

    print ("The result of the exponentiation of two numbers is", result_num)

    decision = input ("Do you want to input another pair of number? (yes/no):")
    if decision != "yes":
        print  ("Thank you")
        break 
