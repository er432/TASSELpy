from TASSELpy.java.lang.Runnable import Runnable
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import metaString
from TASSELpy.java.lang.Long import metaLong
from TASSELpy.utils.Overloading import javaConstructorOverload
from TASSELpy.utils.helper import make_sig

java_imports = {'Runnable':'java/lang/Runnable',
                'String':'java/lang/String',
                'Thread':'java/lang/Thread',
                'ThreadGroup':'java/lang/ThreadGroup'}
class Thread(Object, Runnable):
    """
    public class Thread
    extends Object
    implements Runnable

    A thread is a thread of execution in a program. The Java Virtual Machine
    allows an application to have multiple threads of execution running concurrently.

    Every thread has a priority. Threads with higher priority are executed in
    preference to threads with lower priority. Each thread may or may not also be
    marked as a daemon. When code running in some thread creates a new Thread object,
    the new thread has its priority initially set equal to the priority of the creating
    thread, and is a daemon thread if and only if the creating thread is a daemon.
    """
    _java_name = java_imports['Thread']
    @javaConstructorOverload(java_imports['Thread'],
            (make_sig([],'void'),()),
            (make_sig([java_imports['Runnable']],'void'),(Runnable,)),
            (make_sig([java_imports['Runnable'],java_imports['String']],'void'),(Runnable,metaString)),
            (make_sig([java_imports['String']],java_imports['String']),(metaString,)),
            (make_sig([java_imports['ThreadGroup'],java_imports['Runnable']],'void'),(Object,Runnable)),
            (make_sig([java_imports['ThreadGroup'],java_imports['Runnable'],java_imports['String']],'void'),
                      (Object,Runnable,metaString)),
            (make_sig([java_imports['ThreadGroup'],java_imports['Runnable'],java_imports['String'],
                       'long'],'void'), (Object,Runnable,metaString,metaLong)),
            (make_sig([java_imports['ThreadGroup'],java_imports['String']],'void'),(Object,metaString)))
    def __init__(self, *args, **kwargs):
        """
        Constructs a new Thread

        Signatures:

        Thread()
        Thread(Runnable target)
        Thread(Runnable target, String name)
        Thread(String name)
        Thread(ThreadGroup group, Runnable target)
        Thread(ThreadGroup group, Runnable target, String name)
        Thread(ThreadGroup group, Runnable target, String name, long stackSize)
        Thread(ThreadGroup group, String name)

        Arguments:

        Thread(Runnable target)
            target -- the object whose run method is invoked when this thread is started
        Thread(Runnable target, String name)
            target -- the object whose run method is invoked when this thread is started
            name -- the name of the new thread
        Thread(String name)
            name -- the name of the new thread
        Thread(ThreadGroup group, Runnable target)
            group -- The thread group
            target --the object whose run method is invoked when this thread is started
        Thread(ThreadGroup group, Runnable target, String name)
            group -- The thread group
            target --the object whose run method is invoked when this thread is started
            name -- the name of the new thread
        Thread(ThreadGroup group, Runnable target, String name, long stackSize)
            group -- The thread group
            target --the object whose run method is invoked when this thread is started
            name -- the name of the new thread
            stackSize -- the desired stack size for the new thread, or zero to indicate this parameter
                         is to be ignored
        Thread(ThreadGroup group, String name)
            group -- The thread group
            name -- the name of the new thread
        """
        pass
