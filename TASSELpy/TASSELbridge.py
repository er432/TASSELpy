import javabridge
import os
from glob import iglob

class TASSELbridge:
    ## Starts the JVM and connects to the TASSEL JAR
    # @param tassel_dir The directory containing the TASSEL JAR
    @staticmethod
    def start(tassel_dir=None):
        """
        Starts the JVM and connects to the TASSEL JAR

        Arguments:

        tassel_dir -- The directory containing the TASSEL JAR
        """
        if tassel_dir is None:
            use_jars = javabridge.JARS + list(iglob(os.path.join(os.path.dirname(__file__), 'lib', '*.jar')))
        else:
            use_jars = javabridge.JARS + [os.path.join(tassel_dir, 'sTASSEL.jar')]
            use_jars += list(iglob(os.path.join(tassel_dir, 'lib', '*.jar')))
        # Start VM
        try:
            try:
                javabridge.start_vm(['-Djava.class.path=' +
                                     os.pathsep.join(use_jars)], class_path=use_jars,
                                    run_headless=True)
            except:
                javabridge.start_vm(class_path=use_jars, run_headless=True)
        except:
            print "Could not start JVM!"

    ## Stops the JVM
    @staticmethod
    def stop():
        """
        Kills the JVM
        """
        javabridge.kill_vm()
