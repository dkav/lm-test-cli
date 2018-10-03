#!/usr/bin/env python2

"""Script to run Climate Linkage Mapper tool.

Assumes Linkage Mapper scripts and test data are in their default folders.

"""

import os

import lm_path
import cc_main


def create_dir(in_dir):
    """Create directory if doesn't exist."""
    if not os.path.exists(in_dir):
        os.makedirs(in_dir)


def in_params(test_dir):
    """Define input paramaters."""
    prj_dir = os.path.join(test_dir,  # Folder containing tests
                           'lm_output',  # Container folder to hold model run
                           'cc_test')  # Climate Linkage Mapper model run folder
    create_dir(prj_dir)

    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         prj_dir,  # Project Folder (1)
         os.path.join(test_dir,
                      'lm_inputs\\cc_cores.shp'),  # Core Area Polygons (2)
         "HCA_ID",  # Core Area Field Name (3)
         os.path.join(test_dir,
                      'lm_inputs\\cc_climate.img'),  # Climate Raster (4)
         os.path.join(test_dir,
                      'lm_inputs\\cc_resist.img'),  # Resistance Raster (5)
         "C:\\Program Files\\GRASS GIS 7.4.1",  # GRASS GIS Folder (6)
         2000,  # Minium Distance Between Core Pairs (7)
         50000,  # Maxium Distance Between Core Pairs (8)
         1,  # Climate Threashold (9)
         50000,  # Climate Variable Cost (10)
         'true',  # Prune Network (11)
         4,  # Number of Connected Nearest Neighbors (12)
         "Cost-Weighted",  # Nearest Neighbor Measurement Unit (13)
         "true"]  # Connect Neighboring Constellations (14)
        )


def main():
    """Run model."""
    cc_main.main(in_params(lm_path.TST_PATH))


if __name__ == "__main__":
    main()
