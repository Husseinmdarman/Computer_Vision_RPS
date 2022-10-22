# %%


class GameLogic:
    """
    This class handles all the logic to do with the rock paper scissors game

    Atrribute:

    Result: Has all the possible consquences when making a move for example, if the outcome was rock vs rock then the result is draw

    """       
       

    result = {'rock' : {"rock" : "draw", "paper" : "loses", "scissors" : "wins" },
          'paper' : {"paper" : "draw", "scissors" : "loses", "rock" : "wins" },
          'scissors' : {"scissors" : "draw", "rock" : "loses", "paper" : "wins" }}
    
    def __init__(self, computer_choice, player_choice):
        """
        This class is initialised with the computer and player choice

        Parameter:

        Computer_Choice:  is the computer choice during the game
        Player_choice: is the player choice during the game
        """
        self.computer_choice = computer_choice
        self.player_choice = player_choice
        
    def get_winner(self):
        """
        Returns the winner between the player and computer
        """

        player_outcome = GameLogic.result[self.player_choice][self.computer_choice]
        
        if(player_outcome == "wins"):
            return [player_outcome, "loses"]
            
        elif(player_outcome == "loses"):
            return [player_outcome, "wins"]
            
        else:
            return ["draw","draw"]
            

     
     
        
# %%
