
import os
import sys
import subprocess

class Case():
  def __init__(self, driver, case_directory, input_file):
    self.driver = driver
    self.case_directory = case_directory
    self.input_file = input_file

    # TODO: how should this error be handled?
    #  - you could create the directory but then you also have to get all the case files from somewhere
    #  - or just bail and leave that up to the user
    if not os.path.isdir(case_directory):
      print('Directory does not exist')

    try:
      self.log_file = self.input_file.split('.')[0] + '.log'
    except:
      self.log_file = input_file + '.log'

    # TODO: if it exists, maybe let the user know its being overwritten?
    if (os.path.exists(os.path.join(case_directory, self.log_file))):
      print('Log file does exist')
    else:
      print('Log file does not exist')
  
  def run(self):
    stdout = sys.stdout  # if verbose else open(os.devnull, 'w')
    os.chdir(self.case_directory)
    command = "{} {} > {}".format(self.driver.executable_path, self.input_file, self.log_file)
    return subprocess.call(command, stdout=stdout, shell=True)

class BeamdynCase(Case):
    def __init__(self, driver, case_directory, input_file):
        super().__init__(driver, case_directory, input_file)

    # TODO: Fill out the defaults
    #  - driver (all use BeamDynDriver)
    #  - input file (all are bd_driver.inp)
    
    # TODO: connect this with the beamdyn file classes
    #  - input files should use the yaml interface
    #  - output files should ultimatley be exported in yaml
