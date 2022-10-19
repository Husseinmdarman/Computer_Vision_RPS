
# %%
import random

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
        while(True):
            list_of_choices = ["rock","paper","scissors"]
            user_choice = input("Please choose an option: ")
            user_choice = user_choice.lower()

            if(user_choice in list_of_choices):
                print("reached if")
                break
            else:
                print("reached else")
                continue

    
# %%
