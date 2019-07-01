# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 19, 2019

import sys
import yaml
from src.base_file import BaseFile

class BeamdynFile(BaseFile):
  """
  Super class for all BeamDyn-related files.
  """
  def __init__(self, filename):

    try:

      super().__init__(filename)
      file_ext = filename.split('.',1)[1]
      output_filename = self.parse_filename(filename,'.'+file_ext,'.yml')
      self.init_output_file(output_filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

class BeamdynPrimaryFile(BeamdynFile):
  """
  Primary input file for BeamDyn.
  """

  def __init__(self, filename):

    try:

      super().__init__(filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def read(self):

    new_dict = {}

    key_list = [
      'Echo',
      'QuasiStaticInit',
      'rhoinf',
      'quadrature',
      'refine',
      'n_fact',
      'DTBeam',
      'load_retries',
      'NRMax',
      'stop_tol',
      'tngt_stf_fd',
      'tngt_stf_comp',
      'tngt_stf_pert',
      'tngt_stf_difftol',
      'RotStates',
      'member_total',
      'kp_total',    
      '49',             # May need in the future          
      'order_elem',
      'BldFile',
      'UsePitchAct',
      'PitchJ',     
      'PitchK',     
      'PitchC',     
      'SumPrint',   
      'OutFmt',     
      'NNodeOuts'
    ]

    matching = list(filter(lambda x: 'kp_total' in x, self.data))
    data_length = self.convert_value(matching[0].split()[0])
    sec_start_list = [3,19,data_length+25,data_length+27,data_length+29,data_length+34]
    length_list = [14,3,1,1,4,3]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)
    
    temp_line = self.data[data_length+37]
    temp_list = temp_line.split('  ')
    temp_list = list(filter(None, temp_list))
    beg_list = ' '.join(temp_list[0:-3])

    new_dict[temp_list[-3].strip()] = beg_list

    temp_key_list = self.data[22].split()
    temp_unit_list = self.remove_parens(self.data[23].split())
    
    temp_dict = {}
    temp_temp_dict = {}
    for tk in temp_key_list:
      temp_temp_dict[tk] = []

    for i in range(self.convert_value(new_dict['kp_total'])):
      
      for j, tk in enumerate(temp_key_list):
      
        temp_value = self.data[25+i-1].split()[j]
        temp_temp_dict[tk].append(self.convert_value(temp_value))
        temp_dict[tk] = {
          'Value': temp_temp_dict[tk],
          'Unit': temp_unit_list[j]
        }

    new_dict['Matrix'] = temp_dict

    ci = 5
    outlist_param = []
    while (self.data[sec_start_list[-1]+ci][0] == '"'):
      outlist_param.append(self.data[sec_start_list[-1]+ci].strip())
      ci += 1
    
    # Add values to the list
    outlist_temp = []
    [outlist_temp.append(ele.split(',')) for ele in outlist_param]
    # Flatten list
    outlist_temp = sum(outlist_temp, [])
    
    # Remove junk from each element in the list
    outlist_final = []
    [outlist_final.append(ele.strip().replace('"',''))  for ele in outlist_temp]
    
    new_dict['OutList'] = outlist_final 

    return new_dict


class BeamdynBladeFile(BeamdynFile):
  """
  BeamDyn file decsribing a blade.
  """

  def __init__(self, filename):

    try: 
    
      super().__init__(filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def read(self):

    new_dict = {}

    key_list = [
      'station_total',
      'damp_type'
    ]

    sec_start_list = [3]
    length_list = [1]
    
    temp_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)
    new_dict['Blade Parameters'] = temp_dict
    
    temp_key_list = self.data[6].split()
    temp_quant_list = self.data[7].split()
    temp_val_list = self.convert_value(self.data[8].split())
    temp_dict = {}

    for i, tk in enumerate(temp_key_list):

      temp_dict[tk+temp_quant_list[i]] = temp_val_list[i] 

    new_dict['Damping Coefficient'] = temp_dict 

    line_start = 11
    line_interval = 15
    num_intervals = self.convert_value(new_dict['Blade Parameters']['station_total'])
    temp_dict = {}

    for line_num in range(line_start-1,(line_start+line_interval*num_intervals)-1,line_interval):
      
      station_loc = self.convert_value(self.data[line_num].strip())
      current_row = 1
      temp_temp_dict = {}
      temp_temp_dict['Stiffness Matrix'] = []

      for j in range(1,7):
        
        current_mat = 'matrix1'
        current_name = current_mat + '_row' + str(current_row)
        temp_row_vals = self.convert_value(self.data[line_num+j].split())      
        temp_temp_dict['Stiffness Matrix'].append({current_name: temp_row_vals})
        current_row += 1

      current_row = 1

      for j in range(8,14):
        
        current_mat = 'matrix2'
        current_name = current_mat + '_row' + str(current_row)
        temp_row_vals = self.convert_value(self.data[line_num+j].split())      
        temp_temp_dict['Stiffness Matrix'].append({current_name: temp_row_vals})
        current_row += 1   

      temp_dict[station_loc] = temp_temp_dict

    new_dict['Distributed Properties'] = temp_dict

    return new_dict


class BeamdynInputFile(BeamdynFile):
  """
  BeamDyn file decsribing the inputs.
  """

  def __init__(self, filename):

    try: 
    
      super().__init__(filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def read(self):

    new_dict = {}

    key_list = [
      'DynamicSolve',
      't_initial',
      't_final',
      'dt',
      'Gx',
      'Gy',
      'Gz',
      'GlbPos(1)',
      'GlbPos(2)',
      'GlbPos(3)',
      'GlbRotBladeT0',
      'RootVel(4)',
      'RootVel(5)',
      'RootVel(6)',
      'DistrLoad(1)',
      'DistrLoad(2)',
      'DistrLoad(3)',
      'DistrLoad(4)',
      'DistrLoad(5)',
      'DistrLoad(6)',
      'TipLoad(1)',
      'TipLoad(2)',
      'TipLoad(3)',
      'TipLoad(4)',
      'TipLoad(5)',
      'TipLoad(6)',
      'NumPointLoads',
      'InputFile'
    ]

    sec_start_list = [3,8,12,20,22,26,42]
    length_list = [3,3,3,1,3,13,1]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)
    
    matrix_rows = self.convert_value(self.data[15].split('(')[1].split(',')[0])
    # matrix_cols = self.data[15].split('(')[1].split(',')[1][0]
    temp_dict = {}
    
    for i,ln in enumerate(range(17,17+matrix_rows)):

      matrix_vals = self.convert_value(self.data[ln].split())
      temp_dict['Row_'+str(i+1)] = matrix_vals
      
    new_dict['Matrix'] = temp_dict

    return new_dict

class BeamdynInputSummaryFile(BeamdynFile):
  """
  BeamDyn file decsribing the summary of the input file.
  """

  def __init__(self, filename):

    try: 
    
      super().__init__(filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def read(self):

    new_dict = {}

    temp_key_list = [
      'Blade center of mass (IEC coords)', 
      'Blade mass moment of inertia', 
      'Global position vector (IEC coords)',
      'Global rotation tensor (IEC coords)',
      'Initial blade orientation tensor (relative to global rotation tensor)',
      'Global rotation WM parameters (IEC coords)',
      'Gravity vector (m/s^2) (IEC coords)'
    ]

    line_start_list = [5,7,11,13,17,21,23]
    temp_length_list = [1,3,1,3,3,1,1]

    line_list = [2,3]

    for ln in line_list:

      temp_val = self.convert_value(self.data[ln].split('  ')[-1].strip())
      temp_value_list = self.data[ln].split('  ')
      temp_value_list = list(filter(None, temp_value_list))
      temp_unit = self.remove_parens(temp_value_list[-2].strip())
      new_dict[self.data[ln].split('  ')[0]] = {'Value':temp_val,'Unit':temp_unit}
    
    for i,tk in enumerate(temp_key_list):
      
      temp_dict = {}
      
      for j in range(temp_length_list[i]):
      
        current_row = 'Row' + str(j)
        current_line = line_start_list[i] + j
        temp_dict[current_row] = self.convert_value(self.data[current_line].strip().split())
      
      new_dict[tk] = temp_dict

    temp_key_list = [
      'Analysis type',                                          
      'Numerical damping parameter',                            
      'Time increment',                                         
      'Maximum number of iterations in Newton-Raphson solution',
      'Convergence parameter',                                  
      'Factorization frequency in Newton-Raphson solution',     
      'Quadrature method',                                      
      'FE mesh refinement factor',                              
      'Number of elements',                                     
      'Number of nodes'
    ]    

    dev_count = 0
    for i,tk in enumerate(temp_key_list):

      if (tk in self.data[24+i-dev_count]):
        new_dict[tk] = self.convert_value(self.data[24+i-dev_count].split('  ')[-1].strip())                         
      else:
        dev_count += 1

    node_section_start = 35-dev_count
    new_dict[self.data[node_section_start].strip()] = {}
    current_element = self.convert_value(self.data[node_section_start+1].split(':')[1].strip())
    
    num_nodes = new_dict['Number of nodes']

    temp_dict = self.parse_xyz(self.data,node_section_start+4,2,num_nodes,'Node ')
    new_dict[self.data[node_section_start].strip()] = {'Element Number':current_element,'Node Values':temp_dict}

    node_section_start = node_section_start+num_nodes+5
    new_dict[self.data[node_section_start].strip()] = {}
    current_element = self.convert_value(self.data[node_section_start+1].split(':')[1].strip())
    
    temp_dict = {}

    for i in range(num_nodes):

      cl_split = self.remove_whitespace(self.data[node_section_start+4+i])
      x_val = self.convert_value(cl_split[2].strip())
      y_val = self.convert_value(cl_split[3].strip())
      z_val = self.convert_value(cl_split[4].strip())
      temp_dict['Node '+str(i)] = {'WM_x':x_val,'WM_y':y_val,'WM_z':z_val}

    new_dict[self.data[node_section_start].strip()] = {'Element Number':current_element,'Node Values':temp_dict}

    node_section_start = node_section_start+num_nodes+5
    new_dict[self.data[node_section_start].strip()] = {}
    current_element = self.convert_value(self.data[node_section_start+1].split(':')[1].strip())
    
    in_file = '/'.join(self.filename.split('/')[:-1]) + '/bd_primary_inp.yml'
    in_dict = yaml.load(open(in_file))

    # TODO: How do I find the right value to use?
    num_elems = in_dict['kp_total']

    if (num_elems > num_nodes):
      
      try:

        temp_dict = self.parse_xyz(self.data,node_section_start+4,2,num_elems,'QP ')
      
      except:

        num_elems = num_nodes
        temp_dict = self.parse_xyz(self.data,node_section_start+4,2,num_elems,'QP ')

    else:

      try:

        num_elems = num_nodes
        temp_dict = self.parse_xyz(self.data,node_section_start+4,2,num_elems,'QP ')
      
      except:

        temp_dict = self.parse_xyz(self.data,node_section_start+4,2,num_elems,'QP ')

    new_dict[self.data[node_section_start].strip()] = {'Element Number':current_element,'Node Values':temp_dict}

    node_section_start = node_section_start+num_elems+5
    new_dict[self.data[node_section_start].strip()] = {}
    current_element = self.convert_value(self.data[node_section_start+1].split(':')[1].strip())
    
    temp_dict = {}

    for i in range(num_elems):

      cl_split = self.remove_whitespace(self.data[node_section_start+4+i])
      x_val = self.convert_value(cl_split[2].strip())
      y_val = self.convert_value(cl_split[3].strip())
      z_val = self.convert_value(cl_split[4].strip())
      temp_dict['QP '+str(i)] = {'WM_x':x_val,'WM_y':y_val,'WM_z':z_val}

    new_dict[self.data[node_section_start].strip()] = {'Element Number':current_element,'Node Values':temp_dict}

    node_section_start = node_section_start+num_elems + 5
    new_header = self.data[node_section_start].strip()
    line_start = node_section_start + 3
    line_interval = 15
    temp_dict = {}
    
    for line_num in range(line_start-1,(line_start+line_interval*num_elems)-1,line_interval):
      
      point_num = self.convert_value(self.data[line_num].split(':')[1].strip())
      current_row = 1
      temp_temp_dict = {}
      temp_temp_dict['Stiffness Matrix'] = []

      for j in range(1,7):
        
        current_mat = 'matrix1'
        current_name = current_mat + '_row' + str(current_row)
        temp_row_vals = self.convert_value(self.data[line_num+j].split())      
        temp_temp_dict['Stiffness Matrix'].append({current_name: temp_row_vals})
        current_row += 1

      current_row = 1

      for j in range(8,14):
        
        current_mat = 'matrix2'
        current_name = current_mat + '_row' + str(current_row)
        temp_row_vals = self.convert_value(self.data[line_num+j].split())      
        temp_temp_dict['Stiffness Matrix'].append({current_name: temp_row_vals})
        current_row += 1   

      temp_dict[point_num] = temp_temp_dict

    new_dict[new_header] = temp_dict

    new_start = line_num + j + 2

    for j in range(4):

      node_section_start = new_start+(j*(num_nodes+2))
      current_head = self.data[node_section_start].strip()

      temp_dict = self.parse_xyz(self.data,node_section_start+1,1,num_nodes,'Node ')
      new_dict[current_head] = temp_dict
    
    node_section_start = node_section_start + num_nodes + 5
    new_header = self.data[node_section_start].strip().replace(':','')
    
    temp_dict = {}

    num_colp = len(in_dict['OutList'])+1

    for i in range(num_colp):

      cl_split = self.remove_whitespace(self.data[node_section_start+4+i]) 
      temp_dict['Col '+str(i)] = {'Parameter':cl_split[1].strip(),'Unit':self.remove_parens(cl_split[2].strip())}

    new_dict[new_header] = temp_dict

    # Some files have a matrix at the end and some don't
    try:

      num_row = 0
      new_start = node_section_start+num_colp+3

      for j in range(4):

        node_section_start = new_start+(j*num_row)+((j+1)*2)
        new_header = self.data[node_section_start]
        num_row = self.convert_value(new_header.split(':')[1].split(' x ')[0].strip())
        # num_col = self.convert_value(new_header.split(':')[1].split(' x ')[1].strip())
        new_header = new_header.split(':')[0].strip()

        temp_dict = {}

        for i in range(num_row):

          cl_split = self.convert_value(self.remove_whitespace_filter(self.data[node_section_start+1+i].split()))
          temp_dict['Row '+str(i)] = cl_split

        new_dict[new_header] = temp_dict

    except:

      pass

    return new_dict

