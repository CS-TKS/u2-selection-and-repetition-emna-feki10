import random
recyclables = ["Plastic Bottles", "Paper Bags", "Bottle Caps", "Glass Bottles", "Metal Cans"]
compostables = ["Banana Peels", "Egg Shells", "Coffee Grounds", "Grass Clippings", "Dry Leaves"]
trash = ["Tissue Paper", "Plastic Bags", "Chip Bags", "Straws", "Plastic Spoons"]

allitems = ["Plastic Bottles", "Paper Bags", "Bottle Caps", "Glass Bottles", "Metal Cans","Banana Peels", "Egg Shells", "Coffee Grounds", "Grass Clippings", "Dry Leaves","Tissue Paper", "Plastic Bags", "Chip Bags", "Straws", "Plastic Spoons"]

random.shuffle(allitems)
print(" ")
print("Hello Welcome to the Trash Sorter quiz!")
print(" ")
print("Instructions: To play, the game will ask you where a specific trash item belongs.")
print("- If you answer is recyclables then enter 1")
print("- If you answer is compostables then enter 2")
print("- If you answer is trash/landfill then enter 3")
print("- If you want to leave the game enter 4")
print(" ")
proceed = int(input("Enter 0 to proceed: "))
print(" ")
if proceed == 0:
    play = True
else:
    play = False

while play == True:
    score = 0
    random.shuffle(allitems)
    for item in allitems:
        if item in recyclables:
            cat = 1
        elif item in compostables:
            cat = 2
        elif item in trash:
            cat = 3

        if score <= 50:
            rate = "Need Work. Practice More!"
        elif 50 < score <= 100:
            rate = "Almost There!"
        elif 100 < score <=150:
            rate= "Amazing! Trash Sorting Expert!"

        ans = int(input("Where does " + item + " go?: "))
        print(" ")
        if ans == cat:
            print("Correct!")
            score = score + 10
            print("Score:" , score)
            print(" ")
        elif ans == 4:
            print("Score:" , score)
            print(rate)
            print("Thanks for playing!")
            break
        else:
            print("Incorrect")
            score = score - 5
            print("Score:" , score)
            print(" ")
    print(rate)
    playagain = input('Do you want to play again? If yes enter "T" if no enter "F".: ')
    print(" ")

    if playagain == "T":
        play = True
        print("New Game")
        print(" ")
    elif playagain == "F":
        play = False
    else:
        break






