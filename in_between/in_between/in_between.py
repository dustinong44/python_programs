while True:
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))

# Ensure 1st number is smaller than 2nd number
    if first_num > second_num:
        first_num, second_num = second_num, first_num  # Swap values if needed

        print(f"Numbers between {first_num} and {second_num}:")

# Loop to print numbers between and 1st number and 2nd number
    for i in range(first_num + 1, second_num):  
        print(i, end=" ")  # Print numbers in a single line

    print() 

    decision = input("Do you want to enter another pair of numbers? (yes/no): ")
    if decision.lower() != "yes":
        print ("Thank you")
        break