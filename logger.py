from position import Position


class Logger:
    """
    This class is used to create a logger and perform various operations on it.
    """
    
    def __init__(self) -> None:
        """
        Initialise a logger object.
        """
        self.__logger = []
    
    def add(self, item : str) -> None:
        """
        Append a string onto the logger stream.
        
        Parameters:
            item (str): String to add to the logger
        """
        self.__logger.append(item)
        
    def clear(self) -> None:
        """
        Clear all the content on the logger stream.
        """
        self.__logger = []
    
    def get(self) -> list[str]:
        """
        Get the logger stream with all the content.
        
        Returns:
            list[str]: The logger stream
        """
        return self.__logger
    
    def is_empty(self) -> bool:
        """
        Test if the logger stream is empty.
        
        Returns:
            bool: True if empty else false
        """
        return (len(self.__logger) == 0)
    
    def remove(self, pos: Position) -> None:
        """
        Remove content from the logger based on the position passed.
        
        Parameters:
            pos (Position): The position to remove from the logger stream
        """
        self.__logger.pop(pos.value)
        return None
    
    def to_string(self, sep='') -> str:
        """
        Converts the logger stream into a single string joined by a separator.
        
        Parameters:
            sep (str): The separator to join the logger stream by, default is ''
            
        Returns:
            str: The logger stream joined together by a separator as a string 
        """
        return sep.join(self.__logger)