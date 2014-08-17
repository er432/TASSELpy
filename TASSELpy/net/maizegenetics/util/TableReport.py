from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger, Integer
from TASSELpy.java.lang.Double import Double
from TASSELpy.java.lang.String import String
from TASSELpy.java.lang.Float import Float
from TASSELpy.java.lang.Byte import Byte
from TASSELpy.java.lang.Long import Long
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.javaObj import javaArray
from TASSELpy.utils.helper import make_sig
import re

java_imports = {'Object':'java/lang/Object',
                'String':'java/lang/String',
                'TableReport':'net/maizegenetics/util/TableReport'}

## Compile regular expressions
int_re = re.compile(r'^-*[\d]+$')
float_re = re.compile(r'(^-*[\d]+\.[\d]+$|^-*[\d]{1}([\.]?[\d])*(E|e)-[\d]+$)')

class TableReport(Object):
    """
    Interface for classes with data that can be presented in tables
    """
    _java_name = java_imports['TableReport']
    ## Instantiates a TableReport
    @javaConstructorOverload(java_imports['TableReport'])
    def __init__(self, *args, **kwargs):
        ## Create dictionary of column -> index
        self.colLabels = dict((str(col), i) for i,col in enumerate(self.getTableColumnNames()))
    def _class_caster(self, x):
        if not isinstance(x, Object):
            return x
        elif x.getClass().getName() == 'java.lang.String':
            return x.castTo(String)
        elif x.getClass().getName() == 'java.lang.Integer':
            return x.castTo(Integer)
        elif x.getClass().getName() == 'java.lang.Double':
            return x.castTo(Double)
        elif x.getClass().getName() == 'java.lang.Float':
            return x.castTo(Float)
        elif x.getClass().getName() == 'java.lang.Byte':
            return x.castTo(Byte)
        elif x.getClass().getName() == 'java.lang.Long':
            return x.castTo(Long)
        else:
            try:
                # Hail Mary cast
                castClass = getattr(__import__('TASSELpy.%s' % x.getClass().getName(),
                                       globals(), locals(),
                                       [x.getClass().getName().split('.')[-1]]),
                                       x.getClass().getName().split('.')[-1])
                return x.castTo(castClass)
            except ImportError:
                return x
            except AttributeError:
                return x
    def __getitem__(self, inds):
        """ Gets an entry from the TableReport

        Parameters
        ----------
        inds : int or tuple
            Either the zero-based index of a row to get or a tuple of
            two numbers, where the first is the row and the second is the
            column, or a tuple of a number of a string, where the string is the
            name of the column to get

        Returns
        -------
        Either a single entry or a dictionary for the row
        """
        if type(inds) == tuple:
            inds = list(inds)
            if len(inds) > 2:
                raise TypeError("Two indices maximum")
            elif type(inds[1]) == str:
                # Get the index associated with the column
                try:
                    inds[1] = self.colLabels[inds[1]]
                except KeyError:
                    raise KeyError("%s is not a column label" % inds[1])
            if type(inds[0]) != int:
                raise TypeError("Row index must be integer")
            row = self.getRow(inds[0])
            return self._class_caster(row[inds[1]])
        elif type(inds) == int:
            row = self.getRow(inds)
            # Return the row as a dictionary
            return dict((k,self._class_caster(row[v])) for k,v in self.colLabels.items())
        else:
            raise TypeError("Row index must be integer")
    def toDict(self):
        """ Outputs the table as a dictionary

        Returns
        -------
        Dictionary of column -> (vals)
        """
        ncols = self.getColumnCount()
        nrows = self.getRowCount()
        # Create dictionary of index -> column name
        col_dict = dict((i, str(x)) for i, x in enumerate(self.getTableColumnNames()))
        return_dict = dict((str(x),[]) for x in self.getTableColumnNames())
        for i in xrange(nrows):
            for j in xrange(ncols):
                val = self.getValueAt(i,j)
                return_dict[col_dict[j]].append(self._class_caster(val))
        return return_dict
    ## Gets the names of the columns
    # @return Column names
    @javaOverload("getTableColumnNames",
                  (make_sig([],java_imports['Object']+'[]'),(),
                   Object.wrap_existing_array))
    def getTableColumnNames(self, *args):
        """
        Gets the names of the columns

        Signatures:

        Object[] getTableColumnNames()

        Returns:

        Column names
        """
        pass
    ## Gets the title of the table
    # @return A string title
    @javaOverload("getTableTitle",
                  (make_sig([],java_imports['String']),(),None))
    def getTableTitle(self, *args):
        """
        Gets the title of the table

        Signatures:

        String getTableTitle()

        Returns:

        A string title
        """
        pass
    ## Gets the number of columns
    # @return Number of columns
    @javaOverload("getColumnCount",
                  (make_sig([],'int'),(),None))
    def getColumnCount(self, *args):
        """
        Gets the number of columns

        Signatures:

        int getColumnCount()

        Returns:

        Number of columns
        """
        pass
    ## Gets the number of rows
    # @return Number of rows
    @javaOverload("getRowCount",
                  (make_sig([],'int'),(),None))
    def getRowCount(self, *args):
        """
        Gets the number of rows

        Signatures:

        int getRowCount()

        Returns:

        Number of rows
        """
        pass
    ## Gets the total number of elements in the dataset
    # @return total number of elements
    @javaOverload("getElementCount",
                  (make_sig([],'int'),(),None))
    def getElementCount(self, *args):
        """
        Gets the total number of elements in the dataset
        Elements = rowCount*columnCount

        Signatures:

        int getElementCount()

        Returns:

        Total number of elements
        """
        pass
    ## Returns the specified row
    # @param row row number
    # @return row
    @javaOverload("getRow",
                  (make_sig(['int'],java_imports['Object']+'[]'),(metaInteger,),
                   Object.wrap_existing_array))
    def getRow(self, *args):
        """
        Returns specified row

        Signatures:

        Object[] getRow(int row)

        Arguments:

        row -- row number

        Returns:

        row
        """
        pass
    ## Returns value at given row and column
    # @param row row number
    # @param col column number
    # @return data
    @javaOverload("getValueAt",
                  (make_sig(['int','int'],java_imports['Object']),(metaInteger,metaInteger),
                   lambda x: Object(obj=x)))
    def getValueAt(self, *args):
        """
        Returns value at given row and column

        Signatures:

        Object getValueAt(int row, int col)

        Arguments:

        row -- row number
        col -- column number

        Returns:

        data
        """
        pass
