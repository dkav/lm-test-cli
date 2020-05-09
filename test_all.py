"""Script to run all Linkage Mapper tests."""

import sys

# Linkage Mapper
import test_lm_t1  # Scenario 1
import test_lm_t2  # Scenario 2 (for Linkage Pathways)

# Alternate Tools
import test_at_lp
import test_at_bm
import test_at_cc
import test_at_cm
import test_at_pp
import test_at_iterate

# Utilities
import test_util_clip
import test_util_coarse
import test_util_del
import test_util_log


def main():
    """Run all Linkage Mapper tests."""
    sys.argv[1] = "lmtest"
    test_lm_t1.main()

    test_at_cc.main()

    test_at_bm.main()
    test_at_cm.main()
    test_at_pp.main()
    test_at_iterate.main()

    test_util_clip.main()
    test_util_coarse.main()
    test_util_del.main()
    test_util_log.main()

    sys.argv[1] = "lptest"
    test_lm_t2.main()
    test_at_lp.main()


if __name__ == "__main__":
    main()
