import numpy as np

class Sun:
    """ Implements the Sun class.

        :param mass:
            The mass of the star in solar mass units.
        :param radius:
            The radius of the star in solar radius units.
        :param luminosity:
            The luminosity in solar luminosity units.
        :param name:
            The name of the star.

        Instance variables:
            - position: The (x, y) coordinates.
        
    """
    def __init__(self, mass=None, radius=None, luminosity=None, name=None):
        """ Initialize a sun object.
        """

        self.mass = mass
        self.radius = radius
        self.luminosity = luminosity
        self.name = name

        # Set the default sun position at the origin
        self.position = np.array([0, 0])

    def __str__(self):
        """ Print relevant sun properties.
        """

        text = ""
        if self.name is not None:
            text += "Star name: %s. \n" % self.name
        if self.mass is not None:
            text += "Mass: %.2f solar mass units.\n" % self.mass
        if self.radius is not None:
            text += "Radius: %.2f solar radius units.\n" % self.radius
        if self.luminosity is not None:
            text += "Luminosity: %.2f solar luminosity units.\n" % self.luminosity

        return text

    def mass_in_kg(self):
        """
        Transform mass from solar units to SI units.
        """
        return self.mass * 1.98847e30 # kg

    def radius_in_m(self):
        """
        Transform radius from solar units to SI units.
        """
        return self.radius * 6.957e8 # m

    def luminosity_in_watt(self):
        """
        Transform luminosity from solar units to SI units.
        """
        return self.luminosity * 3.83e26 # watts
