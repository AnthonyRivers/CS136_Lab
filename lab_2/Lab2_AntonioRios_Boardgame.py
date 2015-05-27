# Antonio Rios
# February 12, 2015
# CS136
# LAB 2: Boardgame dice simulation
#############################################



from __future__ import print_function
import random

# A static class used to roll the dice various times
class DiceRoller(object):

    @staticmethod
    def roll(times, die):
        total = 0
        for i in range(times):
            roll = random.randint(1, die)
            total += roll
        return total

# The dice rolling object used throughout the code
r = DiceRoller()


# This class allows for the creation of attacks that the adventurers use
class Attack(object):

    def __init__(self, name, number, damage_die, d_type, bonus=0):
        self._name = name
        self._damage_die = damage_die
        self._number = number
        self._d_type = d_type
        self._bonus = bonus

    def get_attack_type(self):
        return self._d_type

    def get_damage(self):
        return r.roll(self._number, self._damage_die) + self._bonus


# This class is the super class for the future subclasses and contains some basic functionality
# that every character has regardless of class
class Adventurer(object):

    def __init__(self, name, hit_points, armor, magic_resistance, initiative):
        self._name = name
        self._hit_points = hit_points
        self._armor = armor
        self._magic_resistance = magic_resistance
        self._initiative = initiative

    # Is used as a check to see if the adventurer is alive and the game can continue
    def is_alive(self):
        if self._hit_points > 0:
            return True
        else:
            return False

    # Determines the adventurer's initiative upon time of calling
    def get_initiative(self):
        return random.randint(0, self._initiative)

    # Is used as the method to deal damage to a character, regardless of class
    # and it also takes into account any mitigations
    def damage(self, amount, d_type):
        damage = 0
        if d_type == "physical":
            damage = amount - self._armor
            defense = str(self._armor) + " armor"
        elif d_type == "magic":
            damage = amount - self._magic_resistance
            defense = str(self._magic_resistance) + " magic resistance"

        if damage > 0:
            self._hit_points -= damage
            print(self._name + " suffers " + str(damage) + " damage after " + defense +
                  " and has " + str(self._hit_points) + " hit points left.")
        elif damage <= 0:
            print(self._name + " resists all damage!")


# Is a subclass of adventurer and one of the two 'playable' classes for the purpose of the game
class Fighter(Adventurer):

    # The declaration and initialization of attributes only the fighter possesses
    # and every fighter has
    __HD = 10
    __ARMOR = 10
    __MR = 4

    def __init__(self, name, hit_dice, initiative):
        super(Fighter, self).__init__(name, r.roll(hit_dice, Fighter.__HD),\
                                      Fighter.__ARMOR,\
                                      Fighter.__MR, initiative)
        self._attack = Attack("Slash", 1, 8, "physical", 2)

    # Determines how effective the fighter's attack is in one instance
    def attack(self):
        damage = self._attack.get_damage()
        d_type = self._attack.get_attack_type()

        print(self._name + " attacks with " + self._attack._name + " for " + str(damage) + " " + d_type)
        return (damage, d_type)

    # A string representation containing all info of the fighter
    def __str__(self):
        return self._name + " with " + str(self._hit_points) + " hit points and a " + self._attack._name + \
    " attack " + "(" + str(self._attack._number) + "d" + str(self._attack._damage_die) + ")"


# is a subclass of the adventurer and one of the two 'playable' classes for the game
class Wizard(Adventurer):

    # The declaration and initialization of attributes only the wizard possesses
    # and every wizard has
    __HD = 4
    __ARMOR = 4
    __MR = 10

    def __init__(self, name, hit_dice, initiative):
        super(Wizard, self).__init__(name, r.roll(hit_dice, Wizard.__HD),\
                                      Wizard.__ARMOR,\
                                      Wizard.__MR, initiative)
        self._attack = Attack("Fireball", 3, 6, "magic")

    # Determines how effective the wizard's cast (attack) is
    def cast(self):
        damage = self._attack.get_damage()
        d_type = self._attack.get_attack_type()
        print(self._name + " attacks with " + self._attack._name + " for " + str(damage) + " " + d_type)
        return (damage, d_type)

    # A string representation of the wizard containing all of his info
    def __str__(self):
        return self._name + " with " + str(self._hit_points) + " hit points and a " + self._attack._name + \
    " spell " + "(" + str(self._attack._number) + "d" + str(self._attack._damage_die) + ")"

# The code that actually runs the game depending on several dice rolls
if __name__ == "__main__":
    # Creation of adventurers
    a = Fighter("Aragorn", 5, 20)
    print("Created: ", a)
    b = Wizard("Gandalf", 5, 20)
    print("Created: ", b)
    print()

    rounds = 1


    # Make sure both adventurers are still alive
    while a.is_alive() and b.is_alive():

        fighter = a.get_initiative()
        wizard = b.get_initiative()

        if fighter > wizard:
            print("**  ROUND " + str(rounds))
            print(a._name + " wins initiative!" )
            damage, dtype = a.attack()
            b.damage(damage, dtype)
            rounds += 1
            print()
        elif wizard > fighter:
            print("**  ROUND " + str(rounds))
            print(b._name + " wins initiative!")
            damage, dtype = b.cast()
            a.damage(damage, dtype)
            rounds += 1
            print()
        else:
            continue

    # Prints winning statement depending on which class won and has a catch all exception for unexpected behavior
    if a.is_alive():
        print(a._name + " has won with " + str(a._hit_points) + " hit points left.")
    elif b.is_alive():
        print(b._name + " has won with " + str(b._hit_points) + " hit points left.")
    else:
        print("Encounter an unexpected ERROR!")
