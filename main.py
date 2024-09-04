# Write a rock, paper, scissors, lizard, spock game with ASCII art
# import random module
import random

# ASCII art for each choice
ascii_art = {
    'rock': '''
    rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''',
    'paper': '''
    paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    ''',
    'scissors': '''
    scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''',
    'lizard': '''
    lizard
     _______
---'   ____)____
          ______)
         _______)
        (____)
---.__(___)
    ''',
    'spock': '''
    spock
     ______
---'   ____)
       (____)___
          ______)
       __________)
---.__(___)
    '''
}

# define main function that handles all the logic
def main():
    # define a list of choices
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    # get user input
    user_choice = input('Enter rock, paper, scissors, lizard, or spock: ').lower()

    # get computer choice
    computer_choice = random.choice(choices)

    # print the choices with ASCII art
    print(f'You chose:\n{ascii_art[user_choice]}')
    print(f'The computer chose:\n{ascii_art[computer_choice]}')

    # determine the winner
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif user_choice == 'rock':
        if computer_choice in ['scissors', 'lizard']:
            print('You win!')
        else:
            print('You lose!')
    elif user_choice == 'paper':
        if computer_choice in ['rock', 'spock']:
            print('You win!')
        else:
            print('You lose!')
    elif user_choice == 'scissors':
        if computer_choice in ['paper', 'lizard']:
            print('You win!')
        else:
            print('You lose!')
    elif user_choice == 'lizard':
        if computer_choice in ['spock', 'paper']:
            print('You win!')
        else:
            print('You lose!')
    elif user_choice == 'spock':
        if computer_choice in ['scissors', 'rock']:
            print('You win!')
        else:
            print('You lose!')
    else:
        print('Invalid input. Please enter rock, paper, scissors, lizard, or spock.')

if __name__ == "__main__":
    main()