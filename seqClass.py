#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Input motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
# Transform the input sequence to uppercase
args.seq = args.seq.upper() 
if re.search('^[ACGUT]+$', args.seq): 
    if 'T' in args.seq and 'U' in args.seq:  # Added condition to check for the presence of both 'T' and 'U' in the sequence ensuring base exclusivity
        print ('The sequence contains both DNA and RNA bases')
    elif 'T' in args.seq:
        print ('The sequence is DNA')
    elif 'U' in args.seq:
        print ('The sequence is RNA')
else:
    print ('The sequence is not DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
