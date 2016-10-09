# Python 2.7.12
#
# Author: Madison Dunning
#
# Purpose:  The Tech Academy Python Course, Step 6/63
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           remember function_name(variable)_ means that we pass in the variable.
#           return_variable_means that we are returning the variable to
#           the calling function.



def start (nice=0, mean=0, name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)



def describe_game(name):
    """
        check to see if this is a new game or not.
        If it is a new game, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    if name != "": # That is, if the user does not have a name than they are a new player
        print ("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
                if name == "":
                    name = raw_input("\nWhat is your name? ").capitalize()
                    if name != "":
                            print("\nWelcome {}!".format(name))
                            print("\nIn this game you will be greeted by several different people. \nYou can be nice or mean.")
                            print("at the end of the game your fate will be influenced from your actions.")
                            stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = raw_input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? n/m:").lower()
        if pick == "n":
            print("They smile, wave, and walk away...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly and abruptly storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()

def show_score(nice,mean,name):
    print ("\n{}, you currently have ({}, Nice) and ({}, Mean) points.".format(name,nice,mean))


def score(nice,mean,name):
    # score function is being passed the values stored in the three variables
    if score>5: # if the condition is valid, call win function and pass on variable
        win(nice,mean,name)
    if score<5:
        lose(nice,mean,name)
    else:       # Else, go back to nice_mean
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you and you now live in a palace.".format(name))
    again(nice,mean,name)


def lose(nice,mean,name):
    print("\nToo bad, game over! \nYou live in a van by the river, wretched and alone.".format(name))
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n.").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', or 'n' for 'NO'...")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # name variable does not have to be reset
    start(nice,mean,name)
    
                                   


if __name__ == "__main__":
    start()
