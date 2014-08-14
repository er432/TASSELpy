from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
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
        pass
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
                val = str(self.getValueAt(i,j))
                if int_re.match(val):
                    val = int(val)
                elif float_re.match(val):
                    val = float(val)
                return_dict[col_dict[j]].append(val)
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
