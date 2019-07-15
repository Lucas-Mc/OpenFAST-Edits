from src.aoc_files import AOCBladeADFile,AOCTowerFile,AOCBladeFile
import os

# this script converts the input files for a AOC driver case
# into yaml files for use with this Python wrapper

parent_directory = os.path.expanduser('~')
case_directory = os.path.join(parent_directory,'OpenFAST_Edits/AOC/initial_input_files')
aoc_input_files = [
  #AOCBladeADFile(case_directory, 'AOC_AeroDyn_blade.dat'),
  AOCTowerFile(case_directory, 'AOC_Tower.dat'),
  #AOCBladeFile(case_directory, 'AOC_Blade.dat')
]

for f in aoc_input_files:
  print(f)
  f.to_yaml(f.read_t2y())

