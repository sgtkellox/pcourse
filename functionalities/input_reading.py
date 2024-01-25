import sys
import argparse


def readInput(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-p", "--path", type=int, help="")
    parser.add_argument("-t", "--thresh", type=int, help="variance thereshold")

    options = parser.parse_args(args)

    path = options.path
    thresh = options.thresh
    return path, thresh


def dropColByName(table, colName):
    newTable = table.drop(colName, axis=1)
    return newTable
