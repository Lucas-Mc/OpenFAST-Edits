from src.aoc_files import AOCBladeADFile
from src.aoc_files import AOCTowerFile
from src.aoc_files import AOCBladeFile
from src.aoc_files import AOCFstFile
from src.aoc_files import AOCElastoDynFile
from src.aoc_files import AOCServoDyn
from src.aoc_files import AOCInflowWind
from src.aoc_files import AOCAD
from src.aoc_files import AOCAD15
#from src.all_files import AeroDataFile
#from src.all_files import AirfoilsFile
#from src.all_files import WindFile
import os

# This script converts the input files for a AOC driver case
# into yaml files for use with this Python wrapper

parent_directory = os.path.expanduser('~')
# Valid entries for current_case: ['WSt','YFix_WSt','YFree_WTurb']
current_case = 'YFree_WTurb'
case_directory = os.path.join(parent_directory,'OpenFAST_Edits','AOC','initial_input_files',current_case)

aoc_input_files = [
  AOCFstFile(case_directory, 'AOC_'+current_case+'.fst'),
  AOCElastoDynFile(case_directory, 'AOC_'+current_case+'_ElastoDyn.dat'),
  AOCInflowWind(case_directory, 'AOC_'+current_case+'_InflowWind.dat'),
  AOCServoDyn(case_directory, 'AOC_'+current_case+'_ServoDyn.dat'),
  # AOCBladeADFile(case_directory, '../AOC_AeroDyn_blade.dat'),
  # AOCTowerFile(case_directory, '../AOC_Tower.dat'),
  # AOCBladeFile(case_directory, '../AOC_Blade.dat'),
]

if (current_case == 'WSt'):
  aoc_input_files.append(AOCAD(case_directory, 'AOC_'+current_case+'_AD.ipt'))
else:
  aoc_input_files.append(AOCAD15(case_directory, 'AOC_'+current_case+'_AD15.ipt'))

for f in aoc_input_files:
  f.to_yaml(f.read_t2y())

