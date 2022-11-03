#Neil Daterao

#Game of sticks between two players (human v. human)

def get_yn_input():
    """Get a yes/no answer from the user."""
    yes_no = input("Do you want to play again? Type y or n.    ")
    while yes_no not in ["y", "n"]:
        print("Please input 'y' or 'n'.")
        yes_no = input("Do you want to play again? Type y or n.    ")
    return yes_no
    
def introduction():
    """Print a welcome message and determine how many sticks should be used."""
    #Introduction text and input for number of sticks
    print("\nWelcome to the game of sticks!")
    num_sticks = int(input("How many sticks are there on the table initially (10-100)? "))
    return num_sticks 

def one_round_of_sticks(total_sticks, player1, player2):
    """player1 and player2 play one round of sticks against each other. 
    They start with a pile of total_sticks sticks."""
    current_player = player1
    other_player = player2
    #player1_choice = 0
    #player2_choice = 0 
    
    
    #The game will play while there are still available sticks 
    while total_sticks > 0: 
        print("\nThere are", total_sticks, "on the board")
        player1_choice = int(player_1_choice())
        total_sticks -= player1_choice
        
        if total_sticks <= 0: 
            print("Player 1, you lose.")
            return 
        
        print("\nThere are", total_sticks, "on the board")
        player2_choice = int(player_2_choice())
        total_sticks -= player2_choice
        
        if total_sticks <= 0: 
            print("Player 2, you lose.")
            return 
        
        
    

def player_1_choice():
    while True:
        choice = input("Player 1: How many sticks do you take (1-3)? ")
        if choice.isdigit() == True:
            choice = int(choice)
            if choice > 3 or choice < 1: 
                print("Please input a number between 1 and 3.")
            
            else: 
                return choice
        else:
            print("Please input a number between 1 and 3.")
            

def player_2_choice():
    while True: 
        choice = int(input("Player 2: How many sticks do you take (1-3)? "))
        if choice > 3 or choice < 1: 
            print("Please input a number between 1 and 3.")
        else: 
            return int(choice)
            
        
        

def sticks():
    total_sticks = introduction()
    player1 = (1, "human")
    player2 = (2, "human")
    
    keep_playing = 'y'
    while keep_playing == 'y':
        one_round_of_sticks(total_sticks, player1, player2)
        keep_playing = get_yn_input()
        if keep_playing == 'y':
            print("Great!")

    print("Ok. See you next time. Bye, bye!")

    
### DO NOT DELETE THIS LINE: beg testing

sticks()
