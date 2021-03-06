"""Script to run Linkage Pathways Tool Version 1.

Assumes Linkage Mapper scripts and test data are in their default folders.

Use commit 58c4e3b rather than v1.1.0 because of intermediate cores bug.
"""

import os

import lm_proj
import lm_prj_dir

import lm_master


def in_params(prj_dir, test_dir):
    """Define input paramaters."""
    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         prj_dir,  # Project Directory (1)
         os.path.join(test_dir,
                      'lm-inputs\\cores.shp'),  # Core Area Feature Class (2)
         "core_ID",  # Core Area Field Name (3)
         os.path.join(test_dir,
                      'lm-inputs\\resistances'),  # Resistance Raster (4)
         "true",  # Step 1 - Identify Adjacent Core Areas (5)
         "true",  # Step 2 - Construct a Network of Core Areas (6)
         "Cost-Weighted & Euclidean",  # Network Adjacency Method (7)
         '#',  # Core Area Distances Text File (8)
         "true",  # Step 3 - Calculate CWD and LCP (9)
         "true",  # Drop Corridors that Intersect Core Areas (10)
         "true",  # Step 4 - Prune Network (11)
         1,  # Option A - Maxium Number of Connected NN (12)
         "Euclidean",  # Option B - NN Measurement Unit (13)
         "true",  # Option C - Connect NC (14)
         "true",  # Step 5 - Calculate, Normalize and Mosaic Corridors (15)
         10000,  # Bounding Circles Buffer Distance(16)
         100000,  # Maximum Cost-Weighted Corridor Distance (17)
         40000]  # Maximum Euclidean Corridor Distance (18)
        )


def main():
    """Run model."""
    lm_master.lm_master(in_params(*lm_prj_dir.lm_dirs(lm_proj.proj_name())))


if __name__ == "__main__":
    main()
