#!/usr/bin/python -tt

#DegParse:
# Parses a Degradome Density File from CleaveLand for likely
# sliced transcripts, regardless of sRNA presence.
# Returns a list of gene names with >x reads AND category 0

import sys

#open a degradome density file

def getFile(filename):
    INfile = open(filename, 'rU')
    gene = ''
    result = []
    for line in INfile:
        if line[:3] == '@ID':
            gene = line[4:-1]
        elif line[:3] == '@LN':
            next(INfile)
        elif line == '\n':
            gene = ''
        else:
            line = gene + '\t' + line
        result.append(line)
    return result

#read each line

def main():
    printout = getFile(sys.argv[1])
    print(printout)

if __name__ == '__main__':
  main()
