.. _start_stop:

Starting and stopping TASSELpy
------------------------------

.. author, Eli Rodgers-Melnick

TASSELpy consists of Python wrappers of Java functions and classes. Therefore, it needs to
connect to the JVM and have access to the TASSEL JAR files in order to work. The connection
can be made using the ``TASSELBridge.start()`` function. This will make the connection using
the libraries that are already packaged with TASSELpy.

Starting the JVM
^^^^^^^^^^^^^^^^

.. doctest::

   >>> from TASSELpy import TASSELbridge
   >>> TASSELbridge.start() 

If you don't want to use the default JARS (e.g. if you want to use some bleeding edge stuff),
you can specify the location of a custom installation of TASSEL using the ``tassel_dir`` keyword.
Replace the ``tassel_dir`` argument with the directory of your own installation.

.. doctest::

   >>> import os
   >>> from TASSELpy import TASSELbridge
   >>> TASSELbridge.start(tassel_dir=os.path.join(os.path.expanduser('~'),'bioinformatics','tassel5-standalone'))

Stopping the JVM
^^^^^^^^^^^^^^^^
You should kill the JVM before ending your python session. If you don't, then the session
may hang until you run a force quit. The JVM can be stopped by running the ``TASSELbridge.stop()``
function. 
**However, once the JVM is stopped, it cannot be turned back on within the same Python session**

.. doctest::

   >>> TASSELbridge.stop()

