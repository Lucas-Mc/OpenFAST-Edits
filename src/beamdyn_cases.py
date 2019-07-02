from src.base_case import BaseCase
from src.beamdyn_driver import BeamdynDriver
from src.beamdyn_files import BeamdynPrimaryFile
from src.beamdyn_files import BeamdynBladeFile
from src.beamdyn_files import BeamdynDriverFile
from src.beamdyn_files import BeamdynInputSummaryFile
from src.output_files import OutputPrimaryFile


class BeamdynCase(BaseCase):
  def __init__(self, openfast_directory, case_directory):
    """
    openfast_directory: Str - # TODO See example in base_case
    case_directory: Str - # TODO See example in base_case
    """
    self.openfast_directory = openfast_directory
    driver = BeamdynDriver(openfast_directory + '/build/modules/beamdyn/beamdyn_driver')
    input_files = [
        BeamdynDriverFile(case_directory, 'bd_driver.yml'),
        BeamdynPrimaryFile(case_directory, 'bd_primary.yml'),
        BeamdynBladeFile(case_directory, 'beam_props.yml'),
    ]
    super().__init__(driver, case_directory, input_files)

  def initialize_input_files(self):
    """
    Convert all yaml files to openfast files
    """
    for f in self.input_files:
      f.to_text(f.read_y2t())

  def inp_to_yaml(self):
    for input_file in self.input_files:
      file_path = self.case_directory + '/' + input_file
      if (input_file == 'bd_driver.inp'):
        temp_file = BeamdynDriverFile(file_path)
      elif (input_file == 'bd_primary.inp'):
        temp_file = BeamdynPrimaryFile(file_path)
      elif (input_file == 'beam_props.inp'):
        temp_file = BeamdynBladeFile(file_path)
      new_dict = temp_file.read_t2y()
      temp_file.to_yaml(new_dict)

  # Convert the outputted summary file to YAML
  def inpsum_to_yaml(self):
    file_path = self.case_directory + '/bd_primary.inp.sum'
    temp_file = BeamdynInputSummaryFile(file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)

  def inpsum_to_text(self):
    file_path = self.case_directory + '/bd_primary_inpsum.yml' 
    temp_file = BeamdynInputSummaryFile(file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def driver_to_yaml(self):
    #print(self.openfast_directory.replace('openfast','OpenFAST_Edits'))
    file_path = self.openfast_directory.replace('openfast','OpenFAST_Edits') + self.case_directory[1:] + 'bd_driver.out'  
    temp_file = OutputPrimaryFile('',file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)

  def driver_to_text(self):
    file_path = self.case_directory + '/bd_driver_out.yml'
    temp_file = OutputPrimaryFile(file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  # TODO: not done yet
  def primary_to_text(self):
    file_path = self.case_directory + '/bd_primary_inp.yml'
    temp_file = BeamdynPrimaryFile(file_path)
    file_string = temp_file.read_y2t()
    temp_file.to_text(file_string)

  def props_to_yaml(self):
    file_path = self.case_directory + '/beam_props.inp'
    temp_file = BeamdynBladeFile(file_path)
    new_dict = temp_file.read_t2y()
    temp_file.to_yaml(new_dict)   

  def props_to_text(self):
    file_path = self.case_directory + '/beam_props_inp.yml' 
    temp_file = BeamdynBladeFile(file_path)
    file_string = temp_file.read_y2t()
