#stdlib
import json

#stdlib routines
from os import environ
from subprocess import check_output
from uuid import uuid4

#3rd party lib routines
from fabric.api import cd, run, settings, env

#with context manager
with open("config/env_data.json", 'r') as fp:
  env_data=json.load(fp)

#setting env varibles
env.host_string=env_data['host_string']
env.password=env_data['password']

def main():
  repoPath='https://github.com/vivekchaturvedi1/cmake-hello-world.git'
  repoName=repoPath.rpartition('/')[2].rpartition('.')[0]
  workingDirectory=str(uuid4().get_hex().upper()[0:6])
  repoDirPath=environ["HOME"]
  repoDirAbsPath=repoDirPath + '/' + workingDirectory

  runShell('mkdir %s' %workingDirectory, '%s' %repoDirPath)
  runShell('git clone %s' %repoPath, '%s' %repoDirAbsPath)
  runShell('mkdir build', '%s/%s' %(repoDirAbsPath, repoName))
  runShell('cmake ..', '%s/%s/build' %(repoDirAbsPath, repoName))
  runShell('make', '%s/%s/build' %(repoDirAbsPath, repoName))
  runShell('./CMakeHelloWorld', '%s/%s/build' %(repoDirAbsPath, repoName))


def runShell(command, directory):
  """
    :param command: 'shell command'
    :param directory: 'the directory-path where to run the shell command'
  """
  with settings(warn_only=True):
    with cd(directory):
      if run(command).failed:
        run("echo %s Failed!" %command)

if __name__ == "__main__":
  main()
