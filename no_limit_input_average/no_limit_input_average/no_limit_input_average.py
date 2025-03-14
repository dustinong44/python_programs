def int_input(prompt):
        while True:
            try:
                user_input = int(input(prompt))
                if user_input > 0:
                    return user_input
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Please enter a valid integer.")

def float_input(prompt):
        while True:
            try:
                user_input = float(input(prompt))
                if user_input >= 0:
                    return user_input
                else:
                    print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid number.")

    



while True:
       num_inputs = int_input ("Please enter your numbers:")

       inputs = []
        

       for i in range(num_inputs):
            number = float_input(f"Enter number {i + 1}: ")
