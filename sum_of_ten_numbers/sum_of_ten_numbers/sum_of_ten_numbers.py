
while True:
    total = 0

    for i in range (0,10):
     user_input = int(input( "Input your Numbers:"))
     total += user_input

    print (total)
    decision = input ("Do you want to input another pair of number? (yes/no):")
    if decision != "yes":
        print  ("Thank you")
        break 
