.. TASSELpy documentation master file, created by
   sphinx-quickstart on Wed Jul 23 13:39:36 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to TASSELpy's documentation!
====================================

**Contents**

.. toctree::
   :maxdepth: 1

   tutorial/index
   TASSELpy

Overview
========

TASSELpy is a Python API for the Java program 
`TASSEL <http://www.maizegenetics.net/index.php?option=com_content&task=view&id=89&Itemid=119>`_.
It provides a number of Python wrappers for the TASSEL classes and functions, allowing the user
to seamlessly interact with the TASSEL program in a completely Pythonic way, even though all calculations
are completed using the Java Virtual Machine. 

TASSEL is primarily used for association mapping and other tasks in quantitiative genetics,
although it has a large number of features for various aspects of biological sequence analysis.
TASSELpy's goal is to provide tools that allow convenient scripting of common genetics tasks
while taking advantage of the efficiency of the JVM.

Installation
============

Installation with Pip
---------------------
::
    pip install -U tasselpy

Installation without Pip
------------------------
::
    python setup.py install

Dependencies
------------

TASSELpy's requirements include those for 
`TASSEL5 <http://www.maizegenetics.net/index.php?option=com_content&task=view&id=89&Itemid=119>`_
(JDK v1.7 or greater), python-javabridge, and numpy. Python-javabridge also requires
a C compiler to run.

On **MacOSX**, there is currently an issue with javabridge using the correct version.
For now this can be manually resolved. First, ensure that the JDK 1.7 or greater
is installed on your system and that /usr/libexec/java_home points to this
JDK. Now perform the following::

    curl "https://pypi.python.org/packages/source/j/javabridge/javabridge-1.0.7.tar.gz" -o "javabridge-1.0.7.tar.gz"
    tar -xvf javabridge-1.0.7.tar.gz
    cd javabridge-1.0.7

Open up the ``setup.py`` file in your favorite plain text editor of choice
(e.g. emacs, nano), and delete the following lines (should be 97 and 98)::

    include_dirs += ['/System/Library/Frameworks/JavaVM.framework/Headers']
    extra_link_args = ['-framework', 'JavaVM'] 

Now, replace those deleted lines with these ones (within the same scope)::

    java_home = subprocess.check_output(['/usr/libexec/java_home']).strip()
    include_dirs += [os.path.join(java_home,'include'),
                    os.path.join(java_home,'include','darwin')]
    include_dirs += ['/System/Library/Frameworks/JavaVM.framework/Headers']
    extra_link_args = ['-L%s' % os.path.join(java_home,'jre','lib','server'),'-ljvm']
    extra_link_args += ['-Wl,-rpath,%s' % os.path.join(java_home,'jre','lib','server')]

On **CentOS** 6, all dependencies can be installed as follows::

    yum install gcc numpy python-devel java-1.7.0-openjdk-devel
    curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    python get-pip.py
    pip install -U javabridge

On **Fedora** 19, the dependencies can be installed as follows::

    yum install gcc numpy python-devel java-1.7.0-openjdk-devel python-pip openssl
    pip install -U javabridge

On **Ubuntu** 13.10 and **Debian** 7.0, the dependencies can be installed as follows::
 
    apt-get install openjdk-7-jdk python-pip python-numpy python-dev
    pip install -U javabridge

On **Windows**::

By default, you probably will not have a C compiler installed, so install
the Windows SDK 7.1 and .Net Framework 4.0 to perform the compile steps
unless there is a preexisting C compiler on your system. Install the Oracle
JDK v 1.7 (or v 1.8). Ensure that the paths to pip and python are in your PATH.
Now perform the following steps:

    Open the Windows SDK command prompt, and provide the following commands::

        set MSSdk=1
	set DISTUTILS_USE_SDK=1
	pip install -U javabridge
	pip install -U tasselpy

Search
======
* :ref:`search`

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

