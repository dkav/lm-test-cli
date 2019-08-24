#!/usr/bin/env python2

"""Script to run Linkage Priority tool.

Assumes Linkage Mapper scripts and test data are in their default folders.

"""

import os

import lm_path
import lm_proj

import lp_main


def in_params(prj_dir, test_dir):
    """Define input paramaters."""
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
         "#",  # Other Core Area Value Raster (5)
         0.33,  # Resistance Weight in CAV Calculation (6)
         0.33,  # Size Weight in CAV Calculation (7)
         0.34,  # Area/Perimeter Weight in CAV Calculation (8)
         0,  # Expert Core Area Value Weight in CAV Calculation (9)
         0,  # Current Flow Centrality Weight in CAV Calculation (10)
         0,  # Other Core Area Value Weight in CAV Calculation (11)
         "#",  # Core Pairs Table (12)
         "#",  # From Core Field (13)
         "#",  # To Core Field (14)
         "#",  # Expert Corridor Importance Value Field (15)
         os.path.join(test_dir,  # Current Climate Signature Raster (16)
                      'lm_inputs\\lp_demo_modoc.gdb'
                      '\\climate_signature_current'),
         "true",  # Modify the Advanced Climate Signature Parameters? (17)
         os.path.join(test_dir,  # Future Climate Signature Raster (18)
                      'lm_inputs\\lp_demo_modoc.gdb'
                      '\\climate_signature_future'),
         0.5,  # Relative Priority of Minimum Climate Analog Ratio (19)
         0,  # Relative Priority of Maximum Climate Analog Ratio (20)
         1.15,  # Lowest Allowable Maximum Climate Analog Ratio (21)
         1,  # Targeted Climate Analog Ratio (22)
         1,  # Relative Priority of Achieving the Targeted Ratio (23)
         0.5,  # Climate Analog Linkage Priority Weight (24)
         351,  # Preferred Climate Signature Value for a Core (25)
         0.5,  # Relative Priority of Min Climate Pref Attainment Ratio (26)
         0,  # Relative Priority of Max Climate Pref Attainment Ratio (27)
         0.5,  # Climate Preference Linkage Priority Weight (28)
         0.25,  # Closeness Weight in CSP Calculation (29)
         0.25,  # Permeability Weight in CSP Calculation (30)
         0.25,  # Core Area Value Weight in CSP Calculation (31)
         0,  # Expert Corridor Importance Value Weight in CSP Calculation (32)
         0.25,  # Climate Envelope Difference Weight in CSP Calculation (33)
         0.6,  # CSP Threashold Value (34)
         0.5,  # Truncated Corridors Weight in Blended Priority Calc (35)
         0.5,  # Linkage Priority Weight in Blended Priority Calculation (36)
         "#",  # Output for ModelBuilder Precondition (37)
         "#"]  # Custom Settings File (38)
        )


def main():
    """Run model."""
    lp_main.main(in_params(*lm_path.dir_paths(lm_proj.proj_name())))


if __name__ == "__main__":
    main()
