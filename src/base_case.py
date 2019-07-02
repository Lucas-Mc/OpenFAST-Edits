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
      print("Given case directory does not exist: {}".format(self.case_directory))
      create_directory = input("Should it be created [y/n]? ")
      if create_directory.lower() == "y":
        os.mkdir(self.case_directory)
      else:
        sys.exit(99)
    os.chdir(self.case_directory)

    parent_directory = os.path.dirname(self.case_directory)
    base_name = os.path.basename(self.primary_input_file.filename) + ".log"
    self.log_file =  os.path.join(parent_directory, base_name)
    if os.path.exists(os.path.join(case_directory, self.log_file)):
      # TODO: Add a helper function
      # TODO: Give the user the opportunity to stop the run?
      print('Log file does exist... ')
      print('\tThis file will be overwritten now: ' + self.log_file)

  def run(self, verbose=True):
    stdout = sys.stdout if verbose else open(os.devnull, 'w')
    command = "{} {} # > {}".format(
      self.driver.executable_path,
      self.primary_input_file.openfast_filename,
      self.log_file
    )
    return subprocess.call(command, stdout=stdout, shell=True)
