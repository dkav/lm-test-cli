#!/usr/bin/env python2

"""Script to run Linkage Pathways Tool.

Assumes Linkage Mapper scripts and test data are in their default folders.

"""

import os
import sys

import lm_path
import lm_master


def create_dir(in_dir):
    """Create directory if doesn't exist."""
    if not os.path.exists(in_dir):
        os.makedirs(in_dir)


def in_params(test_dir, run_dir):
    """Define input paramaters."""
    gp_blank = '#'  # Geoprocessing's empty parameter value

    prj_dir = os.path.join(test_dir,  # Folder containing tests
                           'lm_output',  # Container folder to hold model run
                           run_dir)  # Linkage Mapper model run folder
    create_dir(prj_dir)

    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         prj_dir,  # Project Directory (1)
         os.path.join(test_dir,
                      'lm_inputs\\cores.shp'),  # Core Area Feature Class (2)
         "core_ID",  # Core Area Field Name (3)
         os.path.join(test_dir,
                      'lm_inputs\\resistances'),  # Resistance Raster (4)
         "true",  # Step 1 - Identify Adjacent Core Areas (5)
         "true",  # Step 2 - Construct a Network of Core Areas (6)
         "Cost-Weighted & Euclidean",  # Network Adjacency Method (7)
         gp_blank,  # Core Area Distances Text File (8)
         "true",  # Step 3 - Calculate CWD and LCP (9)
         "true",  # Drop Corridors that Intersect Core Areas (10)
         "true",  # Step 4 - Prune Network (11)
         4,  # Option A - Maxium Number of Connected NN (12)
         "Cost-Weighted",  # Option B - NN Measurement Unit (13)
         "true",  # Option C - Connect NC (14)
         "true",  # Step 5 - Calculate, Normalize and Mosaic Corridors (15)
         "true",  # Truncate Corridors (16)
         200000,  # CWD Threashold to Use in Truncating Corridors (17)
         10000,  # Bounding Circles Buffer Distance(18)
         100000,  # Maximum Cost-Weighted Corridor Distance (19)
         40000,  # Maximum Euclidean Corridor Distance (20)
         gp_blank,  # Output for ModelBuilder Precondition (21)
         gp_blank]  # Custom Settings File (22)
        )


def main():
    """Run model."""
    if len(sys.argv) > 1:
        run_dir = sys.argv[1]
    else:
        run_dir = 'lm_test'

    lm_master.lm_master(in_params(lm_path.TST_PATH, run_dir))


if __name__ == "__main__":
    main()
