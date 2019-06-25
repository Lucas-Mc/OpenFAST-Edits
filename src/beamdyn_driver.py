
import os
from stat import ST_MODE

class BeamdynDriver():
  def __init__(self, executable_path):
    # Verify that the executable exists
    if not os.path.isfile(executable_path):
      raise OSError(2, "Driver file does not exist", executable_path)

    # Verify that the executable can be executed
    permissionsMask = oct(os.stat(executable_path)[ST_MODE])[-1:]
    if not int(permissionsMask) % 2 == 1:
      raise OSError(1, "Driver file cannot be executed", executable_path)

    self.executable_path = executable_path
