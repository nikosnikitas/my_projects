#   Exercise Program for teaching Python
#   Author: Nikos-Nikitas
#   GitHub: nikosnikitas

# ------------------------------------- #

# importing sleep function to wait before next step
from time import sleep

# the Exercise class can be customized to your needs
# starts with a level which it checks and if it is completed or not.
class Exercise():
    
    # Constructor - when object is made it prints
    def __init__(self,level,completed):

        self.level = level
        self.completed = completed
        print(f"New Exercise begins!\nLevel: {level}\nCompleted: {completed}")

        # Level 1 of Exercise
        def lv1():
            
            points = 0

            correct_answers1 = ["print(\"hello, world\")", "print('hello world')"]
            
            print("Welcome!")
            name = input("What's your name?\n>>> ")
            print(f"Hello {name}! Nice to meet you!")
            sleep(0.4)
            print("This is your first exercise.")
            print("To complete this exercise and win 100 points solve this:")

            answer = str(input("CHALLENGE: Print 'Hello World' to the screen!\nYour answer > "))

            # if user's answer (in lowercase letters) is in correct answers list
            # prints the text of the user's print() function
            if answer.lower() in correct_answers1:
                print(answer[7:18])
                points += 100
                
                # opens/creates the save file progress.k and writes the points and the user's name
                with open("progress.k","w") as f:
                    f.write(str(points))
                    f.write(f"User Name: {name}")
                f.close()
                    
                print(f"Congratulations!!\n You now have: {points} points!")
                sleep(0.3)
                print("Thank you for playing!\n")
                sleep(0.4)
                print("Your progress is saved in 'progress.k'.\nGoodbye!")
                self.completed = True
            # if answer is not correct repeats the level
            else:
                print("Nope! Try again.")
                lv1()

        # checks given level
        if level == 1:
            lv1()
        else:
            print("No level found.")

# new Exercise object ( Level: 1, Completed: False )
ex = Exercise(1,False)
