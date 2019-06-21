# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 14, 2019

import os
import sys
import yaml
from src.crushing_inp_file import CrushingInpFile
from src.beamdyn_files import BeamdynPrimaryFile, BeamdynBladeFile, BeamdynInputFile, BeamdynInputSummaryFile
from src.turbsim_files import TurbsimInputFile, TurbsimSummaryFile

input_file_type = 6
# 0: Input file (Main folder / FAST / Crushing)               * NOT DONE
# 1: Input file (Wind folder / TurbSim / Inp)                 * DONE
# 2: Summary file (Wind folder / TurbSim / Sum)               * NOT DONE
# 3: Summary file (Main folder / FAST / Beamdyn (Primary))    * DONE
# 4: Summary file (Main folder / FAST / Beamdyn Blade)        * DONE
# 5: Input file (Main folder / FAST / Beamdyn Input)          * DONE
# 6: Input file (Main folder / FAST / Beamdyn Input Summary)  * NOT DONE

current_dir = os.path.dirname(os.path.abspath(__file__))
folder_name = 'openfast_files'

if (input_file_type == 0):

  file_name = 'NRELOffshrBsline5MW_Monopile_IEC_Crushing.inp'

elif (input_file_type == 1):
    
  file_name = '90m_12mps_twr.inp'

elif (input_file_type == 2):
    
  file_name = '90m_12mps_twr.sum'

elif (input_file_type == 3):
    
  file_name = 'NRELOffshrBsline5MW_BeamDyn.dat'

elif (input_file_type == 4):
    
  file_name = 'NRELOffshrBsline5MW_BeamDyn_Blade.dat'

elif (input_file_type == 5):
    
  file_name = 'bd_driver.inp'

elif (input_file_type == 6):
    
  file_name = 'bd_primary_inp.sum'

else:

  pass

file_path = os.path.join(current_dir, folder_name, file_name)

if (input_file_type == 0):

  try:

    crushing_file = CrushingInpFile(file_path)
    new_dict = crushing_file.read()
    crushing_file.to_yaml(new_dict)
  
  except:

    print('Oops!',sys.exc_info(),'occured.')

elif (input_file_type == 1):

  try:

    turbsim_file = TurbsimInputFile(file_path)
    new_dict = turbsim_file.read()
    turbsim_file.to_yaml(new_dict)

  except:

    print('Oops!',sys.exc_info(),'occured.')

elif (input_file_type == 2):
    
  try:

    turbsim_file = TurbsimSummaryFile(file_path)
    new_dict = turbsim_file.read()
    turbsim_file.to_yaml(new_dict)
  
  except:

    print('Oops!',sys.exc_info(),'occured.')

elif (input_file_type == 3):
    
  try:

    beamdyn_file = BeamdynPrimaryFile(file_path)
    new_dict = beamdyn_file.read()
    beamdyn_file.to_yaml(new_dict)
  
  except:

    print('Oops!',sys.exc_info(),'occured.')

elif (input_file_type == 4):
    
  try:

    beamdyn_blade_file = BeamdynBladeFile(file_path)
    new_dict = beamdyn_blade_file.read()
    beamdyn_blade_file.to_yaml(new_dict)
  
  except:

    print('Oops!',sys.exc_info(),'occured.')

elif (input_file_type == 5):
    
  try:

    beamdyn_input_file = BeamdynInputFile(file_path)
    new_dict = beamdyn_input_file.read()
    beamdyn_input_file.to_yaml(new_dict)
  
  except:

    print('Oops!',sys.exc_info(),'occured.')

elif (input_file_type == 6):
    
  try:

    beamdyn_input_sum_file = BeamdynInputSummaryFile(file_path)
    new_dict = beamdyn_input_sum_file.read()
    beamdyn_input_sum_file.to_yaml(new_dict)
  
  except:

    print('Oops!',sys.exc_info(),'occured.')

else: 

  print('No valid file types were selected!')

#new_file.close()
#output_file.close()
