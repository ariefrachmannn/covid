import subprocess

#cp = subprocess.call("cd /home/redbit/crawling/covid/", shell=True)
cp = subprocess.call("git add .", shell=True)
message = "update the repository"
cp = subprocess.call("git commit -m '{message}'".format(message=message), shell=True)
cp = subprocess.call("git push -u origin master -f", shell=True)
