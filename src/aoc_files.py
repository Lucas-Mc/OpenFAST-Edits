import sys
import yaml
from src.base_file import BaseFile

class AOCFstFile(BaseFile):
  """
  Input file for the openfast driver
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}
    
    key_list = [
      'Echo',          
      'AbortLevel',    
      'TMax',          
      'DT',            
      'InterpOrder',   
      'NumCrctn',     
      'DT_UJac',       
      'UJacSclFact',   
      'CompElast',     
      'CompInflow',    
      'CompAero',      
      'CompServo',     
      'CompHydro',     
      'CompSub',       
      'CompMooring',   
      'CompIce',       
      'EDFile',        
      'BDBldFile(1)',  
      'BDBldFile(2)',  
      'BDBldFile(3)',  
      'InflowFile',    
      'AeroFile',      
      'ServoFile',     
      'HydroFile',     
      'SubFile',       
      'MooringFile',   
      'IceFile',    
      'SumPrint',    
      'SttsTime',    
      'ChkptTime',    
      'DT_Out',    
      'TStart',    
      'OutFileFmt',    
      'TabDelim',    
      'OutFmt',    
      'Linearize',    
      'NLinTimes',    
      # 'LinTimes',    
      'LinInputs', 
      'LinOutputs', 
      'LinOutJac', 
      'LinOutMod', 
      'WrVTK', 
      'VTK_type', 
      'VTK_fields', 
      'VTK_fps'
    ] 

    sec_start_list = [3,12,21,33,42,45,50]
    length_list = [7,8,11,8,2,4,4]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)

    matching = list(filter(lambda x: 'LinTimes' in x, self.data))
    # data_length = self.convert_value(matching[0].split()[0])
    temp_ln = matching[1].split('LinTimes')[0].split(',')
    final_ln = [self.convert_value(ln.strip()) for ln in temp_ln]
    new_dict['LinTimes'] = final_ln

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += '------- OpenFAST example INPUT FILE -------------------------------------------\n'
    # TODO: should this be dynamic?
    file_string += 'FAST Certification Test #01: AWT-27CR2 with many DOFs with fixed yaw error and steady wind\n'
    file_string += '---------------------- SIMULATION CONTROL --------------------------------------\n'
    
    key_list = [
      'Echo',  
      'AbortLevel',  
      'TMax',  
      'DT',  
      'InterpOrder',  
      'NumCrctn',  
      'DT_UJac',  
      'UJacSclFact'  
    ]

    desc_list = [
      '- Echo input data to <RootName>.ech (flag)',
      '- Error level when simulation should abort (string) {"WARNING", "SEVERE", "FATAL"}',
      '- Total run time (s)',
      '- Recommended module time step (s)',
      '- Interpolation order for input/output time history (-) {1=linear, 2=quadratic}',
      '- Number of correction iterations (-) {0=explicit calculation, i.e., no corrections}',
      '- Time between calls to get Jacobians (s)',
      '- Scaling factor used in Jacobians (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- FEATURE SWITCHES AND FLAGS ------------------------------\n'

    key_list = [
      'CompElast',
      'CompInflow',
      'CompAero',
      'CompServo',
      'CompHydro',
      'CompSub',
      'CompMooring',
      'CompIce'
    ]

    desc_list = [
      '- Compute structural dynamics (switch) {1=ElastoDyn; 2=ElastoDyn + BeamDyn for blades}',
      '- Compute inflow wind velocities (switch) {0=still air; 1=InflowWind; 2=external from OpenFOAM}',
      '- Compute aerodynamic loads (switch) {0=None; 1=AeroDyn v14; 2=AeroDyn v15}',
      '- Compute control and electrical-drive dynamics (switch) {0=None; 1=ServoDyn}',
      '- Compute hydrodynamic loads (switch) {0=None; 1=HydroDyn}',
      '- Compute sub-structural dynamics (switch) {0=None; 1=SubDyn; 2=External Platform MCKF}',
      '- Compute mooring system (switch) {0=None; 1=MAP++; 2=FEAMooring; 3=MoorDyn; 4=OrcaFlex}',
      '- Compute ice loads (switch) {0=None; 1=IceFloe; 2=IceDyn}'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- INPUT FILES ---------------------------------------------\n'
    
    key_list = [
      'EDFile',
      'BDBldFile(1)',
      'BDBldFile(2)',
      'BDBldFile(3)',
      'InflowFile',
      'AeroFile',
      'ServoFile',
      'HydroFile',
      'SubFile',
      'MooringFile',
      'IceFile'
    ]

    desc_list = [
      '- Name of file containing ElastoDyn input parameters (quoted string)',
      '- Name of file containing BeamDyn input parameters for blade 1 (quoted string)',
      '- Name of file containing BeamDyn input parameters for blade 2 (quoted string)',
      '- Name of file containing BeamDyn input parameters for blade 3 (quoted string)',
      '- Name of file containing inflow wind input parameters (quoted string)',
      '- Name of file containing aerodynamic input parameters (quoted string)',
      '- Name of file containing control and electrical-drive input parameters (quoted string)',
      '- Name of file containing hydrodynamic input parameters (quoted string)',
      '- Name of file containing sub-structural input parameters (quoted string)',
      '- Name of file containing mooring system input parameters (quoted string)',
      '- Name of file containing ice input parameters (quoted string)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- OUTPUT --------------------------------------------------\n'
    
    key_list = [
      'SumPrint',
      'SttsTime',
      'ChkptTime',
      'DT_Out',
      'TStart',
      'OutFileFmt',
      'TabDelim',
      'OutFmt'
    ]

    desc_list = [
      '- Print summary data to "<RootName>.sum" (flag)',
      '- Amount of time between screen status messages (s)',
      '- Amount of time between creating checkpoint files for potential restart (s)',
      '- Time step for tabular output (s) (or "default")',
      '- Time to begin tabular output (s)',
      '- Format for tabular (time-marching) output file (switch) {1: text file [<RootName>.out], 2: binary file [<RootName>.outb], 3: both}',
      '- Use tab delimiters in text tabular output file? (flag) {uses spaces if false}',
      '- Format used for text tabular output, excluding the time channel.  Resulting field should be 10 characters. (quoted string)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- LINEARIZATION -------------------------------------------\n'

    key_list = [
      'Linearize',
      'NLinTimes'
    ]

    desc_list = [
      '- Linearization analysis (flag)',
      '- Number of times to linearize (-) [>=1] [unused if Linearize=False]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    for i,num in enumerate(in_dict['LinTimes']):
      if (i != len(in_dict['LinTimes'])-1):
        temp_string = str(num) + ',  '
        file_string += temp_string
      else:
        temp_string = str(num) + '  '
        file_string += temp_string

    file_string += 'LinTimes        - List of times at which to linearize (s) [1 to NLinTimes] [unused if Linearize=False]\n'

    key_list = [
      'LinInputs',
      'LinOutputs',
      'LinOutJac',
      'LinOutMod'
    ]

    desc_list = [
      '- Inputs included in linearization (switch) {0=none; 1=standard; 2=all module inputs (debug)} [unused if Linearize=False]',
      '- Outputs included in linearization (switch) {0=none; 1=from OutList(s); 2=all module outputs (debug)} [unused if Linearize=False]',
      '- Include full Jacobians in linearization output (for debug) (flag) [unused if Linearize=False; used only if LinInputs=LinOutputs=2]',
      '- Write module-level linearization output files in addition to output for full system? (flag) [unused if Linearize=False]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- VISUALIZATION ------------------------------------------\n'

    key_list = [
      'WrVTK',
      'VTK_type',
      'VTK_fields',
      'VTK_fps'
    ]

    desc_list = [
      '- VTK visualization data output: (switch) {0=none; 1=initialization data only; 2=animation}',
      '- Type of VTK visualization data: (switch) {1=surfaces; 2=basic meshes (lines/points); 3=all meshes (debug)} [unused if WrVTK=0]',
      '- Write mesh fields to VTK data files? (flag) {true/false} [unused if WrVTK=0]',
      '- Frame rate for VTK output (frames per second){will use closest integer multiple of DT} [used only if WrVTK=2]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    return file_string

class AOCElastoDynFile(BaseFile):
  """
  Input file for the openfast driver
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}
    
    key_list = [
      'Echo',  
      'Method',  
      'DT',  
      'Gravity',  
      'FlapDOF1',  
      'FlapDOF2',  
      'EdgeDOF',  
      'TeetDOF',  
      'DrTrDOF',  
      'GenDOF',  
      'YawDOF',  
      'TwFADOF1',  
      'TwFADOF2',  
      'TwSSDOF1',  
      'TwSSDOF2',  
      'PtfmSgDOF',  
      'PtfmSwDOF',  
      'PtfmHvDOF',  
      'PtfmRDOF',  
      'PtfmPDOF',  
      'PtfmYDOF',  
      'OoPDefl',  
      'IPDefl',  
      'BlPitch(1)',  
      'BlPitch(2)',  
      'BlPitch(3)',  
      'TeetDefl',  
      'Azimuth',  
      'RotSpeed',  
      'NacYaw',  
      'TTDspFA',  
      'TTDspSS',  
      'PtfmSurge',  
      'PtfmSway',  
      'PtfmHeave',  
      'PtfmRoll',  
      'PtfmPitch',  
      'PtfmYaw',  
      'NumBl',  
      'TipRad',  
      'HubRad',  
      'PreCone(1)',  
      'PreCone(2)',  
      'PreCone(3)',  
      'HubCM',  
      'UndSling',  
      'Delta3',  
      'AzimB1Up',  
      'OverHang',  
      'ShftGagL',  
      'ShftTilt',  
      'NacCMxn',  
      'NacCMyn',  
      'NacCMzn',  
      'NcIMUxn',  
      'NcIMUyn',  
      'NcIMUzn',  
      'Twr2Shft',  
      'TowerHt',  
      'TowerBsHt',  
      'PtfmCMxt',  
      'PtfmCMyt',  
      'PtfmCMzt',  
      'PtfmRefzt',  
      'TipMass(1)',  
      'TipMass(2)',  
      'TipMass(3)',  
      'HubMass',  
      'HubIner',  
      'GenIner',  
      'NacMass',  
      'NacYIner',  
      'YawBrMass',  
      'PtfmMass',  
      'PtfmRIner',  
      'PtfmPIner',  
      'PtfmYIner',  
      'BldNodes',  
      'BldFile(1)',  
      'BldFile(2)',  
      'BldFile(3)',  
      'TeetMod',  
      'TeetDmpP',  
      'TeetDmp',  
      'TeetCDmp',  
      'TeetSStP',  
      'TeetHStP',  
      'TeetSSSp',  
      'TeetHSSp',  
      'GBoxEff',  
      'GBRatio',  
      'DTTorSpr',  
      'DTTorDmp',  
      'Furling',  
      'FurlFile',  
      'TwrNodes',  
      'TwrFile',  
      'SumPrint',  
      'OutFile',  
      'TabDelim',  
      'OutFmt',  
      'TStart',  
      'DecFact',  
      'NTwGages',  
      'TwrGagNd',  
      'NBlGages'  
    ] 

    # matching = list(filter(lambda x: 'NTwInpSt' in x, self.data))
    # data_length = self.convert_value(matching[0].split()[0])
    sec_start_list = [3,7,9,27,45,72,86,91,100,105,108,111]
    length_list = [2,1,17,17,26,13,4,8,4,2,2,9]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)

    temp_ln = self.data[120].split('BldGagNd')[0].split(',')
    final_ln = [self.convert_value(ln.strip()) for ln in temp_ln]
    new_dict['BldGagNd'] = final_ln

    start_ind = 122
    end_ind = len(self.data)-2
    temp_dict = {}

    for i in range(start_ind,end_ind):
      current_line = self.data[i]
      temp_dict[current_line.split('  ')[0]] = current_line.split('-',1)[1].strip()
    
    new_dict['OutList'] = temp_dict

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += '------- ELASTODYN v1.03.* INPUT FILE -------------------------------------------\n'
    # TODO: should this be dynamic?
    file_string += 'FAST certification Test #06: AOC 15/50 with many DOFs with gen start loss of grid and tip-brake shutdown. Many parameters are pure fiction.\n'
    file_string += '---------------------- SIMULATION CONTROL --------------------------------------\n'
    
    key_list = [
      'Echo',  
      'Method',
      'DT' 
    ]

    desc_list = [
      '- Echo input data to "<RootName>.ech" (flag)',
      '- Integration method: {1: RK4, 2: AB4, or 3: ABM4} (-)',
      '- Integration time step (s)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- ENVIRONMENTAL CONDITION ---------------------------------\n'

    key_list = [
      'Gravity'
    ]

    desc_list = [
      '- Gravitational acceleration (m/s^2)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- DEGREES OF FREEDOM --------------------------------------\n'
    
    key_list = [
      'FlapDOF1',
      'FlapDOF2',
      'EdgeDOF',
      'TeetDOF',
      'DrTrDOF',
      'GenDOF',
      'YawDOF',
      'TwFADOF1',
      'TwFADOF2',
      'TwSSDOF1',
      'TwSSDOF2',
      'PtfmSgDOF',
      'PtfmSwDOF',
      'PtfmHvDOF',
      'PtfmRDOF',
      'PtfmPDOF',
      'PtfmYDOF'
    ]

    desc_list = [
      '- First flapwise blade mode DOF (flag)',
      '- Second flapwise blade mode DOF (flag)',
      '- First edgewise blade mode DOF (flag)',
      '- Rotor-teeter DOF (flag) [unused for 3 blades]',
      '- Drivetrain rotational-flexibility DOF (flag)',
      '- Generator DOF (flag)',
      '- Yaw DOF (flag)',
      '- First fore-aft tower bending-mode DOF (flag)',
      '- Second fore-aft tower bending-mode DOF (flag)',
      '- First side-to-side tower bending-mode DOF (flag)',
      '- Second side-to-side tower bending-mode DOF (flag)',
      '- Platform horizontal surge translation DOF (flag)',
      '- Platform horizontal sway translation DOF (flag)',
      '- Platform vertical heave translation DOF (flag)',
      '- Platform roll tilt rotation DOF (flag)',
      '- Platform pitch tilt rotation DOF (flag)',
      '- Platform yaw rotation DOF (flag)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- INITIAL CONDITIONS --------------------------------------\n'
    
    key_list = [
      'OoPDefl',
      'IPDefl',
      'BlPitch(1)',
      'BlPitch(2)',
      'BlPitch(3)',
      'TeetDefl',
      'Azimuth',
      'RotSpeed',
      'NacYaw',
      'TTDspFA',
      'TTDspSS',
      'PtfmSurge',
      'PtfmSway',
      'PtfmHeave',
      'PtfmRoll',
      'PtfmPitch',
      'PtfmYaw',
    ]

    desc_list = [
      '- Initial out-of-plane blade-tip displacement (meters)',
      '- Initial in-plane blade-tip deflection (meters)',
      '- Blade 1 initial pitch (degrees)',
      '- Blade 2 initial pitch (degrees)',
      '- Blade 3 initial pitch (degrees) [unused for 2 blades]',
      '- Initial or fixed teeter angle (degrees) [unused for 3 blades]',
      '- Initial azimuth angle for blade 1 (degrees)',
      '- Initial or fixed rotor speed (rpm)',
      '- Initial or fixed nacelle-yaw angle (degrees)',
      '- Initial fore-aft tower-top displacement (meters)',
      '- Initial side-to-side tower-top displacement (meters)',
      '- Initial or fixed horizontal surge translational displacement of platform (meters)',
      '- Initial or fixed horizontal sway translational displacement of platform (meters)',
      '- Initial or fixed vertical heave translational displacement of platform (meters)',
      '- Initial or fixed roll tilt rotational displacement of platform (degrees)',
      '- Initial or fixed pitch tilt rotational displacement of platform (degrees)',
      '- Initial or fixed yaw rotational displacement of platform (degrees)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- TURBINE CONFIGURATION -----------------------------------\n'

    key_list = [
      'NumBl',
      'TipRad',
      'HubRad',
      'PreCone(1)',
      'PreCone(2)',
      'PreCone(3)',
      'HubCM',
      'UndSling',
      'Delta3',
      'AzimB1Up',
      'OverHang',
      'ShftGagL',
      'ShftTilt',
      'NacCMxn',
      'NacCMyn',
      'NacCMzn',
      'NcIMUxn',
      'NcIMUyn',
      'NcIMUzn',
      'Twr2Shft',
      'TowerHt',
      'TowerBsHt',
      'PtfmCMxt',
      'PtfmCMyt',
      'PtfmCMzt',
      'PtfmRefzt'
    ]

    desc_list = [
      '- Number of blades (-)',
      '- The distance from the rotor apex to the blade tip (meters)',
      '- The distance from the rotor apex to the blade root (meters)',
      '- Blade 1 cone angle (degrees)',
      '- Blade 2 cone angle (degrees)',
      '- Blade 3 cone angle (degrees) [unused for 2 blades]',
      '- Distance from rotor apex to hub mass [positive downwind] (meters)',
      '- Undersling length [distance from teeter pin to the rotor apex] (meters) [unused for 3 blades]',
      '- Delta-3 angle for teetering rotors (degrees) [unused for 3 blades]',
      '- Azimuth value to use for I/O when blade 1 points up (degrees)',
      '- Distance from yaw axis to rotor apex [3 blades] or teeter pin [2 blades] (meters)',
      '- Distance from rotor apex [3 blades] or teeter pin [2 blades] to shaft strain gages [positive for upwind rotors] (meters)',
      '- Rotor shaft tilt angle (degrees)',
      '- Downwind distance from the tower-top to the nacelle CM (meters)',
      '- Lateral  distance from the tower-top to the nacelle CM (meters)',
      '- Vertical distance from the tower-top to the nacelle CM (meters)',
      '- Downwind distance from the tower-top to the nacelle IMU (meters)',
      '- Lateral  distance from the tower-top to the nacelle IMU (meters)',
      '- Vertical distance from the tower-top to the nacelle IMU (meters)',
      '- Vertical distance from the tower-top to the rotor shaft (meters)',
      '- Height of tower above ground level [onshore] or MSL [offshore] (meters)',
      '- Height of tower base above ground level [onshore] or MSL [offshore] (meters)',
      '- Downwind distance from the ground level [onshore] or MSL [offshore] to the platform CM (meters)',
      '- Lateral distance from the ground level [onshore] or MSL [offshore] to the platform CM (meters)',
      '- Vertical distance from the ground level [onshore] or MSL [offshore] to the platform CM (meters)',
      '- Vertical distance from the ground level [onshore] or MSL [offshore] to the platform reference point (meters)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- MASS AND INERTIA ----------------------------------------\n'

    key_list = [
      'TipMass(1)',
      'TipMass(2)',
      'TipMass(3)',
      'HubMass',
      'HubIner',
      'GenIner',
      'NacMass',
      'NacYIner',
      'YawBrMass',
      'PtfmMass',
      'PtfmRIner',
      'PtfmPIner',
      'PtfmYIner'
    ]

    desc_list = [
      '- Tip-brake mass, blade 1 (kg)',
      '- Tip-brake mass, blade 2 (kg)',
      '- Tip-brake mass, blade 3 (kg) [unused for 2 blades]',
      '- Hub mass (kg)',
      '- Hub inertia about rotor axis [3 blades] or teeter axis [2 blades] (kg m^2)',
      '- Generator inertia about HSS (kg m^2)',
      '- Nacelle mass (kg)',
      '- Nacelle inertia about yaw axis (kg m^2)',
      '- Yaw bearing mass (kg)',
      '- Platform mass (kg)',
      '- Platform inertia for roll tilt rotation about the platform CM (kg m^2)',
      '- Platform inertia for pitch tilt rotation about the platform CM (kg m^2)',
      '- Platform inertia for yaw rotation about the platform CM (kg m^2)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- BLADE ---------------------------------------------------\n'

    key_list = [
      'BldNodes',
      'BldFile(1)',
      'BldFile(2)',
      'BldFile(3)'
    ]

    desc_list = [
      '- Number of blade nodes (per blade) used for analysis (-)',
      '- Name of file containing properties for blade 1 (quoted string)',
      '- Name of file containing properties for blade 2 (quoted string)',
      '- Name of file containing properties for blade 3 (quoted string) [unused for 2 blades]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- ROTOR-TEETER --------------------------------------------\n'

    key_list = [
      'TeetMod',
      'TeetDmpP',
      'TeetDmp',
      'TeetCDmp',
      'TeetSStP',
      'TeetHStP',
      'TeetSSSp',
      'TeetHSSp'
    ]

    desc_list = [
      '- Rotor-teeter spring/damper model {0: none, 1: standard, 2: user-defined from routine UserTeet} (switch) [unused for 3 blades]',
      '- Rotor-teeter damper position (degrees) [used only for 2 blades and when TeetMod=1]',
      '- Rotor-teeter damping constant (N-m/(rad/s)) [used only for 2 blades and when TeetMod=1]',
      '- Rotor-teeter rate-independent Coulomb-damping moment (N-m) [used only for 2 blades and when TeetMod=1]',
      '- Rotor-teeter soft-stop position (degrees) [used only for 2 blades and when TeetMod=1]',
      '- Rotor-teeter hard-stop position (degrees) [used only for 2 blades and when TeetMod=1]',
      '- Rotor-teeter soft-stop linear-spring constant (N-m/rad) [used only for 2 blades and when TeetMod=1]',
      '- Rotor-teeter hard-stop linear-spring constant (N-m/rad) [used only for 2 blades and when TeetMod=1]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- DRIVETRAIN ----------------------------------------------\n'

    key_list = [
      'GBoxEff',
      'GBRatio',
      'DTTorSpr',
      'DTTorDmp'
    ]

    desc_list = [
      '- Gearbox efficiency (%)',
      '- Gearbox ratio (-)',
      '- Drivetrain torsional spring (N-m/rad)',
      '- Drivetrain torsional damper (N-m/(rad/s))'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- FURLING -------------------------------------------------\n'

    key_list = [
      'Furling',
      'FurlFile'
    ]

    desc_list = [
      '- Read in additional model properties for furling turbine (flag) [must currently be FALSE)',
      '- Name of file containing furling properties (quoted string) [unused when Furling=False]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- TOWER ---------------------------------------------------\n'

    key_list = [
      'TwrNodes',
      'TwrFile'
    ]

    desc_list = [
      '- Number of tower nodes used for analysis (-)',
      '- Name of file containing tower properties (quoted string)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- OUTPUT --------------------------------------------------\n'

    key_list = [
      'SumPrint',
      'OutFile',
      'TabDelim',
      'OutFmt',
      'TStart',
      'DecFact',
      'NTwGages',
      'TwrGagNd',
      'NBlGages'
    ]

    desc_list = [
      '- Print summary data to "<RootName>.sum" (flag)',
      '- Switch to determine where output will be placed: {1: in module output file only; 2: in glue code output file only; 3: both} (currently unused)',
      '- Use tab delimiters in text tabular output file? (flag) (currently unused)',
      '- Format used for text tabular output (except time).  Resulting field should be 10 characters. (quoted string) (currently unused)',
      '- Time to begin tabular output (s) (currently unused)',
      '- Decimation factor for tabular output {1: output every time step} (-) (currently unused)',
      '- Number of tower nodes that have strain gages for output [0 to 9] (-)',
      '- List of tower nodes that have strain gages [1 to TwrNodes] (-) [unused if NTwGages=0]',
      '- Number of blade nodes that have strain gages for output [0 to 9] (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    for i,num in enumerate(in_dict['BldGagNd']):
      if (i != len(in_dict['BldGagNd'])-1):
        temp_string = str(num) + ',  '
        file_string += temp_string
      else:
        temp_string = str(num) + '  '
        file_string += temp_string
    
    file_string += 'BldGagNd    - List of blade nodes that have strain gages [1 to BldNodes] (-) [unused if NBlGages=0]\n'

    file_string += 'OutList     - The next line(s) contains a list of output parameters.  See OutListParameters.xlsx for a listing of available output channels, (-)\n'
    for outp in in_dict['OutList'].keys():
      file_string += outp
      file_string += '  - '
      file_string += in_dict['OutList'][outp]
      file_string += '\n'

    file_string += 'END of input file (the word "END" must appear in the first 3 columns of this last OutList line)\n'
    file_string += '---------------------------------------------------------------------------------------\n'

    return file_string


class AOCTowerFile(BaseFile):
  """
  Input file for the AOC module
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}
    
    key_list = [
      'NTwInpSt',
      'TwrFADmp(1)',
      'TwrFADmp(2)',
      'TwrSSDmp(1)',
      'TwrSSDmp(2)',
      'FAStTunr(1)',
      'FAStTunr(2)',
      'SSStTunr(1)',
      'SSStTunr(2)',
      'AdjTwMa',
      'AdjFASt',
      'AdjSSSt',
      'TwFAM1Sh(2)',
      'TwFAM1Sh(3)',
      'TwFAM1Sh(4)',
      'TwFAM1Sh(5)',
      'TwFAM1Sh(6)',
      'TwFAM2Sh(2)',
      'TwFAM2Sh(3)',
      'TwFAM2Sh(4)',
      'TwFAM2Sh(5)',
      'TwFAM2Sh(6)',
      'TwSSM1Sh(2)',
      'TwSSM1Sh(3)',
      'TwSSM1Sh(4)',
      'TwSSM1Sh(5)',
      'TwSSM1Sh(6)',
      'TwSSM2Sh(2)',
      'TwSSM2Sh(3)',
      'TwSSM2Sh(4)',
      'TwSSM2Sh(5)',
      'TwSSM2Sh(6)'
    ]

    matching = list(filter(lambda x: 'NTwInpSt' in x, self.data))
    data_length = self.convert_value(matching[0].split()[0])
    sec_start_list = [3,9,data_length+20,data_length+31]
    length_list = [4,7,10,10]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)

    temp_key_list = self.data[17].split()
    temp_unit_list = self.remove_parens(self.data[18].split())
   
    temp_dict = {}
    temp_temp_dict = {}
    for tk in temp_key_list:
      temp_temp_dict[tk] = []

    for i in range(self.convert_value(new_dict['NTwInpSt'])):
      
      for j, tk in enumerate(temp_key_list):
      
        temp_value = self.data[20+i-1].split()[j]
        temp_temp_dict[tk].append(self.convert_value(temp_value))
        temp_dict[tk] = {
          'Value': temp_temp_dict[tk],
          'Unit': temp_unit_list[j]
        }

    new_dict['Matrix'] = temp_dict

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += '------- ELASTODYN V1.00.* TOWER INPUT FILE -------------------------------------\n'
    # TODO: should this be dynamic?
    file_string += 'AOC tower data.  This is pure fiction.\n'
    file_string += '---------------------- TOWER PARAMETERS ----------------------------------------\n'
    
    key_list = [
      'NTwInpSt',
      'TwrFADmp(1)',
      'TwrFADmp(2)',
      'TwrSSDmp(1)',
      'TwrSSDmp(2)'
    ]

    desc_list = [
      '- Number of input stations to specify tower geometry',
      '- Tower 1st fore-aft mode structural damping ratio (%)',
      '- Tower 2nd fore-aft mode structural damping ratio (%)',
      '- Tower 1st side-to-side mode structural damping ratio (%)',
      '- Tower 2nd side-to-side mode structural damping ratio (%)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- TOWER ADJUSTMUNT FACTORS --------------------------------\n'

    key_list = [
      'FAStTunr(1)', 
      'FAStTunr(2)', 
      'SSStTunr(1)', 
      'SSStTunr(2)', 
      'AdjTwMa', 
      'AdjFASt', 
      'AdjSSSt'        
    ]

    desc_list = [
      '- Tower fore-aft modal stiffness tuner, 1st mode (-)',
      '- Tower fore-aft modal stiffness tuner, 2nd mode (-)',
      '- Tower side-to-side stiffness tuner, 1st mode (-)',
      '- Tower side-to-side stiffness tuner, 2nd mode (-)',
      '- Factor to adjust tower mass density (-)',
      '- Factor to adjust tower fore-aft stiffness (-)',
      '- Factor to adjust tower side-to-side stiffness (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- DISTRIBUTED TOWER PROPERTIES ----------------------------\n'
    
    tt_keys = list(in_dict['Matrix'].keys())
    for i,tk in enumerate(tt_keys):
      if (tk == 'HtFract'):
        ind1 = i
      if (tk == 'TMassDen'):
        ind2 = i
      if (tk == 'TwFAStif'):
        ind3 = i
      if (tk == 'TwSSStif'):
        ind4 = i  
    rearrange_list = [ind1,ind2,ind3,ind4] 
    
    temp_keys = []
    for i,v in enumerate(rearrange_list):
      temp_keys.append(tt_keys[v])

    temp_string = ''
    for tk in temp_keys:
      temp_string += '  '
      temp_string += tk
    file_string += temp_string
    file_string += '\n'

    temp_string = ''
    for tk in temp_keys:
      tu = in_dict['Matrix'][tk]['Unit']
      temp_string += '  '
      ind_string = '(' + tu + ')'
      temp_string +=ind_string
    file_string += temp_string
    file_string += '\n'

    num_vals = len(in_dict['Matrix']['HtFract']['Value'])

    for i in range(num_vals):
      temp_string = ''
      for tk in temp_keys:
        temp_string += str(in_dict['Matrix'][tk]['Value'][i])
        temp_string += '  '
      file_string += temp_string
      file_string += '\n'
      
    file_string += '---------------------- TOWER FORE-AFT MODE SHAPES ------------------------------\n'
    
    key_list = [
      'TwFAM1Sh(2)',
      'TwFAM1Sh(3)',
      'TwFAM1Sh(4)',
      'TwFAM1Sh(5)',
      'TwFAM1Sh(6)',
      'TwFAM2Sh(2)',
      'TwFAM2Sh(3)',
      'TwFAM2Sh(4)',
      'TwFAM2Sh(5)',
      'TwFAM2Sh(6)'
    ]

    desc_list = [
      '- Mode 1, coefficient of x^2 term',
      '-       , coefficient of x^3 term',
      '-       , coefficient of x^4 term',
      '-       , coefficient of x^5 term',
      '-       , coefficient of x^6 term',
      '- Mode 2, coefficient of x^2 term',
      '-       , coefficient of x^3 term',
      '-       , coefficient of x^4 term',
      '-       , coefficient of x^5 term',
      '-       , coefficient of x^6 term'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- TOWER SIDE-TO-SIDE MODE SHAPES --------------------------\n'

    key_list = [
      'TwSSM1Sh(2)',
      'TwSSM1Sh(3)',
      'TwSSM1Sh(4)',
      'TwSSM1Sh(5)',
      'TwSSM1Sh(6)',
      'TwSSM2Sh(2)',
      'TwSSM2Sh(3)',
      'TwSSM2Sh(4)',
      'TwSSM2Sh(5)',
      'TwSSM2Sh(6)'
    ]

    desc_list = [
      '- Mode 1, coefficient of x^2 term',
      '-       , coefficient of x^3 term',
      '-       , coefficient of x^4 term',
      '-       , coefficient of x^5 term',
      '-       , coefficient of x^6 term',
      '- Mode 2, coefficient of x^2 term',
      '-       , coefficient of x^3 term',
      '-       , coefficient of x^4 term',
      '-       , coefficient of x^5 term',
      '-       , coefficient of x^6 term'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    return file_string


class AOCBladeFile(BaseFile):
  """
  AOC file decsribing a blade.
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)
  
  def read_t2y(self):

    new_dict = {}
    
    key_list = [
      'NBlInpSt',
      'BldFlDmp(1)',
      'BldFlDmp(2)',
      'BldEdDmp(1)',
      'FlStTunr(1)',
      'FlStTunr(2)',
      'AdjBlMs',
      'AdjFlSt',
      'AdjEdSt',
      'BldFl1Sh(2)',
      'BldFl1Sh(3)',
      'BldFl1Sh(4)',
      'BldFl1Sh(5)',
      'BldFl1Sh(6)',
      'BldFl2Sh(2)',
      'BldFl2Sh(3)',
      'BldFl2Sh(4)',
      'BldFl2Sh(5)',
      'BldFl2Sh(6)',
      'BldEdgSh(2)',
      'BldEdgSh(3)',
      'BldEdgSh(4)',
      'BldEdgSh(5)',
      'BldEdgSh(6)'
    ]

    matching = list(filter(lambda x: 'NBlInpSt' in x, self.data))
    data_length = self.convert_value(matching[0].split()[0])
    sec_start_list = [3,8,data_length+17]
    length_list = [3,5,15]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)

    temp_key_list = self.data[14].split()
    temp_unit_list = self.remove_parens(self.data[15].split())
   
    temp_dict = {}
    temp_temp_dict = {}
    for tk in temp_key_list:
      temp_temp_dict[tk] = []

    for i in range(self.convert_value(new_dict['NBlInpSt'])):
      
      for j, tk in enumerate(temp_key_list):
      
        temp_value = self.data[17+i-1].split()[j]
        temp_temp_dict[tk].append(self.convert_value(temp_value))
        temp_dict[tk] = {
          'Value': temp_temp_dict[tk],
          'Unit': temp_unit_list[j]
        }

    new_dict['Matrix'] = temp_dict

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += '------- ELASTODYN V1.00.* INDIVIDUAL BLADE INPUT FILE --------------------------\n'
    # TODO: should this be dynamic?
    file_string += 'AOC 15/50 blade file.  GJStiff -> EdgEAof are mostly lies.\n'
    file_string += '---------------------- BLADE PARAMETERS ----------------------------------------\n'
    
    key_list = [
      'NBlInpSt',
      'BldFlDmp(1)',
      'BldFlDmp(2)',
      'BldEdDmp(1)'
    ]

    desc_list = [
      '- Number of blade input stations (-)',
      '- Blade flap mode #1 structural damping in percent of critical (%)',
      '- Blade flap mode #2 structural damping in percent of critical (%)',
      '- Blade edge mode #1 structural damping in percent of critical (%)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- BLADE ADJUSTMENT FACTORS --------------------------------\n'

    key_list = [
      'FlStTunr(2)',
      'FlStTunr(1)',
      'AdjBlMs',
      'AdjFlSt',
      'AdjEdSt'
    ]

    desc_list = [
      '- Blade flapwise modal stiffness tuner, 1st mode (-)',
      '- Blade flapwise modal stiffness tuner, 2nd mode (-)',
      '- Factor to adjust blade mass density (-)',
      '- Factor to adjust blade flap stiffness (-)',
      '- Factor to adjust blade edge stiffness (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- DISTRIBUTED BLADE PROPERTIES ----------------------------\n'
    
    tt_keys = list(in_dict['Matrix'].keys())
    for i,tk in enumerate(tt_keys):
      if (tk == 'BlFract'):
        ind1 = i
      if (tk == 'PitchAxis'):
        ind2 = i
      if (tk == 'StrcTwst'):
        ind3 = i
      if (tk == 'BMassDen'):
        ind4 = i  
      if (tk == 'FlpStff'):
        ind5 = i  
      if (tk == 'EdgStff'):
        ind6 = i  
    rearrange_list = [ind1,ind2,ind3,ind4,ind5,ind6] 
    
    temp_keys = []
    for i,v in enumerate(rearrange_list):
      temp_keys.append(tt_keys[v])

    temp_string = ''
    for tk in temp_keys:
      temp_string += '  '
      temp_string += tk
    file_string += temp_string
    file_string += '\n'

    temp_string = ''
    for tk in temp_keys:
      tu = in_dict['Matrix'][tk]['Unit']
      temp_string += '  '
      ind_string = '(' + tu + ')'
      temp_string +=ind_string
    file_string += temp_string
    file_string += '\n'

    num_vals = len(in_dict['Matrix']['BlFract']['Value'])

    for i in range(num_vals):
      temp_string = ''
      for tk in temp_keys:
        temp_string += str(in_dict['Matrix'][tk]['Value'][i])
        temp_string += '  '
      file_string += temp_string
      file_string += '\n'
      
    file_string += '---------------------- BLADE MODE SHAPES ---------------------------------------\n'
    
    key_list = [
      'BldFl1Sh(2)',
      'BldFl1Sh(3)',
      'BldFl1Sh(4)',
      'BldFl1Sh(5)',
      'BldFl1Sh(6)',
      'BldFl2Sh(2)',
      'BldFl2Sh(3)',
      'BldFl2Sh(4)',
      'BldFl2Sh(5)',
      'BldFl2Sh(6)',
      'BldEdgSh(2)',
      'BldEdgSh(3)',
      'BldEdgSh(4)',
      'BldEdgSh(5)',
      'BldEdgSh(6)'
    ]

    desc_list = [
      '- Flap mode 1, coeff of x^2',
      '-            , coeff of x^3',
      '-            , coeff of x^4',
      '-            , coeff of x^5',
      '-            , coeff of x^6',
      '- Flap mode 2, coeff of x^2',
      '-            , coeff of x^3',
      '-            , coeff of x^4',
      '-            , coeff of x^5',
      '-            , coeff of x^6',
      '- Edge mode 1, coeff of x^2',
      '-            , coeff of x^3',
      '-            , coeff of x^4',
      '-            , coeff of x^5',
      '-            , coeff of x^6'
   ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    return file_string


class AOCBladeADFile(BaseFile):
  """
  AOC file decsribing the blade aerodynamic parameters.
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}

    key_list = [
      'NumBlNds'
    ]
    
    matching = list(filter(lambda x: 'NumBlNds' in x, self.data))
    # data_length = self.convert_value(matching[0].split()[0])
    sec_start_list = [3]
    length_list = [0]
    
    new_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)

    temp_key_list = self.data[4].split()
    temp_unit_list = self.remove_parens(self.data[5].split())
   
    temp_dict = {}
    temp_temp_dict = {}
    for tk in temp_key_list:
      temp_temp_dict[tk] = []

    for i in range(self.convert_value(new_dict['NumBlNds'])):
      
      for j, tk in enumerate(temp_key_list):
      
        temp_value = self.data[7+i-1].split()[j]
        temp_temp_dict[tk].append(self.convert_value(temp_value))
        temp_dict[tk] = {
          'Value': temp_temp_dict[tk],
          'Unit': temp_unit_list[j]
        }

    new_dict['Matrix'] = temp_dict

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += '------- AERODYN v15.00.* BLADE DEFINITION INPUT FILE -------------------------------------\n'
    # TODO: should this be dynamic?
    file_string += 'AOC blade aerodynamic parameters\n'
    file_string += '======  Blade Properties =================================================================\n'
    
    key_list = [
      'NumBlNds'
    ]

    desc_list = [
      '- Number of blade nodes used in the analysis (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    tt_keys = list(in_dict['Matrix'].keys())
    for i,tk in enumerate(tt_keys):
      if (tk == 'BlSpn'):
        ind1 = i
      if (tk == 'BlCrvAC'):
        ind2 = i
      if (tk == 'BlSwpAC'):
        ind3 = i
      if (tk == 'BlCrvAng'):
        ind4 = i  
      if (tk == 'BlTwist'):
        ind5 = i  
      if (tk == 'BlChord'):
        ind6 = i  
      if (tk == 'BlAFID'):
        ind7 = i 
    rearrange_list = [ind1,ind2,ind3,ind4,ind5,ind6,ind7] 
    
    temp_keys = []
    for i,v in enumerate(rearrange_list):
      temp_keys.append(tt_keys[v])

    temp_string = ''
    for tk in temp_keys:
      temp_string += '  '
      temp_string += tk
    file_string += temp_string
    file_string += '\n'

    temp_string = ''
    for tk in temp_keys:
      tu = in_dict['Matrix'][tk]['Unit']
      temp_string += '  '
      ind_string = '(' + tu + ')'
      temp_string +=ind_string
    file_string += temp_string
    file_string += '\n'

    num_vals = len(in_dict['Matrix']['BlSpn']['Value'])

    for i in range(num_vals):
      temp_string = ''
      for tk in temp_keys:
        temp_string += str(in_dict['Matrix'][tk]['Value'][i])
        temp_string += '  '
      file_string += temp_string
      file_string += '\n'
      
    return file_string


