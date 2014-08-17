.. _py_java_basics:

.. currentmodule:: TASSELpy

Running Java through Python
---------------------------

.. author, Eli Rodgers-Melnick

Although Python and Java have their similarities, they also have quite a few differences
that can make them tricky to reconcile with one another. Primarally, Java is
statically-typed and allows function overloading, while Python is dynamically-typed
and does not do function overloading. In ``TASSELpy`` I have created a number of 
features that make translation from Java to Python a very straightforward process.

Importing and Instantiating a Class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All classes in ``TASSELpy`` are named according to their placement in the Java
namespace, so importing them is straightforward, once you're familiar with
the Java API. In addition to providing classes
for the TASSEL program, I also provide classes for many of the included JDK classes
(i.e. ``java.lang.String``, ``java.lang.Integer``, ``java.util.ArrayList``). 

Below, I import and instantiate a String from the 
:class:`TASSELpy.java.lang.String.String` class and a Taxon from the
:class:`TASSELpy.net.maizegenetics.taxa.Taxon.Taxon` class.

.. doctest::

   >>> from TASSELpy.java.lang.String import String
   >>> from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
   >>> aString = String("I'm a Java String!")
   >>> aString
   String('I'm a Java String!')
   >>> aString.o
   <Java object at 0x1605c8d0>
   >>> aTaxon = Taxon("jabberwocky")
   >>> aTaxon
   Taxon(jabberwocky)
   >>> aTaxon.o
   <Java object at 0x1605c8e8>

In both cases, Java is creating an object that is then passed to a Python
wrapper object, meaning that the actual String and Taxon objects instantiated
are present in the JVM. The underlying Java objects are instances of
``javabridge.JB_Object`` and can be accessed with the ``o`` attribute.
The wrapper now allows access to the Java object just like in Java.

.. doctest::

   >>> aString.getClass().getName()
   u'java.lang.String'
   >>> aTaxon.getClass().getName()
   u'net.maizegenetics.taxa.Taxon'
   >>> aTaxon.getName()
   u'jabberwocky'

Getting help
^^^^^^^^^^^^

As usual, help can be accessed interactively using Python's built-in
``help()`` function. For example:

.. doctest::

   >>> help(aTaxon.getClass)
   Help on method getClass in module TASSELpy.java.lang.Object:
   
   getClass(*args) method of TASSELpy.net.maizegenetics.taxa.Taxon.Taxon instance
       Returns the runtime class of this Object.

       Signatures:

       final Class<?> getClass()

       Returns:

       The Class object that represents the runtime class of this object

Argument Types
^^^^^^^^^^^^^^

When looking up how to use a ``TASSELpy`` function that is wrapping
up a Java function, you will see one or more "Signatures". These signify
the ways in which the function can be called in Java and, likewise,
in Python. For example, when the Java function requires a Taxon object,
you would use an instance of 
:class:`TASSELpy.net.maizegenetics.taxa.Taxon.Taxon`. All arguments
are positional, meaning that you should not call a TASSELpy
wrapper function with a ``somearg=someval`` argument.

Some argument types can take both wrapped java objects and regular Python
objects as arguments. These include ``String`` and any of the Java primitive
types, along with their arrays. A full list of these java argument types
and the python types that they can accept is below.

Single Arguments
''''''''''''''''

* ``String`` (i.e. instance of java.lang.String)
    
  * ``TASSELpy.java.lang.String.String``
  * ``str``
  * ``unicode``
  * ``numpy.string_``

* ``int`` (i.e. instance of java primitive int)

  * ``TASSELpy.java.lang.Integer.Integer``
  * ``int``
  * ``numpy.int32``
  * ``numpy.uint32``

* ``double`` (i.e. instance of java primitive double)

  * ``TASSELpy.java.lang.Double.Double``
  * ``numpy.float64``
  * ``numpy.longdouble``

* ``float`` (i.e. instance of java primitive float)

  * ``TASSELpy.java.lang.Float.Float``
  * ``float``
  * ``numpy.float32``

* ``byte`` (i.e. instance of java primitive byte)

  * ``TASSELpy.java.lang.Byte.Byte``
  * ``numpy.int8``
  * ``numpy.uint8``

* ``long`` (i.e. instance of java primitive long)

  * ``TASSELpy.java.lang.Long.Long``
  * ``long``
  * ``numpy.int64``
  * ``numpy.uint64``

Array Arguments
'''''''''''''''

All primitive java array arguments can accept either a ``numpy.ndarray``
instance of the appropriate type. Details on how to make an instance of
a Java array can be found in :ref:`making-java-arrays`.

.. _making-java-arrays:

Making Java Arrays
^^^^^^^^^^^^^^^^^^

``TASSELpy`` can create wrappped instances of Java arrays for both
classes and primitives. These are instantiated in different ways. However,
access to both is similar.

Java arrays for Objects
'''''''''''''''''''''''

Java arrays for Objects (i.e. java objects descended from 
``java.lang.Object``) are instantiated using the ``getArray`` function.
Likewise, double arrays (e.g. ``String[][]`) can be instantiated using the
``getDblArray`` function. Once instantiated, use of the array essentially
follows Java syntax.

.. doctest::

   >>> from TASSELpy.java.lang.String import String
   >>> singleArray = String.getArray(3)
   >>> len(singleArray)
   3
   >>> singleArray[0] = 'TASSEL'
   >>> singleArray[2] = 'silk'
   >>> [x for x in singleArray]
   [String('TASSEL'), None, String('silk')]
   >>> doubleArray = String.getDblArray(3,2)
   >>> doubleArray[0][0] = '0,0'
   >>> doubleArray[0][1] = '0,1'
   >>> doubleArray[1][1] = '1,1'
   >>> doubleArray[2][0] = '2,0'
   >>> for arr in doubleArray: print arr
   ...
   javaArray([0,0, 0,1])
   javaArray([None, 1,1])
   javaArray([2,0, None])
   >>> doubleArray = String.getDblArray(3)
   >>> doubleArray
   javaArray([None, None, None])
   >>> doubleArray[0] = String.getArray(2)
   >>> doubleArray[2] = String.getArray(5)
   >>> doubleArray[2][4] = 'lastEntry'
   >>> for arr in doubleArray: print arr
   ...
   javaArray([None, None])
   None
   javaArray([None, None, None, None, lastEntry])

Java Arrays for Primitives
''''''''''''''''''''''''''

Java arrays for java primitives (e.g. ``int``, ``byte``, ``double``) 
are instantiated using the
:class:`TASSELpy.utils.primativeArray.javaPrimativeArray` class. Single
dimension arrays are instantiated using the ``make_array`` function, while
double arrays (e.g. ``int[][]``) are instantiated using the 
``make_dbl_array`` function. Once instantiated, manipulation of both
types is essentially equivalent to java syntax.

.. doctest::

   >>> from TASSELpy.utils.primativeArray import javaPrimativeArray 
   >>> singleArray = javaPrimativeArray.make_array('int',3)
   >>> singleArray[0] = 1
   >>> singleArray[2] = 3
   >>> len(singleArray)
   3
   >>> singleArray
   javaArray([1, 0, 3])
   >>> doubleArray = javaPrimativeArray.make_dbl_array('int',3,2)
   >>> doubleArray[0][0] = 1
   >>> doubleArray[2][1] = 6
   >>> doubleArray[1][0] = 3
   >>> for arr in doubleArray: print arr
   ...
   javaArray([1, 0])
   javaArray([3, 0])
   javaArray([0, 6])
   >>> doubleArray = javaPrimativeArray.make_dbl_array('int',3)
   >>> doubleArray[0] = javaPrimativeArray.make_array('int',2)
   >>> doubleArray[2] = javaPrimativeArray.make_array('int',5)
   >>> doubleArray[0][0] = 1
   >>> doubleArray[2][4] = 6
   >>> for arr in doubleArray: print arr
   ...
   javaArray([1, 0])
   None
   javaArray([0, 0, 0, 0, 6])

Java Generics
^^^^^^^^^^^^^

Some Java classes, particularly those in the Java collections framework, 
can operate on variables of many different classes. In Java, the class or
classes that the a particular object is interpreted to act upon is specified 
within angle brackets (e.g. ArrayList<String>). ``TASSELpy`` supports
the use of these generic types with the ``generic`` keyword argument
upon instantiation. This accepts a tuple of Python type(s) for wrappers
of the desired Java class. I demonstrate this below with an ArrayList
of Strings and of Taxons. 

Note here that, in the case of String objects, I use the Python-wrapped
java String rather than a plain Python str instance. This is because
``String`` is explicitly specified by the user here as the argument type,
and automatic conversion isn't available yet under these generic types.

.. doctest::

   >>> from TASSELpy.java.util.ArrayList import ArrayList
   >>> from TASSELpy.java.lang.String import String
   >>> from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
   >>> stringList.add(String('First'))
   True
   >>> stringList.add(String('Second'))
   True
   >>> stringList.add(String('Third'))
   True
   >>> [x for x in stringList]
   [String('First'), String('Second'), String('Third')]
   >>> stringList[1]
   String('Second')
   >>> taxonList = ArrayList(generic=(Taxon,))
   >>> taxonList.add(Taxon('Maize'))
   True
   >>> taxonList.add(Taxon('Teosinte'))
   True
   >>> taxonList.add(Taxon('Tripsacum'))
   True
   >>> [x for x in taxonList]
   [Taxon(Maize), Taxon(Teosinte), Taxon(Tripsacum)]
   >>> taxonList[1]
   Taxon(Teosinte)
