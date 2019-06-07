import random
my_list = ["rock","paper","scissors"]
computer_choise = random.choice(my_list)
# print computer_choise
    while True:
        print computer_choise
        user_play = raw_input("enter a rock, paper, scissor :)")
        if computer_choise not in user_play:
            print "invalid"
        elif computer_choise == user_play:
            print "Drow"
        elif computer_choise == "rock" and user_play == "paper":
            print "win"
        elif computer_choise == "paper" and user_play == "scissors":
            print "win"
        elif computer_choise == "scissor" and user_play == "rock":
            print "win"
        elif computer_choise == "scissor" and user_play == "paper":
            print "win"
        elif computer_choise == "paper" and user_play == "rock":
            print "win"
        elif computer_choise == "rock" and user_play == "paper":
            print "win"
        else:
            print "lose"
        again_user = raw_input('Do you want to play again? (yes or no)')
        if again_user == "yes":
            continue
        elif again_user == "no":
            break









