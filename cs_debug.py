# Code snippet for debugging Circuitscape.

# Replace following line:
# lu.call_circuitscape(cfg.CSPATH, outConfigFile)

import imp, pdb

cs_run = imp.load_source(
    "cs_run",
    "F:\\cs-workspace\\cs_testing\\cs-test-cli\\cs_run.py")
pdb.set_trace()
cs_run.main(outConfigFile)
