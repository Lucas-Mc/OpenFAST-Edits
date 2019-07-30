from base_file import BaseFile


class TurbsimSumFile(BaseFile):

  def __init__(self,filename):

    super().__init__(filename)
    self.output_filename = self.parse_filename(filename,'.sum','.yml')

  def read(self):

    new_dict = {}
    temp_dict = {}
    temp_2d_array = []

    for line_num,line in enumerate(self.data[4:]):

      fl = line[0]
      
      if (fl.isalnum()):

        new_header = self.remove_char(line,[':','\n']) 

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

      elif (line_num == 47):

        temp_dict = {}
        temp_line = line.split()
        temp_dict['File name'] = temp_line[0]
        temp_dict['File type'] = self.remove_parens(self.combine_text_spaces(temp_line[1:]))
        new_dict['Generated File'] = temp_dict

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

        if (line_num == 82):

          temp_value_list = self.split_line(line)

        elif (line_num == 83):

          temp_unit_list = line.split()
          temp_unit_list = [self.remove_parens(i) for i in temp_unit_list]           

        elif ((line_num >= 85)):

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

      elif ((new_header.split()[0] == 'Hub-Height') and (len(line.split()) > 0)):

          if (line_num == 129):

              temp_value_list = self.split_line(line)
              temp_temp_dict = {}

          elif ((line_num >= 131) and (line_num <= 139)):

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

          elif (line_num == 140):

              temp_value_list = self.split_line(line)

          elif (line_num == 141): 

              temp_value_list2 = self.split_line(line)

              for i,tlv in enumerate(temp_value_list):

                  temp_value_list[i] = tlv + ' ' + temp_value_list2[i+1]

              temp_value_list.insert(0,temp_value_list2[0])
              temp_temp_dict2 = {}

          elif ((line_num >= 143) and (line_num <= 145)):

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

      elif ((line_num >= 148) and (line_num <= 150)):

        temp_key,temp_value,temp_unit = self.sep_string_double(line,'=',' ')
        temp_dict[temp_key] = {'Value':self.convert_value(temp_value),'Unit':temp_unit}

      elif ((new_header.split()[0] == 'Grid') and (len(line.split()) > 0)):

        if (line.split()[0] == 'Y-coord'):

          y_coord_list = line.split()[1:]
          temp_temp_dict = {}

        elif (line.split()[0] == 'Height'):

          current_title = line.split()[1:]
          current_title = self.remove_char(self.combine_text_spaces(current_title),[':'])
          ch = 0
          temp_temp_temp_dict = {}

        elif ((line_num >= 256) and (line_num <= 259)):
            
          if (line.split()[0] == 'Mean'):

            temp_key = self.remove_char(line,[':']).strip()
            temp_temp_temp_dict = {}

          else:

            temp_temp_key,temp_var,temp_unit = self.sep_string_double(line,':',' ')
            temp_temp_temp_dict[temp_temp_key] = {'Unit':temp_unit,'Value':self.convert_value(temp_var)}
            temp_temp_dict[temp_key] = temp_temp_temp_dict

          temp_dict = temp_temp_dict

        else:

          for i,current_y in enumerate(y_coord_list):
              
            current_height = line.split()[0]
            current_value = line.split()[i+1]

            current_GP = 'GP' + '_' + str(ch) + '_' + str(i)
            temp_temp_temp_dict[current_GP] = {'Height':self.convert_value(current_height),'Y-coord':self.convert_value(current_y),'Value':self.convert_value(current_value)}
            temp_temp_dict[current_title] = temp_temp_temp_dict

          temp_dict = temp_temp_dict
          ch += 1

      elif ((new_header.split()[0] == 'U-component') and (len(line.split()) > 0)):

        temp_key,temp_value,temp_unit = self.sep_string_double(line,'=',' ')
        temp_dict[temp_key] = {'Unit':temp_unit,'Value':self.convert_value(temp_value)} 

      elif ((len(line.split()) == 0) and (line_num != 64) and (line_num != 70) and (line_num != 139)and (line_num != 146)and (line_num != 147)):

        if (len(temp_dict.keys()) > 0):

          new_dict[new_header] = temp_dict

        temp_dict = {}
  
    return new_dict

