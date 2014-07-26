from TASSELpy.java.util.List import List

## Python-specific class used to apply functional programming
# filtering to a wrapped java list
class FilterList(List):
    """
    Python-specific class used to apply functional programming
    filtering to a wrapped java list
    """
    def __init__(self, *args, **kwargs):
        super(FilterList,self).__init__(*args,**kwargs)
    ## Iterates through the list, but only returns items for which a
    # function evaluates True
    # @param filterFunc A function that accepts the list generic type as an argument
    # and returns true or false
    # @return An iterator that only returns objects evaluating true
    def filterIterator(self, filterFunc):
        """
        Iterates through the list, but only returns items for which a function
        evaluates True.

        Arguments:

        filterFunc -- A function that accepts the list generic type as an argument and
                      returns true or false

        Returns:

        An iterator that only returns objects evaluating true
        """
        ## Loop through the iterator
        for item in self.iterator():
            if filterFunc(item):
                yield item
    ## Enumerates the list, returning index and items for which a function
    # evaluates True
    # @param filterFunc A function that accepts the list generic type as an argument
    # and returns true or false
    # @return An iterator of (index, object) for objects evaluating true
    def filterEnumerator(self, filterFunc):
        """
        Enumerates the list, returning index and items for which a function
        evaluates True

        Arguments:

        filterFunc -- A function that accepts the list generic type as an argument and
                      returns true or false

        Returns:

        An iterator of (index, object) for objects evaluating true
        """
        ## Loop through the iterator
        ind = 0
        for item in self.iterator():
            if filterFunc(item):
                yield (ind, item)
            ind += 1
        
    
