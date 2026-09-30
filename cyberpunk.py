door = input("You are in a haunted house and need to escape. "
             "Pick door 1, 2 or 3: ")

if door == "1":
    book = input("You enter a library. Pick book 1, 2 or 3: ")
    if book == "1":
        print("You feel dizzy and return to the first room. Run the game again.")
    elif book == "2":
        print("You find a secret passage and escape!")
    elif book == "3":
        print("Flames come out of the book and you die.")
    else:
        print("That's not a book.")

elif door == "2":
    bowl = input("You enter a kitchen. Pick bowl 1, 2 or 3: ")
    if bowl == "1":
        print("You float away... nobody knows what happens.")
    elif bowl == "2":
        print("The floor opens and flames shoot out. You die.")
    elif bowl == "3":
        print("You feel a key in your mouth and escape through a secret passage!")
    else:
        print("That's not a bowl.")

elif door == "3":
    print("The door opens, flames come out, and you die.")

else:
    print("That's not a door.")
