# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 19, 2019
from fileclass import File

class Crushing_inp_file(File):

  def __init__(self,filename):

    super().__init__(filename)
    output_filename = filename.split('/')[len(filename.split('/'))-1].replace('.inp','.yml').replace('.','_inp.')
    self.init_output_file(output_filename)

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

