from argparse import ArgumentParser
from key_stroke_logger import KeyStrokeLogger
import logging


def init_argument_parser():
    """
    Create the CLI argument parser to allow the user to pass the arguments to
    the program.
    
    Returns:
        Namespace: The parsed arguments from the CLI
    """
    parser = ArgumentParser("KeyStrokeLogger", 
                description="Logs the keys pressed by the user to a log file.")
    parser.add_argument(
        "-output-folder", 
        nargs='?', 
        default="/tmp", 
        help="The directory where the key stroke logs are outputted")
    return parser.parse_args()

if __name__ == "__main__":
    parsed_cli_args = init_argument_parser()
    # Initialise the logger and the format for terminal-based logging
    logging.basicConfig(format="[{asctime}] {levelname}: {message}",
                        style="{",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.DEBUG)
    KeyStrokeLogger(parsed_cli_args.output_folder).start_logger()