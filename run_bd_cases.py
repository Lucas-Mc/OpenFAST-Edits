import os.path
from src.cases import BeamdynCase
from src.beamdyn_driver import BeamdynDriver

# Set a common home directory
homedir = os.path.expanduser("~")

# Keep a handle to the openfast directory
openfast_directory = homedir + '/openfast'

# Specific case to test
case_type = 'bd_static_cantilever_beam'

# Build the case
# driver = BeamdynDriver(homedir + '/openfast/build/modules/beamdyn/beamdyn_driver')
# case_directory = '/Users/lmccullu/openfast/build/reg_tests/modules/beamdyn/bd_static_cantilever_beam'
# input_file = 'bd_driver.inp'
case = BeamdynCase(openfast_directory, case_type)
case.run()
