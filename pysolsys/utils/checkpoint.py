# PySolSys: a solar system generator
#
# GNU GPLv3
#
# Copyright (C) 2025 PySolSys developers.
#
# This file is part of PySolSys.

import numpy as np
import h5py


def read_from_checkpoint_file(filename):
    """Read data from checkpoint file.

    :param filename:
            The name of the checkpoint file.

    :return:
            a dictionary with NumPy arrays.
    """

    # TODO: Check that the filename is a valid file.
    hf = h5py.File(filename, "r")

    keys = hf.keys() # Get data labels
    output_dict = {}

    # FIXME: Add check to make sure that what is
    # read can be represented as an array.
    for key in keys:
        array = np.array(hf.get(key))
        output_dict[key] = array

    hf.close()

    return output_dict


def write_to_checkpoint_file(filename, input_dict):
    """Read data from checkpoint file.

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
