import numpy as np

class Sun:
	""" Implements the Sun class.

		:param mass:
			The mass of the sun in astronomical units.
		:param radius:
			The sun radius in astronomical units.

		Instance variables:
			- position: The (x, y) coordinates.
		
	"""
	def __init__(self, mass=None, radius=None):
		""" Initializes a sun object.
		"""

		self.mass = mass
		self.radius = radius

		# Set the default sun position at the origin
		self.position = np.array([0, 0])
