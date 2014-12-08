#stdlibRoutine
from os import environ
from subprocess import check_output
from uuid import uuid4

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
  try:
    output=check_output(cmdArg.split(" "), cwd=cwdArg)
    if cmdArg=='make':
      print output
  except subprocess.CalledProcessError as excep:
    print excep

if __name__ == "__main__":
  main()
