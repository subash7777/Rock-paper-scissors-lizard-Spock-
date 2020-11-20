# Rock-paper-scissors-lizard-Spock code


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
def name_to_number(name) :
    
    #converting name to number using if/elif/else and returning the result

    if name == "rock" :
        return 0
    elif name == "Spock" :
        return 1
    elif name == "paper" :
        return 2
    elif name == "lizard" :
        return 3
    elif name == "scissors" :
        return 4
    else :
        return "Error in the name"
  

def number_to_name(number):
    # converting number to a name using if/elif/else and returning the result

    if number == 0 :
        return "rock"
    elif number == 1 :
        return "Spock"
    elif number == 2 :
        return "paper"
    elif number == 3 :
        return "lizard"
    elif number == 4 :
        return "scissors"
    else :
        return "Error"
    

def rpsls(player_choice):
    
    # printing out the message for the player's choice
    print " Player's choice is ", player_choice
    
    # converting the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # computing random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # converting comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # printing out the message for computer's choice
    print " Computer's choice is", comp_choice
    
    # computing difference of comp_number and player_number modulo five
    difference_mod_five = (comp_number - player_number) % 5
    
    # using if/elif/else to determine winner, print winner message
    if difference_mod_five == 3 or difference_mod_five == 4 :
        print " The winner is Player !!!"
    elif difference_mod_five == 0 :
        print " The choices matched. So there's a tie !!! " 
    elif difference_mod_five == 1 or difference_mod_five == 2:
        print " The winner is Computer !!! "
    else :
        print "Error"
    # printing a blank line to separate consecutive games
    print " "
    
    
# testing the code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




