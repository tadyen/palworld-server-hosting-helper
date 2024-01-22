#!/usr/bin/python3

# Converts PalWorldSettings.ini to the actual .ini file for the PalWorld server
# The output location is in Pal/Saved/Config/<Windows|Linux>Server/PalWorldSettings.ini.
# The transpilation must be in CRLF (Windows) format even if the server build is Linux

import sys, io, os, shutil

def osname():
  match sys.platform:
    case 'win32':
      return "Windows"
    case _:
      return "Linux"
OS = osname()

PALWORLD_SETTINGS_FILENAME = "PalWorldSettings.ini"
PALWORLD_SETTINGS_DESTINATION = f"Pal/Saved/Config/{OS}Server/PalWorldSettings.ini"
TMP_FILENAME = 'tmpfile'

# replace with path to PalServer
# eg. "C:\ProgramFiles\Steam\steamapps\common\PalServer" or "/home/steam/Steam/SteamApps/common/PalServer"
PALSERVER_PATH = "C:\Intricate Installation\Steam\steamapps\common\PalServer"

with open(PALWORLD_SETTINGS_FILENAME, "r") as f:
  lines = f.read().splitlines()
  lines = [ l.split(';')[0].strip() for l in lines ]
  out = ''.join(lines).replace(']', ']\n')

with io.open(TMP_FILENAME, 'w', newline='\r\n') as f:
  f.write(f'{out}')

dest_path = os.path.join(
  PALSERVER_PATH,
  PALWORLD_SETTINGS_DESTINATION
)
dest_path = os.path.normpath(dest_path)

shutil.move(TMP_FILENAME, dest_path)
