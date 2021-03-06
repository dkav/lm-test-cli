"""Script to run Centrality Mapper tool.

Assumes Linkage Mapper scripts and test data are in their default folders.

"""

import os

import lm_path
import lm_proj

import circuitscape_master


def in_params(prj_dir, test_dir):
    """Define input paramaters."""
    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         prj_dir,  # Project Directory (1)
         os.path.join(test_dir,
                      'lm-inputs\\cores.shp'),  # Core Area Feature Class (2)
         "core_ID"]  # Core Area Field Name (3)
        )


def main():
    """Run model."""
    circuitscape_master.circuitscape_master(
        in_params(*lm_path.dir_paths(lm_proj.proj_name())))


if __name__ == "__main__":
    main()
