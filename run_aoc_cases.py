import os
from src.aoc_cases import AOCCase
from src.aoc_driver import AOCDriver

# Set a common home directory
homedir = os.path.expanduser("~")

# Keep a handle to the openfast directory
openfast_directory = homedir + '/openfast'

# Build the cases
aoc_cases = [
    AOCCase(openfast_directory, './AOC/')
]

# Run each case
for i, case in enumerate(aoc_cases):
  case.start()

  # converts the yaml input files to openfast-style files
  case.initialize_input_files()

  # executes the driver using the files generated above
  case.run()

  # converts the ".out" and/or ".outb" files to yaml
  # ignore summary files for now
  case.convert_output()

  case.end()