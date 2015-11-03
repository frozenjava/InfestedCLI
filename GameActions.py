#
# GameActions.py
# Josh Artuso
#
# This file contains all of the actions that can happen in the game
#

from Rat import Rat
from time import sleep
from random import randint


def handle_fight(player, rat_damage_points, rat_life_points):
    """
    Handle a fight between the player and the rat
    :param player: The player object for the player
    :param rat_damage_points: The damage points to give to the rat
    :param rat_life_points: The life points to give to the rat
    :return: None
    """

    # Create the rat object
    rat = Rat()

    # Set the life and damage points for the rat
    rat.set_damage_points(rat_damage_points)
    rat.set_life_points(rat_life_points)

    # Loop until the player or the rat is dead
    while player.check_player() and rat.check_rat():

        # Get the damage the player inflicts onto the rat
        players_damage = player.inflict_damage(rat.life_points)
        rat.remove_life_points(players_damage)
        if players_damage:
            print "You hit the rat and caused " + str(players_damage) + " damage to it!"
        else:
            print "You failed to hit any damage on the rat"
        sleep(.15)

        # Get the damage the rat inflicts onto the player
        rats_damage = rat.inflict_damage(player.life_points)
        player.remove_life_points(rats_damage)

        if rats_damage > 0:
            print "OUCH! The rat hits a " + str(rats_damage) + " on you!"
        else:
            print "Lucky you! The rat didn't hit any damage!"
        sleep(.15)

    if not rat.check_rat():             # The rat died
        print "\nYou defeated the rat! You have " + str(player.life_points) + " life points left."
    elif not player.check_player():     # The rat defeated the player
        print "\nThe rat defeated you!"
        handle_game_over(False)
    else:                               # Do this if neither of the above happened
        print "You shouldn't ever see this..."


def handle_closet(player, level, reward_list):
    """
    Handle a closet
    :param player: The player object for the player
    :param level: The level that the player is on
    :return reward: The reward given to the player
    """

    # Print the dialogue for the closet
    print "You found a closet. It appears to be unlocked."
    print "Should you open it?"

    # Get the players move
    player_move = handle_options(player, ["Open the Closet!", "No! Its a trap!"])

    reward = None

    if player_move == 1:

        # Decide what happens when the person opens the closet
        closet_outcome = randint(0, 5)

        if closet_outcome < level:  # There is a rat inside the closet
            print "OH NO! There is a giant man eating rat in there!"
            handle_fight(player, 3, 10)
        else:                       # You get a helpful reward from the closet
            reward = reward_list[randint(0, len(reward_list)-1)]
            print "Congratulations! You found a " + reward + "!"
            print "This item increases your damage points by", 2 * level
            player.add_damage_points(2*level)

    return reward


def handle_options(player, options_list):
    """
    Print a menu of options for the user to choose from
    :param player: The player object for the player
    :param options_list: The list of options
    :return selected_option: The option selected
    """

    # Add a player info option to the front of the options_list
    options_list = ["Player Info"] + options_list

    # The selected option
    selected_option = None

    # Loop until the user selects a valid option
    while selected_option not in options_list:

        print "\n---- OPTIONS ----"
        # Print each option in the list
        for option in options_list:
            print str(options_list.index(option)) + " - " + option

        # Get the users choice
        users_number = input("\nSelect an option> ")

        # Check if the user entered a valid option
        if users_number <= len(options_list) and users_number > 0:
            selected_option = options_list[users_number]
        elif users_number == 0:
            print "\n---- PLAYER INFO ----"
            print "Life Points: ", player.life_points
            print "Damage Points: ", player.damage_points

            print "\nLife points represent the amount of life you have left"
            print "Damage points represent the max amount of damage you can hit on an opponent"

            print "\nNow select an option from the menu"

        else:
            print "That's not an option. Choose again"

    return options_list.index(selected_option)


def handle_dialogue(dialogues, sleep_time=4):
    """
    Handle what happens to dialogue
    :param dialogues: A list of the dialogue to print
    :return: None
    """
    for dialogue in dialogues:
        print dialogue
        sleep(sleep_time)


def handle_game_over(winner):
    """
    Handle what happens when the game is over
    :param winner: Did the player win
    :return: None
    """
    if winner == True:
        print "Congratulations! You won!"
    else:
        print "You lose."
        print "GAME OVER!"

    exit()