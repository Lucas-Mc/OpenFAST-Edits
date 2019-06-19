# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 14, 2019
import sys
import yaml
from fileclass import File
from turbsim_inp_file import Turbsim_inp_file
from turbsim_sum_file import Turbsim_sum_file
from crushing_inp_file import Crushing_inp_file

input_file_type = 2
# 0: Input file (Main folder / FAST / Crushing)
# 1: Input file (Wind folder / TurbSim / Inp)
# 2: Summary file (Wind folder / TurbSim / Sum)

if (input_file_type == 0):

    file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/NRELOffshrBsline5MW_Monopile_IEC_Crushing.inp'

elif (input_file_type == 1):
    
    file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/Wind/90m_12mps_twr.inp'

elif (input_file_type == 2):
    
    file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/Wind/90m_12mps_twr.sum'

else:
    pass

if (input_file_type == 0):

    crushing_file = Crushing_inp_file(file_name)
    new_dict = crushing_file.read()
    crushing_file.to_yaml(new_dict)

elif (input_file_type == 1):

    turbsim_file = Turbsim_inp_file(file_name)
    new_dict = turbsim_file.read()
    turbsim_file.to_yaml(new_dict)

elif (input_file_type == 2):
    
    turbsim_file = Turbsim_sum_file(file_name)
    new_dict = turbsim_file.read()
    turbsim_file.to_yaml(new_dict)

else: 

    pass

#new_file.close()
#output_file.close()
