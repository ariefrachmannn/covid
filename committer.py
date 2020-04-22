import subprocess

cp = subprocess.call("git add /home/covid/", shell=True)
message = "update the repository"
cp = subprocess.call("git commit -m '{message}'".format(message=message), shell=True)
cp = subprocess.call("git push -u origin master -f", shell=True)
