"""Setup paths for Linkage Mapper test scripts."""


import os
import sys


#LM_PATH = '..\\..\\lm-repo\\toolbox\\scripts'
LM_PATH = '..\\..\\lm-fork\\toolbox\\scripts'


TST_PATH = (os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))

sys.path.append(os.path.join(TST_PATH, LM_PATH))


def prj_dir_path(run_dir):
    """Get project directory path."""
    return os.path.join(TST_PATH,  # Folder containing tests
                        'lm_output',  # Container folder to hold model run
                        run_dir)  # Linkage Mapper model run folder


def dir_paths(run_dir):
    """Provide folder inputs."""
    return prj_dir_path(run_dir), TST_PATH
