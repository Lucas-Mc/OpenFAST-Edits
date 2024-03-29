from base_file import BaseFile


class TurbsimInputFile(BaseFile):

    def __init__(self,filename):
        super().__init__(filename)
        output_filename = filename.split('/')[len(filename.split('/'))-1].replace('.inp','.yml')
        #output_filename = output_filename.replace('.sum','.yml').replace('.','_sum.')
        self.init_output_file(output_filename)

    def read(self):
        new_dict = {}
        temp_dict = {}
        #output_file.write('# '+data[0])
            
        for line in self.data[2:]:

            if (line[0] == '-'):

                new_header = self.remove_char(line,['-','\n'])
                
            elif ((len(line.split()) > 0) and (line[0] != '=')):
                
                new_line = line.split()
                temp_value = new_line[0]
                temp_key = new_line[1]
                description = self.combine_text_spaces(new_line[3:]).replace('"','\'')
                temp_dict[temp_key] = {'Value':temp_value,'Description':description}

            elif (len(line.split()) == 0):

                new_dict[new_header] = temp_dict
                temp_dict = {}

            else: 
                
                pass
            
        return new_dict
