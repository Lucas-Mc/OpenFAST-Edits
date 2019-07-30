from src.base_case import BaseCase
from src.aoc_driver import AOCDriver
from src.aoc_files import AOCTowerFile
from src.aoc_files import AOCBladeFile
from src.aoc_files import AOCBladeADFile
from src.aoc_files import AOCFstFile
from src.aoc_files import AOCElastoDynFile
from src.aoc_files import AOCServoDyn
from src.aoc_files import AOCInflowWind
from src.aoc_files import AOCAD
from src.aoc_files import AOCAD15
from src.all_files import AeroDataFile
from src.output_files import OutputPrimaryFile
import os

# Fix the repetitive code in here

class AOC_WSt_Case(BaseCase):
  
  def __init__(self, openfast_directory, case_directory):
    """
    Args:
      openfast_directory::[string] 
        - The location of the OpenFAST case folder
      case_directory::[string] 
        - The location of this case
    """
    self.openfast_directory = openfast_directory
    driver = AOCDriver(os.path.join(openfast_directory,'build','glue-codes','openfast','openfast'))
    input_files = [
      AOCFstFile(case_directory, 'AOC_WSt.yml'),
      AOCElastoDynFile(case_directory, 'AOC_WSt_ElastoDyn.yml'),
      AOCInflowWind(case_directory, 'AOC_WSt_InflowWind.yml'),
      AOCAD(case_directory, 'AOC_WSt_AD.yml'),
      AOCServoDyn(case_directory, 'AOC_WSt_ServoDyn.yml'),
      AOCTowerFile(case_directory, 'AOC_Tower.yml'),
      AOCBladeFile(case_directory, 'AOC_Blade.yml')
    ]
    self.expected_output_files = [
      'AOC_WSt.out'
    ]
    super().__init__(driver, case_directory, input_files)

  def initialize_input_files(self):
    """
    Convert all yaml files to openfast files
    """
    for f in self.input_files:
      f.to_text(f.read_y2t())
  
  def convert_output(self):
    for f in self.expected_output_files:
      outfile = OutputPrimaryFile(".", f)
      outfile.to_yaml(outfile.read_t2y())

  def inp_to_yaml(self):
    for input_file in self.input_files:
      file_path = os.path.join(self.case_directory,input_file)
      if (input_file == 'AOC_AeroDyn_blade.dat'):
        temp_file = AOCBladeADFile('',file_path)
      elif (input_file == 'AOC_Tower.dat'):
        temp_file = AOCTowerFile('',file_path)
      elif (input_file == 'AOC_Blade.dat'):
        temp_file = AOCBladeFile('',file_path)
      new_dict = temp_file.read_t2y()
      temp_file.to_yaml(new_dict)

  def fst_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC.fst')
    temp_file = AOCFstFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)  

  def fst_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC.yml')
    temp_file = AOCFstFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def elastodyn_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC_WSt_ElastoDyn.dat')
    temp_file = AOCElastoDynFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)  

  def elastodyn_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_WSt_ElastoDyn.yml')
    temp_file = AOCElastoDynFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def bladead_to_yaml(self):
    # print(self.openfast_directory.replace('openfast','OpenFAST_Edits'))
    # file_path = self.openfast_directory.replace('openfast','OpenFAST_Edits') + self.case_directory[1:] 
    file_path = os.path.join(self.case_directory,'AOC_AeroDyn_blade.dat')
    temp_file = AOCBladeADFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)

  def bladead_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_AeroDyn_blade_inp.yml')
    temp_file = AOCBladeADFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def tower_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC_Tower.dat')
    temp_file = AOCTowerFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)  

  def tower_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_Tower_inp.yml')
    temp_file = AOCTowerFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def blade_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC_Blade.dat')
    temp_file = AOCBladeFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)   

  def blade_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_Blade_inp.yml')
    temp_file = AOCBladeFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)


class AOC_YFix_WSt_Case(BaseCase):
  
  def __init__(self, openfast_directory, case_directory):
    """
    Args:
      openfast_directory::[string] 
        - The location of the OpenFAST case folder
      case_directory::[string] 
        - The location of this case
    """
    self.openfast_directory = openfast_directory
    driver = AOCDriver(os.path.join(openfast_directory,'build','glue-codes','openfast','openfast'))
    input_files = [
      AOCFstFile(case_directory, 'AOC_YFix_WSt.yml'),
      AOCElastoDynFile(case_directory, 'AOC_YFix_WSt_ElastoDyn.yml'),
      AOCInflowWind(case_directory, 'AOC_YFix_WSt_InflowWind.yml'),
      AOCAD15(case_directory, 'AOC_YFix_WSt_AD15.yml'),
      AOCServoDyn(case_directory, 'AOC_YFix_WSt_ServoDyn.yml'),
      AOCBladeADFile(case_directory, 'AOC_AeroDyn_blade.yml'),
      AOCTowerFile(case_directory, 'AOC_Tower.yml'),
      AOCBladeFile(case_directory, 'AOC_Blade.yml')
    ]
    self.expected_output_files = [
      'AOC_YFix_WSt.out'
    ]
    super().__init__(driver, case_directory, input_files)

  def initialize_input_files(self):
    """
    Convert all yaml files to openfast files
    """
    for f in self.input_files:
      print(f)
      f.to_text(f.read_y2t())
  
  def convert_output(self):
    for f in self.expected_output_files:
      outfile = OutputPrimaryFile(".", f)
      outfile.to_yaml(outfile.read_t2y())

  def inp_to_yaml(self):
    for input_file in self.input_files:
      file_path = os.path.join(self.case_directory,input_file)
      if (input_file == 'AOC_AeroDyn_blade.dat'):
        temp_file = AOCBladeADFile('',file_path)
      elif (input_file == 'AOC_Tower.dat'):
        temp_file = AOCTowerFile('',file_path)
      elif (input_file == 'AOC_Blade.dat'):
        temp_file = AOCBladeFile('',file_path)
      new_dict = temp_file.read_t2y()
      temp_file.to_yaml(new_dict)

  def fst_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC.fst')
    temp_file = AOCFstFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)  

  def fst_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC.yml')
    temp_file = AOCFstFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def elastodyn_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC_WSt_ElastoDyn.dat')
    temp_file = AOCElastoDynFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)  

  def elastodyn_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_WSt_ElastoDyn.yml')
    temp_file = AOCElastoDynFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def bladead_to_yaml(self):
    # print(self.openfast_directory.replace('openfast','OpenFAST_Edits'))
    # file_path = self.openfast_directory.replace('openfast','OpenFAST_Edits') + self.case_directory[1:] 
    file_path = os.path.join(self.case_directory,'AOC_AeroDyn_blade.dat')
    temp_file = AOCBladeADFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)

  def bladead_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_AeroDyn_blade_inp.yml')
    temp_file = AOCBladeADFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def tower_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC_Tower.dat')
    temp_file = AOCTowerFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)  

  def tower_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_Tower_inp.yml')
    temp_file = AOCTowerFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def blade_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC_Blade.dat')
    temp_file = AOCBladeFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)   

  def blade_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_Blade_inp.yml')
    temp_file = AOCBladeFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)


class AOC_YFree_WTurb_Case(BaseCase):
  
  def __init__(self, openfast_directory, case_directory):
    """
    Args:
      openfast_directory::[string] 
        - The location of the OpenFAST case folder
      case_directory::[string] 
        - The location of this case
    """
    self.openfast_directory = openfast_directory
    driver = AOCDriver(os.path.join(openfast_directory,'build','glue-codes','openfast','openfast'))
    input_files = [
      AOCFstFile(case_directory, 'AOC_YFree_WTurb.yml'),
      AOCElastoDynFile(case_directory, 'AOC_YFree_WTurb_ElastoDyn.yml'),
      AOCInflowWind(case_directory, 'AOC_YFree_WTurb_InflowWind.yml'),
      AOCAD15(case_directory, 'AOC_YFree_WTurb_AD15.yml'),
      AOCServoDyn(case_directory, 'AOC_YFree_WTurb_ServoDyn.yml'),
      AOCBladeADFile(case_directory, 'AOC_AeroDyn_blade.yml'),
      AOCTowerFile(case_directory, 'AOC_Tower.yml'),
      AOCBladeFile(case_directory, 'AOC_Blade.yml')
    ]
    self.expected_output_files = [
      'AOC_YFree_WTurb.out'
    ]
    super().__init__(driver, case_directory, input_files)

  def initialize_input_files(self):
    """
    Convert all yaml files to openfast files
    """
    for f in self.input_files:
      f.to_text(f.read_y2t())
  
  def convert_output(self):
    for f in self.expected_output_files:
      outfile = OutputPrimaryFile(".", f)
      outfile.to_yaml(outfile.read_t2y())

  def inp_to_yaml(self):
    for input_file in self.input_files:
      file_path = os.path.join(self.case_directory,input_file)
      if (input_file == 'AOC_AeroDyn_blade.dat'):
        temp_file = AOCBladeADFile('',file_path)
      elif (input_file == 'AOC_Tower.dat'):
        temp_file = AOCTowerFile('',file_path)
      elif (input_file == 'AOC_Blade.dat'):
        temp_file = AOCBladeFile('',file_path)
      new_dict = temp_file.read_t2y()
      temp_file.to_yaml(new_dict)

  def fst_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC.fst')
    temp_file = AOCFstFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)  

  def fst_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC.yml')
    temp_file = AOCFstFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def elastodyn_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC_WSt_ElastoDyn.dat')
    temp_file = AOCElastoDynFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)  

  def elastodyn_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_WSt_ElastoDyn.yml')
    temp_file = AOCElastoDynFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def bladead_to_yaml(self):
    # print(self.openfast_directory.replace('openfast','OpenFAST_Edits'))
    # file_path = self.openfast_directory.replace('openfast','OpenFAST_Edits') + self.case_directory[1:] 
    file_path = os.path.join(self.case_directory,'AOC_AeroDyn_blade.dat')
    temp_file = AOCBladeADFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)

  def bladead_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_AeroDyn_blade_inp.yml')
    temp_file = AOCBladeADFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def tower_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC_Tower.dat')
    temp_file = AOCTowerFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)  

  def tower_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_Tower_inp.yml')
    temp_file = AOCTowerFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def blade_to_yaml(self):
    file_path = os.path.join(self.case_directory,'/AOC_Blade.dat')
    temp_file = AOCBladeFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)   

  def blade_to_text(self):
    file_path = os.path.join(self.case_directory,'/AOC_Blade_inp.yml')
    temp_file = AOCBladeFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)
