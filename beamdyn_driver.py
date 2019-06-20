
import subprocess
import os
from stat import ST_MODE
import sys


class Case():
    def __init__(self, case_directory, input_file):
        self.case_directory = case_directory
        # TODO: check that this directory exists
        self.input_file = input_file

        # TODO: derive log file from input file or case directory
        self.log_file = input_file + ".log"


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
    stdout = sys.stdout # if verbose else open(os.devnull, 'w')
    bd_driver = BeamdynDriver("/Users/rmudafor/Development/openfast/build/modules/beamdyn/beamdyn_driver")
    case = BeamdynCase(
        "/Users/rmudafor/Development/openfast/build/reg_tests/modules/beamdyn/bd_static_cantilever_beam",
        "bd_primary.inp",
        bd_driver
    )
    bd_driver.run_case(case, stdout)
