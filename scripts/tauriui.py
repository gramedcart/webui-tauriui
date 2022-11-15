import os
import sys
from modules import scripts
import subprocess

if sys.platform.startswith('win32'):
    print('Opening TauriUI')
    child  = subprocess.Popen(os.path.join(scripts.basedir(), 'files','tauriUI-win.exe'))
else:
    print("TauriUI is'nt supported in {sys.platform}")
