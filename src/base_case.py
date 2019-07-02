import os
import sys
import subprocess


class BaseCase():
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
      self.log_file = self.primary_input_file.filename + '.log'

    if (os.path.exists(os.path.join(case_directory, self.log_file))):
      # TODO: Add a helper function
      print('Log file does exist... ')
      print('\tThis file will be overwritten now: ' + self.log_file)

  def run(self):
    stdout = sys.stdout  # if verbose else open(os.devnull, 'w')
    os.chdir(self.case_directory)
    command = "{} {} > {}".format(
        self.driver.executable_path, self.primary_input_file, self.log_file)
    return subprocess.call(command, stdout=stdout, shell=True)
