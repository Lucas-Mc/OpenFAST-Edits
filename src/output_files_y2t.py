# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 27, 2019

import sys
import yaml
from src.base_file import BaseFile

class OutputFile(BaseFile):
  """
  Super class for all output-related files.
  """
  def __init__(self, filename):

    try:

      super().__init__(filename)
      file_ext = '.out'
      input_filename = self.parse_filename(filename,'.yml',file_ext)
      self.init_input_file(input_filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

class OutputPrimaryFile(OutputFile):
  """
  Primary output file.
  """

  def __init__(self, filename):

    try:

      super().__init__(filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def read(self):
    # print(self.filename)
    in_file = '/'.join(self.filename.split('/')[:-1]) + '/bd_driver_out.yml'
    in_dict = yaml.load(open(in_file))

    file_string = ''
    file_string += '\n'
    # TODO: make dynamic
    file_string += 'Predictions were generated on 26-Jun-2019 at 13:50:04 using BeamDyn'
    file_string += '\n\n\n\n\n'
    
    for kn in in_dict.keys():
      file_string += kn + '\t'

    file_string += '\n'

    for kn in in_dict.keys():
      temp_string = '(' + in_dict[kn]['Unit'] + ') '
      file_string += temp_string
    
    file_string += '\n'

    for i in range(len(in_dict['Time']['Value'])):
      for kn in in_dict.keys():
        file_string += ' '
        file_string += str(in_dict[kn]['Value'][i])
      file_string += '\n'

    return file_string

