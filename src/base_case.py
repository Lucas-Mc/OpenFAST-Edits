import os
import sys
import subprocess

class BaseCase():

  def __init__(self, driver, case_directory, input_files, primary_input_index=0):
    """
    Args:
      driver::[string] 
        - The Driver object which will be used to run this case
      case_directory::[string] 
        - The location of this case
      input_files::[list]  
        - A list of all the input files which describe this case
      Optional primary_input_index:[int] 
        - The location in input_files of the primary input file
    Returns:
      None
    """
    self.driver = driver

    # The case directory should be of this form: <path_to>/<case_name>
    self.case_directory = case_directory.rstrip(os.path.sep)

    self.input_files = input_files
    self.primary_input_file = self.input_files[primary_input_index]

    if not os.path.isdir(case_directory):
      print("Given case directory does not exist: {}".format(self.case_directory))
      create_directory = input("Should it be created [y/n]? ")
      if create_directory.lower() == "y":
        os.mkdir(self.case_directory)
      else:
        sys.exit(99)
    
    # Log file should be the name of the case directory + ".log"
    self.log_file = os.path.basename(self.case_directory.split(os.path.sep)[-1]) + ".log"

    # Store the current directory so we know where to return on end()
    self.calling_directory = os.getcwd()

  def start(self):
    """
    Change the current directory to the case directory to prepare driver
    """
    os.chdir(self.case_directory)

  def run(self, verbose=True):
    """
    Create the shell command which will run the driver
    Args:
      verbose::[bool]
        - Determines whether or not excess output should be printed
    Returns:
      Shell command and call
    """
    stdout = sys.stdout if verbose else open(os.devnull, 'w')
    command = "{} {} > {}".format(
      self.driver.executable_path,
      self.primary_input_file.openfast_filename,
      self.log_file
    )
    return subprocess.call(command, stdout=stdout, shell=True)

  def end(self):
    """
    Change the current directory to the calling directory to close out driver
    """
    os.chdir(self.calling_directory)
