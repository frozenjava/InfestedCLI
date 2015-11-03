#
# Player.py
# Josh Artuso
# This contains the player object
#

from random import randint


class Player:

    # life points attribute
    life_points = 50

    # player damage attribute
    damage_points = 3

    def check_player(self):
        """
        Check if the player is still alive
        :return alive: true or false if the player is alive
        """
        if self.life_points > 0:
            return True
        else:
            return False

    def inflict_damage(self, opponent_life):
        """
        Generate a number representing the amount of damage to inflict on the opponent
        :param opponent_life: The amount of life the opponent has left
        :return damage: The amount of damage inflicted
        """
        damage = randint(0, self.damage_points)

        # Check if the player is inflicting more damage than the opponent has left
        if damage > opponent_life:
            damage = opponent_life

        return damage

    def set_life_points(self, amount):
        """
        Set the players life points
        :param amount: The number to set life points to
        :return: None
        """
        self.life_points = amount

    def add_life_points(self, amount):
        """
        Add life points to the player
        :param amount: the amount of life points to add
        :return: None
        """
        self.life_points += amount

    def remove_life_points(self, amount):
        """
        Remove life points from the player
        :param amount: the amount of life points to remove
        :return: None
        """
        self.life_points -= amount

    def set_damage_points(self, amount):
        """
        Set the number of damage points
        :param amount: The number to set damage points too
        :return: None
        """
        self.damage_points = amount

    def add_damage_points(self, amount):
        """
        Add damage point to the player
        :param amount: The amount of damage points to add
        :return: None
        """
        self.damage_points += amount

    def remove_damage_points(self, amount):
        """
        Remove damage points from a player
        :param amount: The amount of points to remove
        :return: None
        """
        if self.damage_points - amount <= 0:
            self.damage_points = 1
        else:
            self.damage_points -= amount