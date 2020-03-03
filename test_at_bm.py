"""Script to run Barrier Mapper tool.

Assumes Linkage Mapper scripts and test data are in their default folders.

"""

import os

import lm_path
import lm_proj

import barrier_master


def in_params(prj_dir, test_dir):
    """Define input paramaters."""
    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         prj_dir,  # Project Directory (1)
         os.path.join(test_dir,
                      'lm-inputs\\resistances'),  # Resistance Raster (2)
         400,  # Minimum Detection Radius (3)
         1200,  # Maximum Detection Radius (4)
         400,  # Radius Step Value (5)
         "Calculate both maximum and sum",  # Method for combining (6)
         "true",  # Save barrier rasters for each search radius (7)
         "false"]  # Calculate percent improvment scores (8)
        )


def main():
    """Run model."""
    barrier_master.bar_master(
        in_params(*lm_path.dir_paths(lm_proj.proj_name())))


if __name__ == "__main__":
    main()
