import numpy as np

# TODO: figure out which parameters are needed
# and which should be calculated.
class Planet:
    """ Implements the Planet class.

        Instance variables
            - mass: The planet's mass.
            - radius: The planet's radius.
            - planet_type: The type of planet based on its mass.
             (Super-Jupyter, giant, super-Neptune, ice giant, sub-Neptune, mini-Neptune, mega-Earth,
             super-Earth, Sub-earth).
            - distance_to_sun: The distance to the sun in astronomical units.
            - starting_position: The starting position on the planet's orbit.
            - orbital_velocity: The planet's orbital velocity.
            - period: The period of rotation around the sun.
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
