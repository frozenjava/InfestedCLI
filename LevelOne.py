#
# LevelOne
# Josh Artuso
#
# All of the code for the first level goes here
#

import GameActions


def move_five(player):
    """
    This is all of the stuff that happens in move five
    :param player: The player object
    :return: None
    """

    dialogue_list = ["\nAfter fighting off all of the rats you notice a bottle of something on the ground...",
                     "Should you drink it?"]

    GameActions.handle_dialogue(dialogue_list)

    player_move = GameActions.handle_options(player, ["Yes, drink it!", "No! Are you crazy?!"])

    if player_move == 1:    # Drink the bottle
        dialogue_list = ["Whatever was in that bottle makes you feel much better!",
                         "You have gained 20 life points!"]
        GameActions.handle_dialogue(dialogue_list, 5)
        player.add_life_points(20)
    else:   # Don't drink the bottle
        GameActions.handle_dialogue(["You drop the bottle back onto the ground."], 5)

    #
    # BOSS FIGHT
    #

    dialogue_list = ["\nYou think you hear something behind you...",
                     "You turn around and see the biggest rat you have ever seen!",
                     "Get ready for the hardest fight yet!"]

    GameActions.handle_dialogue(dialogue_list, 5)
    GameActions.handle_fight(player, 5, 45)

    # Give the player some damage points as a reward for killing the boss
    player.add_damage_points(3)

    dialogue_list = ["\n\nAfter the fight you feel a little bit stronger...",
                     "Congratulations! You've earned 3 more damage points!",
                     "You spot an open door on the other side of the court yard and run to it..."]

    GameActions.handle_dialogue(dialogue_list, 2)


def move_four(player, possible_closet_rewards):
    """
    This is all of the stuff that happens in move 4
    :param player: The player object
    :param possible_closet_rewards: The possible rewards granted in a closet
    :return: None
    """
    # Print the next dialogue

    dialogue_list = ["\nYou reach the end of the hallway..",
                     "On your right you see a closet and on your left a door leading to the court yard.",
                     "What should you do?"]

    GameActions.handle_dialogue(dialogue_list, 4)

    player_move = GameActions.handle_options(player, ["Closet", "Court Yard"])

    if player_move == 1:    # Closet
        # There is a closet here
        given_reward = GameActions.handle_closet(player, 1, possible_closet_rewards)
        # If the user got a reward from the closet remove it from the list of possible rewards
        if given_reward is not None:
            possible_closet_rewards.remove(given_reward)

        GameActions.handle_dialogue(["Having nowhere else to go you walk towards the court yard"], 3)
    else:   # Court yard
        pass

    dialogue_list = ["As soon as you open the door to the court yard you are attacked by 4 rats!",
                     "Get ready to fight!"]

    GameActions.handle_dialogue(dialogue_list, 4)

    for i in range(0, 4):
        GameActions.handle_dialogue(["\nYou start fighting rat" + str(i+1)], 2)
        GameActions.handle_fight(player, 2, 7)


def move_three(player):
    """
    This is all of the stuff that happens in move three
    :param player: The player object
    :return: None
    """
    # Print the next set of dialogue
    dialogue_list = ["\nAt the end of this hallway you notice a missing ceiling tile...",
                     "You have 2 options. Go left, or climb into the ceiling to try and avoid rats."]

    GameActions.handle_dialogue(dialogue_list, 4)

    player_move = GameActions.handle_options(player, ["Turn Left", "Into The Ceiling!"])

    if player_move == 1:    # Turn left
        GameActions.handle_dialogue(["A giant rat runs out of no where! Prepare to fight!"], 2)
        GameActions.handle_fight(player, 2, 7)

    else:   # Try and get the in the ceiling
        dialogue_list = ["You try to climb into the ceiling...",
                         "As you feel the ceiling tiles beneath you crack, you realize this was a horrible idea!",
                         "OUCH! You fall from the ceiling losing 5 life points in the process.",
                         "After giving up on your dreams of being Indiana Jones, you continue in the direction you should have."]

        GameActions.handle_dialogue(dialogue_list, 5)

        player.remove_life_points(5)


def move_two(player):
    """
    This is all of the stuff that happens in move two
    :param player: The player object
    :return: None
    """
    # Print the next set of dialogue
    GameActions.handle_dialogue(["\nYou find yourself at a fork"], 1)

    player_move = GameActions.handle_options(player, ["Continue Straight", "Turn Right"])

    if player_move == 1:    # Continue Straight
        GameActions.handle_dialogue(["You continue straight down the hallway..."], 4)
    else:   # Turn right
        GameActions.handle_dialogue(["OH NO! There are 3 giant rats here!"], 3)
        for i in range(0, 3):
            GameActions.handle_dialogue(["\nYou start fighting rat" + str(i+1)], 2)
            GameActions.handle_fight(player, 2, 7)

        dialogue_list = ["You reach the end of the hall and see that it is a dead end...",
                         "You sadly turn around, walk back, and take a right back into the main hallway."]

        GameActions.handle_dialogue(dialogue_list, 4)


def move_one(player, possible_closet_rewards):
    """
    This is all of the stuff that happens in the first move
    :param player: The player object
    :param possible_closet_rewards: The possible rewards granted in a closet
    :return: None
    """
    # Print some dialogue
    GameActions.handle_dialogue(["You get up and walk out side into the hallway."], 1)

    # Ask the player what they want to do
    player_move = GameActions.handle_options(player, ["Walk Left", "Walk Right"])

    if player_move == 1:    # Walk Left
        # There is a closet here
        given_reward = GameActions.handle_closet(player, 1, possible_closet_rewards)
        # If the user got a reward from the closet remove it from the list of possible rewards
        if given_reward is not None:
            possible_closet_rewards.remove(given_reward)

        GameActions.handle_dialogue(["\nYou walk back to the right past your class room"], 1)

    else:   # Walk Right
        GameActions.handle_dialogue(["You walk to the right..."], 1)


def play_level_one(player):
    """
    Play the first level of the game
    :param player: The player object
    :return: None
    """

    # These are the rewards that you can possibly find in a closet for this level
    possible_closet_rewards = ["Steel Toed Boots", "Broom Handle", "Sludge Hammer"]

    # Play the first move of the level
    move_one(player, possible_closet_rewards)

    # Play the second move of the level
    move_two(player)

    # Play the third move of the level
    move_three(player)

    # Play the fourth move of the level
    move_four(player, possible_closet_rewards)

    # Play the fifth move of the level
    move_five(player)