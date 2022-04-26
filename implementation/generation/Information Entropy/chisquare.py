# https://github.com/oeschsec/pwmsecurity-usenix2020

import csv
import os
from collections import Counter
import scipy.stats
from Volsec import *

dirstring = "..\password_corpus"
outputfile = "chisquare.csv"
directory = os.fsencode(dirstring)

out = open(os.path.join(os.getcwd(), outputfile), 'w')

files = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        files.append(filename)

files.sort() #sort the files by name

filenames = []
for i in range(0,len(files)):
    filenames.append(files[i][0:-4])

for z in range(0,len(files)):
    #store file name
    filefullname = files[z]
    filename = filenames[z]
    counter = Counter()
    length = 0
    count = 0
    with open(os.path.join(dirstring, filefullname), encoding='utf8') as file:
        # had to use symbol that would not show up in passwords to avoid aberrant behaviour for quote and delimiter - defaults of '"' and ',' a problem
        reader = csv.reader(file,quotechar='Ω',delimiter='Ω')
        rowcount = 0
        for row in reader:
            rowcount += 1
            if rowcount > 1000000:
                break
            if len(row) >= 1:
                password = row[0]
                if length == 0:
                    length = len(password)
                count += length
                password = password.replace('\n', '').replace('\r', '')
                counter.update(password)
    labels, values = zip(*counter.items())
    foo = scipy.stats.chisquare(values)
    print(filename + "," + str(foo[0]) + "," + str(foo[1]) + "\n")
    out.write(filename + "," + str(foo[0]) + "," + str(foo[1]) + "\n")

out.close()
