# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 14, 2019
import sys
import yaml
from fileclass import File
from turbsim_input__file import Turbsim_input_file

# All required functions

input_file_type = 1
# 0: Input file (Main folder / FAST)
# 1: Input file (Wind folder / TurbSim)
# 2: Summary file (TurbSim)

if (input_file_type == 0):
    file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/NRELOffshrBsline5MW_Monopile_IEC_Crushing.inp'
elif (input_file_type == 1):
    file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/Wind/90m_12mps_twr.inp'
elif (input_file_type == 2):
    file_name = '/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/Wind/90m_12mps_twr.sum'
else:
    pass

#turbsim_file = File('/Users/lmccullu/openfast/build/reg_tests/glue-codes/openfast/5MW_Baseline/Wind/90m_12mps_twr.inp')
#turbsim_file.read()
#turbsim_file.export()

if (input_file_type == 0):

    new_dict = {}
    temp_dict = {}
    temp_var = data[0].split()
    output_file.write('# '+combine_text_spaces(temp_var[1:])+'\n')
    
    for line in data[2:]:

        if ((line[0] == '!') and (len(line.split()) > 1)):

            new_header = line.split()[1:]
            new_header = combine_text_spaces(new_header).replace(' ','_')

        elif (line[0] != '!'):

            temp_key,temp_value = sep_string(line,' ')
            temp_dict[temp_key] = temp_value

        elif (line[0] == '!'):
            
            new_dict[new_header] = temp_dict
            temp_dict = {}

    new_dict[new_header] = temp_dict

    File.to_yaml(output_filename,new_dict)

elif (input_file_type == 1):

    turbsim_file = Turbsim_input_file(file_name)
    new_dict = turbsim_file.read()
    print(new_dict)
    turbsim_file.to_yaml(new_dict)
    #turbsim_input_file.export()

    #File.to_yaml(output_filename,new_dict)

# elif (input_file_type == 2):
    
#     new_dict = {}
#     temp_dict = {}
#     temp_2d_array = []
    
#     output_file.write('# '+data[1])

#     for line_num,line in enumerate(data[4:]):

#         fl = line[0]
        
#         if (fl.isalnum()):

#             new_header = remove_char(line,[':','\n']) 

#             if (new_header.split()[0] == 'Nyquist'):

#                 new_header,temp_value,temp_unit = sep_string_double(line,'=',' ')
#                 temp_dict = {'Unit':temp_unit,'Value':convert_value(temp_value)} 

#             elif (new_header.split()[0] == 'Processing'):

#                 new_header = 'Processing Time'
#                 temp_key = line.split()
#                 temp_unit = remove_char(combine_text_spaces(temp_key[3:-1]),['.']) 
#                 temp_value = temp_key[2]
#                 temp_dict = {'Unit':temp_unit,'Value':convert_value(temp_value)}
#                 new_dict[new_header] = temp_dict

#         elif (((new_header.split()[0] == 'Runtime') or (new_header.split()[0] == 'Turbine/Model') or (new_header.split()[0] == 'Meteorological')) and (len(line.split()) > 0)):

#             temp_value = line.split()[0]

#             if (temp_value == '0'):

#                 temp_value = '0 -  NONE'
#                 temp_var = line.split()[3:]

#             else:

#                 temp_var = line.split()[1:]

#             temp_key = combine_text_spaces(temp_var)
#             if ('[' in temp_key):
#                 temp_var = temp_key.split()
#                 temp_unit = remove_brackets(temp_var[len(temp_var)-1])
#                 temp_key = combine_text_spaces(temp_var[0:(len(temp_var)-1)])
#                 if (temp_value != 'N/A'):
#                     temp_dict[temp_key] = {'Unit':temp_unit,'Value':convert_value(temp_value)}
#                 else:
#                     temp_dict[temp_key] = {'Unit':temp_unit,'Value':temp_value}
#             else: 
#                 temp_dict[temp_key] = convert_value(temp_value)

#         elif (line_num == 47):

#             temp_dict = {}
#             temp_line = line.split()
#             temp_dict['File name'] = temp_line[0]
#             temp_dict['File type'] = remove_parens(combine_text_spaces(temp_line[1:]))
#             new_dict['Generated File'] = temp_dict

#         elif ((new_header.split()[0] == 'Turbulence') and (len(line.split()) > 0)):

#             temp_key,temp_value = sep_string(line,'=')

#             if ((len(temp_value.split()) > 1) and (is_int(temp_value.split()[0]) or is_float(temp_value.split()[0]))):
#                 temp_var,temp_unit = sep_string(temp_value,' ')
#                 temp_dict[temp_key] = {'Unit':temp_unit,'Value':convert_value(temp_var)}
#             else:
#                 if ('%' in temp_value):
#                     temp_var = temp_value[:-1]
#                     temp_unit = '%'
#                     temp_dict[temp_key] = {'Unit':temp_unit,'Value':convert_value(temp_var)}
#                 else:
#                     temp_dict[temp_key] = convert_value(temp_value)

#         elif ((new_header.split()[0] == 'Mean') and (new_header.split()[1] == 'Flow') and (len(line.split()) > 0)):

#             temp_key,temp_value,temp_unit = sep_string_double(line,'=',' ')
#             temp_dict[temp_key] = {'Unit':temp_unit,'Value':convert_value(temp_value)}            

#         elif ((new_header.split()[0] == 'Mean') and (new_header.split()[1] == 'Wind') and (len(line.split()) > 0)):

#             if (line_num == 82):

#                 temp_value_list = split_line(line)

#             elif (line_num == 83):

#                 temp_unit_list = line.split()
#                 temp_unit_list = [remove_parens(i) for i in temp_unit_list]           

#             elif ((line_num >= 85)):

#                 temp_vals = line.split()
#                 temp_2d_array.append(temp_vals)

#                 for i,tv in enumerate(temp_value_list):

#                     temp_list = []

#                     for j in range(len(temp_2d_array)):

#                         temp_list.append(convert_value(temp_2d_array[j][i]))

#                     temp_dict[tv] = {'Unit':temp_unit_list[i],'Value':temp_list}

#         elif ((new_header.split()[0] == 'Harvested') and (len(line.split()) > 0)):

#             temp_value,temp_key = sep_string(line,' ')
#             temp_dict[temp_key] = convert_value(temp_value)

#         elif ((new_header.split()[0] == 'Hub-Height') and (len(line.split()) > 0)):

#             if (line_num == 129):

#                 temp_value_list = split_line(line)
#                 temp_temp_dict = {}

#             elif ((line_num >= 131) and (line_num <= 139)):

#                 temp_line_vals = split_line(line)
#                 temp_temp_temp_dict = {}

#                 for k,tv in enumerate(temp_value_list[1:]):

#                     temp_var = tv
#                     temp_unit = tv.split()
#                     temp_title = combine_text_spaces(temp_unit[0:(len(temp_unit)-1)])
#                     temp_unit = remove_parens(temp_unit[len(temp_unit)-1]) 
#                     temp_temp_temp_dict[temp_title] = {'Unit':temp_unit,'Value':convert_value(temp_line_vals[k+1])}

#                 temp_temp_dict[temp_line_vals[0]] = temp_temp_temp_dict
#                 temp_dict[temp_value_list[0]] = temp_temp_dict

#             elif (line_num == 140):

#                 temp_value_list = split_line(line)

#             elif (line_num == 141): 

#                 temp_value_list2 = split_line(line)

#                 for i,tlv in enumerate(temp_value_list):

#                     temp_value_list[i] = tlv + ' ' + temp_value_list2[i+1]

#                 temp_value_list.insert(0,temp_value_list2[0])
#                 temp_temp_dict2 = {}

#             elif ((line_num >= 143) and (line_num <= 145)):

#                 temp_line_vals = split_line(line)
#                 temp_temp_temp_dict = {}

#                 for k,tv in enumerate(temp_value_list[1:]):

#                     temp_var = tv

#                     if (tv.split()[0] == 'Correlation'):
#                         temp_title = temp_var
#                         temp_temp_temp_dict[temp_title] = convert_value(temp_line_vals[k+1])
#                     else:
#                         temp_unit = tv.split()
#                         temp_title = combine_text_spaces(temp_unit[0:(len(temp_unit)-1)])
#                         temp_unit = temp_unit[len(temp_unit)-1]
#                         temp_temp_temp_dict[temp_title] = {'Unit':temp_unit,'Value':convert_value(temp_line_vals[k+1])}

#                 temp_temp_dict2[temp_line_vals[0]] = temp_temp_temp_dict
#                 temp_dict[temp_value_list[0]] = temp_temp_dict2

#             elif ((line_num >= 148) and (line_num <= 150)):

#                 temp_key,temp_value,temp_unit = sep_string_double(line,'=',' ')
#                 temp_dict[temp_key] = {'Value':convert_value(temp_value),'Unit':temp_unit}

#         elif ((new_header.split()[0] == 'Grid') and (len(line.split()) > 0)):

#             if (line.split()[0] == 'Y-coord'):

#                 y_coord_list = line.split()[1:]
#                 temp_temp_dict = {}

#             elif (line.split()[0] == 'Height'):

#                 current_title = line.split()[1:]
#                 current_title = remove_char(combine_text_spaces(current_title),[':'])
#                 ch = 0
#                 temp_temp_temp_dict = {}

#             elif ((line_num >= 256) and (line_num <= 259)):
                
#                 if (line.split()[0] == 'Mean'):

#                     temp_key = remove_char(line,[':']).strip()
#                     temp_temp_temp_dict = {}

#                 else:

#                     temp_temp_key,temp_var,temp_unit = sep_string_double(line,':',' ')
#                     temp_temp_temp_dict[temp_temp_key] = {'Unit':temp_unit,'Value':convert_value(temp_var)}
#                     temp_temp_dict[temp_key] = temp_temp_temp_dict

#                 temp_dict = temp_temp_dict

#             else:

#                 for i,current_y in enumerate(y_coord_list):
                    
#                     current_height = line.split()[0]
#                     current_value = line.split()[i+1]

#                     current_GP = 'GP' + '_' + str(ch) + '_' + str(i)
#                     temp_temp_temp_dict[current_GP] = {'Height':convert_value(current_height),'Y-coord':convert_value(current_y),'Value':convert_value(current_value)}
#                     temp_temp_dict[current_title] = temp_temp_temp_dict

#                 temp_dict = temp_temp_dict
#                 ch += 1

#         elif ((new_header.split()[0] == 'U-component') and (len(line.split()) > 0)):

#             temp_key,temp_value,temp_unit = sep_string_double(line,'=',' ')
#             temp_dict[temp_key] = {'Unit':temp_unit,'Value':convert_value(temp_value)} 

#         elif ((len(line.split()) == 0) and (line_num != 64) and (line_num != 70) and (line_num != 139)and (line_num != 146)and (line_num != 147)):

#             if (len(temp_dict.keys()) > 0):

#                 new_dict[new_header] = temp_dict

#             temp_dict = {}

#         else:

#             pass

#     # Write the saved dictionary to a YAML output file
#     File.to_yaml(output_filename,new_dict)

else: 

    pass

#new_file.close()
#output_file.close()
