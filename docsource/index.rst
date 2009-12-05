Tipi
====

Overview
--------

Tipi is a tool for creating and managing Python virtual environments. It builds upon the capabilities of virtualenv and aims to provide tools for improving how you organize and utilize virtualenv. Much of Tipi has been inspired by virtualenv_wrapper and virtual-commands.

Features
--------

- Knows about virtualenvs on your system and provides conveniences for switching between them
- Copy (clone) existing virtualenvs
- "Inheritance" via an extension mechanism. Lets you stack up virtualenvs so that extended virtualenvs
work as if they had all the installed packages of their ancestors
- Multi environments let you group environments together and apply operations (such as installing packages) across all of them. 
- Provides hooks like virtualenv_wrapper for more control over how environments are created and activated.


Configuring
-----------

TIPI_VENV_HOME

version_group = 2.4+
version_group = pypy, unladen_swallow, jython
interpreters = 2.4, 2.5
interpreters = /opt/python/2.5/python

Running
-------

TIPI_ACTIVE_ENV

Copying
-------

The copy operation is the equivalent of creating two separate VEs based on the same interpreter and installing the same exact packages (including package versions) into each one. 

virtualenv ve1
easy_install somepkg
easy_install someotherpkg
virtualenv ve2
easy_install somepkg
easy_install someotherpkg
source ve1/bin/activate
(ve1) which python

(ve1) python
>>> import somepkg

...



Extending
---------

Extending is a way to establish an inheritance relationship between VEs such that a VE "inherits" the VE it extends from (the parent). Whereas Copy duplicates the packages into the copied VE, Extend works by making the packages available from the parent VE so that they are available to the child VE.  



Grouping
--------

You can create groups of VEs. Use groups to manage multiple VEs where most aspects will be in common but you want to vary an aspect of each. For example, using different Python
interpreters for each one, or installing different point releases of a particular package in each one. 

Installing Python Packages
---------------------------



Commands
--------

config

create
  -from tipi export
  -from pip reqs file
  -from repo
  
  --startdir
  
creategroup

copy

remove

extend
changeparent
addparent

group

export
exportgroup

install

startdir - specify where the starting dir should be after activating an env
