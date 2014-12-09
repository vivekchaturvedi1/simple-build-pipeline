#stdlibRoutine
from os import environ
from subprocess import check_output
from uuid import uuid4
from fabric.api import cd, run, settings, env

env.host_string='vivek@10.10.10.60:22'
env.password='vivek!'

def main():
  repoPath='https://github.com/vivekchaturvedi1/cmake-hello-world.git'
  repoName=repoPath.rpartition('/')[2].rpartition('.')[0]
  repoDirName=str(uuid4().get_hex().upper()[0:6])
  repoDirPath=environ["HOME"]
  repoDirAbsPath=repoDirPath + '/' + repoDirName

  runShell('mkdir %s' %repoDirName, '%s' %repoDirPath)
  runShell('git clone %s' %repoPath, '%s' %repoDirAbsPath)
  runShell('mkdir build', '%s/%s' %(repoDirAbsPath, repoName))
  runShell('cmake ..', '%s/%s/build' %(repoDirAbsPath, repoName))
  runShell('make', '%s/%s/build' %(repoDirAbsPath, repoName))
  runShell('./CMakeHelloWorld', '%s/%s/build' %(repoDirAbsPath, repoName))


def runShell(cmdArg, cwdArg):

  with settings(warn_only=True):
    with cd(cwdArg):
      if run(cmdArg).failed:
        run("echo %s Failed!" %cmdArg)

if __name__ == "__main__":
  main()
