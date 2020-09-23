#  Script that converts a file from one encoding to another. 

#!usr/bin/env python3 

import sys
import logging
import argparse

__version__ = '1.00'

logging.basicConfig(level = logging.DEBUG) 

class Encode:
    """
    Class that converts a file from one encoding to another
    """
   
    def __init__(self, fin, input_encode, output_encode):
        self.input_encode = input_encode
        self.output_encode = output_encode
        self.fin = fin
    
    def run(self):
        """
        Logic for encode conversion
        """
        logging.debug(f"Converting file from {self.input_encode}")
        with open(self.fin, encoding = self.input_encode) as file_1:
            content = file_1.read()
        with open(self.fin, 'w', encoding = self.output_encode) as file_2:
            file_2.write(content)
        logging.debug(f"File converted to {self.output_encode}")
        
def main(args):
    """
    Logic to run Arguments
    """
    parser = argparse.ArgumentParser(description= "Convert file from one encoding to another")
    parser.add_argument("-f","--file", type = str, required = True, help = "File input")
    parser.add_argument("-i","--input", type = str, default = "utf-8", help = "The encoding you want to input")
    parser.add_argument("-o","--output", type = str, required = True, help = "The encoding you want as your output")
    parser.add_argument("-v", "--version", action = 'version', version = __version__)
    args = parser.parse_args()
    encode = Encode(args.file, args.input, args.output)
    encode.run()
    logging.debug("Done")
    
if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except (FileNotFoundError, LookupError) as e:
        logging.debug(e)
