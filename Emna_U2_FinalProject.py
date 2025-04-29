
# To import the random module to randomize the items
import random


# Lists of items organized in their categories
recyclables = ["Plastic Bottles", "Paper Bags", "Bottle Caps", "Glass Bottles", "Metal Cans"]
compostables = ["Banana Peels", "Egg Shells", "Coffee Grounds", "Grass Clippings", "Dry Leaves"]
trash = ["Tissue Paper", "Plastic Bags", "Chip Bags", "Straws", "Plastic Spoons"]

# Combined list with all items to be tested on in the quiz
allitems = ["Plastic Bottles", "Paper Bags", "Bottle Caps", "Glass Bottles", "Metal Cans","Banana Peels", "Egg Shells", "Coffee Grounds", "Grass Clippings", "Dry Leaves","Tissue Paper", "Plastic Bags", "Chip Bags", "Straws", "Plastic Spoons"]

# Shuffle/randomize the order of the items in the list
random.shuffle(allitems)

# Game inroduction and instructions
print("\n Hello Welcome to the Trash Sorter quiz! \n")
print("Instructions: To play, the game will ask you where a specific trash item belongs.")
print("- If you answer is recyclables then enter 1")
print("- If you answer is compostables then enter 2")
print("- If you answer is trash/landfill then enter 3")
print("- If you want to leave the game enter 4")
print(" ")
# Ask the player to start the quiz
proceed = int(input("Enter 0 to proceed: "))
print(" ")
if proceed == 0:
    play = True
else:
    play = False

# Main game loop
while play == True:
    score = 0 # Reset score every round
    random.shuffle(allitems) # To shuffle/randomize the item order every round
    for item in allitems:
        if item in recyclables: # Determine the correct category of the item
            cat = 1
        elif item in compostables:
            cat = 2
        elif item in trash:
            cat = 3


        if score <= 50:
            rate = "Need Work. Practice More!" # Determine how well the user did/ give feedback based of the users score
        elif 50 < score <= 100:
            rate = "Almost There!"
        elif 100 < score <=150:
            rate= "Amazing! Trash Sorting Expert!"

        # Ask the user where each item belongs
        ans = int(input("Where does " + item + " go?: "))
        print(" ")
        if ans == cat:
            print("Correct!")
            score = score + 10 # Increase the score if the answer is correct
            print("Score:" , score)
            print(" ")
        elif ans == 4: # Player chooses to exit the game
            print("Score:" , score)
            print(rate)
            print("Thanks for playing!")
            break
        else:
            print("Incorrect")
            score = score - 5 # Remove points for incorrect answers
            print("Score:" , score)
            print(" ")

    # Print feedback/level
    print(rate)
    playagain = input('Do you want to play again? If yes enter "T" if no enter "F".: ')
    print(" ")

    # Ask the user to play again
    if playagain == "T":
        play = True
        print("New Game")
        print(" ")
    elif playagain == "F": # Determine if the loop will loop again
        play = False
    else: # End game if input s not recognized
        break






