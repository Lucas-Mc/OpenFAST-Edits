
import os
import sys
import subprocess

class Case():
  def __init__(self, driver, case_directory, input_file):
    self.driver = driver
    self.case_directory = case_directory

    # TODO: check that this directory exists
    if (os.path.isdir(case_directory)):
      print('Directory does exist')
    else:
      print('Directory does not exist')
      # Maybe should also do more to prevent further errors?

    # Input file is simply the template so 'bd_driver' not 'bd_driver.inp'
    self.input_file = input_file

    # TODO: derive log file from input file or case directory
    try:
      self.log_file = self.input_file.split('.')[0] + '.log'
    except:
      self.log_file = input_file + '.log'

    if (os.path.exists(os.path.join(case_directory, self.log_file))):
      print('Log file does exist')
    else:
      print('Log file does not exist')
      # Maybe should also do more to prevent further errors? 
  
  def run(self):
    stdout = sys.stdout  # if verbose else open(os.devnull, 'w')
    os.chdir(self.case_directory)
    command = "{} {} > {}".format(self.driver.executable_path, self.input_file, self.log_file)
    return subprocess.call(command, stdout=stdout, shell=True)

class BeamdynCase(Case):
    def __init__(self, driver, case_directory, input_file):
        super().__init__(driver, case_directory, input_file)
