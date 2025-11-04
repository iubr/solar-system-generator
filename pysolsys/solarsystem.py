from .sun import Sun
from .planet import Planet

import numpy as np

class SolarSystem:
    """ Implements a SolarSystem class which consists of one sun and
        a collection of planets.

        :param sun:
            the sun.
        :param number_of_plantes:
            the number of planets in the solar system.

        Instance variables
            - sun: The sun.
            - number_of_planets: The number of planets.
            - planets: The list of planets.

    """

    def __init__(self, sun, number_of_planets):
        """ Initializes a solar system.
        """

        # check if variable sun is a Sun-type object.
        if isinstance(sun, Sun):
            self.sun = sun
        else:
            raise TypeError("SolarSystem: no sun provided.")

        # check if the number of planets is an integer
        if isinstance(number_of_planets, int):
            self.number_of_planets = number_of_planets
            self.planets = []

            # create new planets and add them to the list
            for i in range(number_of_planets):
                new_planet = Planet()
                self.planets.append(new_planet)
        else:
            raise TypeError("SolarSystem: the number of planets is not an integer.")

    def __str__(self):
        """ Print information about the solar system.
        """
        text = "The solar system consists of one star and %d planets.\n\n" % self.number_of_planets
        text += self.sun.__str__() + "\n"
        for planet in self.planets:
            if planet.name is not None:
                text += planet.name
            if planet.planet_type is not None:
                text += " (%s)\n" % planet.planet_type
        return text
