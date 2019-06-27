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
  # If case_num.run() isn't executed the resulting files will be placed in your current directory,
  # otherwise they will be placed in the same directory as the driver
  case_num.output_to_text()

  # case_num.output_to_yaml()

  # case_num.import_to_yaml()
  # case_num.export_to_yaml()

  # try:
  #   case_num.import_to_yaml()
  #   print('SUCCESSFUL IMPORT: ' + case_num.case_type)
  # except:
  #   print('FAILED IMPORT: ' + case_num.case_type)
  # try:
  #   case_num.export_to_yaml()
  #   print('SUCCESSFUL EXPORT: ' + case_num.case_type)
  # except:
  #   print('FAILED EXPORT: ' + case_num.case_type)
