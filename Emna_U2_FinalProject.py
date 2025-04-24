import random
recyclables = ["Plastic Bottle", "Paper Bag", "Bottle Caps", "Glass Bottles", "Metal Can"]
compostables = ["Banana Peels", "Egg Shells", "Coffee Grounds", "Grass Clippings", "Dry Leaves"]
trash = ["Tissue Paper", "Plastic Bag", "Chip Bag", "Straw", "Plastic Spoon"]

allitems = ["Plastic Bottle", "Paper Bag", "Bottle Caps", "Glass Bottles", "Metal Can","Banana Peels", "Egg Shells", "Coffee Grounds", "Grass Clippings", "Dry Leaves","Tissue Paper", "Plastic Bag", "Chip Bag", "Straw", "Plastic Spoon"]

random.shuffle(allitems)


proceed = int(input("Enter 0 to proceed: "))
if proceed == 0:
    play = True

while play == True:
    score = 0

    for item in allitems:
        if item in recyclables:
            cat = 1
        elif item in compostables:
            cat = 2
        elif item in trash:
            cat = 3

        ans = int(input("Where does ", item, " go?: "))
        if ans == cat:
            print("Correct!")
            score = score + 1
        elif ans == "exit":
            break
        else:
            print("Incorrect")

    play = input('Do you want to play again? if yes write "True" if no write "False"')






