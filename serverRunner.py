#!/usr/bin/python3

# Runs the palworld server into a subprocess
# Periodically checks the subprocess if it's alive. Restarts the subprocess if it's dead

import subprocess, configparser, os, time, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--debug', dest='debug', required=False, default=False, action="store_true", type=bool)
args = parser.parse_args()

CONFIG_FILE = "config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_FILE)
PALSERVER_PATH = config["SERVER_FILES"]["Path"]

PALSERVER_EXEC_FILENAME = "PalServer.sh"

exec_path = os.path.join(
  PALSERVER_PATH,
  PALSERVER_EXEC_FILENAME
)
exec_path = os.path.normpath(exec_path)
# exec_path = os.path.abspath("./asdf.sh")

def get_server():
  return subprocess.Popen(f"exec {exec_path}", shell=True)

server = None
while True:
  if not server:
    server = get_server()
    print("getting server")
    time.sleep(10)

  if args.debug:
    print(f'server: {server}')
    print(f'poll: {server.poll()}')
    print(f'returncode: {server.returncode}')

  if server.returncode is not None:
    print("restart")
    server = get_server()
  else:
    if args.debug: print("sleep10")
  time.sleep(10)
