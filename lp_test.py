#!/usr/bin/env python2

"""Script to run Linkage Priority tool.

Assumes Linkage Mapper scripts and test data are in their default folders.

"""

import os

import lm_path
import lp_main


def in_params(test_dir):
    """Define input paramaters."""
    gp_blank = "#"  # Geoprocessing's empty parameter value

    prj_dir = os.path.join(test_dir,  # Folder containing tests
                           'lm_output',  # Container folder to hold model run
                           'lp_test')  # Linkage Mapper model run folder

    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         prj_dir,  # Project Directory (1)
         os.path.join(test_dir,
                      'lm_inputs\\lp_demo_modoc.gdb'
                      '\\cores'),  # Core Area Feature Class (2)
         "core_ID",  # Core Area Field Name (3)
         os.path.join(test_dir,
                      'lm_inputs\\lp_demo_modoc.gdb'
                      '\\resistance_modoc'),  # Resistance Raster (4)
         gp_blank,  # Other Core Area Value Raster (5)
         0.33,  # Resistance Weight in CAV Calculation (6)
         0.33,  # Size Weight in CAV Calculation (7)
         0.34,  # Area/Perimeter Weight in CAV Calculation (8)
         0,  # Expert Core Area Value Weight in CAV Calculation (9)
         0,  # Current Flow Centrality Weight in CAV Calculation (10)
         0,  # Other Core Area Value Weight in CAV Calculation (11)
         gp_blank,  # Core Pairs Table (12)
         gp_blank,  # From Core Field (13)
         gp_blank,  # To Core Field (14)
         gp_blank,  # Expert Corridor Importance Value Field (15)
         gp_blank,  # Current Climate Envelope Raster (16)
         gp_blank,  # Future Climate Envelope Raster (17)
         'false',  # Higher Climate Envelope Values are Cooler (18)
         0.33,  # Closeness Weight in CSP Calculation (19)
         0.33,  # Permeability Weight in CSP Calculation (20)
         0.34,  # Core Area Value Weight in CSP Calculation (21)
         0,  # Expert Corridor Importance Value Weight in CSP Calculation (22)
         0,  # Climate Envelope Difference Weight in CSP Calculation (23)
         0.02,  # Proportion of Top CSP Values to Keep (24)
         0.5,  # Truncated Corridors Weight in Blended Priority Calc (25)
         0.5,  # Linkage Priority Weight in Blended Priority Calculation (26)
         gp_blank,  # Output for ModelBuilder Precondition (27)
         gp_blank]  # Custom Settings File (28)
        )


def main():
    """Run model."""
    lp_main.main(in_params(lm_path.TST_PATH))


if __name__ == "__main__":
    main()
