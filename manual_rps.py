
# %%
import random
import camera_rps

class choice: 

    def get_computer_choice(): 
        """
        Return randomized choice between rock paper scissors
     
        """
        list_of_choices = ["rock","paper","scissors"]
        computer_choice_made = random.choice(list_of_choices)
        return computer_choice_made

    def get_user_choice():

        """
     Return choice made by the user 
        """
        choice = camera_rps.get_prediction()
        return choice 
        # while(True):
        #     list_of_choices = ["rock","paper","scissors"]
        #     user_choice = input("Please choose an option: ")
        #     user_choice = user_choice.lower()

        #     if(user_choice in list_of_choices):
        #         print("reached if")
        #         return user_choice
                
        #     else:
        #         print("reached else")
        #         continue

    
# %%
