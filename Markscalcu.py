"""Students marks/grade calculator"""

marks = int(input("Enter the marks:"))
if(marks>=40):
    print("Your are pass");
    if(marks>=90):
        print("Congratulation You got A Grade");
    else:
        print("You got B Grade")
else:
    print("Better luck next time !")