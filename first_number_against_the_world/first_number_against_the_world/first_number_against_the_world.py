while True:
    first_num = float(input("Enter the 1st number:")) #input for the 1st number upto the last number from line 2 to line 11
    second_num = float(input("Enter the 2nd number:"))
    third_num = float(input("Enter the 3rd number:"))
    fourth_num = float(input("Enter the 4th number:"))
    fifth_num = float(input("Enter the 5th number:"))
    sixth_num = float(input("Enter the 6th number:"))
    seventh_num = float(input("Enter the 7th number:"))
    eighth_num = float(input("Enter the 8th number:"))
    ninth_num = float(input("Enter the 9thnumber:"))
    tenth_num = float(input("Enter the 10th number:"))

    result_difference = first_num - (second_num + third_num + fourth_num + fifth_num + sixth_num + seventh_num + eighth_num + ninth_num + tenth_num) #calculation
    
    print("The difference between the 1st number and the sum of the other numbers is:", result_difference)

    decision = input("Do you want to enter another set of numbers? (yes/no):")
    if decision != "yes":
        print ("Thank you!!")
        break