import unittest
import sys
sys.path.append("..")
import os
from src.base_file import BaseFile

class TestBaseFile(unittest.TestCase):

  def test_open_file(self):
    # Build up the baseline objects
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_primary.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)
    new_file = os.path.join(baseline_pd,baseline_fn)
    op = BaseFile.open_file(baseline_case,new_file)
    self.assertEqual(op.name, new_file)
    op.close()

  def test_load_yaml(self):
    # Build up the baseline objects
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)
    self.assertNotEqual(baseline_case.data, None)

  def test_load_openfast(self):
    # Build up the baseline objects
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    baseline_pd = os.path.join(baseline_pd,'initial_input_files')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.inp'
    baseline_case = BaseFile(baseline_pd,baseline_fn)
    self.assertNotEqual(baseline_case.data, None)

  def test_to_yaml(self):
    # Build up the baseline objects
    baseline_pd = os.path.dirname(os.path.realpath(__file__))
    baseline_dict = {
      'key0':'val0',
      'key1':'val1',
      'key2':'val2',
      'key3':'val3',
    }
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'temp_file.yml'
    temp_f = open(os.path.join(baseline_pd,baseline_fn),'w+')
    baseline_case = BaseFile(baseline_pd,baseline_fn)
    BaseFile.to_yaml(baseline_case,baseline_dict)
    
    line_list = [
      'key0: val0\n',
      'key1: val1\n',
      'key2: val2\n',
      'key3: val3\n'
    ]
    ttf = open(baseline_fn,'r')
    for i,line in enumerate(ttf):
      self.assertEqual(line, line_list[i])
    ttf.close()

    temp_f.close()
    os.remove(baseline_fn)

  def test_to_text(self):
    # Build up the baseline objects
    baseline_pd = os.path.dirname(os.path.realpath(__file__))
    baseline_string = 'key0: val0\nkey1: val1\nkey2: val2\nkey3: val3\n'
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'test_file.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)
    BaseFile.to_text(baseline_case,baseline_string)
    
    line_list = [
      'key0: val0\n',
      'key1: val1\n',
      'key2: val2\n',
      'key3: val3\n'
    ]
    ttf = open(os.path.join(baseline_pd,baseline_fn),'r')
    for i,line in enumerate(ttf):
      self.assertEqual(line, line_list[i])
    ttf.close()

  def test_is_float(self):
    # Build up the baseline objects
    baseline_value1 = '1.2'
    baseline_value2 = '1'
    baseline_value3 = 's'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.is_float(baseline_case,baseline_value1), True)
    self.assertEqual(BaseFile.is_float(baseline_case,baseline_value2), True)
    self.assertEqual(BaseFile.is_float(baseline_case,baseline_value3), False)

  def test_is_int(self):
    # Build up the baseline objects
    baseline_value1 = '1.2'
    baseline_value2 = '1'
    baseline_value3 = 's'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.is_int(baseline_case,baseline_value1), False)
    self.assertEqual(BaseFile.is_int(baseline_case,baseline_value2), True)
    self.assertEqual(BaseFile.is_int(baseline_case,baseline_value3), False)

  def test_convert_value(self):
    # Build up the baseline objects
    baseline_value1 = '1.2'
    baseline_value2 = '1'
    baseline_value3 = 's'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.convert_value(baseline_case,baseline_value1), 1.2)
    self.assertEqual(BaseFile.convert_value(baseline_case,baseline_value2), 1)
    self.assertEqual(BaseFile.convert_value(baseline_case,baseline_value3), 's')

  def test_combine_text(self):
    # Build up the baseline objects
    baseline_list = ['1','2','3']
    baseline_sep = ' a '
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.combine_text(baseline_case,baseline_list,baseline_sep), '1 a 2 a 3')

  def test_combine_text_spaces(self):
    # Build up the baseline objects
    baseline_list = ['1','2','3']
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.combine_text_spaces(baseline_case,baseline_list), '1 2 3')

  def test_remove_char(self):
    # Build up the baseline objects
    baseline_list = '12345'
    baseline_c = ['2','5']
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.remove_char(baseline_case,baseline_list,baseline_c), '134')

  def test_remove_parens(self):
    # Build up the baseline objects
    baseline_list = '12()(345)'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.remove_parens(baseline_case,baseline_list), '12345')

  def test_remove_brackets(self):
    # Build up the baseline objects
    baseline_list = '12[]]345]'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.remove_brackets(baseline_case,baseline_list), '12345')

  def test_split_line(self):
    # Build up the baseline objects
    baseline_list = '1 :2 : 3   :   56'
    delim = ':'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.split_line(baseline_case,baseline_list,delim), ['1','2','3','56'])

  def test_split_line_spaces(self):
    # Build up the baseline objects
    baseline_list = '1 2  3      56'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.split_line_spaces(baseline_case,baseline_list), ['1 2','3','56'])

  def test_sep_string(self):
    # Build up the baseline objects
    baseline_list = '1 /     7'
    delim = '/'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.sep_string(baseline_case,baseline_list,delim), ('1','7'))

  def test_sep_string_double(self):
    # Build up the baseline objects
    baseline_list = '1 /     7 >     2'
    delim1 = '/'
    delim2 = '>'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.sep_string_double(baseline_case,baseline_list,delim1,delim2), ('1','7','2'))

  def test_capitalize_list(self):
    # Build up the baseline objects
    baseline_list = ['abc','aBC','Abc','ABC']
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.capitalize_list(baseline_case,baseline_list), ['Abc','Abc','Abc','Abc'])

  def test_remove_whitespace(self):
    # Build up the baseline objects
    baseline_list = '1 2     4  5    6'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.remove_whitespace(baseline_case,baseline_list), ['1 2',' 4','5','6'])

  def test_remove_whitespace_filter(self):
    # Build up the baseline objects
    baseline_list = '1 2  4'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.remove_whitespace_filter(baseline_case,baseline_list), ['1',' ','2',' ',' ','4'])

  def test_parse_type1(self):
    # Build up the baseline objects
    baseline_list = '5    fish    - here it is'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.parse_type1(baseline_case,baseline_list), ('fish', {'Value': 5, 'Description': 'here it is'}))

  def test_parse_filename(self):
    # Build up the baseline objects
    filename1 = 'a.inp'
    filename2 = 'a.sum'
    filename3 = 'a.inp.sum'
    filename4 = 'a.out'
    filename5 = 'a.log'
    filename6 = 'a.inp.ech'
    filename7 = 'a.yml'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.parse_filename(baseline_case,filename1,'.inp','.yml'), 'a_inp.yml')
    self.assertEqual(BaseFile.parse_filename(baseline_case,filename2,'.sum','.yml'), 'a_sum.yml')
    self.assertEqual(BaseFile.parse_filename(baseline_case,filename3,'.inp.sum','.yml'), 'a_inpsum.yml')
    self.assertEqual(BaseFile.parse_filename(baseline_case,filename4,'.out','.yml'), 'a_out.yml')
    self.assertEqual(BaseFile.parse_filename(baseline_case,filename5,'.log','.yml'), 'a_log.yml')
    self.assertEqual(BaseFile.parse_filename(baseline_case,filename6,'.inp.ech','.yml'), 'a_inpech.yml')
    self.assertEqual(BaseFile.parse_filename(baseline_case,filename7,'.yml','.inp'), 'a.inp')

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
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.parse_filetype_valuefirst(baseline_case,baseline_contents,baseline_keys,baseline_sec_start,baseline_length), check_dict)

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
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.parse_xyz(baseline_case,baseline_string,baseline_startd,baseline_starti,baseline_loops,baseline_key), check_dict)

  def test_write_valdesc(self):
    # Build up the baseline objects
    baseline_dict1 = {
      'fish':{
        'key0':'desc0',
        'key1':'desc1',
        'key2':'desc2',
        'key3':'desc3',
        'key4':'desc4',
        'key5':'desc5'
      },
      'apple':{
        'key00':'desc00',
        'key01':'desc01',
        'key02':'desc02'
      }
    }
    baseline_dict2 = {
      'key0':'desc0',
      'key1':'desc1',
      'key2':'desc2',
      'key3':'desc3',
      'key4':'desc4',
      'key5':'desc5'
    }
    baseline_keys = ['key1','key2','key4']
    baseline_desc = ['desc1','desc2','desc4']
    baseline_cats1 = 'fish'
    baseline_cats2 = None
    check_string = 'desc1  key1  desc1\ndesc2  key2  desc2\ndesc4  key4  desc4\n'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Temp parent directory to instantiate a case of BaseFile
    baseline_pd = dir_path.replace('tests','bd_5MW_dynamic')
    # Temp filename to instantiate a case of BaseFile
    baseline_fn = 'bd_driver.yml'
    baseline_case = BaseFile(baseline_pd,baseline_fn)

    self.assertEqual(BaseFile.write_valdesc(baseline_case,baseline_dict1,baseline_keys,baseline_desc,baseline_cats1), check_string)
    self.assertEqual(BaseFile.write_valdesc(baseline_case,baseline_dict2,baseline_keys,baseline_desc,baseline_cats2), check_string)

def tearDownModule():
    # Clean up and remove all temporary files
    os.remove('test_file.inp')


if __name__ == '__main__':
  unittest.main()


