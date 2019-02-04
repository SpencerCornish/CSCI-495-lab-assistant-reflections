from datetime import datetime, timedelta
import os
import sys

today = datetime.today()
idx = (today.weekday() + 1) % 7
sun = today - timedelta(7+idx)
filePath = "md/{:%m-%d-%Y}.md".format(sun)

if os.path.isfile(filePath):
    print("ERROR: File already exists! " + filePath)
    sys.exit(1)

templateFile = open("md/TEMPLATE.md", "r")
newFile = open(filePath, "w")

for line in templateFile:
    if "%DATE%" in line:
        line = line.replace("%DATE%", "{:%m-%d-%Y}".format(sun))
    newFile.write(line)

templateFile.close()
newFile.close()
