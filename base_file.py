# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 18, 2019

import sys
import yaml

class BaseFile():

  def __init__(self, filename):

    try:

      self.filename = filename
      new_file = open(filename)
      self.data = new_file.readlines()

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def init_output_file(self, output_filename):

    try:

      self.output_file = open(output_filename,'w') 
      self.output_file.write('---\n')
      self.output_file.write('# Input information for: '+self.remove_char(output_filename,['.yml'])+'\n')

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def to_yaml(self, new_dict):

    try:

      self.new_dict = new_dict
      yaml.safe_dump(new_dict, self.output_file)
      self.output_file.close()

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def is_float(self, s):
    '''
    Determines if a string (s) can be converted to a float
    '''
    try:
        float(s)
        return True
    except ValueError:
        return False

  def is_int(self, s):
    '''
    Determines if a string (s) can be converted to an integer
    '''
    try:
        int(s)
        return True
    except ValueError:
        return False

  def convert_value(self, s_list):
    '''
    Determines and converts a string (s) to either int, float, or string
    '''
    new_list = []

    for s in s_list:

      if (self.is_int(s)):
          new_list.append(int(s))
      elif (self.is_float(s)):
          new_list.append(float(s))
      else:
          new_list.append(s)

    if (len(new_list) == 1):
      return new_list[0]
    else:
      return new_list

  def combine_text(self, s_list, sep):
    '''
    s_list: list of strings ready and in order to be merged
    sep: the character used to join the list of strings (s_list)
    '''
    new_string = sep.join(s_list)
    return new_string

  def combine_text_spaces(self, s_list):
    '''
    Combines a list of strings (s_list) with the default seperator as a space character
    '''
    return self.combine_text(s_list, sep=' ')

  def remove_char(self, s, c_list):
    '''
    Remove all the characters in a string (s) based on a list (c_list)
    '''
    new_s = s
    for c in c_list:
        new_s = new_s.replace(c, '')
    return new_s

  def remove_parens(self, s):
    '''
    Remove parentheses from a string (s)
    '''
    return self.remove_char(s, ['(', ')'])

  def remove_brackets(self, s):
    '''
    Remove brackets from a string (s)
    '''
    return self.remove_char(s, ['[', ']'])

  def split_line(self, current_line, delimiter='  '):
    '''
    Take the line and split by whitespace while conserving spaces in categories
    '''
    temp_value_list = current_line.split(delimiter)
    temp_value_list = [self.remove_char(i, ['\n']).strip() for i in temp_value_list]
    temp_value_list = list(filter(None, temp_value_list))

    return temp_value_list

  def split_line_spaces(self, current_line):
    '''
    Splits a line by the default delimiter of double spaces to conserve titles
    '''
    return self.split_line(current_line, delimiter='  ')

  def sep_string(self, s, sep):
    '''
    Takes an input sting and divides it into two by a chosen character
    s: the input string
    sep: the character that will split the string
    '''
    tl = s.split(sep)
    tl = list(filter(None, tl))
    value1 = tl[0].strip()
    value2 = tl[1].strip()
    return value1, value2

  def sep_string_double(self, s, c1, c2):
    '''
    s: input string
    c1: first character after splitting
    c2: second character after splitting
    '''
    val1, val2 = self.sep_string(s, c1)
    val2, val3 = self.sep_string(val2, c2)
    return val1, val2, val3

  def capitalize_list(self, s_list):
    '''
    CONTROL --> Control
    s_list: list of strings to be capitalized
    '''
    return [s.capitalize() for s in s_list]

  def remove_whitespace(self, s):
    '''
    s: input string
    '''
    return list(filter(None, s.split('  ')))

  def parse_type1(self, s):
    '''
    VAL   KEY   - DESC
    s: input string
    '''
    temp_vals = self.remove_whitespace(s)
    temp_value = temp_vals[0].strip()
    temp_key = temp_vals[1].strip()
    temp_desc = temp_vals[2][2:].strip()
    parsed_dict = {'Value':self.convert_value(temp_value),'Description':temp_desc}
    return temp_key,parsed_dict

  def parse_filename(self, s, in_type, out_type):
    '''
    s: input string
    in_type: file extension of input file
    out_type:file extension of output file
    '''
    parsed_filename = s.split('/')[-1].replace(in_type,out_type)
    
    if (in_type == '.inp'):
    
      parsed_filename = s.split('/')[-1].replace(in_type,out_type).replace('.','_inp.')
    
    if (in_type == '.sum'):
    
      parsed_filename = s.split('/')[-1].replace(in_type,out_type).replace('.','_sum.')
    
    return parsed_filename

  def parse_filetype_dash(self, contents, key_list, sec_start_list, length_list):
    '''

    '''
    new_dict = {}
    current_sec_ind = 0
    current_line_ind = 0

    for i,k in enumerate(key_list):

      current_line = sec_start_list[current_sec_ind] + current_line_ind
      new_dict[k] = contents[current_line].split()[0]
      current_line_ind += 1

      if (i >= sum(length_list[:(current_sec_ind+1)])):

        current_sec_ind += 1
        current_line_ind = 0

    return new_dict

