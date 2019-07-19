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

    temp_dict = self.create_outlist(self.data, 122)
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

    temp_string = self.write_outlist(in_dict, '  - ')
    file_string += temp_string

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
   
    temp_dict = self.create_val_un_dict(self.data, new_dict, temp_key_list, temp_unit_list, 'NTwInpSt')
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
    
    temp_string = self.write_val_un_table(in_dict, rearrange_list, tt_keys, 'HtFract')
    file_string += temp_string
      
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
   
    temp_dict = self.create_val_un_dict(self.data, new_dict, temp_key_list, temp_unit_list, 'NBlInpSt')
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
    
    temp_string = self.write_val_un_table(in_dict, rearrange_list, tt_keys, 'BlFract')
    file_string += temp_string
      
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
    
    temp_string = self.write_val_un_table(in_dict, rearrange_list, tt_keys, 'BlSpn')
    file_string += temp_string

    return file_string


class AOCInflowWind(BaseFile):
  """
  Input file for the inflow wind
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}

    new_dict['line1'] = self.data[0].strip()
    new_dict['line2'] = self.data[1].strip()
    
    key_list = [
      'Echo',          
      'WindType',      
      'PropagationDir',
      'NWindVel',      
      'WindVxiList',   
      'WindVyiList',   
      'WindVziList',   
      'HWindSpeed',    
      'RefHt',        
      'PLexp',         
      'Filename',    
      'RefHt',       
      'RefLength',   
      'Filename',    
      'FilenameRoot',
      'TowerFile',   
      'FileName_u',
      'FileName_v',
      'FileName_w',
      'nx',         
      'ny',         
      'nz',         
      'dx',         
      'dy',         
      'dz',         
      'RefHt',     
      'ScaleMethod',
      'SFx',        
      'SFy',        
      'SFz',        
      'SigmaFx',    
      'SigmaFy',    
      'SigmaFz',    
      'URef',       
      'WindProfile',
      'PLExp',      
      'Z0',         
      'SumPrint'   
    ] 

    sec_start_list = [3,11,15,19,21,24,35,43,48]
    length_list = [6,3,3,1,2,10,7,4,1]
    
    temp_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)
    new_dict.update(temp_dict)

    start_ind = 50
    end_ind = len(self.data)-2
    temp_dict = {}

    for i in range(start_ind,end_ind):
      current_line = self.data[i].split('  ')
      current_line = self.remove_whitespace_filter(current_line)
      temp_dict[current_line[0]] = current_line[1].strip()
    
    new_dict['OutList'] = temp_dict

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += in_dict['line1']
    file_string += '\n'
    file_string += in_dict['line2']
    file_string += '\n'
    file_string += '---------------------------------------------------------------------------------------------------------------\n'

    key_list = [
      'Echo',
      'WindType',
      'PropagationDir',
      'NWindVel',
      'WindVxiList',
      'WindVyiList',
      'WindVziList'
    ]

    desc_list = [
      '- Echo input data to <RootName>.ech (flag)',
      '- switch for wind file type (1=steady; 2=uniform; 3=binary TurbSim FF; 4=binary Bladed-style FF; 5=HAWC format; 6=User defined)',
      '- Direction of wind propagation (meteoroligical rotation from aligned with X (positive rotates towards -Y) -- degrees)',
      '- Number of points to output the wind velocity    (0 to 9)',
      '- List of coordinates in the inertial X direction (m)',
      '- List of coordinates in the inertial Y direction (m)',
      '- List of coordinates in the inertial Z direction (m)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '================== Parameters for Steady Wind Conditions [used only for WindType = 1] =========================\n'

    key_list = [
      'HWindSpeed',
      'RefHt',
      'PLexp'
    ]

    desc_list = [
      '- Horizontal windspeed                            (m/s)',
      '- Reference height for horizontal wind speed      (m)',
      '- Power law exponent                              (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '================== Parameters for Uniform wind file   [used only for WindType = 2] ============================\n'
    
    key_list = [
      'Filename',
      'RefHt',
      'RefLength'
    ]

    desc_list = [
      '- Filename of time series data for uniform wind field.      (-)',
      '- Reference height for horizontal wind speed                (m)',
      '- Reference length for linear horizontal and vertical sheer (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '================== Parameters for Binary TurbSim Full-Field files   [used only for WindType = 3] ==============\n'
    
    key_list = [
      'Filename'
    ]

    desc_list = [
      '- Name of the Full field wind file to use (.bts)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '================== Parameters for Binary Bladed-style Full-Field files   [used only for WindType = 4] =========\n'

    key_list = [
      'FilenameRoot',
      'TowerFile'
    ]

    desc_list = [
      '- Rootname of the full-field wind file to use (.wnd, .sum)',
      '- Have tower file (.twr) (flag)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '================== Parameters for HAWC-format binary files  [Only used with WindType = 5] =====================\n'

    key_list = [
      'FileName_u',
      'FileName_v',
      'FileName_w',
      'nx',
      'ny',
      'nz',
      'dx',
      'dy',
      'dz',
      'RefHt'
    ]

    desc_list = [
      '- name of the file containing the u-component fluctuating wind (.bin)',
      '- name of the file containing the v-component fluctuating wind (.bin)',
      '- name of the file containing the w-component fluctuating wind (.bin)',
      '- number of grids in the x direction (in the 3 files above) (-)',
      '- number of grids in the y direction (in the 3 files above) (-)',
      '- number of grids in the z direction (in the 3 files above) (-)',
      '- distance (in meters) between points in the x direction    (m)',
      '- distance (in meters) between points in the y direction    (m)',
      '- distance (in meters) between points in the z direction    (m)',
      '- reference height; the height (in meters) of the vertical center of the grid (m)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '  -------------   Scaling parameters for turbulence   ---------------------------------------------------------\n'

    key_list = [
      'ScaleMethod',
      'SFx',
      'SFy',
      'SFz',
      'SigmaFx',
      'SigmaFy',
      'SigmaFz'
    ]

    desc_list = [
      '- Turbulence scaling method   [0 = none, 1 = direct scaling, 2 = calculate scaling factor based on a desired standard deviation]',
      '- Turbulence scaling factor for the x direction (-)   [ScaleMethod=1]',
      '- Turbulence scaling factor for the y direction (-)   [ScaleMethod=1]',
      '- Turbulence scaling factor for the z direction (-)   [ScaleMethod=1]',
      '- Turbulence standard deviation to calculate scaling from in x direction (m/s)    [ScaleMethod=2]',
      '- Turbulence standard deviation to calculate scaling from in y direction (m/s)    [ScaleMethod=2]',
      '- Turbulence standard deviation to calculate scaling from in z direction (m/s)    [ScaleMethod=2]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '  -------------   Mean wind profile parameters (added to HAWC-format files)   ---------------------------------\n'

    key_list = [
      'URef',
      'WindProfile',
      'PLExp',
      'Z0'
    ]

    desc_list = [
      '- Mean u-component wind speed at the reference height (m/s)',
      '- Wind profile type (0=constant;1=logarithmic,2=power law)',
      '- Power law exponent (-) (used for PL wind profile type only)',
      '- Surface roughness length (m) (used for LG wind profile type only)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '====================== OUTPUT ==================================================\n'

    key_list = [
      'SumPrint'
    ]

    desc_list = [
      '- Print summary data to <RootName>.IfW.sum (flag)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    temp_string = self.write_outlist(in_dict, '  ')
    file_string += temp_string

    return file_string


class AOCServoDyn(BaseFile):
  """
  Input file for the servodyn
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}

    new_dict['line1'] = self.data[0].strip()
    new_dict['line2'] = self.data[1].strip()
    
    key_list = [
      'Echo', 
      'DT', 
      'PCMode', 
      'TPCOn', 
      'TPitManS(1)', 
      'TPitManS(2)', 
      'TPitManS(3)', 
      'PitManRat(1)', 
      'PitManRat(2)', 
      'PitManRat(3)', 
      'BlPitchF(1)', 
      'BlPitchF(2)', 
      'BlPitchF(3)', 
      'VSContrl', 
      'GenModel', 
      'GenEff', 
      'GenTiStr', 
      'GenTiStp', 
      'SpdGenOn', 
      'TimGenOn', 
      'TimGenOf', 
      'VS_RtGnSp', 
      'VS_RtTq', 
      'VS_Rgn2K', 
      'VS_SlPc', 
      'SIG_SlPc', 
      'SIG_SySp', 
      'SIG_RtTq', 
      'SIG_PORt', 
      'TEC_Freq', 
      'TEC_NPol', 
      'TEC_SRes', 
      'TEC_RRes', 
      'TEC_VLL', 
      'TEC_SLR', 
      'TEC_RLR', 
      'TEC_MR', 
      'HSSBrMode', 
      'THSSBrDp', 
      'HSSBrDT', 
      'HSSBrTqF', 
      'YCMode', 
      'TYCOn', 
      'YawNeut', 
      'YawSpr', 
      'YawDamp', 
      'TYawManS', 
      'YawManRat', 
      'NacYawF', 
      'CompNTMD', 
      'NTMDfile', 
      'CompTTMD', 
      'TTMDfile', 
      'DLL_FileName', 
      'DLL_InFile', 
      'DLL_ProcName', 
      'DLL_DT', 
      'DLL_Ramp', 
      'BPCutoff', 
      'NacYaw_North', 
      'Ptch_Cntrl', 
      'Ptch_SetPnt', 
      'Ptch_Min', 
      'Ptch_Max', 
      'PtchRate_Min', 
      'PtchRate_Max', 
      'Gain_OM', 
      'GenSpd_MinOM', 
      'GenSpd_MaxOM', 
      'GenSpd_Dem', 
      'GenTrq_Dem', 
      'GenPwr_Dem', 
      'DLL_NumTrq', 
      'SumPrint', 
      'OutFile', 
      'TabDelim', 
      'OutFmt', 
      'TStart'
    ] 

    sec_start_list = [3,6,18,27,32,37,46,51,60,65,85,89]
    length_list = [1,11,8,4,4,8,4,8,4,19,1,5]
    
    temp_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)
    new_dict.update(temp_dict)

    temp_dict = self.create_outlist(self.data, 95)
    new_dict['OutList'] = temp_dict

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += in_dict['line1']
    file_string += '\n'
    file_string += in_dict['line2']
    file_string += '\n'
    file_string += '---------------------- SIMULATION CONTROL --------------------------------------\n'

    key_list = [
      'Echo',
      'DT'
    ]

    desc_list = [
      '- Echo input data to <RootName>.ech (flag)',
      '- Communication interval for controllers (s) (or "default")'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- PITCH CONTROL -------------------------------------------\n'

    key_list = [
      'PCMode',
      'TPCOn',
      'TPitManS(1)',
      'TPitManS(2)',
      'TPitManS(3)',
      'PitManRat(1)',
      'PitManRat(2)',
      'PitManRat(3)',
      'BlPitchF(1)',
      'BlPitchF(2)',
      'BlPitchF(3)'
    ]

    desc_list = [
      '- Pitch control mode {0: none, 3: user-defined from routine PitchCntrl, 4: user-defined from Simulink/Labview, 5: user-defined from Bladed-style DLL} (switch)',
      '- Time to enable active pitch control (s) [unused when PCMode=0]',
      '- Time to start override pitch maneuver for blade 1 and end standard pitch control (s)',
      '- Time to start override pitch maneuver for blade 2 and end standard pitch control (s)',
      '- Time to start override pitch maneuver for blade 3 and end standard pitch control (s) [unused for 2 blades]',
      '- Pitch rate at which override pitch maneuver heads toward final pitch angle for blade 1 (deg/s)',
      '- Pitch rate at which override pitch maneuver heads toward final pitch angle for blade 2 (deg/s)',
      '- Pitch rate at which override pitch maneuver heads toward final pitch angle for blade 3 (deg/s) [unused for 2 blades]',
      '- Blade 1 final pitch for pitch maneuvers (degrees)',
      '- Blade 2 final pitch for pitch maneuvers (degrees)',
      '- Blade 3 final pitch for pitch maneuvers (degrees) [unused for 2 blades]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- GENERATOR AND TORQUE CONTROL ----------------------------\n'
    
    key_list = [
      'VSContrl',
      'GenModel',
      'GenEff',
      'GenTiStr',
      'GenTiStp',
      'SpdGenOn',
      'TimGenOn',
      'TimGenOf'
    ]

    desc_list = [
      '- Variable-speed control mode {0: none, 1: simple VS, 3: user-defined from routine UserVSCont, 4: user-defined from Simulink/Labview, 5: user-defined from Bladed-style DLL} (switch)',
      '- Generator model {1: simple, 2: Thevenin, 3: user-defined from routine UserGen} (switch) [used only when VSContrl=0]',
      '- Generator efficiency [ignored by the Thevenin and user-defined generator models] (%)',
      '- Method to start the generator {T: timed using TimGenOn, F: generator speed using SpdGenOn} (flag)',
      '- Method to stop the generator {T: timed using TimGenOf, F: when generator power = 0} (flag)',
      '- Generator speed to turn on the generator for a startup (HSS speed) (rpm) [used only when GenTiStr=False]',
      '- Time to turn on the generator for a startup (s) [used only when GenTiStr=True]',
      '- Time to turn off the generator (s) [used only when GenTiStp=True]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- SIMPLE VARIABLE-SPEED TORQUE CONTROL --------------------\n'
    
    key_list = [
      'VS_RtGnSp',
      'VS_RtTq',
      'VS_Rgn2K',
      'VS_SlPc'
    ]

    desc_list = [
      '- Rated generator speed for simple variable-speed generator control (HSS side) (rpm) [used only when VSContrl=1]',
      '- Rated generator torque/constant generator torque in Region 3 for simple variable-speed generator control (HSS side) (N-m) [used only when VSContrl=1]',
      '- Generator torque constant in Region 2 for simple variable-speed generator control (HSS side) (N-m/rpm^2) [used only when VSContrl=1]',
      '- Rated generator slip percentage in Region 2 1/2 for simple variable-speed generator control (%) [used only when VSContrl=1]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- SIMPLE INDUCTION GENERATOR ------------------------------\n'

    key_list = [
      'SIG_SlPc',
      'SIG_SySp',
      'SIG_RtTq',
      'SIG_PORt'
    ]

    desc_list = [
      '- Rated generator slip percentage (%) [used only when VSContrl=0 and GenModel=1]',
      '- Synchronous (zero-torque) generator speed (rpm) [used only when VSContrl=0 and GenModel=1]',
      '- Rated torque (N-m) [used only when VSContrl=0 and GenModel=1]',
      '- Pull-out ratio (Tpullout/Trated) (-) [used only when VSContrl=0 and GenModel=1]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- THEVENIN-EQUIVALENT INDUCTION GENERATOR -----------------\n'

    key_list = [
      'TEC_Freq',
      'TEC_NPol',
      'TEC_SRes',
      'TEC_RRes',
      'TEC_VLL',
      'TEC_SLR',
      'TEC_RLR',
      'TEC_MR'
    ]

    desc_list = [
      '- Line frequency [50 or 60] (Hz) [used only when VSContrl=0 and GenModel=2]',
      '- Number of poles [even integer > 0] (-) [used only when VSContrl=0 and GenModel=2]',
      '- Stator resistance (ohms) [used only when VSContrl=0 and GenModel=2]',
      '- Rotor resistance (ohms) [used only when VSContrl=0 and GenModel=2]',
      '- Line-to-line RMS voltage (volts) [used only when VSContrl=0 and GenModel=2]',
      '- Stator leakage reactance (ohms) [used only when VSContrl=0 and GenModel=2]',
      '- Rotor leakage reactance (ohms) [used only when VSContrl=0 and GenModel=2]',
      '- Magnetizing reactance (ohms) [used only when VSContrl=0 and GenModel=2]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- HIGH-SPEED SHAFT BRAKE ----------------------------------\n'

    key_list = [
      'HSSBrMode',
      'THSSBrDp',
      'HSSBrDT',
      'HSSBrTqF'
    ]

    desc_list = [
      '- HSS brake model {0: none, 1: simple, 3: user-defined from routine UserHSSBr, 4: user-defined from Simulink/Labview, 5: user-defined from Bladed-style DLL} (switch)',
      '- Time to initiate deployment of the HSS brake (s)',
      '- Time for HSS-brake to reach full deployment once initiated (sec) [used only when HSSBrMode=1]',
      '- Fully deployed HSS-brake torque (N-m) [unused when HSSBrMode=5]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- NACELLE-YAW CONTROL -------------------------------------\n'

    key_list = [
      'YCMode',
      'TYCOn',
      'YawNeut',
      'YawSpr',
      'YawDamp',
      'TYawManS',
      'YawManRat',
      'NacYawF'
    ]

    desc_list = [
      '- Yaw control mode {0: none, 3: user-defined from routine UserYawCont, 4: user-defined from Simulink/Labview, 5: user-defined from Bladed-style DLL} (switch)',
      '- Time to enable active yaw control (s) [unused when YCMode=0]',
      '- Neutral yaw position--yaw spring force is zero at this yaw (degrees)',
      '- Nacelle-yaw spring constant (N-m/rad)',
      '- Nacelle-yaw damping constant (N-m/(rad/s))',
      '- Time to start override yaw maneuver and end standard yaw control (s)',
      '- Yaw maneuver rate (in absolute value) (deg/s)',
      '- Final yaw angle for override yaw maneuvers (degrees)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- TUNED MASS DAMPER ---------------------------------------\n'

    key_list = [
      'CompNTMD',
      'NTMDfile',
      'CompTTMD',
      'TTMDfile'
    ]

    desc_list = [
      '- Compute nacelle tuned mass damper {true/false} (flag)',
      '- Name of the file for nacelle tuned mass damper (quoted string) [unused when CompNTMD is false]',
      '- Compute tower tuned mass damper {true/false} (flag)',
      '- Name of the file for tower tuned mass damper (quoted string) [unused when CompTTMD is false]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- BLADED INTERFACE ---------------------------------------- [used only with Bladed Interface]\n'

    key_list = [
      'DLL_FileName',
      'DLL_InFile',
      'DLL_ProcName',
      'DLL_DT',
      'DLL_Ramp',
      'BPCutoff',
      'NacYaw_North',
      'Ptch_Cntrl',
      'Ptch_SetPnt',
      'Ptch_Min',
      'Ptch_Max',
      'PtchRate_Min',
      'PtchRate_Max',
      'Gain_OM',
      'GenSpd_MinOM',
      'GenSpd_MaxOM',
      'GenSpd_Dem',
      'GenTrq_Dem',
      'GenPwr_Dem'
    ]

    desc_list = [
      '- Name/location of the dynamic library {.dll [Windows] or .so [Linux]} in the Bladed-DLL format (-) [used only with Bladed Interface]',
      '- Name of input file sent to the DLL (-) [used only with Bladed Interface]',
      '- Name of procedure in DLL to be called (-) [case sensitive; used only with DLL Interface]',
      '- Communication interval for dynamic library (s) (or "default") [used only with Bladed Interface]',
      '- Whether a linear ramp should be used between DLL_DT time steps [introduces time shift when true] (flag) [used only with Bladed Interface]',
      '- Cuttoff frequency for low-pass filter on blade pitch from DLL (Hz) [used only with Bladed Interface]',
      '- Reference yaw angle of the nacelle when the upwind end points due North (deg) [used only with Bladed Interface]',
      '- Record 28: Use individual pitch control {0: collective pitch; 1: individual pitch control} (switch) [used only with Bladed Interface]',
      '- Record  5: Below-rated pitch angle set-point (deg) [used only with Bladed Interface]',
      '- Record  6: Minimum pitch angle (deg) [used only with Bladed Interface]',
      '- Record  7: Maximum pitch angle (deg) [used only with Bladed Interface]',
      '- Record  8: Minimum pitch rate (most negative value allowed) (deg/s) [used only with Bladed Interface]',
      '- Record  9: Maximum pitch rate  (deg/s) [used only with Bladed Interface]',
      '- Record 16: Optimal mode gain (Nm/(rad/s)^2) [used only with Bladed Interface]',
      '- Record 17: Minimum generator speed (rpm) [used only with Bladed Interface]',
      '- Record 18: Optimal mode maximum speed (rpm) [used only with Bladed Interface]',
      '- Record 19: Demanded generator speed above rated (rpm) [used only with Bladed Interface]',
      '- Record 22: Demanded generator torque above rated (Nm) [used only with Bladed Interface]',
      '- Record 13: Demanded power (W) [used only with Bladed Interface]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += '---------------------- BLADED INTERFACE TORQUE-SPEED LOOK-UP TABLE -------------\n'

    key_list = [
      'DLL_NumTrq'
    ]

    desc_list = [
      '- Record 26: No. of points in torque-speed look-up table {0 = none and use the optimal mode parameters; nonzero = ignore the optimal mode PARAMETERs by setting Record 16 to 0.0} (-) [used only with Bladed Interface]'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    file_string += 'GenSpd_TLU   GenTrq_TLU\n'
    file_string += '(rpm)          (Nm)\n'

    file_string += '---------------------- OUTPUT --------------------------------------------------\n'

    key_list = [
      'SumPrint',
      'OutFile',
      'TabDelim',
      'OutFmt',
      'TStart'
    ]

    desc_list = [
      '- Print summary data to <RootName>.sum (flag) (currently unused)',
      '- Switch to determine where output will be placed: {1: in module output file only; 2: in glue code output file only; 3: both} (currently unused)',
      '- Use tab delimiters in text tabular output file? (flag) (currently unused)',
      '- Format used for text tabular output (except time).  Resulting field should be 10 characters. (quoted string) (currently unused)',
      '- Time to begin tabular output (s) (currently unused)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    temp_string = self.write_outlist(in_dict, '  - ')
    file_string += temp_string

    return file_string

class AOCAD(BaseFile):
  """
  Input file for the servodyn
  """

  def __init__(self, parent_directory, filename):
    super().__init__(parent_directory, filename)

  def read_t2y(self):

    new_dict = {}

    new_dict['line1'] = self.data[0].strip()
    new_dict['line2'] = self.data[1].strip()
    
    key_list = [
      'StallMod',
      'UseCm',
      'InfModel',
      'IndModel',
      'AToler',
      'TLModel',
      'HLModel',
      'TwrShad',
      'ShadHWid',
      'T_Shad_Refpt',
      'AirDens',
      'KinVisc',
      'DTAero',
      'NumFoil'
    ] 

    sec_start_list = [2]
    length_list = [14]
    
    temp_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)
    new_dict.update(temp_dict)

    new_dict['FoilNm'] = []
    new_dict['FoilNm'].append(self.data[16].split('  ')[0].strip())

    if (new_dict['NumFoil'] > 1):

      for ln in range(17,16+new_dict['NumFoil']):
        # print(ln)
        new_dict['FoilNm'].append(self.data[ln].strip())

    key_list = [
      'BldNodes'
    ] 

    sec_start_list = [16+new_dict['NumFoil']]
    length_list = [0]
    
    temp_dict = self.parse_filetype_valuefirst(self.data,key_list,sec_start_list,length_list)
    new_dict.update(temp_dict)

    temp_key_list = self.data[17+new_dict['NumFoil']].split()

    temp_dict = {}
    temp_temp_dict = {}
    for tk in temp_key_list:
      temp_temp_dict[tk] = []

    for i in range(self.convert_value(new_dict['BldNodes'])):
      
      for j, tk in enumerate(temp_key_list):
      
        temp_value = self.data[19+new_dict['NumFoil']+i-1].split()[j]
        temp_temp_dict[tk].append(self.convert_value(temp_value))
        temp_dict[tk] = {
          'Value': temp_temp_dict[tk]
        }

    new_dict['Matrix'] = temp_dict

    return new_dict
      
  def read_y2t(self):

    in_dict = self.data

    file_string = ''
    file_string += in_dict['line1']
    file_string += '\n'
    file_string += in_dict['line2']
    file_string += '\n'

    key_list = [
      'StallMod',
      'UseCm',
      'InfModel',
      'IndModel',
      'AToler',
      'TLModel',
      'HLModel',
      'TwrShad',
      'ShadHWid',
      'T_Shad_Refpt',
      'AirDens',
      'KinVisc',
      'DTAero',
      'NumFoil'
    ]

    desc_list = [
      '- Dynamic stall included [BEDDOES or STEADY] (unquoted string)',
      '- Use aerodynamic pitching moment model? [USE_CM or NO_CM] (unquoted string)',
      '- Inflow model [DYNIN or EQUIL] (unquoted string)',
      '- Induction-factor model [NONE or WAKE or SWIRL] (unquoted string)',
      '- Induction-factor tolerance (convergence criteria) (-)',
      '- Tip-loss model (EQUIL only) [PRANDtl, GTECH, or NONE] (unquoted string)',
      '- Hub-loss model (EQUIL only) [PRANdtl or NONE] (unquoted string)',
      '- Tower-shadow velocity deficit (-)',
      '- Tower-shadow half width (m)',
      '- Tower-shadow reference point (m)',
      '- Air density (kg/m^3)',
      '- Kinematic air viscosity [CURRENTLY IGNORED] (m^2/sec)',
      '- Time interval for aerodynamic calculations (sec)',
      '- Number of airfoil files (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    temp_string = in_dict['FoilNm'][0] + '  FoilNm  - Names of the airfoil files [NumFoil lines] (quoted strings)\n'
    file_string += temp_string

    for ts in in_dict['FoilNm'][1:]:
      file_string += ts
      file_string += '\n'

    key_list = [
      'BldNodes'
    ]

    desc_list = [
      '- Number of blade nodes used for analysis (-)'
    ]

    temp_string = self.write_valdesc(in_dict,key_list,desc_list,None)
    file_string += temp_string

    tt_keys = list(in_dict['Matrix'].keys())
    for i,tk in enumerate(tt_keys):
      if (tk == 'RNodes'):
        ind1 = i
      if (tk == 'AeroTwst'):
        ind2 = i
      if (tk == 'DRNodes'):
        ind3 = i
      if (tk == 'Chord'):
        ind4 = i  
      if (tk == 'NFoil'):
        ind5 = i  
      if (tk == 'PrnElm'):
        ind6 = i  
    rearrange_list = [ind1,ind2,ind3,ind4,ind5,ind6] 
    
    temp_string = self.write_val_un_table(in_dict, rearrange_list, tt_keys, 'RNodes', has_un=False)
    file_string += temp_string

    return file_string