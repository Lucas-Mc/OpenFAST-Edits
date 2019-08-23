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
    INPUT:

    ::

      2

    OUTPUT:

    ::

      False
    
    Args:
      s (string):
        - The initial input string to be tested
    
    Returns:
      UN-NAMED (bool):
        - The final list of values that have been converted
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

  def is_int(self, s):
    """
    INPUT:

    ::

      2.3

    OUTPUT:

    ::

      False
    
    Args:
      s (string):
        - The initial input string to be tested
    
    Returns:
      UN-NAMED (bool):
        - The final list of values that have been converted
    """
    try:
        int(s)
        return True
    except ValueError:
        return False

  def convert_value(self, s_list):
    """
    INPUT:

    ::

      ['4','2.3','one']

    OUTPUT:

    ::

      [4,2.3,'one']
    
    Args:
      s_list (string):
        - The initial input list of strings to be converted
    
    Returns:
      s_list/new_list (list):
        - The final list of values that have been converted
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
    INPUT:

    ::

      s_list = ['the','best','one','knows']
      sep = '+'

    OUTPUT:

    ::

      the+best+one+knows
    
    Args:
      s_list (string):
        - The initial input list of strings to be parsed
      sep (string):
        - The character that will be used to combine the strings in s_list
    
    Returns:
      new_string (string):
        - The final string that has been joined with the custom seperator
    """
    new_string = sep.join(s_list)
    return new_string

  def combine_text_spaces(self, s_list):
    """
    INPUT:

    ::

      ['the','best','one','knows']

    OUTPUT:

    ::

      the best one knows
    
    Args:
      s_list (string):
        - The initial input list of strings to be parsed
    
    Returns:
      UN-NAMED:[list]
        - The final output list of the combined text
    """
    return self.combine_text(s_list, sep=' ')

  def remove_char(self, s, c_list):
    """
    INPUT:

    ::

      s = 'the be$t %ne knows'
      c_list = ['$','%','k']

    OUTPUT:

    ::

      new_s = 'the bet ne nows'
    
    Args:
      s (string):
        - The initial input string to be parsed
      c_list (list): 
        - The list of characters to be removed
   
    Returns:
      new_s (string):
        - The final output string of the filtered string
    """
    new_s = s
    for c in c_list:
        new_s = new_s.replace(c, '')
    return new_s

  def remove_parens(self, s_list):
    """
    INPUT:

    ::

      (VAL1 is ()here)()

    OUTPUT:

    ::

      VAL1 is here
    
    Args:
      s_list (list): 
        - The initial input strings to be parsed
    
    Returns:
      new_list/UN-NAMED (list):
        - The final output list of the parsed data
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
    INPUT:

    ::

      [VAL1 is []here][]

    OUTPUT:

    ::

      VAL1 is here
    
    Args:
      s_list (list): 
        - The initial input strings to be parsed
   
    Returns:
      new_list (list):
        - The final output list of the parsed data
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
    INPUT:

    ::

      current_line = 'VAL1  +  VAL2'
      delimiter = '+'

    OUTPUT:

    ::

      [VAL1, VAL2]
    
    Args:
      current_line (string): 
        - The initial input string
      delimiter (string,default='  ')
        - The character that will be used to split the text
    
    Returns:
      temp_value_list (list):
        - The final output list of the parsed data
    """
    temp_value_list = current_line.split(delimiter)
    temp_value_list = [self.remove_char(i, ['\n']).strip() for i in temp_value_list]
    temp_value_list = list(filter(None, temp_value_list))

    return temp_value_list

  def split_line_spaces(self, current_line):
    """
    INPUT:

    ::

      VAL1  VAL2

    OUTPUT:

    ::

      [VAL1, VAL2]
    
    Args:
      current_line (string): 
        - The initial input string
    
    Returns:
      UN-NAMED (list):
        - The final output list of the split line
    """
    return self.split_line(current_line, delimiter='  ')

  def sep_string(self, s, sep):
    """
    INPUT:

    ::

      s = 'VAL1  -  VAL2'
      sep = '-'

    OUTPUT:

    ::

      value1 = VAL1
      value2 = VAL2
    
    Args:
      s (string): 
        - The initial input string
      sep (string): 
        - The character to be split by
    
    Returns:
      value1 (string):
        - The first value parsed from the initial input string
      value2 (string):
        - The second value parsed from the initial input string
    """
    tl = s.split(sep)
    tl = list(filter(None, tl))
    value1 = tl[0].strip()
    value2 = tl[1].strip()
    return value1, value2

  def sep_string_double(self, s, c1, c2):
    """
    INPUT:

    ::

      s = 'VAL1  -  VAL2  +  VAL3'
      c1 = '-'
      c2 = '+'

    OUTPUT:

    ::

      val1 = VAL1
      val2 = VAL2
      val3 = VAL3
    
    Args:
      s (string): 
        - The initial input string
      c1 (string): 
        - The first character to be split by
      c2 (string): 
        The second character to be split by
    
    Returns:
      val1 (string):
        - The first value parsed from the initial input string
      val2 (string):
        - The second value parsed from the initial input string
      val3 (string):
        - The third value parsed from the initial input string
    """
    val1, val2 = self.sep_string(s, c1)
    val2, val3 = self.sep_string(val2, c2)
    return val1, val2, val3

  def capitalize_list(self, s_list):
    """
    INPUT:

    ::

      [CONTROL, CONtrOL, ...]

    OUTPUT:

    ::

      [Control, Control, ...]
    
    Args:
      s_list (string):
        - The list of strings to be capitalized
    
    Returns:
      UN-NAMED (list):
        - The final capitalized list of input strings 
    """
    return [s.capitalize() for s in s_list]

  def remove_whitespace(self, s):
    """
    INPUT:

    ::

      VAL1  VAL2    VAL3

    OUTPUT:

    ::

      ['VAL1','VAL2','VAL3]
    
    Args:
      s (string):
        - The input string to be parsed
    
    Returns:
      UN-NAMED (list):
        - The final ist of input strings where whitespace has been removed
    """
    return list(filter(None, s.split('  ')))

  def remove_whitespace_filter(self, s):
    """
    INPUT:

    ::

      ['VAL1  VAL2','','VAL3']
    
    OUTPUT:

    ::

      ['VAL1  VAL2','VAL3']
    
    Args:
      s (string):
        - The input string to be parsed
    
    Returns:
      UN-NAMED (list):
        - The final ist of input strings where whitespace has been removed
    """
    return list(filter(None, s))

  def parse_type1(self, s):
    """
    INPUT:

    ::

      VAL   KEY   - DESC

    OUTPUT:

    ::

      {
        Value: VAL
        Description: DESC
      }
    
    Args:
      s (string): 
        - The starting input string
    
    Returns:
      temp_key (string):
        - The new key value which is returned to be used later
      parsed_dict (dict):
        - The final output dictionary which contains the values and descriptions for each key
    """
    temp_vals = self.remove_whitespace(s)
    temp_value = temp_vals[0].strip()
    temp_key = temp_vals[1].strip()
    temp_desc = temp_vals[2][2:].strip()
    parsed_dict = {'Value':self.convert_value(temp_value),'Description':temp_desc}
    return temp_key,parsed_dict

  def parse_filename(self, s, in_type, out_type):
    """
    Args:
      s (string): 
        - The starting input string
      in_type (string): 
        - The file extension of input file
      out_type (string):
        - The file extension of output file
    
    Returns:
      parsed_filename (string):
        - The final filename to be returned
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

    return parsed_filename

  def parse_filetype_valuefirst(self, contents, key_list, sec_start_list, length_list, sep='  '):
    """
    INPUT:

    ::

      sec_start_list = [2,8]  # The first value should be the real value minus 1
      length_list = [4,5]
      [Line  3]---------------------- TITLE0 ----------------------------------------
      [Line  4]            VAL0     key_list[0]    - DESC0
      [Line  5]            VAL1     key_list[1]    - DESC1
      [Line  6]            VAL2     key_list[2]    - DESC2
      [Line  7]            VAL3     key_list[3]    - DESC3
      [Line  8]---------------------- TITLE1 ----------------------------------------
      [Line  9]            VAL4     key_list[4]    - DESC4
      [Line 10]            VAL5     key_list[5]    - DESC5
      [Line 11]            VAL6     key_list[6]    - DESC6
      [Line 12]            VAL7     key_list[7]    - DESC7
      [Line 13]            VAL8     key_list[8]    - DESC8
    
    OUTPUT:

    ::

      {
        key_list[0]: VAL0
        key_list[1]: VAL1
        key_list[2]: VAL2
        key_list[3]: VAL3
        key_list[4]: VAL4
        key_list[5]: VAL5
        key_list[6]: VAL6
        key_list[7]: VAL7
        key_list[8]: VAL8
      }
    
    Args:
      contents (list):
        - The starting list of text lines to be parsed
      key_list (list):
        - The list of key values to search for in contents to be parsed
      sec_start_list (list):
        - The starting line of the section with valuable content
      length_list (list):
        - The total length of the section with valuable content
      sep (string,default='  ')
        - The seperator to be used to split the sections
    
    Returns:
      new_dict (dict):
        - The final converted dictionary
    """
    new_dict = {}
    current_sec_ind = 0
    current_line_ind = 0

    for i,k in enumerate(key_list):

      current_line = sec_start_list[current_sec_ind] + current_line_ind
      temp_ln = self.remove_whitespace_filter(contents[current_line].split(sep))
      new_dict[k] = self.convert_value(temp_ln[0])
      current_line_ind += 1

      if (i >= sum(length_list[:(current_sec_ind+1)])):

        current_sec_ind += 1
        current_line_ind = 0

    return new_dict

  def parse_xyz(self, s, d, i, n, k, ok=None):
    """
    INPUT:

    ::

      Element number:    1
        k  Global node         ok[0]             ok[1]             ok[2]        
      ---- -----------  ----------------- ----------------- -----------------
       n-5      1               a11               a12               a13
       n-4      2               a21               a22               a23
       n-3      3               a31               a32               a33
       n-2      4               a41               a42               a43
       n-1      5               a51               a52               a53
        n       6               a61               a62               a63
    
    OUTPUT:

    ::

      {
        k 0:
          ok[0]: a11
          ok[1]: a12
          ok[2]: a13
        k n-5:
          ok[0]: a21
          ok[1]: a22
          ok[2]: a23
        k n-4:
          ok[0]: a31
          ok[1]: a32
          ok[2]: a33
        k n-3:
          ok[0]: a41
          ok[1]: a42
          ok[2]: a43
        k n-2:
          ok[0]: a51
          ok[1]: a52
          ok[2]: a53
        k n-1:
          ok[0]: a61
          ok[1]: a62
          ok[2]: a63
      }
    
    Args:
      s (string): 
        - The input string to be parsed
      d (int): 
        - The starting index of the data group
      i (int): 
        - The starting index to begin parsing the data in the group
      n (int): 
        - The total number of loops to be parsed 
      k (string): 
        - The new key to be created for the dictionary
    
    Returns:
      temp_dict (dict):
        - The final converted dictionary
    """
    temp_dict = {}

    for j in range(n):

      cl_split = self.remove_whitespace(s[d+j])
      x_val = self.convert_value(cl_split[i].strip())
      y_val = self.convert_value(cl_split[i+1].strip())
      z_val = self.convert_value(cl_split[i+2].strip())
      if (ok is None):
        temp_dict[k+str(j+1)] = {'X':x_val,'Y':y_val,'Z':z_val}
      else:
        temp_dict[k+str(j+1)] = {ok[0]:x_val,ok[1]:y_val,ok[2]:z_val}

    return temp_dict

  def write_valdesc(self,inp_d,k_list,d_list,cat_name=None):
    """
    INPUT:

    ::

      A bunch of different variables
    
    OUTPUT:

    ::

      inp_d[k_list[0]]  k_list[0]  - d_list[0]
      inp_d[k_list[1]]  k_list[1]  - d_list[1]
      inp_d[k_list[2]]  k_list[2]  - d_list[2]
      .
      .
      .
    
    Args:
      inp_d (dict):
        - The starting dictionary to be used to get data values
      k_list (list): 
        - The list of keys to be used in the creation of the final strings
      d_list (list):
        - The list of descriptions to be used in the creation of the final strings 
      cat_name (string,default=None)
        - The name of main dictionary category (if applicable)
    
    Returns:
      file_string (string):
        - The final string that is generated by the given data
    """
    file_string = ''

    for i,kn in enumerate(k_list):

      if (cat_name is None):
        temp_string = str(inp_d[kn]) + '  ' + str(kn) + '  ' + str(d_list[i]) + '\n'
      else:
        temp_string = str(inp_d[cat_name][kn]) + '  ' + str(kn) + '  ' + str(d_list[i]) + '\n'
      
      file_string += temp_string

    return file_string

  def create_val_un_dict(self, contents, new_dict, temp_key_list, temp_unit_list, key_val, sv = 17):
    """
    INPUT:

    ::

      temp_key_list[0]   temp_key_list[1]   temp_key_list[2]   temp_key_list[3]
      temp_unit_list[0]  temp_unit_list[1]  temp_unit_list[2]  temp_unit_list[3]
            a11                 a12                a13                a14  
            a21                 ...                ...                ...  
            a31                 ...                ...                ...  
            a41                 ...                ...                ...  
            a51                 ...                ...                ...  
            a61                 ...                ...                ...  
            a71                 ...                ...                ...  
            a81                 ...                ...                ...  
    
    OUTPUT:

    ::

      {
        Matrix:
          temp_key_list[0]: 
            Unit: temp_unit_list[0]
            Value:
            - a11
            - a21
            - a31
            - a41
            - a51
            - a61
            - a71
            - a81
          temp_key_list[1]:
            Unit: temp_unit_list[1]
            Value:
            - a12
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
          temp_key_list[2]:
            Unit: temp_unit_list[2]
            Value:
            - a13
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
          temp_key_list[3]:
            Unit: temp_unit_list[3]
            Value:
            - a14
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
      }
    
    Args:
      contents (list):
        - The starting list of text lines to be parsed
      new_dict (dict):
        - The current created dictionary to be added to
      temp_key_list (list):
        - The list of key values to be used for the final output dictionary
      temp_unit_list (list):
        - The list of unit values to be used for the final output dictionary
      key_val (string):
        - The key value to be used to determine how many iterations should be used
      sv (int):
        - The starting line value of the data
    
    Returns:
      temp_dict (dict):
        - The final dictionary containing all the parsed content
    """
    temp_dict = {}
    temp_temp_dict = {}
    for tk in temp_key_list:
      temp_temp_dict[tk] = []

    for i in range(self.convert_value(new_dict[key_val])):
      
      for j, tk in enumerate(temp_key_list):
      
        temp_value = contents[sv+i-1].split()[j]
        temp_temp_dict[tk].append(self.convert_value(temp_value))
        temp_dict[tk] = {
          'Value': temp_temp_dict[tk],
          'Unit': temp_unit_list[j]
        }

    return temp_dict

  def write_val_un_table(self, in_dict, tt_keys, ord_keys, key_val, has_un=True):
    """
    INPUT:

    ::

      {
        Matrix:
          tt_keys[0]: 
            Unit: UNIT0
            Value:
            - a11
            - a21
            - a31
            - a41
            - a51
            - a61
            - a71
            - a81
          tt_keys[1]:
            Unit: UNIT1
            Value:
            - a12
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
          tt_keys[2]:
            Unit: UNIT2
            Value:
            - a13
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
          tt_keys[3]:
            Unit: UNIT3
            Value:
            - a14
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
            - ...
      }

    OUTPUT:

    ::

      ord_keys[0]   ord_keys[1]   ord_keys[2]   ord_keys[3]
        UNIT0         UNIT1         UNIT2         UNIT3
         a11           a12           a13           a14  
         a21           ...           ...           ...  
         a31           ...           ...           ...  
         a41           ...           ...           ...  
         a51           ...           ...           ...  
         a61           ...           ...           ...  
         a71           ...           ...           ...  
         a81           ...           ...           ...  
    
    Args:
      in_dict (dict):
        - The starting dictionary with which to read the values and their respective units
      tt_keys (list):
        - The current un-ordered list of keys 
      ord_keys (list):
        - The ordered list of keys to be used as a reference
      key_val (string):
        - The final key value to be used for the output dictionary
      has_un (bool,default=True)
        - Determines whether or not the input data contains a unit description line or not
    
    Returns:
      end_string (string):
        - The final string to be returned including the output list
    """
    rearrange_list = [0]*len(tt_keys)

    for i,ok in enumerate(ord_keys):
      for _,tk in enumerate(tt_keys):
        if (tk == ok):
          rearrange_list[i] = tk

    end_string = ''
    temp_keys = []
    for i,v in enumerate(rearrange_list):
      temp_keys.append(v)

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
    INPUT:

    ::

                    OutList     - The next line(s) contains a list of output parameters.  See OutListParameters.xlsx for a listing of available output channels, (-)
      "VAL0"                 - DESC0
      "VAL1"                 - DESC1
      "VAL2"                 - DESC2
    
    OUTPUT:

    ::

      {
        OutList:
          '"VAL0"': DESC0
          '"VAL1"': DESC1
          '"VAL2"': DESC2
      }
    
    Args:
      contents (string):
        - The input list of strings to be parsed
      start_ind (int):
        - The line in the file contents where the outlist begins
    
    Returns:
      temp_dict (dict):
        - The final converted dictionary
    """
    end_ind = len(contents)-2
    temp_dict = {}

    for i in range(start_ind,end_ind):
      current_line = contents[i]
      temp_dict[current_line.split('  ')[0]] = current_line.split('-',1)[1].strip()

    return temp_dict

  def write_outlist(self, in_dict):
    """
    INPUT:

    ::

      {
        OutList:
        - KEY0
        - KEY1
        - ...
        - ...
      }

    OUTPUT:

    ::

      OutList     - The next line(s) contains a list of output parameters.  See OutListParameters.xlsx for a listing of available output channels, (-)'
      "in_dict['OutList'][KEY0]"
      "in_dict['OutList'][KEY1]"
      ...
      ...
      END of input file (the word "END" must appear in the first 3 columns of this last OutList line)'
      ---------------------------------------------------------------------------------------'
   
    Args:
      in_dict (dict):
        - The starting dictionary with which to read in the values for the output list
    
    Returns:
      end_string (string):
        - The final string to be returned including the output list
    """
    end_string = ''
    end_string += 'OutList     - The next line(s) contains a list of output parameters.  See OutListParameters.xlsx for a listing of available output channels, (-)\n'
    for outp in in_dict['OutList']:
      end_string += '"'
      end_string += outp
      end_string += '"'
      end_string += '\n'

    end_string += 'END of input file (the word "END" must appear in the first 3 columns of this last OutList line)\n'
    end_string += '---------------------------------------------------------------------------------------\n'

    return end_string

  def write_outlist_kv(self, in_dict, delim):
    """
    INPUT:

    ::

      {
        OutList:
          '"KEY0"': in_dict['OutList'][KEY0]
          '"KEY1"': in_dict['OutList'][KEY1]
          '"..."' : ...
          '"..."' : ...
      }
    
    OUTPUT:

    ::

      OutList     - The next line(s) contains a list of output parameters.  See OutListParameters.xlsx for a listing of available output channels, (-)'
      KEY0 {delim} in_dict['OutList'][KEY0]
      KEY1 {delim} in_dict['OutList'][KEY1]
      ...
      ...
      END of input file (the word "END" must appear in the first 3 columns of this last OutList line)'
      ---------------------------------------------------------------------------------------'
    
    Args:
      in_dict (dict):
        - The starting dictionary with which to read in the values for the output list
      delim (string):
        - The string of characters to be added in between each value in the output list
    
    Returns:
      end_string (string):
        - The final string to be returned including the output list
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

  def create_node_dict(self, new_dict, node_section_start, current_element, temp_dict, num_nodes):
    """
    INPUT:

    ::

      Initial position vectors (IEC coordinate system)
        Element number:    1
        Node Global node          X                 Y                 Z        
        ---- -----------  ----------------- ----------------- -----------------
          1         1             x1                y1                z1
          2         2             x2                y2                z2
          3         3             x3                y3                z3
          4         4             x4                y4                z4
          5         5             x5                y5                z5
          6         6             x6                y6                z6
    
    OUTPUT:

    ::

      {
        Initial position vectors (IEC coordinate system):
          Element Number: 1
          Node Values:
            Node 0:
              X: x1
              Y: y1
              Z: z1          
            Node 1:
              X: x2
              Y: y2
              Z: z2
            Node 2:
              X: x3
              Y: y3
              Z: z3
            Node 3:
              X: x4
              Y: y4
              Z: z4
            Node 4:
              X: x5
              Y: y5
              Z: z5
            Node 5:
              X: x6
              Y: y6
              Z: z6
      }

    Args:
      new_dict (dict):
        - The current already established dictionary to be added to
      node_section_start (int):
        - The line number where the node section begins
      current_element (int):
        - The current element number of the group of nodes to be parsed
      temp_dict (dict):
        - An already created dictionary for storing the nodes and their values
      num_nodes (int):
        - The total number of nodes per element to be parsed
    
    Returns:
      new_dict (dict):
        - The updated dictionary after parsing which is to be updated to the input new_dict
      current_element (int):
        - The most recent element which was parsed to be used in further code
      node_section_start (int):
        - The line number where the final node section begins to be used in further code
    """
    new_dict[self.data[node_section_start].strip()] = {'Element Number':current_element,'Node Values':temp_dict}

    node_section_start = node_section_start+num_nodes+5
    new_dict[self.data[node_section_start].strip()] = {}
    current_element = self.convert_value(self.data[node_section_start+1].split(':')[1].strip())

    return new_dict, current_element, node_section_start
    
  def convert_double_matrix(self, contents, line_start, line_interval, type, num_intervals=0, num_elems=0):
    """
    INPUT:

    ::

      *** type == "station" ***
      VAL1
       a11  a12  a13  a14  a15  a16
       a21  ...  ...  ...  ...  ...
       a31  ...  ...  ...  ...  ...
       a41  ...  ...  ...  ...  ...
       a51  ...  ...  ...  ...  ...
       a61  ...  ...  ...  ...  ...

       b11  b12  b13  b14  b15  b16
       b21  ...  ...  ...  ...  ...
       b31  ...  ...  ...  ...  ...
       b41  ...  ...  ...  ...  ...
       b51  ...  ...  ...  ...  ...
       b61  ...  ...  ...  ...  ...

      VAL2
       a11  a12  a13  a14  a15  a16
       a21  ...  ...  ...  ...  ...
       a31  ...  ...  ...  ...  ...
       a41  ...  ...  ...  ...  ...
       a51  ...  ...  ...  ...  ...
       a61  ...  ...  ...  ...  ...

       b11  b12  b13  b14  b15  b16
       b21  ...  ...  ...  ...  ...
       b31  ...  ...  ...  ...  ...
       b41  ...  ...  ...  ...  ...
       b51  ...  ...  ...  ...  ...
       b61  ...  ...  ...  ...  ...

      *** type == "point" ***
      Quadrature point number:    1
          a11  a12  a13  a14  a15  a16
          a21  ...  ...  ...  ...  ...
          a31  ...  ...  ...  ...  ...
          a41  ...  ...  ...  ...  ...
          a51  ...  ...  ...  ...  ...
          a61  ...  ...  ...  ...  ...

          b11  b12  b13  b14  b15  b16
          b21  ...  ...  ...  ...  ...
          b31  ...  ...  ...  ...  ...
          b41  ...  ...  ...  ...  ...
          b51  ...  ...  ...  ...  ...
          b61  ...  ...  ...  ...  ...

      Quadrature point number:    2
          a11  a12  a13  a14  a15  a16
          a21  ...  ...  ...  ...  ...
          a31  ...  ...  ...  ...  ...
          a41  ...  ...  ...  ...  ...
          a51  ...  ...  ...  ...  ...
          a61  ...  ...  ...  ...  ...

          b11  b12  b13  b14  b15  b16
          b21  ...  ...  ...  ...  ...
          b31  ...  ...  ...  ...  ...
          b41  ...  ...  ...  ...  ...
          b51  ...  ...  ...  ...  ...
          b61  ...  ...  ...  ...  ...
    
    OUTPUT:

    ::

      {
        VAL1:
          Stiffness Matrix:
          - matrix1_row1:
            - a11
            - a12
            - a13
            - a14
            - a15
            - a16
          - matrix1_row2:
            - a21
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix1_row3:
            - a31
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix1_row4:
            - a41
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix1_row5:
            - a51
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix1_row6:
            - a61
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix2_row1:
            - b11
            - b12
            - b13
            - b14
            - b15
            - b16
          - matrix2_row2:
            - b21
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix2_row3:
            - b31
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix2_row4:
            - b41
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix2_row5:
            - b51
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix2_row6:
            - b61
            - ...
            - ...
            - ...
            - ...
            - ...

        VAL2:
          Stiffness Matrix:
          - matrix1_row1:
            - a11
            - a12
            - a13
            - a14
            - a15
            - a16
          - matrix1_row2:
            - a21
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix1_row3:
            - a31
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix1_row4:
            - a41
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix1_row5:
            - a51
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix1_row6:
            - a61
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix2_row1:
            - b11
            - b12
            - b13
            - b14
            - b15
            - b16
          - matrix2_row2:
            - b21
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix2_row3:
            - b31
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix2_row4:
            - b41
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix2_row5:
            - b51
            - ...
            - ...
            - ...
            - ...
            - ...
          - matrix2_row6:
            - b61
            - ...
            - ...
            - ...
            - ...
            - ...
      }

    Args:
      contents (list):
        - The file contents to be parsed
      line_start (int):
        - The line number to begin parsing
      line_interval (int):
        - The space between groups of data
      type (string):
        - The type of double matrix being parsed (represent two slightly different styles)
      num_intervals (int,default=0)
        - The number of spaces between groups of data
      num_elems (int,default=0)
        - The total number of extra groups of data per group
    
    Returns:
      temp_dict (dict):
        - The final converted dictionary
      line_num (int):
        - The new line number to resume parsing the data
    """
    temp_dict = {}

    if (type=='station'):
    
      itter_cond = line_start-1,(line_start+line_interval*num_intervals)-1,line_interval
    
    elif (type == 'point'):
      
      itter_cond = line_start-1,(line_start+line_interval*num_elems)-1,line_interval

    for line_num in range(itter_cond):
      
      if (type=='station'):

        station_loc = self.convert_value(contents[line_num].strip())

      elif (type == 'point'):

        station_loc = self.convert_value(contents[line_num].split(':')[1].strip())
      
      current_row = 1
      temp_temp_dict = {}
      temp_temp_dict['Stiffness Matrix'] = []

      for j in range(1,7):
        
        current_mat = 'matrix1'
        current_name = current_mat + '_row' + str(current_row)
        temp_row_vals = self.convert_value(contents[line_num+j].split())      
        temp_temp_dict['Stiffness Matrix'].append({current_name: temp_row_vals})
        current_row += 1

      current_row = 1

      for j in range(8,14):
        
        current_mat = 'matrix2'
        current_name = current_mat + '_row' + str(current_row)
        temp_row_vals = self.convert_value(contents[line_num+j].split())      
        temp_temp_dict['Stiffness Matrix'].append({current_name: temp_row_vals})
        current_row += 1   

      temp_dict[station_loc] = temp_temp_dict

    return temp_dict, line_num

  def parse_mulitple_first(self, contents, key_val, num_entry, line_start):
    """
    INPUT: 

    ::

      ...
      "VAL1"    key_val      - DESC
      "VAL2"
      "VAL3"
      "VAL4"
      "VAL5"
      ...

    OUTPUT: 

    ::

      {
        key_val:
          - 'VAL1'
          - 'VAL2'
          - 'VAL3'
          - 'VAL4'
          - 'VAL5'
      }

    Args:
      contents (list):
        - The file contents to be parsed
      key_val (string):
        - The current key value to be used (the one with multiple values)
      num_entry (int):
        - The number of total values to be added to the relative key in the dictionary
      line_start (int):
        - The line number where the data to be parsed occurs
    
    Returns:
      final_string (string):
        - The final string to be outputted 
    """
    temp_dict = {}
    temp_dict[key_val] = []
    temp_dict[key_val].append(contents[line_start].split('  ')[0].strip())

    if (num_entry > 1):

      for ln in range(line_start+1,line_start+num_entry):
        temp_dict[key_val].append(contents[ln].strip())

    return temp_dict

  def write_multiple_first(self, contents, key_val, desc_val):
    """
    INPUT: 

    ::

      {
        key_val:
          - 'VAL1'
          - 'VAL2'
          - 'VAL3'
          - 'VAL4'
          - 'VAL5'
      }

    OUTPUT: 

    ::

      "VAL1"    key_val      - desc_val
      "VAL2"
      "VAL3"
      "VAL4"
      "VAL5"

    Args:
      contents (list):
        - The file contents to be parsed
      key_val (string):
        - The current key value to be used (the one with multiple values)
      desc_val (string):
        - The description associated with the current key value
    
    Returns:
      final_string (string):
        - The final string to be outputted 
    """
    temp_string = ''
    final_string = ''
    temp_string = contents[key_val][0] + '  ' + key_val + '  ' + desc_val + '\n'
    final_string += temp_string

    for ts in contents[key_val][1:]:
      final_string += ts
      final_string += '\n'

    return final_string

  def create_comma_dict(self, matching_list):
    """
    INPUT: 

    ::

      VAL1, VAL2, VAL3, VAL4    KEY_VALUE        - DESC
    
    OUTPUT:

    ::

      {
        KEY_VALUE: [VAL1, VAL2, VAL3, VAL4]
      }

    Args:
      matching_list (list):
        - A list of lines to be converted
    
    Returns:
      temp_dict (dict):
        - The final converted dictionary 
    """
    temp_dict = {}
    for mk in matching_list:
      matching = list(filter(lambda x: mk in x, self.data))
      # Make this better
      try:
        temp_ln = matching[1].split(mk)[0].split(',')
      except:
        temp_ln = matching[0].split(mk)[0].split(',')
      final_ln = [self.convert_value(ln.strip()) for ln in temp_ln]
      temp_dict[mk] = final_ln

    return temp_dict

  def create_outlist_multiple(self, contents, current_ind):
    """
    INPUT: 

    ::

      ...
              OutList        - DESC
      "VAL1, VAL2"                             
      "VAL3, VAL4, VAL5"  
      "VAL6"
      ...

    OUTPUT: 

    ::

      {
        OutList: [VAL1, VAL2, VAL3, VAL4, VAL5, VAL6]
      }

    Args:
      contents (list):
        - The file contents to be parsed
      current_ind (int):
        - The current line of the file contents to be parsed
    
    Returns:
      temp_dict (dict):
        - The final converted dictionary 
    """
    temp_dict = {}
    outlist_param = []
    while (contents[current_ind][0] == '"'):
      outlist_param.append(contents[current_ind].strip())
      current_ind += 1
    
    # Add values to the list
    outlist_temp = []
    [outlist_temp.append(ele.split(',')) for ele in outlist_param]
    # Flatten list
    outlist_temp = sum(outlist_temp, [])
    
    # Remove junk from each element in the list
    outlist_final = []
    [outlist_final.append(ele.strip().replace('"',''))  for ele in outlist_temp]
    
    temp_dict['OutList'] = outlist_final 

    return temp_dict

  def write_comma_list(self, contents, key_val, desc_val):
    """
    INPUT: 

    ::

      {
        ...
        key_val: [VAL1, VAL2, VAL3, VAL4]
        ...
      }

    OUTPUT:

    ::

      VAL1, VAL2, VAL3, VAL4    key_val        - desc_val
    
    Args:
      contents (list):
        - The file contents to be parsed
      key_val (string):
        - The current key value to be used (the one with multiple values)
      desc_val (string):
        - The description associated with the current key value
    
    Returns:
      final_string (string):
        - The final string to be outputted 
    """
    final_string = ''
    for i,num in enumerate(contents[key_val]):
      if (i != len(contents[key_val])-1):
        temp_string = str(num) + ',  '
        final_string += temp_string
      else:
        temp_string = str(num) + '  ' + key_val + '  ' + desc_val + '\n'
        final_string += temp_string

    return final_string
