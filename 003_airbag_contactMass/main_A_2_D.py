# Load the module
from vortex_radioss.animtod3plot.Anim_to_D3plot import readAndConvert
  
# Use the file stem e.g for "folder/fileA001", "folder/fileA002" would be:
readAndConvert("/mnt/c/work/001_CAE/openradioss/work/20240524_airbag/003_airbag_contactMass/500_main")

# The D3plots files "folder/file.d3plot*" will be generated