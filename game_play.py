# %%
import manual_rps as getCompandPlayerChoice
import game_logic

_rounds = []

def final_winner(game_outcome: list):
    user_outcome = sum([i[0] == 'wins' for i in game_outcome])
    computer_outcome = sum([i[1] == 'wins' for i in game_outcome])

    if(computer_outcome > user_outcome):
        print(f'the computer has won {computer_outcome} whereas the player lost')
    elif(user_outcome > computer_outcome):
        print(f'the player has won {user_outcome} whereas the computer lost')
    

def play():
    """
    Simulates one round of rock paper scissors
    """
    while(len(_rounds) < 4):
        computer_choice = getCompandPlayerChoice.choice.get_computer_choice()
        player_choice = getCompandPlayerChoice.choice.get_user_choice()
        print(computer_choice, player_choice)
        game_play = game_logic.GameLogic(computer_choice, player_choice)
        winner = game_play.get_winner()
        if(winner[1] != 'draw'):
            _rounds.append(winner)
        
    final_winner(_rounds)

if __name__ == "__main__": 
    play()
    pass    
    


# %%