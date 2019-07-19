import os
import sys
import yaml


class BaseFile():

  _openfast_extension = 'inp'

  def __init__(self, parent_directory, filename):
    self.parent_directory = parent_directory
    self.filename = filename
    self.filepath = os.path.join(self.parent_directory, self.filename)
    # self.file_handle = self.open_file(self.filepath)

    # Load the data based on the filetype given
    # All cases store data in self.data
    file_ext = filename.split('.')[-1]
    if file_ext == 'yml' or file_ext == 'yaml':
      self.load_yaml()
      self.yaml_filename = self.filename
      self.openfast_filename = self.filename.replace(file_ext, BaseFile._openfast_extension)
    else:
      self.load_openfast()
      self.openfast_filename = self.filename
      self.yaml_filename = self.filename.replace(file_ext, 'yaml')

  def open_file(self, filepath):
    return open(filepath, 'r')

  def load_yaml(self):
    self.file_handle = self.open_file(self.filepath)
    self.data = yaml.load(self.file_handle, Loader=yaml.FullLoader)
    self.file_handle.close()

  def load_openfast(self):
    self.file_handle = self.open_file(self.filepath)
    self.data = self.file_handle.readlines()
    self.file_handle.close()

  def to_yaml(self, new_dict):
    outfile = open(self.yaml_filename, 'w')
    yaml.safe_dump(new_dict, outfile)
    outfile.close()

  def to_text(self, file_string):
    outfile = open(self.openfast_filename, 'w')
    outfile.write(file_string)
    outfile.close()

  def is_float(self, s):
    """
    Determines if a string (s) can be converted to a float
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

  def is_int(self, s):
    """
    Determines if a string (s) can be converted to an integer
    """
    try:
        int(s)
        return True
    except ValueError:
        return False

  def convert_value(self, s_list):
    """
    Determines and converts a list of strings (s_list) to either int, float, or string
    """
    if (type(s_list) is not list):

      if (self.is_int(s_list)):
          return int(s_list)
      elif (self.is_float(s_list)):
          return float(s_list)
      else:
          return s_list

    else:

      new_list = []

      for s in s_list:

        if (self.is_int(s)):
            new_list.append(int(s))
        elif (self.is_float(s)):
            new_list.append(float(s))
        else:
            new_list.append(s)

      return new_list

  def combine_text(self, s_list, sep):
    """
    s_list: list of strings ready and in order to be merged
    sep: the character used to join the list of strings (s_list)
    """
    new_string = sep.join(s_list)
    return new_string

  def combine_text_spaces(self, s_list):
    """
    Combines a list of strings (s_list) with the default seperator as a space character
    """
    return self.combine_text(s_list, sep=' ')

  def remove_char(self, s, c_list):
    """
    Remove all the characters in a string (s) based on a list (c_list)
    """
    new_s = s
    for c in c_list:
        new_s = new_s.replace(c, '')
    return new_s

  def remove_parens(self, s_list):
    """
    Remove parentheses from a list of strings (s_list)
    """
    if (type(s_list) is list):
      new_list = []

      for s in s_list:  
        new_list.append(self.remove_char(s, ['(', ')']))

      return new_list  
    
    else:

      return self.remove_char(s_list, ['(', ')'])

  def remove_brackets(self, s_list):
    """
    Remove brackets from a string (s_list)
    """
    if (type(s_list) is list):
      new_list = []

      for s in s_list:  
        new_list.append(self.remove_char(s, ['[', ']']))

      return new_list  
    
    else:

      return self.remove_char(s_list, ['[', ']'])

  def split_line(self, current_line, delimiter='  '):
    """
    Take the line and split by whitespace while conserving spaces in categories
    """
    temp_value_list = current_line.split(delimiter)
    temp_value_list = [self.remove_char(i, ['\n']).strip() for i in temp_value_list]
    temp_value_list = list(filter(None, temp_value_list))

    return temp_value_list

  def split_line_spaces(self, current_line):
    """
    Splits a line by the default delimiter of double spaces to conserve titles
    """
    return self.split_line(current_line, delimiter='  ')

  def sep_string(self, s, sep):
    """
    Takes an input sting and divides it into two by a chosen character
    s: the input string
    sep: the character that will split the string
    """
    tl = s.split(sep)
    tl = list(filter(None, tl))
    value1 = tl[0].strip()
    value2 = tl[1].strip()
    return value1, value2

  def sep_string_double(self, s, c1, c2):
    """
    s: input string
    c1: first character to be split by
    c2: second character to be split by
    """
    val1, val2 = self.sep_string(s, c1)
    val2, val3 = self.sep_string(val2, c2)
    return val1, val2, val3

  def capitalize_list(self, s_list):
    """
    CONTROL --> Control
    s_list: list of strings to be capitalized
    """
    return [s.capitalize() for s in s_list]

  def remove_whitespace(self, s):
    """
    s: input string
    """
    return list(filter(None, s.split('  ')))

  def remove_whitespace_filter(self, s):
    """
    s: input string
    """
    return list(filter(None, s))

  def parse_type1(self, s):
    """
    VAL   KEY   - DESC
    s: input string
    """
    temp_vals = self.remove_whitespace(s)
    temp_value = temp_vals[0].strip()
    temp_key = temp_vals[1].strip()
    temp_desc = temp_vals[2][2:].strip()
    parsed_dict = {'Value':self.convert_value(temp_value),'Description':temp_desc}
    return temp_key,parsed_dict

  def parse_filename(self, s, in_type, out_type):
    """
    s: input string
    in_type: file extension of input file
    out_type:file extension of output file
    """
    parsed_filename = s.split('/')[-1].replace(in_type,out_type)

    if ((in_type == '.inp') or (in_type == '.dat')):
    
      parsed_filename = parsed_filename.replace('.','_inp.')
    
    elif (in_type == '.sum'):
    
      parsed_filename = parsed_filename.replace('.','_sum.')

    elif (in_type == '.inp.sum'):
    
      parsed_filename = parsed_filename.replace('.','_inpsum.')

    elif (in_type == '.out'):
    
      parsed_filename = parsed_filename.replace('.','_out.')

    elif (in_type == '.log'):
    
      parsed_filename = parsed_filename.replace('.','_log.')

    elif (in_type == '.inp.ech'):
    
      parsed_filename = parsed_filename.replace('.','_inpech.')

    # Temporary
    # elif (in_type == '.yml'):
    
    #   parsed_filename = parsed_filename.replace('.','_t.')

    return parsed_filename

  def parse_filetype_valuefirst(self, contents, key_list, sec_start_list, length_list):
    """
    VALUE   KEY   - DESC
    contents: the contents of the data file
    key_list: list of keys to be added to the dictionary
    sec_start_list: list of starting line numbers for dictionary values
    length_list: list of the lengths of each section
    """
    new_dict = {}
    current_sec_ind = 0
    current_line_ind = 0

    for i,k in enumerate(key_list):

      current_line = sec_start_list[current_sec_ind] + current_line_ind
      new_dict[k] = self.convert_value(contents[current_line].split()[0])
      current_line_ind += 1

      if (i >= sum(length_list[:(current_sec_ind+1)])):

        current_sec_ind += 1
        current_line_ind = 0

    return new_dict

  def parse_xyz(self, s, d, i, n, k):
    """
    s: string to be parsed
    d: data starting index
    i: starting index to parse
    n: number of loops
    k: dictionary key
    """
    temp_dict = {}

    for j in range(n):

      cl_split = self.remove_whitespace(s[d+j])
      x_val = self.convert_value(cl_split[i].strip())
      y_val = self.convert_value(cl_split[i+1].strip())
      z_val = self.convert_value(cl_split[i+2].strip())
      temp_dict[k+str(j)] = {'X':x_val,'Y':y_val,'Z':z_val}

    return temp_dict

  def write_valdesc(self,inp_d,k_list,d_list,cat_name):
    """
    inp_d: input dictionary 
    k_list: list of keys
    d_list: list of descriptions 
    cat_name: name of main dictionary category
    """
    file_string = ''

    for i,kn in enumerate(k_list):

      if (cat_name is None):
        temp_string = str(inp_d[kn]) + '  ' + str(kn) + '  ' + str(d_list[i]) + '\n'
      else:
        temp_string = str(inp_d[cat_name][kn]) + '  ' + str(kn) + '  ' + str(d_list[i]) + '\n'
      
      file_string += temp_string

    return file_string

  def parse_filetype_twocol(self, contents, key_list, sec_start_list, length_list):
    """
    VALUE  DESC
    contents: the contents of the data file
    key_list: list of keys to be added to the dictionary
    sec_start_list: list of starting line numbers for dictionary values
    length_list: list of the lengths of each section
    """
    new_dict = {}
    current_sec_ind = 0
    current_line_ind = 0

    for i,k in enumerate(key_list):

      current_line = sec_start_list[current_sec_ind] + current_line_ind
      new_dict[k] = self.convert_value(contents[current_line].split('  ')[0])
      current_line_ind += 1

      if (i >= sum(length_list[:(current_sec_ind+1)])):

        current_sec_ind += 1
        current_line_ind = 0

    return new_dict

  def create_val_un_dict(self, contents, new_dict, temp_key_list, temp_unit_list, key_val):
    """
    contents,
    new_dict,
    temp_key_list,
    temp_unit_list,
    key_val
    """
    temp_dict = {}
    temp_temp_dict = {}
    for tk in temp_key_list:
      temp_temp_dict[tk] = []

    for i in range(self.convert_value(new_dict[key_val])):
      
      for j, tk in enumerate(temp_key_list):
      
        temp_value = contents[17+i-1].split()[j]
        temp_temp_dict[tk].append(self.convert_value(temp_value))
        temp_dict[tk] = {
          'Value': temp_temp_dict[tk],
          'Unit': temp_unit_list[j]
        }

    return temp_dict

  def write_val_un_table(self, in_dict, rearrange_list, tt_keys, key_val, has_un=True):
    """
    in_dict,
    rearrange_list,
    tt_keys,
    key_val,
    has_un
    """
    end_string = ''
    temp_keys = []
    for i,v in enumerate(rearrange_list):
      temp_keys.append(tt_keys[v])

    temp_string = ''
    for tk in temp_keys:
      temp_string += '  '
      temp_string += tk
    end_string += temp_string
    end_string += '\n'

    if (has_un):

      temp_string = ''
      for tk in temp_keys:
        tu = in_dict['Matrix'][tk]['Unit']
        temp_string += '  '
        ind_string = '(' + tu + ')'
        temp_string +=ind_string
      end_string += temp_string
      end_string += '\n'

    num_vals = len(in_dict['Matrix'][key_val]['Value'])

    for i in range(num_vals):
      temp_string = ''
      for tk in temp_keys:
        temp_string += str(in_dict['Matrix'][tk]['Value'][i])
        temp_string += '  '
      end_string += temp_string
      end_string += '\n'

    return end_string

  def create_outlist(self, contents, start_ind):
    """
    contents,
    start_ind
    """
    end_ind = len(contents)-2
    temp_dict = {}

    for i in range(start_ind,end_ind):
      current_line = contents[i]
      temp_dict[current_line.split('  ')[0]] = current_line.split('-',1)[1].strip()

    return temp_dict
    
  def write_outlist(self, in_dict, delim):
    """
    in_dict,
    delim
    """
    end_string = ''
    end_string += 'OutList     - The next line(s) contains a list of output parameters.  See OutListParameters.xlsx for a listing of available output channels, (-)\n'
    for outp in in_dict['OutList'].keys():
      end_string += outp
      end_string += delim
      end_string += in_dict['OutList'][outp]
      end_string += '\n'

    end_string += 'END of input file (the word "END" must appear in the first 3 columns of this last OutList line)\n'
    end_string += '---------------------------------------------------------------------------------------\n'

    return end_string