import random

hands = ('rock', 'paper', 'scissors')
you_choice = random.choice(hands)


def vs_result(my_choice):
    if my_choice == 'rock':
        if you_choice == 'scissors':
            return 'win'
        elif you_choice == 'paper':
            return 'lose'
        else:
            return 'one more'
    elif my_choice == 'paper':
        if you_choice == 'rock':
            return 'win'
        elif you_choice == 'scissors':
            return 'lose'
        else:
            return 'one more'
    elif my_choice == 'scissors':
        if you_choice == 'paper':
            return 'win'
        elif you_choice == 'rock':
            return 'lose'
        else:
            return 'one more'


my_hand = input('handchoice("rock" or "paper" or "scissors"): ')
result = vs_result(my_hand)

print('myhand:', my_hand)
print('youhand:', you_choice)
print('result:', result)
