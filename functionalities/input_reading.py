import sys
import argparse

def readInput(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-p", "--path", type=int, help="Dennis is a cunt")
    
    options = parser.parse_args(args)
    
    path = options.path 
    return path