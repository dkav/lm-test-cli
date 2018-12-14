"""Setup paths for Linkage Mapper test scripts."""


import os
import sys


LM_PATH = '..\\..\\lm-repo\\toolbox\\scripts'

TST_PATH = (os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))

sys.path.append(os.path.join(TST_PATH, LM_PATH))


def create_prj_dir(test_dir, run_dir):
    """Create project directory if doesn't exist."""
    prj_dir = os.path.join(test_dir,  # Folder containing tests
                           'lm_output',  # Container folder to hold model run
                           run_dir)  # Linkage Mapper model run folder

    if not os.path.exists(prj_dir):
        os.makedirs(prj_dir)

    return prj_dir


def dir_paths():
    """Provide folder inputs."""
    return create_prj_dir(TST_PATH, sys.argv[1]), TST_PATH
