# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 14, 2019

import os
import sys
import yaml
from crushing_inp_file import CrushingInpFile
from beamdyn_files import BeamdynPrimaryFile, BeamdynBladeFile, BeamdynInputFile
from turbsim_files import TurbsimInputFile, TurbsimSummaryFile

input_file_type = 3
# 0: Input file (Main folder / FAST / Crushing)
# 1: Input file (Wind folder / TurbSim / Inp)
# 2: Summary file (Wind folder / TurbSim / Sum)
# 3: Summary file (Main folder / FAST / Beamdyn (Primary))
# 4: Summary file (Main folder / FAST / Beamdyn Blade)
# 5: Input file (Main folder / FAST / Beamdyn Input)

current_dir = os.path.dirname(os.path.abspath(__file__))

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

else:

  pass

file_path = os.path.join(current_dir, file_name)

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

else: 

  print('No valid file types were selected!')

#new_file.close()
#output_file.close()
