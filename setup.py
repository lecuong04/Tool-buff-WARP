from distutils.core import setup
from configparser import ConfigParser
from shutil import copyfile
import py2exe
import sys

config_object  = ConfigParser()
config_object ['INFO'] = {'build': '1994',
                          'script_version': '6.7'}
with open('config.ini', 'w') as configfile:
    config_object.write(configfile)

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")
    
setup(
    options = {'py2exe': {'bundle_files': 1,
                          'compressed': 1}},
    console = [
        {
            "script": "main.py",
            "icon_resources": [(0, "icon.ico")]
        }
    ],
) 

copyfile('config.ini', 'dist\config.ini')