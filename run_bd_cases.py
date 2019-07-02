import os.path
from src.beamdyn_cases import BeamdynCase
from src.beamdyn_driver import BeamdynDriver

# Set a common home directory
homedir = os.path.expanduser("~")

# Keep a handle to the openfast directory
openfast_directory = homedir + '/openfast'

# Build the cases
beamdyn_cases = [
    BeamdynCase(openfast_directory, './bd_5MW_dynamic/'),               # DONE
    BeamdynCase(openfast_directory, './bd_5MW_dynamic_gravity_Az00/'),   # DONE
    BeamdynCase(openfast_directory, './bd_5MW_dynamic_gravity_Az90/'),   # DONE
    BeamdynCase(openfast_directory, './bd_curved_beam/'),               # DONE
    BeamdynCase(openfast_directory, './bd_isotropic_rollup/'),          # DONE
    BeamdynCase(openfast_directory, './bd_static_cantilever_beam/'),     # DONE
    BeamdynCase(openfast_directory, './bd_static_twisted_with_k1/')      # DONE
]

# Run each case
for i, case in enumerate(beamdyn_cases):
  print(i)
  print(case)
  # converts the yaml input files to openfast-style files
  case.initialize_input_files()

  # executes the driver using the files generated above
  case.run()

  # converts the ".out" and/or ".outb" files to yaml
  # ignore summary files for now
  case.driver_to_yaml()
  #case.convert_output()
