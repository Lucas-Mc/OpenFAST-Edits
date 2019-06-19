# Rafael Mudafort
# NWTC
# June 19, 2019
from base_file import BaseFile


class BeamdynFile(BaseFile):

  def __init__(self,filename):

    super().__init__(filename)
    output_filename = filename.split('/')[len(filename.split('/'))-1].replace('.dat','.yml')
    self.init_output_file(output_filename)

  def read(self):
      
    new_dict = {}

    for line in self.data[2:]:

      if ((line[0] == '-') and (' ' in line)):

        new_header = self.remove_char(line,['-']).split()
        new_header = self.capitalize_list(new_header)
        new_header = self.combine_text_spaces(new_header)
        temp_dict = {}

      elif (new_header.split()[0] == 'Simulation'):
          
        temp_vals = list(filter(None, line.split('  ')))
        temp_value = temp_vals[0].strip()

        try:

          temp_desc = self.remove_char(temp_vals[2],['-']).strip()
          temp_key = temp_vals[1].strip()

        except:

          temp_key,temp_desc = self.sep_string(temp_vals[1],'-')
          temp_desc = self.remove_char(temp_desc,['-']).strip()
          temp_key = temp_key.strip()

        temp_dict[temp_key] = {'Value':self.convert_value(temp_value),'Description':temp_desc}

      elif (new_header.split()[0] == 'Geometry'):

        if (type(self.convert_value(line.split()[3])) is str):
            
          if (line.split()[0] == 'kp_xr'):
              
            temp_key_list = line.split()
              
            for tk in temp_key_list:
                  
              temp_temp_dict[tk] = []

          elif ('(' in line.split()[0]): 
                
            temp_unit_list = [self.remove_parens(s) for s in line.split()]
            
          else:
              
            temp_temp_dict = {} 
            temp_vals = list(filter(None, line.split('  ')))
            temp_value = temp_vals[0].strip()
            temp_desc = temp_vals[2][2:].strip()
            temp_key = temp_vals[1].strip()
            temp_dict[temp_key] = {'Value':self.convert_value(temp_value),'Description':temp_desc}

        else:

          for i,tk in enumerate(temp_key_list):
                
            temp_value = line.split()[i]
            temp_temp_dict[tk].append(self.convert_value(temp_value))
            temp_dict[tk] = {'Value':temp_temp_dict[tk],'Unit':temp_unit_list[i]}
        
      elif ((new_header.split()[0] == 'Mesh') or (new_header.split()[0] == 'Material') or (new_header.split()[0] == 'Pitch')):

        temp_vals = list(filter(None, line.split('  ')))
        temp_value = temp_vals[0].strip()

        try:

          if (new_header.split()[0] == 'Mesh'):

            temp_desc = temp_vals[2][2:].strip()

          else:

            temp_desc = self.remove_char(temp_vals[2],['-']).strip()
            
          temp_key = temp_vals[1].strip()

        except:

          temp_key,temp_desc = self.sep_string(temp_vals[1],'-')
          temp_desc = self.remove_char(temp_desc,['-']).strip()
          temp_key = temp_key.strip()

        temp_dict[temp_key] = {'Value':self.convert_value(temp_value),'Description':temp_desc}

      elif (new_header.split()[0] == 'Outputs'):

        if ('OutNd' in line):

          temp_vals = list(filter(None, line.split('  ')))
          node_list = [self.convert_value(self.remove_char(s,[','])) for s in temp_vals[:-3]]
          temp_key = temp_vals[-3]
          temp_desc = self.combine_text_spaces(temp_vals[-2:])[2:].strip()
          temp_dict[temp_key] = {'Nodes':node_list,'Description':temp_desc}

        elif (line.count(',') == 2):

          print(line)
        
        else:

          temp_vals = list(filter(None, line.split('  ')))
          temp_value = temp_vals[0].strip()
          temp_desc = temp_vals[2][2:].strip()
          temp_key = temp_vals[1].strip()
          temp_dict[temp_key] = {'Value':self.convert_value(temp_value),'Description':temp_desc}

      new_dict[new_header] = temp_dict

    return new_dict
