"""Script to run Coarsen Raster Cell Sizes utility.

Assumes Linkage Mapper scripts and test data are in their default folders.
"""

import os

import lm_path
import lm_proj

import raster_aggregator as rast_agg


def in_params(prj_dir, test_dir):
    """Define input paramaters."""
    out_dir = os.path.join(prj_dir, "output")
    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         out_dir,  # Output Directory (1)
         3,  # Aggregation Factor (2)
         "Mean",  # Aggregation Method (3)
         "True",  # Smooth Input (4)
         os.path.join(test_dir,
                      'lm-inputs\\resistances'),  # Resistance Raster (5)
         "#", "#", "#", "#"]  # Resistance Rasters 2-5 (6-10)
        )


def main():
    """Run model."""
    rast_agg.raster_aggregator(
        in_params(*lm_path.dir_paths(lm_proj.proj_name())))


if __name__ == "__main__":
    main()
