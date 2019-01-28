from datetime import datetime, timedelta
import os
import sys

today = datetime.today()
idx = (today.weekday() + 1) % 7
sun = today - timedelta(7+idx)

if os.path.isfile("{:%m-%d-%Y}.md".format(sun)):
    print("ERROR: File already exists! ")
    sys.exit(1)

templateFile = open("TEMPLATE.md", "r")
newFile = open("{:%m-%d-%Y}.md".format(sun), "w")

for line in templateFile:
    if "%DATE%" in line:
        line = line.replace("%DATE%", "{:%m-%d-%Y}".format(sun))
    newFile.write(line)

templateFile.close()
newFile.close()
