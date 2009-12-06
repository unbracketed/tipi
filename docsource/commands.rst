Commands
--------

config

create
-------

Creates a new virtual environment using virtualenv. 

    tipi create <myenv myenv2 ...>

Options
^^^^^^^^

**-p, --python**
    Specify the Python interpreter to use when creating a new environment. If
    you specify anything other than an absolute path tipi will attempt to
    resolve it in the PATH. create will fail if the specified interpreter
    cannot be found.

  TODO
  --startdir
  
creategroup
------------

copy
----


remove

extend
changeparent
addparent

group

export
exportgroup

info - display info about the environment: Interpreter version, inheritance, groups, etc.

install


startdir - specify where the starting dir should be after activating an env
