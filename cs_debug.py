# Code snippet for debugging Circuitscape.

# Replace following line:
# lu.call_circuitscape(cfg.CSPATH, outConfigFile)

import imp, pdb

cs_run = imp.load_source(
    "cs_run",
    "E:\\cs-workspace\\cs_testing\\test_scripts\\cs_run.py")
pdb.set_trace()
cs_run.main(out_config_file)
