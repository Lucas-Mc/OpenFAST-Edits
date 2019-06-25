import os
import sys
import subprocess
from src.beamdyn_driver import BeamdynDriver
from src.beamdyn_files import BeamdynPrimaryFile, BeamdynBladeFile, BeamdynInputFile, BeamdynInputSummaryFile

class Case():
  def __init__(self, driver, case_directory, input_file):
    self.driver = driver
    self.case_directory = case_directory
    self.input_file = input_file

    if not os.path.isdir(case_directory):
      print('Directory does not exist... Please setup the following: ' + case_directory)

    try:
      self.log_file = self.input_file.split('.')[0] + '.log'
    except:
      self.log_file = input_file + '.log'

    if (os.path.exists(os.path.join(case_directory, self.log_file))):
      print('Log file does exist... ')
      print('\tThis file will be overwritten now: ' + self.log_file)
      print('\tThis file is located in: ' + self.case_directory)
    else:
      print('Log file does not exist')
  
  def run(self):
    stdout = sys.stdout  # if verbose else open(os.devnull, 'w')
    os.chdir(self.case_directory)
    command = "{} {} > {}".format(self.driver.executable_path, self.input_file, self.log_file)
    return subprocess.call(command, stdout=stdout, shell=True)

class BeamdynCase(Case):
  def __init__(self, openfast_directory, case_type):
    # Set a common home directory
    homedir = os.path.expanduser("~")
    # Each case uses the same driver
    driver = BeamdynDriver(homedir + '/openfast/build/modules/beamdyn/beamdyn_driver')
    # Each case uses the same input file
    input_file = 'bd_driver.inp'
    # The location of the .log, .out, .ech, and .sum files
    case_directory = openfast_directory + '/build/reg_tests/modules/beamdyn/' + case_type 
    super().__init__(driver, case_directory, input_file)

  # TODO: connect this with the beamdyn file classes
  #  - input files should use the yaml interface
  #  - output files should ultimatley be exported in yaml

  # @staticmethod
  # def import_to_yaml():
  #   pass

  # Convert the outputted summary file to YAML
  def export_to_yaml(self):
  
    file_path = self.case_directory + '/bd_primary.inp.sum'
    beamdyn_input_sum_file = BeamdynInputSummaryFile(file_path)
    new_dict = beamdyn_input_sum_file.read()
    beamdyn_input_sum_file.to_yaml(new_dict)
  