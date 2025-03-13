while True:
    even_number = 0  

    for a in range(10):  # Loop 10 times
        user_input = int(input("Please enter your number: "))  

        if user_input % 2 == 0: #check if the number is even  
            even_number += 1  

    print("There are", even_number, "even numbers in the set of numbers.")

    decision = input("Do you want to enter another set of numbers? (yes/no): ")
    if decision != "yes":
        print("Thank you!")
        break  


