import os.path
from src.beamdyn_cases import BeamdynCase
from src.beamdyn_driver import BeamdynDriver

# Set a common home directory
homedir = os.path.expanduser("~")

# Keep a handle to the openfast directory
openfast_directory = homedir + '/openfast'

# Build the cases
beamdyn_cases = [
    # BeamdynCase(openfast_directory, 'bd_5MW_dynamic'),
    # BeamdynCase(openfast_directory, 'bd_5MW_dynamic_gravity_Az00'),
    # BeamdynCase(openfast_directory, 'bd_5MW_dynamic_gravity_Az90'),
    BeamdynCase(openfast_directory, './bd_curved_beam/'),
    # BeamdynCase(openfast_directory, 'bd_isotropic_rollup'),
    # BeamdynCase(openfast_directory, 'bd_static_cantilever_beam'),
    # BeamdynCase(openfast_directory, 'bd_static_twisted_with_k1')
]

# Run each case
for i, case in enumerate(beamdyn_cases):
  # converts the yaml input files to openfast-style files
  case.initialize_input_files()

  # executes the driver using the files generated above
  # case.run()

  # converts the ".out" and/or ".outb" files to yaml
  # ignore summary files for now
  # case.convert_output()
