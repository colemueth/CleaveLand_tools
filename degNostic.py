#!/usr/bin/python -tt

"""
DegNostic.py
Parses two CleaveLand-generated degradome density files
for cut sites that are unique to one treatment.
It's agnostic with regard to sRNA presence, i.e. it identifies differences
regardless of whether an sRNA is predicted to bind there or not.

Usage:
degNostic.py file1 n1 file2 n2
where file1 is the degradome density file of interest;
n1 is an integer cutoff for calling significant peaks in file1;
file2 is a second degradome density file that is being "subtracted";
n2 is an integer cutoff for excluding peaks that are also present in file2.

Example:
python InfSample_dd.txt 15 UninfectedFile.dd.txt 2
will output the cut sites with 15 or more reads in "InfSample"
and 2 or fewer reads in "UninfSample".
"""

import sys

def getDegradome(filename):
# Read in a degradome density file.
# Add gene names to each block of degradome entries and return it as a list.
    INfile = open(filename, 'r')
    gene = ''
    degradome = []
    for line in INfile:
        if line.startswith('#'): # ignore header comments
            continue
        elif '@ID:' in line: # cut off '@ID:' and store gene name
            gene = line[4:-1]
            next(INfile)    # skip the next line (@LN...)
        elif line == '\n': # clear gene name when a new degradome entry is reached
            gene = ''
        elif line[-2].isdigit(): # if last char is a degradome category:
            degLine = gene + '\t' + line # add gene name and row to list
            degradome.append(degLine)
    INfile.close()
    return degradome

# Establish "positive" cases, where n1 or more reads are present at a given
# location in infected, and it is the "Category 0" (highest) peak for that transcript.
def infected():
    degI = getDegradome(sys.argv[1])
    Ilist = []
    for irow in degI:
        rowList = irow.split()
        if int(rowList[2]) >= int(sys.argv[2]) and int(rowList[3]) == 0:
        # if reads at cut site are above threshold and it is Cat 0
            Ilist.append(str(rowList[0] + '\t' + rowList[1]))
    return Ilist

# Establish "negative" cases, where multiple reads are present at a given
# location in uninfected.
def uninfected():
    degU = getDegradome(sys.argv[3])
    Ulist = []
    for urow in degU:
        rowList = urow.split()
        if int(rowList[2]) >= int(sys.argv[4]): # if site is above exclusion cutoff
            Ulist.append(str(rowList[0] + '\t' + rowList[1]))
    return Ulist

def main():
    OUTfile = open(sys.argv[1] + '_filter.txt', 'w') # create output file
    degU = uninfected()
    print("Items in Uninfected list: ", len(degU))
    degI = infected()
    print("Items in Infected list: ", len(degI))
    for i in degI:
        if i not in degU: # list comparison
            OUTfile.write(i + '\n')
    OUTfile.close()

if __name__ == '__main__':
    main()
