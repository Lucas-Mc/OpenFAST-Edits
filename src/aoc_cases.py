from src.base_case import BaseCase
from src.aoc_driver import AOCDriver
from src.aoc_files import AOCTowerFile
from src.aoc_files import AOCBladeFile
from src.aoc_files import AOCBladeADFile
from src.output_files import OutputPrimaryFile


class AOCCase(BaseCase):
  
  def __init__(self, openfast_directory, case_directory):
    """
    openfast_directory: Str - # TODO See example in base_case
    case_directory: Str - # TODO See example in base_case
    """
    self.openfast_directory = openfast_directory
    driver = AOCDriver(openfast_directory + '/build/glue-codes/openfast/openfast')
    input_files = [
        #AOCBladeADFile(case_directory, 'AOC_AeroDyn_blade.yml'),
        #AOCTowerFile(case_directory, 'AOC_Tower.yml'),
        AOCBladeFile(case_directory, 'AOC_Blade.yml'),
    ]
    self.expected_output_files = [
        'AOC_driver.out'
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
      file_path = self.case_directory + '/' + input_file
      if (input_file == 'AOC_AeroDyn_blade.dat'):
        temp_file = AOCBladeADFile('',file_path)
      elif (input_file == 'AOC_Tower.dat'):
        temp_file = AOCTowerFile('',file_path)
      elif (input_file == 'AOC_Blade.dat'):
        temp_file = AOCBladeFile('',file_path)
      new_dict = temp_file.read_t2y()
      temp_file.to_yaml(new_dict)

  def bladead_to_yaml(self):
    # print(self.openfast_directory.replace('openfast','OpenFAST_Edits'))
    # file_path = self.openfast_directory.replace('openfast','OpenFAST_Edits') + self.case_directory[1:] 
    file_path = self.case_directory + 'AOC_AeroDyn_blade.dat'  
    temp_file = AOCBladeADFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)

  def bladead_to_text(self):
    file_path = self.case_directory + '/AOC_AeroDyn_blade_inp.yml'
    temp_file = AOCBladeADFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def tower_to_yaml(self):
    file_path = self.case_directory + '/AOC_Tower.dat'
    temp_file = AOCTowerFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)  

  def tower_to_text(self):
    file_path = self.case_directory + '/AOC_Tower_inp.yml'
    temp_file = AOCTowerFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def blade_to_yaml(self):
    file_path = self.case_directory + '/AOC_Blade.dat'
    temp_file = AOCBladeFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)   

  def blade_to_text(self):
    file_path = self.case_directory + '/AOC_Blade_inp.yml' 
    temp_file = AOCBladeFile('',file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)
