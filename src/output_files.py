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
      file_ext = filename.split('.',1)[1]
      output_filename = self.parse_filename(filename,'.'+file_ext,'.yml')
      self.init_output_file(output_filename)

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

    new_dict = {}
    len_file = len(self.data)
    param_list = self.data[6].split('\t')
    param_list = [p.strip() for p in param_list]
    param_list = list(filter(None, param_list))
    unit_list = self.remove_parens(self.data[7].split())

    new_dict = {}
    for i in range(len(param_list)):

      value_list = []

      for j in range(8,len_file):
        split_list = self.data[j].split()
        split_list = list(filter(None, split_list))
        value_list.append(split_list[i])

      new_dict[param_list[i]] = {'Unit':unit_list[i],'Value':self.convert_value(value_list)}
    
    return new_dict
