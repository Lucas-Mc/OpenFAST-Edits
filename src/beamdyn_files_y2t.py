# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 27, 2019

import sys
import yaml
from src.base_file import BaseFile

class BeamdynFile(BaseFile):
  """
  Super class for all output-related files.
  """
  def __init__(self, filename):

    try:

      super().__init__(filename)
      file_ext = filename.split('.',1)[1]
      if (file_ext == 'yml'):
        if ('_inp.' in filename):
          input_filename = self.parse_filename(filename,'.yml','.inp')
        if ('_out.' in filename):
          input_filename = self.parse_filename(filename,'.yml','.out')
        if ('_inpsum.' in filename):
          input_filename = self.parse_filename(filename,'.yml','.inp.sum')
      else:
        input_filename = self.parse_filename(filename,'.yml',file_ext)
      
      self.init_input_file(input_filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

class BeamdynPrimaryFile(BeamdynFile):
  # TODO: not done yet
  """
  Primary output file.
  """

  def __init__(self, filename):

    try:

      super().__init__(filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def read(self):

    # in_file = '/'.join(self.filename.split('/')[:-1]) + '/bd_driver_out.yml'
    in_dict = yaml.load(open(self.filename))

    file_string = ''
    file_string += '--------- BEAMDYN with OpenFAST INPUT FILE -------------------------------------------\n'
    # TODO: should this be dynamic?
    file_string += 'NREL 5MW blade\n'
    file_string += '---------------------- SIMULATION CONTROL --------------------------------------\n'
    
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
      'RotStates'
    ]

    desc_list = [
      '- Echo input data to "<RootName>.ech" (flag)',
      '- Use quasistatic pre-conditioning with centripetal accelerations in initialization (flag) [dynamic solve only]',
      '- Numerical damping parameter for generalized-alpha integrator',
      '- Quadrature method: 1=Gaussian; 2=Trapezoidal (switch)',
      '- Refinement factor for trapezoidal quadrature (-). DEFAULT = 1 [used only when quadrature=2]',
      '- Factorization frequency (-). DEFAULT = 5',
      '- Time step size (s).',
      '- Number of factored load retries before quitting the aimulation',
      '- Max number of iterations in Newton-Ralphson algorithm (-). DEFAULT = 10',
      '- Tolerance for stopping criterion (-)',
      '- Flag to use finite differenced tangent stiffness matrix (-)',
      '- Flag to compare analytical finite differenced tangent stiffness matrix  (-)',
      '- perturbation size for finite differencing (-)',
      '- Maximum allowable relative difference between analytical and fd tangent stiffness (-)',
      '- Orient states in the rotating frame during linearization? (flag) [used only when linearizing]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list)
    file_string += temp_string

    file_string += '---------------------- GEOMETRY PARAMETER --------------------------------------\n'

    key_list = [
      'member_total',
      'kp_total'    
      # '49',             May need in the future          
    ]

    desc_list = [
      '- Total number of members (-)',
      '- Total number of key points (-) [must be at least 3]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list)
    file_string += temp_string

    file_string += '---------------------- MESH PARAMETER ------------------------------------------\n'
    
    key_list = [
      'order_elem'
    ]

    desc_list = [
      '- Order of interpolation (basis) function (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list)
    file_string += temp_string

    file_string += '---------------------- MATERIAL PARAMETER --------------------------------------\n'

    key_list = [
      'BldFile'
    ]

    desc_list = [
      '- Name of file containing properties for blade (quoted string)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list)
    file_string += temp_string

    file_string += '---------------------- PITCH ACTUATOR PARAMETERS -------------------------------\n'

    key_list = [
      'UsePitchAct',
      'PitchJ',     
      'PitchK',     
      'PitchC'
    ]

    desc_list = [
      '- Whether a pitch actuator should be used (flag)',
      '- Pitch actuator inertia (kg-m^2) [used only when UsePitchAct is true]',
      '- Pitch actuator stiffness (kg-m^2/s^2) [used only when UsePitchAct is true]',
      '- Pitch actuator damping (kg-m^2/s) [used only when UsePitchAct is true]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list)
    file_string += temp_string

    file_string += '---------------------- OUTPUTS -------------------------------------------------\n'

    key_list = [     
      'SumPrint',   
      'OutFmt',     
      'NNodeOuts'  
    ]

    desc_list = [
      '- Print summary data to "<RootName>.sum" (flag)',
      '- Format used for text tabular output, excluding the time channel.',
      '- Number of nodes to output to file [0 - 9] (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list)
    file_string += temp_string

    file_string += '---------------------------------------------------------------------------------------\n'

    return file_string

class BeamdynBladeFile(BeamdynFile):
  # TODO: not done yet
  """
  Primary output file.
  """

  def __init__(self, filename):

    try:

      super().__init__(filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def read(self):

    in_dict = yaml.load(open(self.filename))

    file_string = ''

    file_string += '   ------- BEAMDYN V1.00.* INDIVIDUAL BLADE INPUT FILE --------------------------\n'
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