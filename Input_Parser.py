# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 14, 2019
import sys
import yaml

input_file_type = 2
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

new_file = open(file_name)
data = new_file.readlines()

output_filename = file_name.split('/')[len(file_name.split('/'))-1].replace('.inp','.yml')
if (input_file_type >= 2):
    output_filename = output_filename.replace('.sum','.yml').replace('.','_sum.')
output_file = open(output_filename,'w') 
output_file.write('---\n')
output_file.write('# Input information for: '+output_filename.replace('.yml','')+'\n')

def split_line(current_line):
    # Take the line and split by whitespace while conserving spaces in categories
    temp_value_list = current_line.split('  ')
    temp_value_list = [i.replace('\n','').strip() for i in temp_value_list]
    temp_value_list = list(filter(None, temp_value_list))
    
    return temp_value_list

if (input_file_type == 0):

    new_dict = {}
    temp_dict = {}
    temp_var = data[0].split()
    seperator = ' '
    output_file.write('# '+seperator.join(temp_var[1:])+'\n')
    
    for line in data[2:]:

        if ((line[0] == '!') and (len(line.split()) > 1)):

            new_header = line.split()[1:]
            seperator = ' '
            new_header = seperator.join(new_header).replace(' ','_')

        elif (line[0] != '!'):

            temp_key = line.split()[0]
            temp_value = line.split()[1]
            temp_dict[temp_key] = temp_value

        elif (line[0] == '!'):
            
            new_dict[new_header] = temp_dict
            temp_dict = {}

    new_dict[new_header] = temp_dict

    with open(output_filename, 'w') as outfile:
        yaml.safe_dump(new_dict, output_file)

elif (input_file_type == 1):

    new_dict = {}
    temp_dict = {}
    output_file.write('# '+data[0])
        
    for line in data[2:]:

        if (line[0] == '-'):

            new_header = line.replace('-','').replace('\n','')
            
        elif ((len(line.split()) > 0) and (line[0] != '=')):
            
            new_line = line.split()
            temp_value = new_line[0]
            temp_key = new_line[1]
            seperator = ' '
            description = seperator.join(new_line[3:]).replace('"','\'')
            temp_dict[temp_key] = {'Value':temp_value,'Description':description}

        elif (len(line.split()) == 0):

            new_dict[new_header] = temp_dict
            temp_dict = {}

        else: 
            
            pass

    with open(output_filename, 'w') as outfile:
        yaml.safe_dump(new_dict, output_file)

elif (input_file_type == 2):
    
    new_dict = {}
    temp_dict = {}
    temp_2d_array = []
    
    output_file.write('# '+data[1])

    for line_num,line in enumerate(data[4:]):

        fl = line[0]
        
        if (fl.isalnum()):

            new_header = line.replace(':','').replace('\n','')

        elif (((new_header.split()[0] == 'Runtime') or (new_header.split()[0] == 'Turbine/Model') or (new_header.split()[0] == 'Meteorological')) and (len(line.split()) > 0)):

            temp_value = line.split()[0]

            if (temp_value == '0'):

                temp_value = '0 -  NONE'
                temp_var = line.split()[3:]

            else:

                temp_var = line.split()[1:]

            seperator = ' '
            temp_key = seperator.join(temp_var)
            if ('[' in temp_key):
                temp_var = temp_key.split()
                temp_unit = temp_var[len(temp_var)-1].replace('[','').replace(']','')
                seperator = ' '
                temp_key = seperator.join(temp_var[0:(len(temp_var)-1)])
                temp_dict[temp_key] = {'Unit':temp_unit,'Value':temp_value}
            else: 
                temp_dict[temp_key] = temp_value

        elif (line_num == 47):

            temp_dict = {}
            temp_line = line.split()
            temp_dict['File name'] = temp_line[0]
            seperator = ' '
            temp_dict['File type'] = seperator.join(temp_line[1:]).replace('(','').replace(')','')
            new_dict['Generated File'] = temp_dict

        elif ((new_header.split()[0] == 'Turbulence') and (line_num < 74) and (len(line.split()) > 0)):

            temp_key = line.split('=')[0].strip()
            temp_value = line.split('=')[1].strip()
            temp_dict[temp_key] = temp_value

        elif ((new_header.split()[0] == 'Mean') and (new_header.split()[1] == 'Flow') and (len(line.split()) > 0)):

            temp_key = line.split('=')[0].strip()
            temp_value = line.split('=')[1].strip()
            temp_unit = temp_value.split()[1]
            temp_value = temp_value.split()[0]
            temp_dict[temp_key] = {'Unit':temp_unit,'Value':temp_value}            

        elif ((new_header.split()[0] == 'Mean') and (new_header.split()[1] == 'Wind') and (len(line.split()) > 0)):

            if (line_num == 82):

                temp_value_list = split_line(line)

            elif (line_num == 83):

                temp_unit_list = line.split()
                temp_unit_list = [i.replace('(','').replace(')','') for i in temp_unit_list]           

            elif ((line_num >= 85)):

                temp_vals = line.split()
                temp_2d_array.append(temp_vals)

                for i,tv in enumerate(temp_value_list):

                    temp_list = []

                    for j in range(len(temp_2d_array)):

                        temp_list.append(temp_2d_array[j][i])

                    temp_dict[tv] = {'Unit':temp_unit_list[i],'Value':temp_list}

        elif ((new_header.split()[0] == 'Harvested') and (len(line.split()) > 0)):

            temp_value = line.split()[0]
            temp_key = line.split()[1]
            temp_dict[temp_key] = temp_value

        elif ((new_header.split()[0] == 'Hub-Height') and (len(line.split()) > 0)):

            if (line_num == 129):

                temp_value_list = split_line(line)
                temp_temp_dict = {}

            elif ((line_num >= 131) and (line_num <= 139)):

                temp_line_vals = split_line(line)
                temp_temp_temp_dict = {}

                for k,tv in enumerate(temp_value_list[1:]):

                    temp_var = tv
                    temp_unit = tv.split()
                    seperator = ' '
                    temp_title = seperator.join(temp_unit[0:(len(temp_unit)-1)])
                    temp_unit = temp_unit[len(temp_unit)-1].replace('(','').replace(')','')
                    temp_temp_temp_dict[temp_title] = {'Unit':temp_unit,'Value':temp_line_vals[k+1]}

                temp_temp_dict[temp_line_vals[0]] = temp_temp_temp_dict
                temp_dict[temp_value_list[0]] = temp_temp_dict

            elif (line_num == 140):

                temp_value_list = split_line(line)

            elif (line_num == 141): 

                temp_value_list2 = split_line(line)

                for i,tlv in enumerate(temp_value_list):

                    temp_value_list[i] = tlv + ' ' + temp_value_list2[i+1]

                temp_value_list.insert(0,temp_value_list2[0])
                temp_temp_dict2 = {}

            elif ((line_num >= 143) and (line_num <= 145)):

                temp_line_vals = split_line(line)
                temp_temp_temp_dict = {}

                for k,tv in enumerate(temp_value_list[1:]):

                    temp_var = tv

                    if (tv.split()[0] == 'Correlation'):
                        temp_title = temp_var
                        #temp_unit = 'N/A'
                        temp_temp_temp_dict[temp_title] = temp_line_vals[k+1]
                    else:
                        temp_unit = tv.split()
                        seperator = ' '
                        temp_title = seperator.join(temp_unit[0:(len(temp_unit)-1)])
                        temp_unit = temp_unit[len(temp_unit)-1]
                        temp_temp_temp_dict[temp_title] = {'Unit':temp_unit,'Value':temp_line_vals[k+1]}

                temp_temp_dict2[temp_line_vals[0]] = temp_temp_temp_dict
                temp_dict[temp_value_list[0]] = temp_temp_dict2

            elif ((line_num >= 148) and (line_num <= 150)):

                temp_key = line.split('=')[0].strip()
                temp_value = line.split('=')[1].split()[0]
                temp_unit = line.split('=')[1].split()[1]

                temp_dict[temp_key] = {'Value':temp_value,'Unit':temp_unit}

        elif ((new_header.split()[0] == 'Grid') and (len(line.split()) > 0)):

            if (line.split()[0] == 'Y-coord'):

                y_coord_list = line.split()[1:]
                temp_temp_dict = {}

            elif (line.split()[0] == 'Height'):

                if ('u' in line.split()):
                    current_comp = 'u'

                if ('v' in line.split()):
                    current_comp = 'v'

                if ('w' in line.split()):
                    current_comp = 'w'

            else:

                

            elif ((line_num >= 256) and (line_num <= 259)):
                
                if (line.split()[0] == 'Mean'):
                    temp_key = line.replace(':','').strip()
                    temp_temp_temp_dict = {}

                else:
                    temp_temp_key = line.split(':')[0].strip()
                    temp_var = line.split(':')[1].split()[0]
                    temp_unit = line.split(':')[1].split()[1]
                    temp_temp_temp_dict[temp_temp_key] = {'Unit':temp_unit,'Value':temp_var}
                
                    temp_temp_dict[temp_key] = temp_temp_temp_dict

                temp_dict = temp_temp_dict

            else (True):
                pass

        elif ((len(line.split()) == 0) and (line_num != 64) and (line_num != 71) and (line_num != 139)and (line_num != 146)and (line_num != 147)):

            if (len(temp_dict.keys()) > 0):

                new_dict[new_header] = temp_dict

            temp_dict = {}

    # Write the saved dictionary to a YAML output file
    with open(output_filename, 'w') as outfile:
        yaml.safe_dump(new_dict, output_file)

else: 

    pass

new_file.close()
output_file.close()
