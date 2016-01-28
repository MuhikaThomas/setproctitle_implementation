# setproctitle_implementation
Using module setproctitle 

__A Python module to customize the process title__

The setproctitle module allows a process to change its title (as displayed by system tools such as ps and top).

Changing the title is mostly useful in multi-process systems, for example when a master process is forked: changing the children’s title allows to identify the task each process is busy with. The technique is used by PostgreSQL and the OpenSSH Server for example.

The procedure is hardly portable across different systems. PostgreSQL provides a good multi-platform implementation: this module is a Python wrapper around PostgreSQL code.

For more information[https://pypi.python.org/pypi/setproctitle]

#Installation

setproctitle is a C extension: in order to build it you will need a C compiler and the Python development support (the python-dev package in most Linux distributions). No further external dependencies are required.

You can use pip to install the module:

$pip install setproctitle
or in debian
$sudo apt-get install python-setproctitle

[Mossein King]
