import yaml

class BaseFile():

  def __init__(self, filename):

    self.filename = filename
    new_file = open(filename)
    self.data = new_file.readlines()

  def init_output_file(self, output_filename):

    self.output_file = open(output_filename,'w') 
    self.output_file.write('---\n')
    self.output_file.write('# Input information for: '+self.remove_char(output_filename,['.yml'])+'\n')

  def to_yaml(self, new_dict):

    self.new_dict = new_dict
    yaml.safe_dump(new_dict, self.output_file)
    self.output_file.close()

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

  def convert_value(self, s):
    '''
    Determines and converts a string (s) to either int, float, or string
    '''
    if (self.is_int(s)):
        return int(s)
    elif (self.is_float(s)):
        return float(s)
    else:
        return s

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

    