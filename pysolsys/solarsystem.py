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

    # TODO: add a check that the sun is a Sun-type object, raise error if not.
    # TODO: check if the number_of_planets is integer, raise error if not.
    def __init__(self, sun, number_of_planets):
        """ Initializes a solar system.
        """

        self.sun = sun
        self.number_of_planets = number_of_planets
        self.planets = []

        for i in range(number_of_planets):
            new_planet = Planet()
            self.planets.append(new_planet)
