#!/usr/bin/env python

"""
@file src/process_runner.py
@author David Stuebe <dstuebe@asascience.com>
@brief Base Class for process execution
"""

import sys
import optparse

from src.data_model_controller import DataModelController, DataProcessException

def get_opts():
    """
    Get command line options.
    Consider moving most command line options to an extensible config file
    """
    p = optparse.OptionParser()

    p.add_option("-i", "--input",           action="store", dest="finput",  help="Specify the path the the input file on disk containing the latest stream packet.")
    p.add_option("-o", "--output",          action="store", dest="foutput", help="Specify the path to the file that will contain the results.")
    p.add_option("-d", "--localdata",       action="store", dest="fdata",   help="Specify the path the file that contains the local context or process state if any.")
    p.add_option("-f", "--datafuncspec",    action="store", dest="ffspec",  help="The yaml file object which specifies the data function and the model inputs and outputs")
    p.add_option("-l", "--logfile",         action="store", dest="flog",    help="Path to the file where logs should be placed.")

    p.set_defaults(finput=None, foutput=None, fdata=None, ffspec=None, flog=None)
    opts, args = p.parse_args()

    print 'opts:',opts
    print 'args:',args

    ## Validate that all input file name arguments are valid


    return vars(opts) # Make the result a dictionary not a Values Instance



def main(ProcessControllerClass = DataModelController):
    """
    Execute the Data Process
    """

    #parse the command line options
    opts = get_opts()

    # Create the data process controller object
    dp = ProcessControllerClass(**opts)

    # Initialize the data process object
    dp.initialize()

    # Run the function on the new data
    dp.run()

    # Process the result
    dp.finish()

    sys.exit(0)

if __name__ == "__main__":
    main()
