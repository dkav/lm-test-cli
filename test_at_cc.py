"""Script to run Climate Linkage Mapper tool.

Assumes Linkage Mapper scripts and test data are in their default folders.

"""

import os

import lm_path
import lm_proj

import cc_main


def in_params(prj_dir, test_dir):
    """Define input paramaters."""
    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         prj_dir,  # Project Folder (1)
         os.path.join(test_dir,
                      'lm-inputs\\cc_cores.shp'),  # Core Area Polygons (2)
         "core_id",  # Core Area Field Name (3)
         os.path.join(test_dir,
                      'lm-inputs\\cc_climate.img'),  # Climate Raster (4)
         os.path.join(test_dir,
                      'lm-inputs\\cc_resist.img'),  # Resistance Raster (5)
         "C:\\Program Files\\GRASS GIS 7.8",  # GRASS GIS Folder (6)
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
    cc_main.main(in_params(*lm_path.dir_paths(lm_proj.proj_name())))


if __name__ == "__main__":
    main()
