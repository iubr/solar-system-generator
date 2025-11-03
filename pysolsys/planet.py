import numpy as np

# TODO: figure out which parameters are needed
# and which should be calculated.
class Planet:
    """ Implements the Planet class.

        Instance variables
            - mass: The planet's mass in Earth masses.
            - radius: The planet's radius in Earth radius.
            - planet_type: The type of planet (super-Jupyter, giant, super-Neptune, ice giant,
              sub-Neptune, mini-Neptune, mega-Earth, super-Earth, Sub-earth).
            - distance_to_sun: The distance to the sun in astronomical units.
            - starting_position: The starting position on the planet's orbit.
            - orbital_velocity: The planet's orbital velocity.
            - period: The period of rotation around the sun.
            - name: Planet name.
    """

    def __init__(self):
        """ Initializes a planet.
        """
        self.mass = None
        self.radius = None
        self.planet_type = None
        self.distance_to_sun = None
        self.starting_position = None
        self.orbital_velocity = None
        self.period = None
        self.name = None

    def __str__(self):
        """ Print relevant sun properties.
        """
        text = ""
        if self.name is not None:
            text += "Planet name: %s \n" % self.name
        if self.mass is not None:
            text += "Mass: %.2f Earth masses.\n" % self.mass
        if self.radius is not None:
            text += "Radius: %.2f Earth radius.\n" % self.radius

        return text

    def mass_in_kg(self):
        """
        Transform from Earth masses to SI units.
        """
        return self.mass * 5.9722e24 # kg

    def radius_in_m(self):
        """
        Transform from Earth radius to SI units.
        """
        return self.radius * 6.371e6 # m
