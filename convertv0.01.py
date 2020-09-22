#  Script that converts a file from one encoding to another. 

# -------To do---------
# 1. Command line should accept an input filename
# 2. Input Encoding (default to UTF-8)
# 3. Output Encoding
# 4. Handle Errors
#----------------------

#!usr/bin/env python3 

import sys
import logging

__version__ = '0.01'

logging.basicConfig(level = logging.DEBUG) 

class Encode:
   
    def __init__(self, fin, output_encode, input_encode):
        self.input_encode = input_encode
        self.output_encode = output_encode
        self.fin = fin
    
    def run(self):
        lis = []
        logging.debug(f"Converting file from {self.input_encode}")
        with open(self.fin, encoding = self.input_encode) as fout:
            for line in fout:
                lis.append(line)
        with open(self.fin, 'w', encoding = self.output_encode) as fout:
            for word in lis:
                fout.write(word)
        logging.debug(f"File converted to {self.output_encode}")
        
def main():
   encode = Encode(sys.argv[1], sys.argv[2], sys.argv[3])
   encode.run()

def log_error(error):
    return error

if __name__ == '__main__':
    try:
        main()
    except (FileNotFoundError, ValueError, IndexError, LookupError) as e:
        logging.debug(log_error(e))
        
        # Add argparse commands next 
