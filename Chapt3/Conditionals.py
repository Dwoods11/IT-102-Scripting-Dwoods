



#First we have to gather if the day is good or bad, Which requires user input
question = input("Is today a good day? Please answer with y or n: ").lower()

#Analyze the value and print of yes it is
if question =='y':
    print("yes it is")
elif question == 'n':
    print("Thats okay tomorrow will be n")
elif question == 'idk':
    print("Thats okay")
else:
 print("Please enter a valid input of y or n for yes or no")

