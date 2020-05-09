"""Script to run Logfile Upgrade utility.

Assumes Linkage Mapper scripts and test data are in their default folders.
"""

import os
from shutil import copyfile
from datetime import datetime

import lm_proj
import lm_prj_dir

import logfile_upgrade as logfile_up


def in_params(prj_dir):
    """Define input paramaters."""
    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         prj_dir]  # Project Directory (1)
        )


def main():
    """Run model."""
    proj_dir, test_dir = lm_prj_dir.lm_dirs(lm_proj.proj_name())
    log_file = datetime.now().strftime("%Y_%m_%d_%H%M_Linkage Mapper.txt")
    tst_lfile = os.path.join(test_dir, 'lm-inputs', 'lm_v1_1_log.txt')
    log_dir = os.path.join(proj_dir, 'run_history', 'log')

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    copyfile(tst_lfile, os.path.join(log_dir, log_file))

    logfile_up.main(in_params(proj_dir))


if __name__ == "__main__":
    main()
