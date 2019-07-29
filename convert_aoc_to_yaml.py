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
current_case = 'YFix_WSt'
case_directory = os.path.join(parent_directory,'OpenFAST_Edits','AOC','initial_input_files',current_case)

if (current_case == 'WSt'):
  aoc_input_files = [
    AOCFstFile(case_directory, 'AOC_WSt.fst'),
    AOCElastoDynFile(case_directory, 'AOC_WSt_ElastoDyn.dat'),
    AOCInflowWind(case_directory, 'AOC_WSt_InflowWind.dat'),
    AOCAD(case_directory, 'AOC_WSt_AD.ipt'),
    AOCServoDyn(case_directory, 'AOC_WSt_ServoDyn.dat'),
    # AOCBladeADFile(case_directory, '../AOC_AeroDyn_blade.dat'),
    # AOCTowerFile(case_directory, '../AOC_Tower.dat'),
    # AOCBladeFile(case_directory, '../AOC_Blade.dat'),
  ]
elif (current_case == 'YFix_WSt'):
  aoc_input_files = [
    # AOCFstFile(case_directory, 'AOC_YFix_WSt.fst'),
    # AOCAD15(case_directory, 'AOC_YFix_WSt_AD15.ipt'),
    # AOCElastoDynFile(case_directory, 'AOC_YFix_WSt_ElastoDyn.dat'),
    # AOCInflowWind(case_directory, 'AOC_YFix_WSt_InflowWind.dat'),
    # AOCServoDyn(case_directory, 'AOC_YFix_WSt_ServoDyn.dat'),
    AOCBladeADFile(case_directory, '../AOC_AeroDyn_blade.dat'),
    AOCTowerFile(case_directory, '../AOC_Tower.dat'),
    AOCBladeFile(case_directory, '../AOC_Blade.dat'),
  ]
elif (current_case == 'YFree_WTurb'):
  aoc_input_files = [
    AOCFstFile(case_directory, 'AOC_YFree_WTurb.fst'),
    AOCAD15(case_directory, 'AOC_YFree_WTurb_AD15.ipt'),
    AOCElastoDynFile(case_directory, 'AOC_YFree_WTurb_ElastoDyn.dat'),
    AOCInflowWind(case_directory, 'AOC_YFree_WTurb_InflowWind.dat'),
    AOCServoDyn(case_directory, 'AOC_YFree_WTurb_ServoDyn.dat'),
    # AOCBladeADFile(case_directory, '../AOC_AeroDyn_blade.dat'),
    # AOCTowerFile(case_directory, '../AOC_Tower.dat'),
    # AOCBladeFile(case_directory, '../AOC_Blade.dat'),
  ]

for f in aoc_input_files:
  f.to_yaml(f.read_t2y())

