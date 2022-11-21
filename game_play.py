# %%
import manual_rps as getCompandPlayerChoice
import game_logic

def play():
    """
    Simulates one round of rock paper scissors
    """
    computer_choice = getCompandPlayerChoice.choice.get_computer_choice()
    player_choice = getCompandPlayerChoice.choice.get_user_choice()
    print(computer_choice, player_choice)
    game_play = game_logic.GameLogic(computer_choice, player_choice)
    winner = game_play.get_winner()
    print(winner)

if __name__ == "__main__": 
    play()
    pass    
    


# %%