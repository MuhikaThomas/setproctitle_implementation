import setproctitle

#the title for the process
title = "Using module setproctitle"
#setting the title using setproctitle
setproctitle.setproctitle(title)
#getting back the title of the process
name = setproctitle.getproctitle()
#printing the title of the process
print name
