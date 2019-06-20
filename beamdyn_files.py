# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 19, 2019

from base_file import BaseFile


class BeamdynFile(BaseFile):
  """
  Super class for all BeamDyn-related files.
  """
  def __init__(self, filename):

    super().__init__(filename)
    output_filename = self.parse_filename(filename,'.dat','.yml')
    self.init_output_file(output_filename)


class BeamdynPrimaryFile(BeamdynFile):
  """
  Primary input file for BeamDyn.
  """

  def __init__(self, filename):

    super().__init__(filename)

  def read(self):

    new_dict = {}

    for line in self.data[2:]:

      if ((line[0] == '-') and (' ' in line)):

        new_header = self.remove_char(line, ['-']).split()
        new_header = self.capitalize_list(new_header)
        new_header = self.combine_text_spaces(new_header)
        temp_dict = {}

      elif (new_header.split()[0] == 'Simulation'):

        temp_vals = self.remove_whitespace(line)
        temp_value = temp_vals[0].strip()

        try:

          temp_desc = self.remove_char(temp_vals[2], ['-']).strip()
          temp_key = temp_vals[1].strip()

        except:

          temp_key, temp_desc = self.sep_string(temp_vals[1], '-')
          temp_desc = self.remove_char(temp_desc, ['-']).strip()
          temp_key = temp_key.strip()

        temp_dict[temp_key] = {'Value': self.convert_value(temp_value), 'Description': temp_desc}

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
            temp_key, parsed_dict = self.parse_type1(line)
            temp_dict[temp_key] = parsed_dict

        else:

          for i, tk in enumerate(temp_key_list):

            temp_value = line.split()[i]
            temp_temp_dict[tk].append(self.convert_value(temp_value))
            temp_dict[tk] = {
              'Value': temp_temp_dict[tk],
              'Unit': temp_unit_list[i]
            }

      elif ((new_header.split()[0] == 'Mesh') or (new_header.split()[0] == 'Material') or (new_header.split()[0] == 'Pitch')):

        temp_vals = self.remove_whitespace(line)
        temp_value = temp_vals[0].strip()

        try:

          if (new_header.split()[0] == 'Mesh'):

            temp_desc = temp_vals[2][2:].strip()

          else:

            temp_desc = self.remove_char(temp_vals[2], ['-']).strip()

          temp_key = temp_vals[1].strip()

        except:

          temp_key, temp_desc = self.sep_string(temp_vals[1], '-')
          temp_desc = self.remove_char(temp_desc, ['-']).strip()
          temp_key = temp_key.strip()

        temp_dict[temp_key] = {
          'Value': self.convert_value(temp_value),
          'Description': temp_desc
        }

      elif (new_header.split()[0] == 'Outputs'):

        if ('OutNd' in line):

          temp_vals = self.remove_whitespace(line)
          node_list = [self.convert_value(self.remove_char(s, [','])) for s in temp_vals[:-3]]
          temp_key = temp_vals[-3]
          temp_desc = self.combine_text_spaces(temp_vals[-2:])[2:].strip()
          temp_dict[temp_key] = {'Nodes': node_list, 'Description': temp_desc}

        elif (line.split()[0] == 'OutList'):

          temp_key = line.split()[0].strip()
          temp_desc = self.combine_text_spaces(line.split()[2:])
          temp_val_list = []

        elif (line.count(',') == 2):

          temp_val_list.append(line.strip())

        elif (line.split()[0] == 'END'):

          temp_dict[temp_key] = {
            'Value': temp_val_list,
            'Description': temp_desc
          }

        elif (line[0] == '-'):

          pass

        else:

          temp_key, parsed_dict = self.parse_type1(line)
          temp_dict[temp_key] = parsed_dict

      new_dict[new_header] = temp_dict

    return new_dict


class BeamdynBladeFile(BeamdynFile):
  """
  BeamDyn file decsribing a blade.
  """

  def __init__(self, filename):

    super().__init__(filename)

  def read(self):

    new_dict = {}

    for line in self.data[2:]:

      if ((line.count('-') > 6) and (' ' in line)):

        new_header = self.remove_char(line, ['-']).split()
        new_header = self.capitalize_list(new_header)
        new_header = self.combine_text_spaces(new_header)
        temp_dict = {}
        temp_key_list = []
        temp_val_list = []

      elif (new_header.split()[0] == 'Blade'):

          temp_key, parsed_dict = self.parse_type1(line)
          temp_dict[temp_key] = parsed_dict

      elif (new_header.split()[0] == 'Damping'):

        if ('mu1' in line.split()[0]):

          temp_key_list = line.split()

        elif ('(' in line):

          temp_quant_list = line.split()

        else:

          temp_val_list = [self.convert_value(s) for s in line.split()]

          for i, tk in enumerate(temp_key_list):

            temp_dict[tk+temp_quant_list[i]] = temp_val_list[i]

      elif (new_header.split()[0] == 'Distributed'):

        if (line.count('.') == 1):

          station_loc = self.convert_value(line.strip())
          current_mat = 'matrix1'
          current_row = 1
          temp_temp_dict = {}
          temp_temp_dict['Stiffness Matrix'] = []

        elif (line.count('.') > 1):

          current_name = current_mat + '_row' + str(current_row)
          temp_row_vals = line.split()
          temp_row_vals = [self.convert_value(s) for s in temp_row_vals]
          temp_temp_dict['Stiffness Matrix'].append({current_name: temp_row_vals})
          current_row += 1

        else:

          current_row = 1

          if (current_mat == 'matrix1'):

            current_mat = 'matrix2'

          else:

            temp_dict[station_loc] = temp_temp_dict
            current_mat = 'matrix1'

      else:

        pass

      new_dict[new_header] = temp_dict

    return new_dict
