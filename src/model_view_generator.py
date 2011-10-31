#!/usr/bin/env python

"""
@file src/model_view_generator.py
@author David Stuebe <dstuebe@asascience.com>
@brief Data Model processing class
"""



class ModelViewGenerator(object):
    """
    The class that provides input and output to the data function based on the data model specification
    """

    def __init__(self, fdata=None):
        """
        Initialize the MVG with the local file name for data and context & a data model object
        """
        # Open an HDF file that will/does contain the data


    def add_packet(self, fname):
        """
        Add the supplement in the fname to the local data context
        """

    def generate_input_view(self, input_model):
        """
        Given a yaml definition of a data model generate specified Numpy arrays from the local model
        """

        return {}

    def package_result_view(self, results, output_model, fname):
        """
        Package the result of the data function according to the data model for transport in an HDF file
        """

        return True


    def close(self):
        """
        Clean up any open HDF files and persist any needed state for next time.
        """
