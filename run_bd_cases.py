

from src.cases import BeamdynCase
from src.beamdyn_driver import BeamdynDriver

# build the case
driver = BeamdynDriver("/Users/rmudafor/Development/openfast/build/modules/beamdyn/beamdyn_driver")
case_directory = '/Users/rmudafor/Development/openfast/build/reg_tests/modules/beamdyn/bd_static_cantilever_beam'
input_file = 'bd_driver.inp'
case = BeamdynCase(driver, case_directory, input_file)
case.run()
