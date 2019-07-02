import unittest
import sys
sys.path.append("..")
from src.base_file import BaseFile

class TestBaseFile(unittest.TestCase):

  def test_is_float(self):
    # Build up the baseline objects
    baseline_value1 = '1.2'
    baseline_value2 = '1'
    baseline_value3 = 's'
    
    # Assertions - test that various strings can be converted to a float
    self.assertEqual(BaseFile.is_float(BaseFile(''),baseline_value1), True)
    self.assertEqual(BaseFile.is_float(BaseFile(''),baseline_value2), True)
    self.assertEqual(BaseFile.is_float(BaseFile(''),baseline_value3), False)

  def test_is_int(self):
    # Build up the baseline objects
    baseline_value1 = '1.2'
    baseline_value2 = '1'
    baseline_value3 = 's'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.is_int(BaseFile(''),baseline_value1), False)
    self.assertEqual(BaseFile.is_int(BaseFile(''),baseline_value2), True)
    self.assertEqual(BaseFile.is_int(BaseFile(''),baseline_value3), False)

  def test_convert_value(self):
    # Build up the baseline objects
    baseline_value1 = '1.2'
    baseline_value2 = '1'
    baseline_value3 = 's'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.convert_value(BaseFile(''),baseline_value1), 1.2)
    self.assertEqual(BaseFile.convert_value(BaseFile(''),baseline_value2), 1)
    self.assertEqual(BaseFile.convert_value(BaseFile(''),baseline_value3), 's')

  def test_combine_text(self):
    # Build up the baseline objects
    baseline_list = ['1','2','3']
    baseline_sep = ' a '
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.combine_text(BaseFile(''),baseline_list,baseline_sep), '1 a 2 a 3')

  def test_combine_text_spaces(self):
    # Build up the baseline objects
    baseline_list = ['1','2','3']
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.combine_text_spaces(BaseFile(''),baseline_list), '1 2 3')

  def test_remove_char(self):
    # Build up the baseline objects
    baseline_list = '12345'
    baseline_c = ['2','5']
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.remove_char(BaseFile(''),baseline_list,baseline_c), '134')

  def test_remove_parens(self):
    # Build up the baseline objects
    baseline_list = '12()(345)'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.remove_parens(BaseFile(''),baseline_list), '12345')

  def test_remove_brackets(self):
    # Build up the baseline objects
    baseline_list = '12[]]345]'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.remove_brackets(BaseFile(''),baseline_list), '12345')

  def test_split_line(self):
    # Build up the baseline objects
    baseline_list = '1 :2 : 3   :   56'
    delim = ':'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.split_line(BaseFile(''),baseline_list,delim), ['1','2','3','56'])

  def test_split_line_spaces(self):
    # Build up the baseline objects
    baseline_list = '1 2  3      56'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.split_line_spaces(BaseFile(''),baseline_list), ['1 2','3','56'])

  def test_sep_string(self):
    # Build up the baseline objects
    baseline_list = '1 /     7'
    delim = '/'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.sep_string(BaseFile(''),baseline_list,delim), ('1','7'))

  def test_sep_string_double(self):
    # Build up the baseline objects
    baseline_list = '1 /     7 >     2'
    delim1 = '/'
    delim2 = '>'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.sep_string_double(BaseFile(''),baseline_list,delim1,delim2), ('1','7','2'))

  def test_capitalize_list(self):
    # Build up the baseline objects
    baseline_list = ['abc','aBC','Abc','ABC']
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.capitalize_list(BaseFile(''),baseline_list), ['Abc','Abc','Abc','Abc'])

  def test_remove_whitespace(self):
    # Build up the baseline objects
    baseline_list = '1 2     4  5    6'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.remove_whitespace(BaseFile(''),baseline_list), ['1 2',' 4','5','6'])

  def test_remove_whitespace_filter(self):
    # Build up the baseline objects
    baseline_list = '1 2  4'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.remove_whitespace_filter(BaseFile(''),baseline_list), ['1',' ','2',' ',' ','4'])

  def test_parse_type1(self):
    # Build up the baseline objects
    baseline_list = '5    fish    - here it is'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.parse_type1(BaseFile(''),baseline_list), ('fish', {'Value': 5, 'Description': 'here it is'}))

  def test_parse_filename(self):
    # Build up the baseline objects
    filename1 = 'a.inp'
    filename2 = 'a.sum'
    filename3 = 'a.inp.sum'
    filename4 = 'a.out'
    filename5 = 'a.log'
    filename6 = 'a.inp.ech'
    filename7 = 'a.yml'
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.parse_filename(BaseFile(''),filename1,'.inp','.yml'), 'a_inp.yml')
    self.assertEqual(BaseFile.parse_filename(BaseFile(''),filename2,'.sum','.yml'), 'a_sum.yml')
    self.assertEqual(BaseFile.parse_filename(BaseFile(''),filename3,'.inp.sum','.yml'), 'a_inpsum.yml')
    self.assertEqual(BaseFile.parse_filename(BaseFile(''),filename4,'.out','.yml'), 'a_out.yml')
    self.assertEqual(BaseFile.parse_filename(BaseFile(''),filename5,'.log','.yml'), 'a_log.yml')
    self.assertEqual(BaseFile.parse_filename(BaseFile(''),filename6,'.inp.ech','.yml'), 'a_inpech.yml')
    self.assertEqual(BaseFile.parse_filename(BaseFile(''),filename7,'.yml','.inp'), 'a.inp')

  def test_parse_filetype_valuefirst(self):
    # Build up the baseline objects
    baseline_contents = [
      'a\n',
      'b  c  - d\n',
      'e  f  - g\n',
      'h\n',
      'i\n',
      'j  k  - l\n',
      'm  n  - o\n',
      'p  q  - r\n'
    ]
    baseline_keys = ['c','f','k','n','q']
    baseline_sec_start = [1,5]
    baseline_length = [1,3]
    check_dict = {
      'c':'b',
      'f':'e',
      'k':'j',
      'n':'m',
      'q':'p'
    }

    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.parse_filetype_valuefirst(BaseFile(''),baseline_contents,baseline_keys,baseline_sec_start,baseline_length), check_dict)

  def test_parse_xyz(self):
    # Build up the baseline objects
    baseline_string = [
      'Wind Value\n',
      'W  1  2   3\n',
      'W  4  5   6\n',
      'W  7  8   9\n',
      'W  10  11   12\n',
      'W  13  14   15\n',
      'W  16  17   18\n',
      'W  19  20   21\n'
    ]
    baseline_startd = 1
    baseline_starti = 1
    baseline_loops = 7
    baseline_key = 'W'
    check_dict = {
      'W0': {'X': 1, 'Y': 2, 'Z': 3},
      'W1': {'X': 4, 'Y': 5, 'Z': 6},
      'W2': {'X': 7, 'Y': 8, 'Z': 9},
      'W3': {'X': 10, 'Y': 11, 'Z': 12},
      'W4': {'X': 13, 'Y': 14, 'Z': 15},
      'W5': {'X': 16, 'Y': 17, 'Z': 18},
      'W6': {'X': 19, 'Y': 20, 'Z': 21}
    }
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.parse_xyz(BaseFile(''),baseline_string,baseline_startd,baseline_starti,baseline_loops,baseline_key), check_dict)

  def test_write_valdesc(self):
    # Build up the baseline objects
    baseline_dict = {}
    baseline_keys = []
    baseline_desc = []
    baseline_cats = []
    check_string = ''
    
    # Assertions - test that various strings can be converted to an integer
    self.assertEqual(BaseFile.write_valdesc(BaseFile(''),baseline_dict,baseline_keys,baseline_desc,baseline_cats), check_string)


if __name__ == '__main__':
  unittest.main()

