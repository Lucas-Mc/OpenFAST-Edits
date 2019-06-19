# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 14, 2019
import sys
import yaml
from turbsim_inp_file import TurbsimInpFile
from turbsim_sum_file import TurbsimSumFile
from crushing_inp_file import CrushingInpFile
from beamdyn_files import BeamdynFile, BeamdynBladeFile

input_file_type = 4
# 0: Input file (Main folder / FAST / Crushing)
# 1: Input file (Wind folder / TurbSim / Inp)
# 2: Summary file (Wind folder / TurbSim / Sum)
# 3: Summary file (Main folder / FAST / Beamdyn)
# 4: Summary file (Main folder / FAST / Beamdyn Blade)

if (input_file_type == 0):

  file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/NRELOffshrBsline5MW_Monopile_IEC_Crushing.inp'

elif (input_file_type == 1):
    
  file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/Wind/90m_12mps_twr.inp'

elif (input_file_type == 2):
    
  file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/Wind/90m_12mps_twr.sum'

elif (input_file_type == 3):
    
  file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/NRELOffshrBsline5MW_BeamDyn.dat'

elif (input_file_type == 4):
    
  file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/NRELOffshrBsline5MW_BeamDyn_Blade.dat'

else:

  pass

if (input_file_type == 0):

  crushing_file = CrushingInpFile(file_name)
  new_dict = crushing_file.read()
  crushing_file.to_yaml(new_dict)

elif (input_file_type == 1):

  turbsim_file = TurbsimInpFile(file_name)
  new_dict = turbsim_file.read()
  turbsim_file.to_yaml(new_dict)

elif (input_file_type == 2):
    
  turbsim_file = TurbsimSumFile(file_name)
  new_dict = turbsim_file.read()
  turbsim_file.to_yaml(new_dict)

elif (input_file_type == 3):
    
  beamdyn_file = BeamdynFile(file_name)
  new_dict = beamdyn_file.read()
  beamdyn_file.to_yaml(new_dict)

elif (input_file_type == 4):
    
  beamdyn_blade_file = BeamdynBladeFile(file_name)
  new_dict = beamdyn_blade_file.read()
  beamdyn_blade_file.to_yaml(new_dict)

else: 

  pass

#new_file.close()
#output_file.close()
