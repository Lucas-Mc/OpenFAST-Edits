import os.path
from src.cases import BeamdynCase
from src.beamdyn_driver import BeamdynDriver

# Set a common home directory
homedir = os.path.expanduser("~")

# Keep a handle to the openfast directory
openfast_directory = homedir + '/openfast'

# Build the cases
beamdyn_cases = [
    BeamdynCase(openfast_directory, 'bd_5MW_dynamic'),
    BeamdynCase(openfast_directory, 'bd_5MW_dynamic_gravity_Az00'),
    BeamdynCase(openfast_directory, 'bd_5MW_dynamic_gravity_Az90'),
    BeamdynCase(openfast_directory, 'bd_curved_beam'),
    BeamdynCase(openfast_directory, 'bd_isotropic_rollup'),
    BeamdynCase(openfast_directory, 'bd_static_cantilever_beam'),
    BeamdynCase(openfast_directory, 'bd_static_twisted_with_k1')
]

# Run each case
for i,case_num in enumerate(beamdyn_cases):
  case_num.run()
  # if (i == 0):
  try:
    case_num.export_to_yaml()
  except:
    print('FAILED: ' + case_num.case_type)
