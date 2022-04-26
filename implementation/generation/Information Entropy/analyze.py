import csv
import os
from collections import Counter
from entropy import EntropyCalculator
from fitdistribution import *
import numpy as np

#a utility developed to aid in graphing
#note that the version here has diverged from the main repo
from Volsec import *

#necessary due to size of csv files
csv.field_size_limit(500 * 1024 * 1024)

#Create directory structure
if not os.path.exists("Graphs/"):
    os.makedirs("Graphs/")
if not os.path.exists("Output/"):
    os.makedirs("Output/")

dirstring = "..\password_corpus"
outputfile = "analyze.csv"
directory = os.fsencode(dirstring)

charsets = [
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '0123456789',
]

ent = EntropyCalculator()

entropy = {}
counters = {}
numpwds = {}
charprobs = {}
counterratios = {}
pwd_len = {}
charlist =  {}
uses_every_char = {}

files = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        files.append(filename)

files.sort() #sort the files by name

filenames = []
for i in range(0,len(files)):
    filenames.append(files[i][0:-4])

def num_there(s):
    return any(i.isdigit() for i in s)

def get_sequences(s):

    seq = {}
    count = 0
    char = ""
    for c in s:
        count += 1
        if c != char:
            if count > 1:
                if char not in seq:
                    seq[char] = [count]
                else:
                    seq[char].append(count)
            count = 0
        char = c

    return seq

def intersect(a, b):
    """ return the intersection of two lists """
    return len(list(set(a) & set(b)))

def uses_char_every_set(password,symbolset):
    uniqueCharInPass = len(set(password))
    letters = intersect(password,charsets[0]) 
    numbers = intersect(password,charsets[1])
    if symbolset == "all":
        if letters > 0 and numbers > 0 and (letters + numbers) < uniqueCharInPass:
            return True 
        else:
            return False 
    elif symbolset == "ls":
        if letters > 0 and numbers == 0 and letters < uniqueCharInPass:
            return True 
        else:
            return False 
    elif symbolset == "l":
        if letters > 0 and numbers ==0 and letters == uniqueCharInPass:
            return True 
        else:
            return False
    if symbolset == "ld":
        if letters > 0 and numbers > 0 and (letters + numbers) == uniqueCharInPass:
            return True 
        else:
            return False
    if symbolset == "sd":
        if numbers > 0 and letters == 0 and numbers < uniqueCharInPass:
            return True 
        else:
            return False

for z in range(0,len(files)):
    #store file name
    filefullname = files[z]
    filename = filenames[z]
    all_comp = ["chrome", "edge", "dashlane", "1password"]
    if filename in all_comp:
        charset = "all"
    else:
        charset = "ld"
    '''
    if "all." in filefullname:
        charset = "all"
    elif "sd." in filefullname:
        charset = "sd"
    elif "ld." in filefullname:
        charset = "ld"
    elif "l." in filefullname:
        charset = "l"
    elif "ls." in filefullname:
        charset = "ls"
    '''


    #zxcscore = []
    repeat = {}

    pwdcount = 0
    length = 0
    useseverycharcount = 0
    counter = Counter() # Use counter to count character usage

    with open(os.path.join(dirstring, filefullname), encoding='utf8') as file:
        # had to use symbol that would not show up in passwords to avoid aberrant behavior for quote and delimiter - defaults of '"' and ',' a problem
        reader = csv.reader(file,quotechar='Ω',delimiter='Ω')
        for row in reader:
            if len(row) >= 1:
                pwdcount += 1
                pwd = row[0]
                if length == 0:
                    length = len(pwd)
                
                #multiCounter.update(pwd)
                #labels, values = zip(*multiCounter.items())
                #multiCounter.clear()
                #seqs = get_sequences(pwd)

                if uses_char_every_set(pwd,charset):
                    useseverycharcount += 1

                counter.update(pwd)

    uses_every_char[filename] = round((float(useseverycharcount) / pwdcount),2)
    counters[filename] = counter
    numpwds[filename] = pwdcount
    pwd_len[filename] = length

    # calculate probability of each character occurring
    labels, values = zip(*counter.items())
    charlist[filename] = ''.join(labels)
    values = [float(x) / (numpwds[filename]*length) for x in values]
    counterratios[filename] = values
    probdict = dict(zip(labels, values))

    charprobs[filename] = probdict

# Calculations
f = open("Output/" + "analyze" + "_stats_readable.txt","w",encoding="utf-8")
f2 = open("Output/" + "analyze" + "_stats.txt","w",encoding="utf-8")
entropies = {}
for filename,prob in charprobs.items():
    # calculate shannon entropy for entire set of data
    ratios = counterratios[filename]
    print(prob)
    shannonEnt = ent.entropy(prob)
    pwdEnt = ent.password_entropy(pwd_len[filename],len(charprobs[filename]))
    stdDev = round(np.std(ratios),3)
    f2.write(filename + "ζ" + charlist[filename] + "ζ" + str(shannonEnt) + "ζ" + str(pwdEnt) + "ζ" + str(len(prob)) + "ζ" + str(numpwds[filename]) + "ζ" +
         str(round(np.mean(ratios),3)) + "ζ" + str(stdDev) + "ζ" + str(round(min(ratios),3)) + "ζ" + str(round(max(ratios),3)) + "ζ" + str(uses_every_char[filename]) + "\n")
    f.write(filename + "\n")
    f.write("character_set: " + charlist[filename] + "\n")
    f.write("set_shannon_entropy: " + str(shannonEnt) + " , pwd_entropy: " + str(pwdEnt) + " with " + str(len(prob)) + " symbols, " + str(numpwds[filename]) + " samples\n")
    f.write("letter frequency ratios: mean: " + str(round(np.mean(ratios),3)) + ", stddev: " + str(stdDev) + ", min: " + str(round(min(ratios),3)) + ", max: " + str(round(max(ratios),3)) + "\n")
    f.write("Percentage that use ever char: " + str(uses_every_char[filename]) + "\n\n")
f.close()
f2.close()


'''
#Graph

if len(counterratios) > 0:
    graph_multi_cdf(counterratios,"Character Frequency / Num Passwords","Password Configuration","Ratio","CDF of Passwords","Graphs/FreqRatio.png",False)

# need to iterate again to get shannon entropies ounce the probabilities of individual characters have been harvested
for z in range(0,len(files)):
    #store file name
    filefullname = files[z]
    filename = filenames[z]

    Ent = []

    with open(os.path.join(dirstring, filefullname), encoding='utf8') as file:
        # had to use symbol that would not show up in passwords to avoid aberrant behavior for quote and delimiter - defaults of '"' and ',' a problem
        reader = csv.reader(file,quotechar='Ω',delimiter='Ω')
        for row in reader:
            if row[0] != "":
                pwd = row[0]
                Ent.append(float(ent.password_entropy(len(pwd),len(charprobs[filename]))))

        entropy[filename] = Ent

def ttest(a,b):
    t, p = ttest_ind(a, b, equal_var=False)
    return [t,p]

for fil,ent in shannon_entropy.items():
    data = fit(ent)
    print(fil + ", mean: " + str(np.mean(ent)) + ", std: " + str(np.std(ent)) + ", fits " + data[0] +  " with p value " + str(data[1]))

print("\n")
f,p = f_oneway(*list(shannon_entropy.values()))

print("F score = " + str(round(f,5)) + ", p value = " + str(round(p,5)))
'''