
import subprocess
import os

class Case():
    def __init__(self, case_directory, input_file):
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
        self.log_file = input_file + '.log'

        if (os.path.exists(os.path.join(case_directory,self.log_file))):
          print('Log file does exist')
        else:
          print('Log file does not exist')
          # Maybe should also do more to prevent further errors?          


class BeamdynDriver():
    def __init__(self, executable_path):
        self.executable_path = executable_path
        # TODO:
        # self.executable = 

        # TODO: check that this executable exists
        # TODO: check that this executable can be executed

    def run_case(self, case, stdout):
        command = "{} {} > {}".format(self.executable, case.input_file, case.log_file)
        return subprocess.call(command, stdout=stdout, shell=True)


if __name__=="__main__":

  current_dir = '/Users/lmccullu/openfast/build/reg_tests/modules-local/beamdyn/bd_static_cantilever_beam'
  inp_file = 'bd_driver'
  case = Case(current_dir,inp_file)
  bd_driver = BeamdynDriver()
  bd_driver.run_case()