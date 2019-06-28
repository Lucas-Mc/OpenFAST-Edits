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
      file_ext = '.out'
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

    in_file = '/'.join(self.filename.split('/')[:-1]) + '/bd_driver_out.yml'
    print(in_file)
    in_dict = yaml.load(open(in_file))

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

