#!/usr/bin/env python2

"""Script to run Centrality Mapper tool.

Assumes Linkage Mapper scripts and test data are in their default folders.

"""

import os

import lm_path
import circuitscape_master


def in_params(test_dir):
    """Define input paramaters."""
    prj_dir = os.path.join(test_dir,  # Folder containing tests
                           'lm_output',  # Container folder to hold model run
                           'lm_test')  # Linkage Mapper model run folder

    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         prj_dir,  # Project Directory (1)
         os.path.join(test_dir,
                      'lm_inputs\\cores.shp'),  # Core Area Feature Class (2)
         "core_ID"]  # Core Area Field Name (3)
        )


def main():
    """Run model."""
    circuitscape_master.circuitscape_master(in_params(lm_path.TST_PATH))


if __name__ == "__main__":
    main()
