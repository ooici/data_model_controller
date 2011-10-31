#!/usr/bin/env python

"""
@file src/process_controller.py
@author David Stuebe <dstuebe@asascience.com>
@brief Base Class for process execution
"""

from src.model_view_generator import ModelViewGenerator

class DataProcessException(Exception):
    """
    Define an exception class for Data Process errors
    """

class DataModelController(object):
    """
    Base class for the data model controller
    Children can inherit or mixin to customize the methods
    """

    def __init__(self, finput=None, foutput=None, fdata=None, ffspec=None, flog=None):
        """
        Initialize the Data Process Controller
        """

        # Store input arguments
        self.finput     = finput
        self.foutput    = foutput
        self.fdata      = fdata
        self.ffspec     = ffspec
        self.flog       = flog

        # Initialize state objects
        self.input_model    = None
        self.output_model   = None
        self.function_spec  = None

        self.mvg            = None
        self.results        = None


    def initialize(self):
        """
        Initialize the data process object
        """
        print 'Initializing...'
        self._parse_data_function_spec()

        self.mvg = self._create_mvg()


    def run(self):
        """
        Run the data process on the supplement
        """
        print 'Running...'
        # Add the supplement to the data model
        self.mvg.add_packet(self.finput)

        # Generate the function input arguments as a view of the model
        kwargs = self.mvg.generate_input_view(self.input_model)

        datafunc = self._get_data_function()

        # Run the function
        self.results = datafunc(**kwargs)
        ## Add try catch to handle invalid data model for function input


    def finish(self):
        """
        Cleanup the data process and return the result
        """
        print 'Finishing...'

        # package the results into the output file
        self.mvg.package_result_view(self.results, self.output_model, self.foutput)
        ## Add try catch to handle invalid data model for function results

        # Complete the actions of the Model Viewer and close all the files
        self.mvg.close()


    def _parse_data_function_spec(self):
        """
        Read the Yaml object and import the data function
        """

    def _get_data_function(self):
        """
        Get the data function specified by the function spec
        """

        def func():
            """
            A dummy data function
            """
            return None

        return func



    def _create_mvg(self):
        """
        Create the Model View Generator for this function
        """

        return ModelViewGenerator(self.fdata)