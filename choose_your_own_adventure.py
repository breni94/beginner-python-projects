name = ("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to and end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around or swim to swim across: ")

    if answer == "swim":
        print("You swam across and eaten by an alligator.")
    elif answer == "walk":
        print("You walked for too long and ran out of water. You lost the game.")
    else:
        print("Not a valid option. You lost the game.")

elif answer == "right":
    answer = input("You arrive at a bridge, it looks unstable. Do you want to cross or go back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and you meet a stranger. Dou you want to talk to them (yes/no) ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and now the are offended. You lose.")
        else:
            print("Not a valid option. You lost the game.")
else:
    print("Not a valid option. You lost the game.")

print("Thank you for playing", name)
    