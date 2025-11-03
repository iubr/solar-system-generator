import numpy as np
import h5py

def read_from_checkpoint_file(filename):
	""" Read data from checkpoint file.

		:param filename:
			The name of the checkpoint file.

		:return:
			a dictionary with NumPy arrays.
	"""

	# TODO: check that the filename is a valid file

	# Open file for reading
	hf = h5py.File(filename, "r")

	keys = hf.keys()

	output_dict = {}

	# TODO: add check to make sure that
	# what is read from file can be represented as an array.
	for key in keys:
		array = np.array(hf.get(key))
		output_dict[key] = array

	# Close file
	hf.close()

	return output_dict

def write_to_checkpoint_file(filename, input_dict):
	""" Read data from checkpoint file.

		:param filename:
			The name of the checkpoint file.
		:param input_dict:
			The input dictionary
	"""

	# TODO: check that the filename is a valid file name
	# TODO: check if the file exists and print a warning (or append)
	# Open file for writing
	hf = h5py.File(filename, "w")

	for key in input_dict:
		hf.create_dataset(key, data=input_dict[key])

	# Close file
	hf.close()
