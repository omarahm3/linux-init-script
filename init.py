import os
import subprocess
import json
from pprint import pprint
import progressbar
from time import sleep


def handleChoice(choice):
  return {
    "1": loadPrograms,
    "2": loadServers
  }.get(str(choice), None)

def openProgram(program):
  subprocess.Popen([str(program)], stdout=open('logs.log', 'w'), stderr=open('errors.log', 'a'), preexec_fn=os.setpgrp)

def loadConfigFile():
  with open('config.json') as file:
    return json.load(file)['configuration']

def loadPrograms(config):
  subprocess.Popen(["clear"])
  sleep(0.1)
  print "\n\n\033[0;37;48m--------------"
  print "\033[0;37;48mOpening registered programs"
  length = len(config['programs'])
  progressbar.print_progress(0, 1, prefix = 'Progress:', suffix = 'Complete', bar_length = 50)
  for i, program in enumerate(config['programs']):
    openProgram(program)
    sleep(0.2)
    progressbar.print_progress(i + 1, length, prefix = 'Progress:', suffix = 'Complete', bar_length = 50)
  print "\033[0;37;48mOpening complete, check errors.log to see if there are any errors"
  print "\033[0;37;48m--------------\n"

def openServer(server):
  os.chdir(str(server['path']))
  logFile   = str(server['name']) + "-logs.log"
  errorLogs = str(server['name']) + "-errors.log"
  subprocess.Popen(str(server['command']).split(), stdout=open(logFile, 'w'), stderr=open(errorLogs, 'a'), preexec_fn=os.setpgrp)

def loadServers(config):
  subprocess.Popen(["clear"])
  sleep(0.1)
  print "\n\n\033[0;37;48m--------------"
  print "\033[0;37;48mOpening registered servers"
  length = len(config['programs'])
  progressbar.print_progress(0, 1, prefix = 'Progress:', suffix = 'Complete', bar_length = 50)
  for i, server in enumerate(config['servers']):
    openServer(server)
    sleep(0.2)
    progressbar.print_progress(i + 1, length, prefix = 'Progress:', suffix = 'Complete', bar_length = 50)
  print "\033[0;37;48mOpening complete, check logs associated with each server"
  print "\033[0;37;48m--------------\n"

print "\n\n\033[1;30;40m-- Initializing..."
print "\033[1;30;40m-- Reading configuration...\n"

config = loadConfigFile()

print "\033[1;33;40m          Hi there, i'm " + config['owner'] + "'s virtual initializer."
print "\033[1;33;40mI'll help you opening common programs and initializing dev servers"
print "\033[1;33;40m            ----------------------------------"

# loadPrograms(config)


while True:
  print "\n\033[1;34;40m[1] Load Programs"
  print "\033[1;34;40m[2] Load Servers"

  choice = raw_input("\n\033[1;37;40mType the number corresponding to your choice: ")
  function = handleChoice(choice)

  if function is None or not callable(function):
    print "\n\033[1;31;40mOh, you entered unknown number, please check again.\n"

  if callable(function):
    function(config)
  