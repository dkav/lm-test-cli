"""Create project folder for Linkage Mapper model runs."""

import os

import lm_path

import lm_master


def lm_run(params):
    """Run Linkage Mappper with provided paramaters."""
    lm_master.lm_master(params)


def create_prj_dir(run_dir):
    """Create project directory if doesn't exist."""
    prj_dir = lm_path.prj_dir_path(run_dir)
    if not os.path.exists(prj_dir):
        os.makedirs(prj_dir)

    return prj_dir


def lm_dirs(run_dir):
    """Get Linkage Mapper model run directories."""
    return create_prj_dir(run_dir), lm_path.TST_PATH
