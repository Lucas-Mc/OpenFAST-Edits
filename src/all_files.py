import sys
import yaml
from src.base_file import BaseFile

class AeroDataFile(BaseFile):
  """
  Input file for the openfast driver
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}

    new_dict['line1'] = self.convert_value(self.data[0].strip())
    new_dict['line2'] = self.convert_value(self.data[1].strip())
    
    key_list = [
      'Number of airfoil tables in this file',                   
      'Table ID parameter',                                      
      'Stall angle (deg)',
      'No longer used, enter zero',                              
      'No longer used, enter zero',                              
      'No longer used, enter zero',                              
      'Angle of attack for zero Cn for linear Cn curve (deg)',             
      'Cn slope for zero lift for linear Cn curve (1/rad)',                
      'Cn at stall value for positive angle of attack for linear Cn curve',
      'Cn at stall value for negative angle of attack for linear Cn curve',
      'Angle of attack for minimum CD (deg)',                              
      'Zero lift drag'
    ] 

    sec_start_list = [2]
    length_list = [12]
    
    temp_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list,sep='  ')
    new_dict.update(temp_dict)

    sec_start = 14
    sec_end = 63
    temp_list_aa = []
    temp_list_cl = []
    temp_list_cd = []
    for ln in range(sec_start,sec_end+1):
      temp_parse = self.remove_whitespace_filter(self.data[ln].split('  '))
      if (ln == sec_start):
        if (len(temp_parse) > 3):
          new_dict['hasInfo'] = 'yes'
        else:
          new_dict['hasInfo'] = 'no'
      temp_list_aa.append(self.convert_value(temp_parse[0].strip()))
      temp_list_cl.append(self.convert_value(temp_parse[1].strip()))
      temp_list_cd.append(self.convert_value(temp_parse[2].strip()))

    new_dict['angle of attack'] = temp_list_aa
    new_dict['Cl'] = temp_list_cl
    new_dict['Cd'] = temp_list_cd

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += in_dict['line1']
    file_string += '\n'
    file_string += in_dict['line2']
    file_string += '\n'

    key_list = [
      'Number of airfoil tables in this file',                   
      'Table ID parameter',                                      
      'Stall angle (deg)',
      'No longer used, enter zero',                              
      'No longer used, enter zero',                              
      'No longer used, enter zero',                              
      'Angle of attack for zero Cn for linear Cn curve (deg)',             
      'Cn slope for zero lift for linear Cn curve (1/rad)',                
      'Cn at stall value for positive angle of attack for linear Cn curve',
      'Cn at stall value for negative angle of attack for linear Cn curve',
      'Angle of attack for minimum CD (deg)',                              
      'Zero lift drag'
    ]

    for k in key_list:
      temp_string = str(in_dict[k]) + '  ' + k + '\n'
      file_string += temp_string

    for i in range(len(in_dict['angle of attack'])):
      file_string += str(in_dict['angle of attack'][i])
      file_string += '  '
      file_string += str(in_dict['Cl'][i])
      file_string += '  '
      file_string += str(in_dict['Cd'][i])
      if (i == 0) or (i == len(in_dict['angle of attack'])-1):
        if (in_dict['hasInfo'] == 'yes'):
          file_string += '  angle of attack, Cl, Cd\n'
        else:
          file_string += '\n'
      else:
        file_string += '\n'   

    return file_string

