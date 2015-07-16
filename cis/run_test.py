from cis.test.runner import run
import os

# Run unit tests
run()

# If the test data directory is specified, run the integration tests as well. We disable parallel processing
# of these though as some have side affects, you also have to specify a time-out which would have to be very large
if os.environ.get("CIS_DATA_HOME", None):
    run('cis.test.integration', n_processors=0)