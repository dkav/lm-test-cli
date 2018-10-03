"""Append sys.path with path to Linkage Mapper scripts."""

import os
import sys


LM_PATH = '..\\..\\lm-repo\\toolbox\\scripts'

TST_PATH = (os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))

sys.path.append(os.path.join(TST_PATH, LM_PATH))
