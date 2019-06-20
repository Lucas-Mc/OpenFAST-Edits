
import subprocess

class Case():
    def __init__(self, case_directory, input_file):
        self.case_directory = case_directory
        # TODO: check that this directory exists
        self.input_file = input_file

        # TODO: derive log file from input file or case directory
        self.log_file = input_file + ".log"


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

