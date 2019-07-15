import sys
import yaml
from src.base_file import BaseFile


class AOCTowerFile(BaseFile):
  """
  Input file for the AOC module
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}
    
    key_list = [
      'NTwInpSt',
      'TwrFADmp(1)',
      'TwrFADmp(2)',
      'TwrSSDmp(1)',
      'TwrSSDmp(2)',
      'FAStTunr(1)',
      'FAStTunr(2)',
      'SSStTunr(1)',
      'SSStTunr(2)',
      'AdjTwMa',
      'AdjFASt',
      'AdjSSSt',
      'TwFAM1Sh(2)',
      'TwFAM1Sh(3)',
      'TwFAM1Sh(4)',
      'TwFAM1Sh(5)',
      'TwFAM1Sh(6)',
      'TwFAM2Sh(2)',
      'TwFAM2Sh(3)',
      'TwFAM2Sh(4)',
      'TwFAM2Sh(5)',
      'TwFAM2Sh(6)',
      'TwSSM1Sh(2)',
      'TwSSM1Sh(3)',
      'TwSSM1Sh(4)',
      'TwSSM1Sh(5)',
      'TwSSM1Sh(6)',
      'TwSSM2Sh(2)',
      'TwSSM2Sh(3)',
      'TwSSM2Sh(4)',
      'TwSSM2Sh(5)',
      'TwSSM2Sh(6)'
    ]

    matching = list(filter(lambda x: 'NTwInpSt' in x, self.data))
    data_length = self.convert_value(matching[0].split()[0])
    sec_start_list = [3,9,data_length+20,data_length+31]
    length_list = [4,7,10,10]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)

    temp_key_list = self.data[17].split()
    temp_unit_list = self.remove_parens(self.data[18].split())
   
    temp_dict = {}
    temp_temp_dict = {}
    for tk in temp_key_list:
      temp_temp_dict[tk] = []

    for i in range(self.convert_value(new_dict['NTwInpSt'])):
      
      for j, tk in enumerate(temp_key_list):
      
        temp_value = self.data[20+i-1].split()[j]
        temp_temp_dict[tk].append(self.convert_value(temp_value))
        temp_dict[tk] = {
          'Value': temp_temp_dict[tk],
          'Unit': temp_unit_list[j]
        }

    new_dict['Matrix'] = temp_dict

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += '------- ELASTODYN V1.00.* TOWER INPUT FILE -------------------------------------\n'
    # TODO: should this be dynamic?
    file_string += 'AOC tower data.  This is pure fiction.\n'
    file_string += '---------------------- TOWER PARAMETERS ----------------------------------------\n'
    
    key_list = [
      'NTwInpSt',
      'TwrFADmp(1)',
      'TwrFADmp(2)',
      'TwrSSDmp(1)',
      'TwrSSDmp(2)'
    ]

    desc_list = [
      '- Number of input stations to specify tower geometry',
      '- Tower 1st fore-aft mode structural damping ratio (%)',
      '- Tower 2nd fore-aft mode structural damping ratio (%)',
      '- Tower 1st side-to-side mode structural damping ratio (%)',
      '- Tower 2nd side-to-side mode structural damping ratio (%)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- TOWER ADJUSTMUNT FACTORS --------------------------------\n'

    key_list = [
      'FAStTunr(1)', 
      'FAStTunr(2)', 
      'SSStTunr(1)', 
      'SSStTunr(2)', 
      'AdjTwMa', 
      'AdjFASt', 
      'AdjSSSt'        
    ]

    desc_list = [
      '- Tower fore-aft modal stiffness tuner, 1st mode (-)',
      '- Tower fore-aft modal stiffness tuner, 2nd mode (-)',
      '- Tower side-to-side stiffness tuner, 1st mode (-)',
      '- Tower side-to-side stiffness tuner, 2nd mode (-)',
      '- Factor to adjust tower mass density (-)',
      '- Factor to adjust tower fore-aft stiffness (-)',
      '- Factor to adjust tower side-to-side stiffness (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string
    
    tt_keys = list(in_dict['Matrix'].keys())
    for i,tk in enumerate(tt_keys):
      if (tk == 'HtFract'):
        ind1 = i
      if (tk == 'TMassDen'):
        ind2 = i
      if (tk == 'TwFAStif'):
        ind3 = i
      if (tk == 'TwSSStif'):
        ind4 = i  
    rearrange_list = [ind1,ind2,ind3,ind4] 
    
    temp_keys = []
    for i,v in enumerate(rearrange_list):
      temp_keys.append(tt_keys[v])

    temp_string = ''
    for tk in temp_keys:
      temp_string += '  '
      temp_string += tk
    file_string += temp_string
    file_string += '\n'

    temp_string = ''
    for tk in temp_keys:
      tu = in_dict['Matrix'][tk]['Unit']
      temp_string += '  '
      ind_string = '(' + tu + ')'
      temp_string +=ind_string
    file_string += temp_string
    file_string += '\n'

    num_vals = len(in_dict['Matrix']['HtFract']['Value'])

    for i in range(num_vals):
      temp_string = ''
      for tk in temp_keys:
        temp_string += str(in_dict['Matrix'][tk]['Value'][i])
        temp_string += '  '
      file_string += temp_string
      file_string += '\n'
      
    file_string += '---------------------- TOWER FORE-AFT MODE SHAPES ------------------------------\n'
    
    key_list = [
      'TwFAM1Sh(2)',
      'TwFAM1Sh(3)',
      'TwFAM1Sh(4)',
      'TwFAM1Sh(5)',
      'TwFAM1Sh(6)',
      'TwFAM2Sh(2)',
      'TwFAM2Sh(3)',
      'TwFAM2Sh(4)',
      'TwFAM2Sh(5)',
      'TwFAM2Sh(6)'
    ]

    desc_list = [
      '- Mode 1, coefficient of x^2 term',
      '-       , coefficient of x^3 term',
      '-       , coefficient of x^4 term',
      '-       , coefficient of x^5 term',
      '-       , coefficient of x^6 term',
      '- Mode 2, coefficient of x^2 term',
      '-       , coefficient of x^3 term',
      '-       , coefficient of x^4 term',
      '-       , coefficient of x^5 term',
      '-       , coefficient of x^6 term'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- TOWER SIDE-TO-SIDE MODE SHAPES --------------------------\n'

    key_list = [
      'TwSSM1Sh(2)',
      'TwSSM1Sh(3)',
      'TwSSM1Sh(4)',
      'TwSSM1Sh(5)',
      'TwSSM1Sh(6)',
      'TwSSM2Sh(2)',
      'TwSSM2Sh(3)',
      'TwSSM2Sh(4)',
      'TwSSM2Sh(5)',
      'TwSSM2Sh(6)'
    ]

    desc_list = [
      '- Mode 1, coefficient of x^2 term',
      '-       , coefficient of x^3 term',
      '-       , coefficient of x^4 term',
      '-       , coefficient of x^5 term',
      '-       , coefficient of x^6 term',
      '- Mode 2, coefficient of x^2 term',
      '-       , coefficient of x^3 term',
      '-       , coefficient of x^4 term',
      '-       , coefficient of x^5 term',
      '-       , coefficient of x^6 term'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    return file_string


class AOCBladeFile(BaseFile):
  """
  AOC file decsribing a blade.
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

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

  def read_y2t(self):

    in_dict = self.data

    file_string = ''

    file_string += '   ------- AOC V1.00.* INDIVIDUAL BLADE INPUT FILE --------------------------\n'
    # TODO: does this line change every file?
    file_string += ' Test Format 1\n'
    file_string += ' ---------------------- BLADE PARAMETERS --------------------------------------\n'

    key_list = [     
      'station_total',   
      'damp_type'       
    ]

    desc_list = [
      '- Number of blade input stations (-)',
      '- Damping type: 0: no damping; 1: damped'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,'Blade Parameters')
    file_string += temp_string

    file_string += '  ---------------------- DAMPING COEFFICIENT------------------------------------\n'
    
    temp_string = ''
    temp_keys = in_dict['Damping Coefficient'].keys()
    for val in temp_keys:
      t_string = '  ' + val.split('(')[0]
      temp_string += t_string
    
    file_string += temp_string
    file_string += '\n'
    
    temp_string = ''
    for val in temp_keys:
      t_string = '  (' + val.split('(')[1]
      temp_string += t_string
    
    file_string += temp_string
    file_string += '\n'

    temp_string = ''
    for val in temp_keys:
      t_string = '  ' + str(in_dict['Damping Coefficient'][val])
      temp_string += t_string
    
    file_string += temp_string
    file_string += '\n'

    file_string += ' ---------------------- DISTRIBUTED PROPERTIES---------------------------------\n'
    
    for tk in in_dict['Distributed Properties'].keys():
      
      temp_string = '  ' + str(tk) + '\n'
      file_string += temp_string
      
      for ttk in in_dict['Distributed Properties'][tk]['Stiffness Matrix']:
        
        temp_key = list(ttk.keys())[0]
        # current_mat = self.convert_value(temp_key.split('_')[0][-1])
        current_row = self.convert_value(temp_key[-1])
        temp_string = ''

        for v in ttk[temp_key]:
          
          t_string = '   ' + str(v)
          temp_string += t_string

        temp_string += '\n'
        file_string += temp_string

        if (current_row == 6):
          
          file_string += '\n'

    return file_string


class AOCBladeADFile(BaseFile):
  """
  AOC file decsribing the inputs.
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

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

  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += '------- AOC Driver with OpenFAST INPUT FILE --------------------------------\n'
    file_string += 'Static analysis of a curved beam\n'
    file_string += '---------------------- SIMULATION CONTROL --------------------------------------\n'
      
    key_list = [
      'DynamicSolve',
      't_initial',   
      't_final',     
      'dt'
    ]          

    desc_list = [
      '- Dynamic solve (false for static solve) (-)',
      '- Starting time of simulation (s) [used only when DynamicSolve=TRUE]',
      '- Ending time of simulation   (s) [used only when DynamicSolve=TRUE]',
      '- Time increment size         (s) [used only when DynamicSolve=TRUE]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- GRAVITY PARAMETER --------------------------------------\n'
    
    key_list = [
      'Gx',            
      'Gy',            
      'Gz' 
    ]

    desc_list = [    
      '- Component of gravity vector along X direction (m/s^2)',       
      '- Component of gravity vector along Y direction (m/s^2)',
      '- Component of gravity vector along Z direction (m/s^2)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- FRAME PARAMETER --------------------------------------\n'

    key_list = [
      'GlbPos(1)',     
      'GlbPos(2)',     
      'GlbPos(3)'   
    ]  

    desc_list = [
      '- Component of position vector of the reference blade frame along X direction (m)',
      '- Component of position vector of the reference blade frame along Y direction (m)',
      '- Component of position vector of the reference blade frame along Z direction (m)'
    ]    

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---The following 3 by 3 matrix is the direction cosine matirx ,GlbDCM(3,3),\n'
    file_string += '---relates global frame to the initial blade root frame\n'

    # TODO: insert matrix here
    temp_string = ''
    for nr in in_dict['Matrix'].keys():
      for v in in_dict['Matrix'][nr]:
        temp_string += str(v)
        temp_string += '  '
      temp_string += '\n'
    file_string += temp_string

    key_list = [
      'GlbRotBladeT0'
    ] 

    desc_list = [
      '- Reference orientation for AOC calculations is aligned with initial blade root'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- ROOT VELOCITY PARAMETER ----------------------------------\n'

    key_list = [
      'RootVel(4)', 
      'RootVel(5)', 
      'RootVel(6)'
    ]

    desc_list = [
      '- Component of angular velocity vector of the beam root about X axis (rad/s)',
      '- Component of angular velocity vector of the beam root about Y axis (rad/s)',   
      '- Component of angular velocity vector of the beam root about Z axis (rad/s)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- APPLIED FORCE ----------------------------------\n'

    key_list = [
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
      'NumPointLoads'
    ]

    desc_list = [
      '- Component of distributed force vector along Y direction (N/m)',
      '- Component of distributed force vector along Z direction (N/m)',
      '- Component of distributed moment vector along X direction (N-m/m)',
      '- Component of distributed force vector along X direction (N/m)',
      '- Component of distributed moment vector along Y direction (N-m/m)',
      '- Component of distributed moment vector along Z direction (N-m/m)',  
      '- Component of concentrated force vector at blade tip along X direction (N)',   
      '- Component of concentrated force vector at blade tip along Y direction (N)',    
      '- Component of concentrated force vector at blade tip along Z direction (N)',    
      '- Component of concentrated moment vector at blade tip along X direction (N-m)',    
      '- Component of concentrated moment vector at blade tip along Y direction (N-m)',   
      '- Component of concentrated moment vector at blade tip along Z direction (N-m)',
      '- Number of point loads along blade'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += 'Non-dim blade-span eta   Fx          Fy            Fz           Mx           My           Mz\n'
    file_string += '(-)                      (N)         (N)           (N)          (N-m)        (N-m)        (N-m)\n'
    file_string += '---------------------- PRIMARY INPUT FILE --------------------------------------\n'

    key_list = [
      'InputFile'
    ]

    desc_list = [
      '- Name of the primary AOC input file'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    return file_string


