
from src.beamdyn_files import BeamdynDriverFile
from src.beamdyn_files import BeamdynPrimaryFile
from src.beamdyn_files import BeamdynBladeFile

# this script converts the input files for a BeamDyn driver case
# into yaml files for use with this Python wrapper

case_directory = "/Users/rmudafor/Development/OpenFAST-Edits//bd_curved_beam/"
bd_input_files = [
    BeamdynDriverFile(case_directory + "bd_driver.inp"),
    BeamdynPrimaryFile(case_directory + "bd_primary.inp"),
    BeamdynBladeFile(case_directory + "beam_props.inp")
]

for f in bd_input_files:
    f.init_output_file(f.filename + ".yml")
    f.to_yaml(f.read_t2y())
