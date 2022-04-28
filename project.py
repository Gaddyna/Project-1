# Function 1: Input Player Rounds
def inputRounds():
    try:
        rounds = int(input("Please enter the number of rounds you would like to play: "))
    except:
        rounds = 2
        print("Invalid response using default value of: ", rounds)
    return rounds

# Function 2: Input Player Word
def inputWord(player,prev_word):
    #take input from user
    word = str(input("Player:"+str(player)+", Please enter your word: "))
    s = 0
    #if player input a valid word, score will be calculated
    if(validWord(word,prev_word)):
        s = playerScore(word)
    #return the word and the score for this turn
    return(word,s)

# Function 3: Validate Word
def validWord(word,prev_word):
    #check for empty word
    if(prev_word==""):
        return True
    #compare current word with previous word
    elif(word=="" or word==prev_word):
        return False
    #if the AND operation of two sets give one or more characters, means they have common letters
    elif(len(list(set(word)&set(prev_word)))>0):
        return True
    else:
        return False


# Function 4: Generate Score
def playerScore(word):
    s = 0 
    for i in word:
        s+=points[i]
    return s

# Method 5: Initialize List with Messages
def initMessages():
    messages = [
    'Player {} Wins with a score of {}!',
    'Tie Game, no winners.',
    'Invalid word! Player {} Wins!',
    'Invalid word! You must enter a valid word to start.',
    'Player {} Entered the Words:'
    ]
    return messages

# Function 6: Initialize Points Dictionary
def initPoints():
    points = {
    "a": 1 , "b": 3 , "c": 3 , "d": 2 ,
    "e": 1 , "f": 4 , "g": 2 , "h": 4 ,
    "i": 1 , "j": 8 , "k": 5 , "l": 1 ,
    "m": 3 , "n": 1 , "o": 1 , "p": 3 ,
    "q": 10, "r": 1 , "s": 1 , "t": 1 ,
    "u": 1 , "v": 4 , "w": 4 , "x": 8 ,
    "y": 4 , "z": 10
    }

    return points

# Main Program
if __name__ == '__main__':
    #initialize global variables
    points = initPoints()
    messages = initMessages()
    
    #intializing variables
    player1 = 1
    player2 = 2
    total_score1 = 0 
    total_score2 = 0
    
    #input the number of rounds
    rounds = int(inputRounds())
    
    #inititalizing variables with empty string
    prev_word1 = ""
    prev_word2 = ""
    
    #for loop to repeat multiple times
    for i in range(0,rounds):
        #printing round number.
        print("Round:",i+1)
        
        #player1 turn
        prev_word1,score = inputWord(player1,prev_word1)
        total_score1+=score
        
        #player2 turn
        prev_word2,score = inputWord(player2,prev_word2)
        total_score2+=score
    
    #printing the total scores        
    print("Player 1 Score:",total_score1)
    print("Player 2 Score:",total_score2)
    
    #printing the winner with greater score
    if(total_score2>total_score1):
        print("Player 2 Won!!!!")
    elif(total_score2<total_score1):
        print("Player 1 Won!!!!")
    else:
        print("Draw!!!")
