
while True:

    print ("Good Day!")

    first_num = float(input("Please Enter your First Number:"))
    second_num = float(input("Please Enter your Second Number:"))

    if first_num == second_num:
        print ("The Given Numbers are Equal")

    else:
        print ("The Given Numbers are Not Equal")


    decision = input ("Do you want to input another pair of number? (yes/no):")
    if decision != "yes":
        print  ("Thank you")
        break 
