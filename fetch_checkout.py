#from bitbucket.bitbucket import Bitbucket
from git.repo.base import Repo
from sys import argv
import subprocess

prompt = '> '

print "Enter the name of branch you need to clone: "
user_branch = raw_input(prompt)

print "You Entered: ",user_branch


print "this will do a git status"
cmd = subprocess.Popen(["git", "status"], stdout=subprocess.PIPE)
output = cmd.communicate()[0]
print output
#for line in output: # output.split("\n"):
if  ("Untracked files:" or "Changes not staged for commit") in  output:
     print "Need to do a Git stash"
     subprocess.Popen(["git", "stash"])
     subprocess.Popen(["git fetch && git checkout"+(user_branch)])
else:
     print "simply do git checkout userbranch"
     subprocess.Popen(["git","pull"])
     subprocess.Popen(["git fetch && git checkout"+(user_branch)])