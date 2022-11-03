#Neil Daterao

#Game of sticks which first trains the AI, then uses the trained AI to play against a user 

import random as r 

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
    
    #Assign the dictionaries to more readable variable names 
    ai_hats = player2[2]
    ai_besides_hats = player2[3]
   
    #Make a boolean variable, if ai_win is true at the end of the game, we'll add all the winning moves to the hats, if ai loses, we'll take out the losing moves from the hats 
    ai_win = bool
    
    while total_sticks > 0: 
        print("\nThere are", total_sticks, "on the board")
        player1_choice = int(player_1_choice())
        total_sticks -= player1_choice
        
        #If player 1 takes the last stick, they lose
        if total_sticks <= 0: 
            print("Player 1, you lose.")
            ai_win = True
            break #The reason for this break is because if you don't exit the loop here, it'll proceed to the next lines of code when the game should already be over 
            
        print("\nThere are", total_sticks, "on the board")
        update_ai = ai_choice(total_sticks, ai_hats, ai_besides_hats) #Get the AI choice and update the hats for the AI 
        aichoice = update_ai[0] #Variable for the actual selection the AI makes 
        
        print("AI selects", aichoice)
        total_sticks -= aichoice
        
        #If the AI takes the last stick, they lose 
        if total_sticks <= 0: 
            print("AI loses")
            ai_win = False
            break
        
    #If the AI wins the game, check each key and value of the besides_hat dictionary 
    if ai_win == True: 
        
        for (hat, ball) in ai_besides_hats.items():
                #If this hat has no balls, move onto the next hat
                if ball == []:
                    pass
                else: 
                    #If this hat has a ball and the ai won, we know that the ball represents the winning move, therefore we should remove it from the besides_hat dictionary and add two of the winning_moves to the ai_hats dictionary to the corresponding hat
                    winning_move = ball[0]
                    ai_besides_hats[hat].remove(winning_move)
                    ai_hats[hat].append(winning_move)
                    ai_hats[hat].append(winning_move)
      
        
    else: 
        #If the AI loses, check each key and value of the besides_hat dictionary
        for (hat, ball) in ai_besides_hats.items():
                #If this hat has no balls, move onto the next hat
                if ball == []:
                    pass
                else: 
                    #If this hat has a ball and the ai loses, we know that the ball represents the losing move. We should then remove that ball from the besides_hat dictionary
                    losing_move = ball[0]
                    ai_besides_hats[hat].remove(losing_move)
                    
                    #We want to make sure each hat has at least one of each ball. If not, add the losing move to the hat. If the losing move is already in the hat, we'll just be tossing the losing move from the besides_hat dictionary
                    if losing_move not in ai_hats[hat]:
                        ai_hats[hat].append(losing_move)
            
def initialize_ai(player_num, total_sticks):
    """Create a new AI player represented as a 4-tuple of the form
    (player_num, "ai", hats, besides_hats)."""
    #Create a hashtable for hats. Each hat starts with ball (1,2,3)
    hats = {}
    for num in range(total_sticks):
        hats[num+1] = [1,2,3]
    
    #Identical hashtable for besides hats, however, these keys just have empty lists as values 
    besides_hats = {}
    for num in range(total_sticks):
        besides_hats[num+1] = []
    
    
    return (player_num, "ai", hats, besides_hats)


def one_round_ai_v_ai(total_sticks, ai):
    
    #skilled AI 
    ai_hats = ai[2]
    ai_besides_hats = ai[3]
    
    #Make a boolean variable, if ai_win is true at the end of the game, we'll add all the winning moves to the hats, if ai loses, we'll take out the losing moves from the hats 
    ai_win = bool
    
    #This is the code for the reguluar AI, which simply just picks a random number between 1 and 3. The purpose of this AI is just to train the skilled AI 
    while total_sticks > 0: 
        reg_ai_choice = r.randint(1,3)
        total_sticks -= reg_ai_choice
        
        if total_sticks <= 0: 
            ai_win = True
            break
        
        update_ai = ai_choice(total_sticks, ai_hats, ai_besides_hats) #Get the AI choice and update the hats for the AI 
        aichoice = update_ai[0] #Variable for the actual selection the AI makes 
        total_sticks -= aichoice
        
        #If the AI takes the last stick, they lose 
        if total_sticks <= 0: 
            ai_win = False
            break
        
    #If the AI wins the game, check each key and value of the besides_hat dictionary 
    if ai_win == True: 
        
        for (hat, ball) in ai_besides_hats.items():
                #If this hat has no balls, move onto the next hat
                if ball == []:
                    pass
                else: 
                    #If this hat has a ball and the ai won, we know that the ball represents the winning move, therefore we should remove it from the besides_hat dictionary and add two of the winning_moves to the ai_hats dictionary to the corresponding hat
                    winning_move = ball[0]
                    ai_besides_hats[hat].remove(winning_move)
                    ai_hats[hat].append(winning_move)
                    ai_hats[hat].append(winning_move)
        
    else: 
        #If the AI loses, check each key and value of the besides_hat dictionary
        for (hat, ball) in ai_besides_hats.items():
                #If this hat has no balls, move onto the next hat
                if ball == []:
                    pass
                else: 
                    #If this hat has a ball and the ai loses, we know that the ball represents the losing move. We should then remove that ball from the besides_hat dictionary
                    losing_move = ball[0]
                    ai_besides_hats[hat].remove(losing_move)
                    
                    #We want to make sure each hat has at least one of each ball. If not, add the losing move to the hat. If the losing move is already in the hat, we'll just be tossing the losing move from the besides_hat dictionary
                    if losing_move not in ai_hats[hat]:
                        ai_hats[hat].append(losing_move)
        
        #Return the trained AI
        return ai 
        
             
def train_ai(ai, total_sticks):
    """Train the given AI by having it play many times against a second,
    new AI."""
    # We need the new AI to make random moves and we'll have our "skilled AI" update the hats based on these random moves 
    print("Training AI, please wait...")
    
    #Go through 10000 rounds of the game to train the AI 
    training_runs = 10000
    
    while training_runs > 0: 
        one_round_ai_v_ai(total_sticks, ai)
        training_runs -= 1
    
    #print(ai[2]) -> You can use this to see the updated AI and the winning moves added to each hat 
    
        
#Choice for player 1
def player_1_choice():
    #Function will repeat until a valid input is given
    while True:
        choice = input("Player 1: How many sticks do you take (1-3)? ")
        #First we want to make sure that the input is a digit, if not, pick again, then check if the number is between 1 and 3, if not pick again. 
        if choice.isdigit() == True:
            choice = int(choice)
            if choice > 3 or choice < 1: 
                print("Please input a number between 1 and 3.")
            
            else: 
                return choice
        else:
            print("Please input a number between 1 and 3.")
            
def ai_choice(total_sticks,hats,besides_hats):                                                          
    #Assign the ai selection to a variable -> We want to go the hat that corresponds with the amount of sticks on the board. Then we'll make a random selection from the list of balls corresponding to that hat 
    ai_selection = int(r.choice(list(hats[total_sticks])))
    
    #We want to remove that ball from the hat and place it in the besides_hat dictionary, corresponding to the same number hat 
    hats[total_sticks].remove(ai_selection)
    besides_hats[total_sticks].append(ai_selection)
    
    return (ai_selection, hats, besides_hats) 
            
# Main

def sticks():
    total_sticks = introduction()
    player1 = (1, "human")
    player2 = initialize_ai(2, total_sticks)
    
    train_ai(player2, total_sticks)
    #print("HATS:", player2[2]) # see what your AI has learned
    
    keep_playing = 'y'
    while keep_playing == 'y':
        one_round_of_sticks(total_sticks, player1, player2)
        keep_playing = get_yn_input()
        if keep_playing == 'y':
            print("Great!")

    print("Ok. See you next time. Bye, bye!")

    
### DO NOT DELETE THIS LINE: beg testing

sticks()
