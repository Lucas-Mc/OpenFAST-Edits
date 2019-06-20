# Lucas McCullum
# Rafael Mudafort
# NWTC
# June 19, 2019

import sys
from base_file import BaseFile

# Maybe use this in the future.. need some help deciding
# class TurbsimFile(BaseFile):
#   """
#   Super class for all Turbsim-related files.
#   """

#   def __init__(self, filename):

#     super().__init__(filename)
#     # output_filename = self.parse_filename(filename)
#     # output_filename = self.parse_filename(filename,'.dat','.yml')
#     # self.init_output_file(output_filename)


class TurbsimInputFile(BaseFile): # (TurbsimFile):
  """
  Primary input file for Turbsim.
  """

  def __init__(self, filename):

    try:

      super().__init__(filename)
      output_filename = self.parse_filename(filename,'.inp','.yml')
      self.init_output_file(output_filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')

  def read(self):

    new_dict = {}

    key_list = [
      'RandSeed1',      
      'RandSeed2',       
      'WrBHHTP',        
      'WrFHHTP',         
      'WrADHH',          
      'WrADFF',          
      'WrBLFF',          
      'WrADTWR',         
      'WrFMTFF',         
      'WrACT',           
      'Clockwise',       
      'ScaleIEC',        
      'NumGrid_Z',       
      'NumGrid_Y',
      'TimeStep',      
      'AnalysisTime',    
      'UsableTime',      
      'HubHt',           
      'GridHeight',      
      'GridWidth',
      'VFlowAng',
      'HFlowAng',       
      'TurbModel',       
      'IECstandard',     
      'IECturbc',        
      'IEC_WindType',    
      'ETMc',            
      'WindProfileType', 
      'RefHt',           
      'URef',            
      'ZJetMax',         
      'PLExp',           
      'Z0',              
      'Latitude',        
      'RICH_NO',         
      'UStar',           
      'ZI',             
      'PC_UW',           
      'PC_UV',           
      'PC_VW',           
      'IncDec1',         
      'IncDec2',         
      'IncDec3',         
      'CohExp',          
      'CTEventPath',     
      'CTEventFile',     
      'Randomize',       
      'DistScl',         
      'CTLy',            
      'CTLz',            
      'CTStartTime'  
    ]

    sec_start_list = [3,17,29,42,55]
    length_list = [11,10,11,11,7]
    current_sec_ind = 0
    current_line_ind = 0

    for i,k in enumerate(key_list):

      current_line = sec_start_list[current_sec_ind] + current_line_ind
      new_dict[k] = self.data[current_line].split()[0]
      current_line_ind += 1

      if (i >= sum(length_list[:(current_sec_ind+1)])):

        current_sec_ind += 1
        current_line_ind = 0

    # sec_start = 3
    # new_dict['RandSeed1'] = self.data[sec_start].split()[0]
    # new_dict['RandSeed2'] = self.data[sec_start+1].split()[0]
    # new_dict['WrBHHTP'] = self.data[sec_start+2].split()[0]
    # new_dict['WrFHHTP'] = self.data[sec_start+3].split()[0]
    # new_dict['WrADHH'] = self.data[sec_start+4].split()[0]
    # new_dict['WrADFF'] = self.data[sec_start+5].split()[0]
    # new_dict['WrBLFF'] = self.data[sec_start+6].split()[0]
    # new_dict['WrADTWR'] = self.data[sec_start+7].split()[0]
    # new_dict['WrFMTFF'] = self.data[sec_start+8].split()[0]
    # new_dict['WrACT'] = self.data[sec_start+9].split()[0]
    # new_dict['Clockwise'] = self.data[sec_start+10].split()[0]
    # new_dict['ScaleIEC'] = self.data[sec_start+11].split()[0]

    # sec_start = 17
    # new_dict['NumGrid_Z'] = self.data[sec_start].split()[0]
    # new_dict['NumGrid_Y'] = self.data[sec_start+1].split()[0]
    # new_dict['TimeStep'] = self.data[sec_start+2].split()[0]
    # new_dict['AnalysisTime'] = self.data[sec_start+3].split()[0]
    # new_dict['UsableTime'] = self.data[sec_start+4].split()[0]
    # new_dict['HubHt'] = self.data[sec_start+5].split()[0]
    # new_dict['GridHeight'] = self.data[sec_start+6].split()[0]
    # new_dict['GridWidth'] = self.data[sec_start+7].split()[0]
    # new_dict['VFlowAng'] = self.data[sec_start+8].split()[0]
    # new_dict['HFlowAng'] = self.data[sec_start+9].split()[0]
   
    # sec_start = 29
    # new_dict['TurbModel'] = self.data[sec_start].split()[0]
    # new_dict['IECstandard'] = self.data[sec_start+1].split()[0]
    # new_dict['IECturbc'] = self.data[sec_start+2].split()[0]
    # new_dict['IEC_WindType'] = self.data[sec_start+3].split()[0]
    # new_dict['ETMc'] = self.data[sec_start+4].split()[0]
    # new_dict['WindProfileType'] = self.data[sec_start+5].split()[0]
    # new_dict['RefHt'] = self.data[sec_start+6].split()[0]
    # new_dict['URef'] = self.data[sec_start+7].split()[0]
    # new_dict['ZJetMax'] = self.data[sec_start+8].split()[0]
    # new_dict['PLExp'] = self.data[sec_start+9].split()[0]
    # new_dict['Z0'] = self.data[sec_start+10].split()[0]

    # sec_start = 42
    # new_dict['Latitude'] = self.data[sec_start].split()[0]
    # new_dict['RICH_NO'] = self.data[sec_start+1].split()[0]
    # new_dict['UStar'] = self.data[sec_start+2].split()[0]
    # new_dict['ZI'] = self.data[sec_start+3].split()[0]
    # new_dict['PC_UW'] = self.data[sec_start+4].split()[0]
    # new_dict['PC_UV'] = self.data[sec_start+5].split()[0]
    # new_dict['PC_VW'] = self.data[sec_start+6].split()[0]
    # new_dict['IncDec1'] = self.data[sec_start+7].split()[0]
    # new_dict['IncDec2'] = self.data[sec_start+8].split()[0]
    # new_dict['IncDec3'] = self.data[sec_start+9].split()[0]
    # new_dict['CohExp'] = self.data[sec_start+10].split()[0]

    # sec_start = 55
    # new_dict['CTEventPath'] = self.data[sec_start].split()[0]
    # new_dict['CTEventFile'] = self.data[sec_start+1].split()[0]
    # new_dict['Randomize'] = self.data[sec_start+2].split()[0]
    # new_dict['DistScl'] = self.data[sec_start+3].split()[0]
    # new_dict['CTLy'] = self.data[sec_start+4].split()[0]
    # new_dict['CTLz'] = self.data[sec_start+5].split()[0]
    # new_dict['CTStartTime'] = self.data[sec_start+6].split()[0]



    # new_dict = {}
    # temp_dict = {}
    # # output_file.write('# '+data[0])
        
    # for line in self.data[2:]:

    #   if (line[0] == '-'):

    #     new_header = self.remove_char(line,['-','\n'])
          
    #   elif ((len(line.split()) > 0) and (line[0] != '=')):
          
    #     new_line = line.split()
    #     temp_value = new_line[0]
    #     temp_key = new_line[1]
    #     description = self.combine_text_spaces(new_line[3:]).replace('"','\'')
    #     temp_dict[temp_key] = {'Value':self.convert_value(temp_value),'Description':description}

    #   elif (len(line.split()) == 0):

    #     new_dict[new_header] = temp_dict
    #     temp_dict = {}

    #   else: 
          
    #     pass
        
    return new_dict

class TurbsimSummaryFile(BaseFile): # (TurbsimFile):
  """
  Primary summary file for Turbsim.
  """

  def __init__(self, filename):

    try:

      super().__init__(filename)
      output_filename = self.parse_filename(filename,'.sum','.yml')
      self.init_output_file(output_filename)

    except:

      print('Oops!',sys.exc_info(),'occured.')
      
  def read(self):

    new_dict = {}
    temp_dict = {}
    temp_2d_array = []
    # output_file.write('# '+data[1])

    for line in self.data[4:]:

      fl = line[0]
      
      if (fl.isalnum()):

        new_header = self.remove_char(line,[':','\n'])
        temp_dict = {} 

        if (new_header.split()[0] == 'Nyquist'):

          new_header,temp_value,temp_unit = self.sep_string_double(line,'=',' ')
          temp_dict = {'Unit':temp_unit,'Value':self.convert_value(temp_value)} 

        elif (new_header.split()[0] == 'Processing'):

          new_header = 'Processing Time'
          temp_key = line.split()
          temp_unit = self.remove_char(self.combine_text_spaces(temp_key[3:-1]),['.']) 
          temp_value = temp_key[2]
          temp_dict = {'Unit':temp_unit,'Value':self.convert_value(temp_value)}
          new_dict[new_header] = temp_dict

      elif (((new_header.split()[0] == 'Runtime') or (new_header.split()[0] == 'Turbine/Model') or (new_header.split()[0] == 'Meteorological')) and (len(line.split()) > 0)):

        temp_value = line.split()[0]

        if (temp_value == '0'):

          temp_value = '0 -  NONE'
          temp_var = line.split()[3:]

        else:

          temp_var = line.split()[1:]

        temp_key = self.combine_text_spaces(temp_var)
        
        if ('[' in temp_key):

          temp_var = temp_key.split()
          temp_unit = self.remove_brackets(temp_var[len(temp_var)-1])
          temp_key = self.combine_text_spaces(temp_var[0:(len(temp_var)-1)])
          
          if (temp_value != 'N/A'):

            temp_dict[temp_key] = {'Unit':temp_unit,'Value':self.convert_value(temp_value)}
          
          else:

            temp_dict[temp_key] = {'Unit':temp_unit,'Value':temp_value}
        
        else: 

          temp_dict[temp_key] = self.convert_value(temp_value)

      elif ((new_header.split()[0] == 'You') and (len(line.split()) > 0)):

        temp_dict = {}
        temp_line = line.split()
        temp_dict['File name'] = temp_line[0]
        temp_dict['File type'] = self.remove_parens(self.combine_text_spaces(temp_line[1:]))

      elif ((new_header.split()[0] == 'Turbulence') and (len(line.split()) > 0)):

        temp_key,temp_value = self.sep_string(line,'=')

        if ((len(temp_value.split()) > 1) and (self.is_int(temp_value.split()[0]) or self.is_float(temp_value.split()[0]))):
            
          temp_var,temp_unit = self.sep_string(temp_value,' ')
          temp_dict[temp_key] = {'Unit':temp_unit,'Value':self.convert_value(temp_var)}
        
        else:
            
            if ('%' in temp_value):

              temp_var = temp_value[:-1]
              temp_unit = '%'
              temp_dict[temp_key] = {'Unit':temp_unit,'Value':self.convert_value(temp_var)}
          
            else:

              temp_dict[temp_key] = self.convert_value(temp_value)

      elif ((new_header.split()[0] == 'Mean') and (new_header.split()[1] == 'Flow') and (len(line.split()) > 0)):

        temp_key,temp_value,temp_unit = self.sep_string_double(line,'=',' ')
        temp_dict[temp_key] = {'Unit':temp_unit,'Value':self.convert_value(temp_value)}            

      elif ((new_header.split()[0] == 'Mean') and (new_header.split()[1] == 'Wind') and (len(line.split()) > 0)):

        if (line.split()[0] == 'Height'):

          temp_value_list = self.split_line(line)

        elif (line.split()[0] == '(m)'):

          temp_unit_list = line.split()
          temp_unit_list = [self.remove_parens(i) for i in temp_unit_list]           

        elif (line.count('-') == 0):

          temp_vals = line.split()
          temp_2d_array.append(temp_vals)

          for i,tv in enumerate(temp_value_list):

            temp_list = []

            for j in range(len(temp_2d_array)):

              temp_list.append(self.convert_value(temp_2d_array[j][i]))

            temp_dict[tv] = {'Unit':temp_unit_list[i],'Value':temp_list}

      elif ((new_header.split()[0] == 'Harvested') and (len(line.split()) > 0)):

        temp_value,temp_key = self.sep_string(line,' ')
        temp_dict[temp_key] = self.convert_value(temp_value)

      elif ((new_header.split()[0] == 'Hub-Height') and (len(line.split()) > 0) and (line.count('-') < 6)):

        if (line.split()[0] == 'Type'):

            temp_value_list = self.split_line(line)
            temp_temp_dict = {}

        elif (line.split()[0] == 'Min'):

            temp_value_list = self.split_line(line)

        elif (line.split()[0] == 'Product'): 

            temp_value_list2 = self.split_line(line)

            for i,tlv in enumerate(temp_value_list):

                temp_value_list[i] = tlv + ' ' + temp_value_list2[i+1]

            temp_value_list.insert(0,temp_value_list2[0])
            temp_temp_dict2 = {}

        elif (line.count("'") == 2):

          temp_line_vals = self.split_line(line)
          temp_temp_temp_dict = {}

          for k,tv in enumerate(temp_value_list[1:]):

            temp_var = tv

            if (tv.split()[0] == 'Correlation'):

              temp_title = temp_var
              temp_temp_temp_dict[temp_title] = self.convert_value(temp_line_vals[k+1])
            
            else:

              temp_unit = tv.split()
              temp_title = self.combine_text_spaces(temp_unit[0:(len(temp_unit)-1)])
              temp_unit = temp_unit[len(temp_unit)-1]
              temp_temp_temp_dict[temp_title] = {'Unit':temp_unit,'Value':self.convert_value(temp_line_vals[k+1])}

          temp_temp_dict2[temp_line_vals[0]] = temp_temp_temp_dict
          temp_dict[temp_value_list[0]] = temp_temp_dict2

        elif (line.count('=') == 1):

          temp_key,temp_value,temp_unit = self.sep_string_double(line,'=',' ')
          temp_dict[temp_key] = {'Value':self.convert_value(temp_value),'Unit':temp_unit}

        else: 

            temp_line_vals = self.split_line(line)
            temp_temp_temp_dict = {}

            for k,tv in enumerate(temp_value_list[1:]):

                temp_var = tv
                temp_unit = tv.split()
                temp_title = self.combine_text_spaces(temp_unit[0:(len(temp_unit)-1)])
                temp_unit = self.remove_parens(temp_unit[len(temp_unit)-1]) 
                temp_temp_temp_dict[temp_title] = {'Unit':temp_unit,'Value':self.convert_value(temp_line_vals[k+1])}

            temp_temp_dict[temp_line_vals[0]] = temp_temp_temp_dict
            temp_dict[temp_value_list[0]] = temp_temp_dict


      elif ((new_header.split()[0] == 'Grid') and (len(line.split()) > 0)):

        if (line.split()[0] == 'Y-coord'):

          y_coord_list = line.split()[1:]
          temp_temp_dict = {}

        elif (line.split()[0] == 'Height'):

          current_title = line.split()[1:]
          current_title = self.remove_char(self.combine_text_spaces(current_title),[':'])
          ch = 0
          temp_temp_temp_dict = {}
            
        elif (line.split()[0] == 'Mean'):

          temp_key = self.remove_char(line,[':']).strip()
          temp_temp_temp_dict = {}

        elif ((line.count('.') > 1) and ('Y-coord' not in line)):

          for i,current_y in enumerate(y_coord_list):
              
            current_height = line.split()[0]
            current_value = line.split()[i+1]

            current_GP = 'GP' + '_' + str(ch) + '_' + str(i)
            temp_temp_temp_dict[current_GP] = {'Height':self.convert_value(current_height),'Y-coord':self.convert_value(current_y),'Value':self.convert_value(current_value)}
            temp_temp_dict[current_title] = temp_temp_temp_dict

          temp_dict = temp_temp_dict
          ch += 1

        else:

          temp_temp_key,temp_var,temp_unit = self.sep_string_double(line,':',' ')
          temp_temp_temp_dict[temp_temp_key] = {'Unit':temp_unit,'Value':self.convert_value(temp_var)}
          temp_temp_dict[temp_key] = temp_temp_temp_dict

        temp_dict = temp_temp_dict

      elif ((new_header.split()[0] == 'U-component') and (len(line.split()) > 0)):

        temp_key,temp_value,temp_unit = self.sep_string_double(line,'=',' ')
        temp_dict[temp_key] = {'Unit':temp_unit,'Value':self.convert_value(temp_value)} 

      elif ((len(line.split()) == 0)):

        if (len(temp_dict.keys()) > 0):

          new_dict[new_header] = temp_dict
  
    return new_dict

