## Custom Exceptions ##

class WrongFormatException(Exception):

    # Exception that can be raised when the format type given as parameter is not supported.
    pass
    
class WrongMetaFileException(Exception):

    # Exception that can be raised when the meta fileformat is not correct
    pass