from datetime import datetime, timedelta
from os import system

today = datetime.today()
idx = (today.weekday() + 1) % 7
sun = today - timedelta(7+idx)

system(
    "markdown-pdf md/{:%m-%d-%Y}.md -o pdfs/{:%m-%d-%Y}.pdf".format(sun, sun))
