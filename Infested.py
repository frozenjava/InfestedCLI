#
# Josh Artuso
# Infested
#
# This is a text based game about escaping a school infested with rats
#

from Player import Player
import GameActions
import LevelOne
import LevelTwo


def main():
    """
    The main function of the game
    :return: None
    """

    # The list of dialogue to print at the beginning of the game
    dialogue_list = ["You open your eyes...",
                     "Looking around the room you realize you have fallen asleep in class...",
                     "Upon further inspection you realize its 4p.m. everyone is gone and the school is closed.\n"]

    # Use the handle_dialogue function to print the list of dialogue with 5 seconds in between
    GameActions.handle_dialogue(dialogue_list, 5)

    # Create a new Player object called player
    player = Player()

    # Start playing the first level
    LevelOne.play_level_one(player)

    # Start playing the second level
    LevelTwo.play_level_two(player)


main()