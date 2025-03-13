while True:
    for a in range (0, 10):
        user_input = input ("Please enter your number:")
        
        odd_number = 0
        
        if a % 2 == 0:
         odd_number += 1
            
        print ("There are", odd_number, "odd numbers on the set of numbers")

    decision = input ("Do you want to enter another set of numbers? (yes/no):")
    if decision != "yes":
        break
