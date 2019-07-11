import sys
from src.base_file import BaseFile


class CrushingInpFile(BaseFile):

  def __init__(self,filename):

    try: 

      super().__init__(filename)
      self.output_filename = self.parse_filename(filename,'.inp','.yml')

    except:

      print('Oops!',sys.exc_info()[0],"occured.")
      
  def read(self):

    new_dict = {}
    temp_dict = {}
    # temp_var = self.data[0].split()
    # output_file.write('# '+combine_text_spaces(temp_var[1:])+'\n')
    
    for line in self.data[2:]:

      if ((line[0] == '!') and (len(line.split()) > 1)):

        new_header = line.split()[1:]
        new_header = self.combine_text_spaces(new_header).replace(' ','_')

      elif (line[0] != '!'):

        temp_key,temp_value = self.sep_string(line,' ')
        temp_dict[temp_key] = self.convert_value(temp_value)

      elif (line[0] == '!'):
          
        new_dict[new_header] = temp_dict
        temp_dict = {}

    new_dict[new_header] = temp_dict

    return new_dict

