
while True:
    print ("Good Day")
    first_number = float (input("Enter your first number:"))
    second_number = float (input("Enter your second number:"))

    if first_number < second_number:
        print (first_number)

    else:
        print (second_number)


    decision = input ("Do you want enter another pair of numbers? (yes/no)")
    if decision != "yes":
        print ("Thank You!!")
        break


