# Things that could be improved: 
# Make the way the computer picks a choice smarter so that it wins more consistently 
# allow more choices other than rock, paper, scissors 
# save the outcomes 
# sanitize the user input: make it so that the program can handle inputs like 'r' for rock, etc 
# be smarter about comparing user and computer choices 
# add some funny commentary from the computer 
# add more game types 
# win/loss percentage 






# write a program to play Rock Paper Scissors with a user
# let's flesh out the rules and think about how this is going to work

# Rules:  
            # rock -> scissors 
            # paper -> rock
            # paper -> rock
ties = 0
wins = 0
losses = 0    


# takes both the players and computer's choices
# decides the outcome 
# what should this function return?
# Returns 0 to indicate a tie, 1 to indicate the user won, and -1 to indicate the computer won
def compare_choices(player_choice, computer_choice):
    if player_choice == programs_choice:
        return 0
    # player wins 
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
        (player_choice == 'scissors' and computer_choice == 'paper') or \
        (player_choice == 'paper' and computer_choice == 'rock'):
        return 1
    # player loses 
    else:
        return -1

possible_choices = ['rock', 'paper', 'scissors']

# Flow: 
    # Start up program 
while True:
        # User will specify their choice
            #  How does the program read the user's choice?
                # Use Python's input function
    users_choice = input('Choose rock, paper, or scissors: ')
    if users_choice== "quit":
        print('See you next time!')
        break
    elif users_choice not in possible_choices:
        print('I do not understand')
        continue
        

        # Program specifies its choice 
            # How does the program determine its choice?
                # have it randomly pick a choice using Python's random.choice function
    import random
    programs_choice = random.choice(possible_choices)
    print(f"Program picks: {programs_choice}")

        # Once both choices are made, compare them via the rules to see who won 
            # How do we do the comparison?
                # Use if statements
                # refactor to make it more readable

    result = compare_choices(users_choice, programs_choice)
    if result == 0:
        print('A TIE!')
        ties += 1
    elif result == 1:
        print("You win!")
        wins += 1
    elif result == -1:
        print('Computer wins!')
        losses += 1

    
        # keep track of number of wins, losses, and ties for the user
            # How do we do this?
                # have separate variables for each
    print(f"Current Score:\nWins: {wins}, Losses: {losses}, Ties: {ties}\n-----------------------------------------------")

