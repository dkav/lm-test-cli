"""Script to run Clip Corridors to Cutoff Width utility.

Assumes Linkage Mapper scripts and test data are in their default folders.
"""

import os

import lm_path
import lm_proj

import clip_corridors as clip_corr


def in_params(prj_dir, prj_name):
    """Define input paramaters."""
    corr_gdb = os.path.join(prj_dir, "output", "corridors.gdb")
    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         os.path.join(
             corr_gdb,
             '_'.join([prj_name, "corridors"])),  # Corridor Raster (1)
         500,  # Cutoff Value (2)
         corr_gdb]  # Output GDB (3)
        )


def main():
    """Run model."""
    proj_name = lm_proj.proj_name()
    clip_corr.clip_corridor(
        in_params(*lm_path.dir_paths(proj_name)[0]), proj_name)


if __name__ == "__main__":
    main()
