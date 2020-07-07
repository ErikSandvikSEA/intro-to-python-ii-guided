# write a program to play Rock Paper Scissors with a user
# let's flesh out the rules and think about how this is going to work

# Rules:  
            # rock -> scissors 
            # paper -> rock
            # paper -> rock
ties = 0
wins = 0
losses = 0        

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
        

        # Program specifies its choice 
            # How does the program determine its choice?
                # have it randomly pick a choice using Python's random.choice function
    import random
    possible_choices = ['rock', 'paper', 'scissors']
    programs_choice = random.choice(possible_choices)
    print(f"Program picks: {programs_choice}")

        # Once both choices are made, compare them via the rules to see who won 
            # How do we do the comparison?
                # Use if statements
    if users_choice == "rock":
        if programs_choice == 'rock':
            print('A TIE!')
            ties += 1
        elif programs_choice == 'paper':
            print('Program won!')
            losses += 1
        else:
            print('YOU WIN!')
            wins += 1
    elif users_choice == "paper":
        if programs_choice == 'paper':
            print('A TIE!')
            ties += 1
        elif programs_choice == 'scissors':
            print('Program won!')
            losses += 1
        else:
            print('YOU WIN!')
            wins += 1
    elif users_choice == "scissors":
        if programs_choice == 'scissors':
            print('A TIE!')
            ties += 1
        elif programs_choice == 'rock':
            print('Program won!')
            losses += 1
        else:
            print('YOU WIN!')
            wins += 1
    else:
        print('I do not understand that')
        # go on to the next loop 
        continue

    
        # keep track of number of wins, losses, and ties for the user
            # How do we do this?
                # have separate variables for each
    print(f"Current Score:\nWins: {wins}, Losses: {losses}, Ties: {ties}")

