
import subprocess
import os
from stat import ST_MODE
import sys

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
        # Verify that the executable exists
        if not os.path.isfile(executable_path):
            raise OSError(2, "Driver file does not exist", executable_path)

        # Verify that the executable can be executed
        permissionsMask = oct(os.stat(executable_path)[ST_MODE])[-1:]
        if not int(permissionsMask) % 2 == 1:
            raise OSError(1, "Driver file cannot be executed", executable_path)

        self.executable_path = executable_path

    def run_case(self, case, stdout):
        os.chdir(case.case_directory)
        command = "{} {} > {}".format(self.executable_path, case.input_file, case.log_file)
        return subprocess.call(command, stdout=stdout, shell=True)



if __name__ == "__main__":
    # build the case
    current_dir = '/Users/lmccullu/openfast/build/reg_tests/modules-local/beamdyn/bd_static_cantilever_beam'
    inp_file = 'bd_driver'
    case = Case(current_dir, inp_file)

    # build the driver
    stdout = sys.stdout # if verbose else open(os.devnull, 'w')
    bd_driver = BeamdynDriver("/Users/rmudafor/Development/openfast/build/modules/beamdyn/beamdyn_driver")

    # run it
    bd_driver.run_case(case, stdout)
    