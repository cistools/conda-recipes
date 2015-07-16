from jasmin_cis.test.runner import run
import os

run()

test_data = os.environ.get("CIS_DATA_HOME", None)

if test_data:
    run('jasmin_cis.test.integration')