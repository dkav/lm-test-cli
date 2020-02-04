"""Script to run Delete CWD Rasters utility.

Assumes Linkage Mapper scripts and test data are in their default folders.
"""

import os

import lm_path
import lm_proj

import delete_cwds as del_cwd


def in_params(prj_dir):
    """Define input paramaters."""
    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         prj_dir]  # Project Directory (1)
        )


def main():
    """Run model."""
    del_cwd.delete_cwd_dir(
        in_params(lm_path.dir_paths(lm_proj.proj_name())[0]))



if __name__ == "__main__":
    main()
