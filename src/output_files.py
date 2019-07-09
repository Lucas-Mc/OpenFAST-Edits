# Lucas McCullum
# Rafael Mudafort
# NWTC
# July 1, 2019

import sys
import yaml
from src.base_file import BaseFile

class OutputFile(BaseFile):
  """
  Super class for all output-related files.
  """
  def __init__(self, parent_directory, filename):
    
    super().__init__(parent_directory, filename)

    file_ext = filename.split('.',1)[1]

    if (file_ext == 'out'):

      self.output_filename = self.parse_filename(filename,'.out','.yml')

    else:

      self.input_filename = self.parse_filename(filename,'.yml','.'+file_ext)


class OutputPrimaryFile(OutputFile):
  """
  Primary output file.
  """

  def __init__(self, parent_directory, filename):
    
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}
    new_dict['Intro'] = self.data[1].strip()

    len_file = len(self.data)
    param_list = self.data[6].split('\t')
    param_list = [p.strip() for p in param_list]
    param_list = list(filter(None, param_list))
    unit_list = self.remove_parens(self.data[7].split())

    for i in range(len(param_list)):

      value_list = []

      for j in range(8,len_file):
        split_list = self.data[j].split()
        split_list = list(filter(None, split_list))
        value_list.append(split_list[i])

      new_dict[param_list[i]] = {'Unit':unit_list[i],'Value':self.convert_value(value_list)}
    
    return new_dict

  def read_y2t(self):

    in_file = self.filename
    # in_file = '/'.join(self.filename.split('/')[:-1]) + '/bd_driver_out.yml'
    in_dict = yaml.load(open(in_file))

    file_string = ''
    file_string += '\n'
    file_string += in_dict['Intro']
    file_string += '\n\n\n\n\n'
    key_list = list(in_dict.keys())
    key_list.remove('Intro')
    
    for kn in key_list:
      file_string += kn + '\t'

    file_string += '\n'

    for kn in key_list:
      temp_string = '(' + in_dict[kn]['Unit'] + ') '
      file_string += temp_string
    
    file_string += '\n'

    for i in range(len(in_dict['Time']['Value'])):
      for kn in key_list:
        file_string += ' '
        file_string += str(in_dict[kn]['Value'][i])
      file_string += '\n'

    return file_string