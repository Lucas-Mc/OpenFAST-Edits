from src.aoc_files import AOCBladeADFile
from src.aoc_files import AOCTowerFile
from src.aoc_files import AOCBladeFile
from src.aoc_files import AOCFstFile
from src.aoc_files import AOCElastoDynFile
from src.aoc_files import AOCServoDyn
from src.aoc_files import AOCInflowWind
from src.aoc_files import AOCAD
#from src.all_files import AeroDataFile
#from src.all_files import AirfoilsFile
#from src.all_files import WindFile
import os

# this script converts the input files for a AOC driver case
# into yaml files for use with this Python wrapper

parent_directory = os.path.expanduser('~')
case_directory = os.path.join(parent_directory,'OpenFAST_Edits/AOC/initial_input_files')
aoc_input_files = [
  # AeroDataFile(case_directory, 'test_AD.yml')
  AOCFstFile(case_directory, 'AOC_WSt.fst'),
  AOCElastoDynFile(case_directory, 'AOC_WSt_ElastoDyn.dat'),
  AOCInflowWind(case_directory, 'AOC_WSt_InflowWind.dat'),
  AOCAD(case_directory, 'AOC_WSt_AD.ipt'),
  AOCServoDyn(case_directory, 'AOC_WSt_ServoDyn.dat'),
  # AOCBladeADFile(case_directory, 'AOC_AeroDyn_blade.dat'),
  AOCTowerFile(case_directory, 'AOC_Tower.dat'),
  AOCBladeFile(case_directory, 'AOC_Blade.dat'),
  # AeroDataFile(case_directory, 'test_AD.dat'),
  # AirfoilsFile(case_directory, 'AOC.fst'),
  # WindFile(case_directory, 'AOC.fst'),
]

for f in aoc_input_files:
  f.to_yaml(f.read_t2y())

