import os
import sys
import subprocess
from src.beamdyn_driver import BeamdynDriver
from src.beamdyn_files import BeamdynPrimaryFile, BeamdynBladeFile, BeamdynDriverFile, BeamdynInputSummaryFile
from src.output_files import OutputPrimaryFile


class Case():
  def __init__(self, driver, case_directory, input_files, primary_input_index=0):
    """
    driver: Driver - The Driver object which will be used to run this case
    case_directory: Str - The location of this case
    input_files: [Str] - A list of all the input files which describe this case
    Optional primary_input_index: Int - The location in input_files of the primary input file
    """
    self.driver = driver
    self.case_directory = case_directory
    self.input_files = input_files
    self.primary_input_file = self.input_files[primary_input_index]

    if not os.path.isdir(case_directory):
      print('Directory does not exist... Please setup the following: ' + case_directory)
      # TODO: probably bail? otherwise, things will fail later on

    # TODO: lets handle this better... use the case directory as the base name instead
    try:
      self.log_file = self.primary_input_file.split('.')[0] + '.log'
    except:
      self.log_file = self.primary_input_file + '.log'

    if (os.path.exists(os.path.join(case_directory, self.log_file))):
      # TODO: Add a helper function
      print('Log file does exist... ')
      print('\tThis file will be overwritten now: ' + self.log_file)
  
  def run(self):
    stdout = sys.stdout  # if verbose else open(os.devnull, 'w')
    os.chdir(self.case_directory)
    command = "{} {} > {}".format(self.driver.executable_path, self.primary_input_file, self.log_file)
    return subprocess.call(command, stdout=stdout, shell=True)

class BeamdynCase(Case):
  def __init__(self, openfast_directory, case_type):
    """
    openfast_directory: Str - # TODO See example above
    case_type: Str - # TODO See example above
    """

    self.openfast_directory = openfast_directory
    self.case_type = case_type
    driver = BeamdynDriver(self.openfast_directory + '/build/modules/beamdyn/beamdyn_driver')
    input_files = [
      'bd_driver.inp',
      'bd_primary.inp',
      'beam_props.inp'
    ]
    self.case_directory = self.openfast_directory + '/build/reg_tests/modules/beamdyn/' + self.case_type

    super().__init__(driver, self.case_directory, input_files)

  # TODO: connect this with the beamdyn file classes
  #  - input files should use the yaml interface
  #  - output files should ultimatley be exported in yaml

  def inp_to_yaml(self):
    for input_file in self.input_files:
      file_path = self.case_directory + '/' + input_file
      if (input_file == 'bd_driver.inp'):
        temp_file = BeamdynDriverFile(file_path)
      elif (input_file == 'bd_primary.inp'):
        temp_file = BeamdynPrimaryFile(file_path)
      elif (input_file == 'beam_props.inp'):
        temp_file = BeamdynBladeFile(file_path)
      new_dict = temp_file.read_t2y()
      temp_file.to_yaml(new_dict)

  # Convert the outputted summary file to YAML
  def inpsum_to_yaml(self):
    file_path = self.case_directory + '/bd_primary.inp.sum'
    temp_file = BeamdynInputSummaryFile(file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)

  def inpsum_to_text(self):
    file_path = self.case_directory + '/bd_primary_inpsum.yml' 
    temp_file = BeamdynInputSummaryFile(file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def driver_to_yaml(self):
    #print(self.openfast_directory.replace('openfast','OpenFAST_Edits'))
    #file_path = self.openfast_directory.replace('openfast','OpenFAST_Edits') + self.case_directory[1:] + 'bd_driver.out'  
    file_path = self.case_directory + '/bd_driver.out'
    temp_file = OutputPrimaryFile(file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)

  def driver_to_text(self):
    file_path = self.case_directory + '/bd_driver_out.yml'
    temp_file = OutputPrimaryFile(file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  # TODO: not done yet
  def primary_to_text(self):
    file_path = self.case_directory + '/bd_primary_inp.yml'
    temp_file = BeamdynPrimaryFile(file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def props_to_yaml(self):
    file_path = self.case_directory + '/beam_props.inp'
    temp_file = BeamdynBladeFile(file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)   

  def props_to_text(self):
    file_path = self.case_directory + '/beam_props_inp.yml' 
    temp_file = BeamdynBladeFile(file_path)
    file_string = temp_file.read_y2t()