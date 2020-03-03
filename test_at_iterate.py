"""Script to run Restore for maximum return of investment utility.

Assumes Linkage Mapper scripts and test data are in their default folders.
"""

import os

import lm_proj
import lm_prj_dir

import iterate_barriers as iter_barr


def in_params(prj_dir, test_dir):
    """Define input paramaters."""
    return (
        [os.path.basename(__file__),  # Script Name ** Do not modify **
         False,  # restore_max_roi (1)
         1,  # restored_resistance_val (2)
         os.path.join(test_dir,
                      "lm-inputs\\iter_barr.gdb"),  # restoration_data_gdb (3)
         prj_dir,  # output_dir (4)
         "URWA_resis",  # resistance_ras (5)
         'URWA_HCAs_Doug_Grant',  # core_fc (6)
         'HCA_ID',  # core_fn (7)
         450,  # radius (8)
         2,  # iterations (9)
         0.75,  # min_ag_threshold  (10)
         0,  # min_improvement_val (11)
         'DougGrantParcelCost_m2_projected_90m',  # parcel_cost_ras (12)
         'restCostPer_m2',  # restoration_cost_ras (13)
         "ARESmaskp_projected",  # ag_ras (14)
         'Maximum',  # barrier_combine_method (15)
         None]  # cwd_thresh (16)
        )


def main():
    """Run model."""
    iter_barr.main(in_params(*lm_prj_dir.lm_dirs(lm_proj.proj_name())))


if __name__ == "__main__":
    main()
