import sys
import yaml
from src.base_file import BaseFile

class AOCFstFile(BaseFile):
  """
  Input file for the openfast driver
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}
    
    key_list = [
      'Echo',          
      'AbortLevel',    
      'TMax',          
      'DT',            
      'InterpOrder',   
      'NumCrctn',     
      'DT_UJac',       
      'UJacSclFact',   
      'CompElast',     
      'CompInflow',    
      'CompAero',      
      'CompServo',     
      'CompHydro',     
      'CompSub',       
      'CompMooring',   
      'CompIce',       
      'EDFile',        
      'BDBldFile(1)',  
      'BDBldFile(2)',  
      'BDBldFile(3)',  
      'InflowFile',    
      'AeroFile',      
      'ServoFile',     
      'HydroFile',     
      'SubFile',       
      'MooringFile',   
      'IceFile',    
      'SumPrint',    
      'SttsTime',    
      'ChkptTime',    
      'DT_Out',    
      'TStart',    
      'OutFileFmt',    
      'TabDelim',    
      'OutFmt',    
      'Linearize',    
      'NLinTimes',    
      'LinTimes',    
      'LinInputs', 
      'LinOutputs', 
      'LinOutJac', 
      'LinOutMod', 
      'WrVTK', 
      'VTK_type', 
      'VTK_fields', 
      'VTK_fps'
    ] 

    matching = list(filter(lambda x: 'NTwInpSt' in x, self.data))
    # data_length = self.convert_value(matching[0].split()[0])
    sec_start_list = [3,12,21,33,42,50]
    length_list = [7,8,11,8,7,4]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += '------- OpenFAST example INPUT FILE -------------------------------------------\n'
    # TODO: should this be dynamic?
    file_string += 'FAST Certification Test #01: AWT-27CR2 with many DOFs with fixed yaw error and steady wind\n'
    file_string += '---------------------- SIMULATION CONTROL --------------------------------------\n'
    
    key_list = [
      'Echo',  
      'AbortLevel',  
      'TMax',  
      'DT',  
      'InterpOrder',  
      'NumCrctn',  
      'DT_UJac',  
      'UJacSclFact'  
    ]

    desc_list = [
      '- Echo input data to <RootName>.ech (flag)',
      '- Error level when simulation should abort (string) {"WARNING", "SEVERE", "FATAL"}',
      '- Total run time (s)',
      '- Recommended module time step (s)',
      '- Interpolation order for input/output time history (-) {1=linear, 2=quadratic}',
      '- Number of correction iterations (-) {0=explicit calculation, i.e., no corrections}',
      '- Time between calls to get Jacobians (s)',
      '- Scaling factor used in Jacobians (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- FEATURE SWITCHES AND FLAGS ------------------------------\n'

    key_list = [
      'CompElast',
      'CompInflow',
      'CompAero',
      'CompServo',
      'CompHydro',
      'CompSub',
      'CompMooring',
      'CompIce'
    ]

    desc_list = [
      '- Compute structural dynamics (switch) {1=ElastoDyn; 2=ElastoDyn + BeamDyn for blades}',
      '- Compute inflow wind velocities (switch) {0=still air; 1=InflowWind; 2=external from OpenFOAM}',
      '- Compute aerodynamic loads (switch) {0=None; 1=AeroDyn v14; 2=AeroDyn v15}',
      '- Compute control and electrical-drive dynamics (switch) {0=None; 1=ServoDyn}',
      '- Compute hydrodynamic loads (switch) {0=None; 1=HydroDyn}',
      '- Compute sub-structural dynamics (switch) {0=None; 1=SubDyn; 2=External Platform MCKF}',
      '- Compute mooring system (switch) {0=None; 1=MAP++; 2=FEAMooring; 3=MoorDyn; 4=OrcaFlex}',
      '- Compute ice loads (switch) {0=None; 1=IceFloe; 2=IceDyn}'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- INPUT FILES ---------------------------------------------\n'
    
    key_list = [
      'EDFile',
      'BDBldFile(1)',
      'BDBldFile(2)',
      'BDBldFile(3)',
      'InflowFile',
      'AeroFile',
      'ServoFile',
      'HydroFile',
      'SubFile',
      'MooringFile',
      'IceFile'
    ]

    desc_list = [
      '- Name of file containing ElastoDyn input parameters (quoted string)',
      '- Name of file containing BeamDyn input parameters for blade 1 (quoted string)',
      '- Name of file containing BeamDyn input parameters for blade 2 (quoted string)',
      '- Name of file containing BeamDyn input parameters for blade 3 (quoted string)',
      '- Name of file containing inflow wind input parameters (quoted string)',
      '- Name of file containing aerodynamic input parameters (quoted string)',
      '- Name of file containing control and electrical-drive input parameters (quoted string)',
      '- Name of file containing hydrodynamic input parameters (quoted string)',
      '- Name of file containing sub-structural input parameters (quoted string)',
      '- Name of file containing mooring system input parameters (quoted string)',
      '- Name of file containing ice input parameters (quoted string)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- OUTPUT --------------------------------------------------\n'
    
    key_list = [
      'SumPrint',
      'SttsTime',
      'ChkptTime',
      'DT_Out',
      'TStart',
      'OutFileFmt',
      'TabDelim',
      'OutFmt'
    ]

    desc_list = [
      '- Print summary data to "<RootName>.sum" (flag)',
      '- Amount of time between screen status messages (s)',
      '- Amount of time between creating checkpoint files for potential restart (s)',
      '- Time step for tabular output (s) (or "default")',
      '- Time to begin tabular output (s)',
      '- Format for tabular (time-marching) output file (switch) {1: text file [<RootName>.out], 2: binary file [<RootName>.outb], 3: both}',
      '- Use tab delimiters in text tabular output file? (flag) {uses spaces if false}',
      '- Format used for text tabular output, excluding the time channel.  Resulting field should be 10 characters. (quoted string)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- LINEARIZATION -------------------------------------------\n'

    key_list = [
      'Linearize',
      'NLinTimes',
      'LinTimes',
      'LinInputs',
      'LinOutputs',
      'LinOutJac',
      'LinOutMod'
    ]

    desc_list = [
      '- Linearization analysis (flag)',
      '- Number of times to linearize (-) [>=1] [unused if Linearize=False]',
      '- List of times at which to linearize (s) [1 to NLinTimes] [unused if Linearize=False]',
      '- Inputs included in linearization (switch) {0=none; 1=standard; 2=all module inputs (debug)} [unused if Linearize=False]',
      '- Outputs included in linearization (switch) {0=none; 1=from OutList(s); 2=all module outputs (debug)} [unused if Linearize=False]',
      '- Include full Jacobians in linearization output (for debug) (flag) [unused if Linearize=False; used only if LinInputs=LinOutputs=2]',
      '- Write module-level linearization output files in addition to output for full system? (flag) [unused if Linearize=False]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- VISUALIZATION ------------------------------------------\n'

    key_list = [
      'WrVTK',
      'VTK_type',
      'VTK_fields',
      'VTK_fps'
    ]

    desc_list = [
      '- VTK visualization data output: (switch) {0=none; 1=initialization data only; 2=animation}',
      '- Type of VTK visualization data: (switch) {1=surfaces; 2=basic meshes (lines/points); 3=all meshes (debug)} [unused if WrVTK=0]',
      '- Write mesh fields to VTK data files? (flag) {true/false} [unused if WrVTK=0]',
      '- Frame rate for VTK output (frames per second){will use closest integer multiple of DT} [used only if WrVTK=2]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    return file_string


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

    file_string += '---------------------- DISTRIBUTED TOWER PROPERTIES ----------------------------\n'
    
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
      'NBlInpSt',
      'BldFlDmp(1)',
      'BldFlDmp(2)',
      'BldEdDmp(1)',
      'FlStTunr(1)',
      'FlStTunr(2)',
      'AdjBlMs',
      'AdjFlSt',
      'AdjEdSt',
      'BldFl1Sh(2)',
      'BldFl1Sh(3)',
      'BldFl1Sh(4)',
      'BldFl1Sh(5)',
      'BldFl1Sh(6)',
      'BldFl2Sh(2)',
      'BldFl2Sh(3)',
      'BldFl2Sh(4)',
      'BldFl2Sh(5)',
      'BldFl2Sh(6)',
      'BldEdgSh(2)',
      'BldEdgSh(3)',
      'BldEdgSh(4)',
      'BldEdgSh(5)',
      'BldEdgSh(6)'
    ]

    matching = list(filter(lambda x: 'NBlInpSt' in x, self.data))
    data_length = self.convert_value(matching[0].split()[0])
    sec_start_list = [3,8,data_length+17]
    length_list = [3,5,15]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)

    temp_key_list = self.data[14].split()
    temp_unit_list = self.remove_parens(self.data[15].split())
   
    temp_dict = {}
    temp_temp_dict = {}
    for tk in temp_key_list:
      temp_temp_dict[tk] = []

    for i in range(self.convert_value(new_dict['NBlInpSt'])):
      
      for j, tk in enumerate(temp_key_list):
      
        temp_value = self.data[17+i-1].split()[j]
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
    file_string += '------- ELASTODYN V1.00.* INDIVIDUAL BLADE INPUT FILE --------------------------\n'
    # TODO: should this be dynamic?
    file_string += 'AOC 15/50 blade file.  GJStiff -> EdgEAof are mostly lies.\n'
    file_string += '---------------------- BLADE PARAMETERS ----------------------------------------\n'
    
    key_list = [
      'NBlInpSt',
      'BldFlDmp(1)',
      'BldFlDmp(2)',
      'BldEdDmp(1)'
    ]

    desc_list = [
      '- Number of blade input stations (-)',
      '- Blade flap mode #1 structural damping in percent of critical (%)',
      '- Blade flap mode #2 structural damping in percent of critical (%)',
      '- Blade edge mode #1 structural damping in percent of critical (%)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- BLADE ADJUSTMENT FACTORS --------------------------------\n'

    key_list = [
      'FlStTunr(2)',
      'FlStTunr(1)',
      'AdjBlMs',
      'AdjFlSt',
      'AdjEdSt'
    ]

    desc_list = [
      '- Blade flapwise modal stiffness tuner, 1st mode (-)',
      '- Blade flapwise modal stiffness tuner, 2nd mode (-)',
      '- Factor to adjust blade mass density (-)',
      '- Factor to adjust blade flap stiffness (-)',
      '- Factor to adjust blade edge stiffness (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- DISTRIBUTED BLADE PROPERTIES ----------------------------\n'
    
    tt_keys = list(in_dict['Matrix'].keys())
    for i,tk in enumerate(tt_keys):
      if (tk == 'BlFract'):
        ind1 = i
      if (tk == 'PitchAxis'):
        ind2 = i
      if (tk == 'StrcTwst'):
        ind3 = i
      if (tk == 'BMassDen'):
        ind4 = i  
      if (tk == 'FlpStff'):
        ind5 = i  
      if (tk == 'EdgStff'):
        ind6 = i  
    rearrange_list = [ind1,ind2,ind3,ind4,ind5,ind6] 
    
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

    num_vals = len(in_dict['Matrix']['BlFract']['Value'])

    for i in range(num_vals):
      temp_string = ''
      for tk in temp_keys:
        temp_string += str(in_dict['Matrix'][tk]['Value'][i])
        temp_string += '  '
      file_string += temp_string
      file_string += '\n'
      
    file_string += '---------------------- BLADE MODE SHAPES ---------------------------------------\n'
    
    key_list = [
      'BldFl1Sh(2)',
      'BldFl1Sh(3)',
      'BldFl1Sh(4)',
      'BldFl1Sh(5)',
      'BldFl1Sh(6)',
      'BldFl2Sh(2)',
      'BldFl2Sh(3)',
      'BldFl2Sh(4)',
      'BldFl2Sh(5)',
      'BldFl2Sh(6)',
      'BldEdgSh(2)',
      'BldEdgSh(3)',
      'BldEdgSh(4)',
      'BldEdgSh(5)',
      'BldEdgSh(6)'
    ]

    desc_list = [
      '- Flap mode 1, coeff of x^2',
      '-            , coeff of x^3',
      '-            , coeff of x^4',
      '-            , coeff of x^5',
      '-            , coeff of x^6',
      '- Flap mode 2, coeff of x^2',
      '-            , coeff of x^3',
      '-            , coeff of x^4',
      '-            , coeff of x^5',
      '-            , coeff of x^6',
      '- Edge mode 1, coeff of x^2',
      '-            , coeff of x^3',
      '-            , coeff of x^4',
      '-            , coeff of x^5',
      '-            , coeff of x^6'
   ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    return file_string


class AOCBladeADFile(BaseFile):
  """
  AOC file decsribing the blade aerodynamic parameters.
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}

    key_list = [
      'NumBlNds'
    ]
    
    matching = list(filter(lambda x: 'NumBlNds' in x, self.data))
    # data_length = self.convert_value(matching[0].split()[0])
    sec_start_list = [3]
    length_list = [0]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)

    temp_key_list = self.data[4].split()
    temp_unit_list = self.remove_parens(self.data[5].split())
   
    temp_dict = {}
    temp_temp_dict = {}
    for tk in temp_key_list:
      temp_temp_dict[tk] = []

    for i in range(self.convert_value(new_dict['NumBlNds'])):
      
      for j, tk in enumerate(temp_key_list):
      
        temp_value = self.data[7+i-1].split()[j]
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
    file_string += '------- AERODYN v15.00.* BLADE DEFINITION INPUT FILE -------------------------------------\n'
    # TODO: should this be dynamic?
    file_string += 'AOC blade aerodynamic parameters\n'
    file_string += '======  Blade Properties =================================================================\n'
    
    key_list = [
      'NumBlNds'
    ]

    desc_list = [
      '- Number of blade nodes used in the analysis (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    tt_keys = list(in_dict['Matrix'].keys())
    for i,tk in enumerate(tt_keys):
      if (tk == 'BlSpn'):
        ind1 = i
      if (tk == 'BlCrvAC'):
        ind2 = i
      if (tk == 'BlSwpAC'):
        ind3 = i
      if (tk == 'BlCrvAng'):
        ind4 = i  
      if (tk == 'BlTwist'):
        ind5 = i  
      if (tk == 'BlChord'):
        ind6 = i  
      if (tk == 'BlAFID'):
        ind7 = i 
    rearrange_list = [ind1,ind2,ind3,ind4,ind5,ind6,ind7] 
    
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

    num_vals = len(in_dict['Matrix']['BlSpn']['Value'])

    for i in range(num_vals):
      temp_string = ''
      for tk in temp_keys:
        temp_string += str(in_dict['Matrix'][tk]['Value'][i])
        temp_string += '  '
      file_string += temp_string
      file_string += '\n'
      
    return file_string


