def starting_screen():
    print("Hello! Welcome to Storming the Bastille: Choose Your Own Adventure game!")
    print("Background: On July 14, 1789 was when this event took " \
    "place. Revolutionary insurgents were attempting to take " \
    "gunpowder from the Bastille fortress. They were also " \
    "wanting to challenge the king's authority with tension high. " \
    "This tension between the king and his subjects were caused by " \
    "food shortages, heavy taxes, arrests of the new National " \
    "Assembly, and even the dismissal of the minister Jacques " \
    "Necker.")
    print("For your first decision: You are now Governor Bernard-Rene Jordan de Launay." \
    " You choose. A: You surrender the gunpowder to the rebels." \
    " Or B: You refuse to surrender the gunpowder without royal orders.")
    decision_1 = input("Which option would you like to choose? ")
    if decision_1 == 'A' or decision_1 == 'a':
        print('You chose to go against history and choose a more peaceful approach.' \
        " You hand over the gunpowder to the rebels. They ready their ammunition. And BOOM." \
        " You died. Nice try.")
    elif decision_1 == 'B' or decision_1 == 'b':
        print("You chose to follow history with this one. The rebels stall for a few hours before they storm the palace and" \
        " you barely manage to escape and hide. Good Job!")
        print("You are now a French Guard at the fortress. You notice the rebels are trying to get into the palace to get to the king. Do you, A: Join them, B: Stand your ground, or C: Run and hide in the fortress?")
        decision_2 = input("What would you like to do? ")
        if decision_2 == 'A' or decision_2 == 'a':
            print("You chose to follow history on this one. You run to join the crowd of rebels and help them ready the cannons.")
        elif decision_2 == 'B' or decision_2 == 'b'
            print("You chose to go against history this time. It did not work out for you. You refused to join the rebels and your head ended up on a pike. How unfortunate.")
        elif decision_2 == 'C' or decision_2 == 'c':
            print("You chose not to follow the history books and it worked out! You run and hide inside the fortress. While trying to find a spot you see" / 
            " Governor Bernard-Rene Jordan de Launay. Will you, A: Ask to hide with him, B: Betray him to the rebels, or C: Find another place to hide.")
            decision_3 = input("What would you like to do? ")
            if decision_3 == 'A' or decision_3 == 'a':
                print("You walk towards the Governor. He takes a step back and hits the wall thinking you're a threat. You reasure him and ask to hide as well. He agrees.")
            if decision_3 == 'B' or decision_3 == 'b':
                print("You decided to betray someone who could have been your friend. How foolish. You call for someone to come. A group of insurgents arrive, kill the governor, " \
                "and put his head on a pike. They quickly move on to you. Like I said, foolish.")
    else:
        print('Not a valid input. Please try again.')
def main():
    starting_screen()

main()
