# mcx setting equivalence test
# ajohnson - 2014 - 2 11

from __future__ import division
import sys

# use ard to send a unix command: mcxquery -computerOnly
# to all the computers that you want to compare mcx values for
# export the command results as a text file, that will be the input

infile = open(sys.argv[1], 'r')

# get raw text
raw = infile.read()
infile.close()

# split by means of two new lines (the separator for computers)
computerlist = raw.split('\n\n')
computerlist = computerlist[:-1]


# now we need to only take the relevant parts of the mcxquery to compare
# starting index = 'com.apple.mcxprinting'
# ending index = the beginning of the next com, which is com.microsoft.autoupdate2

mcxlist = []

for computer in computerlist:

    # in case there is just no plist...
    if 'com.apple.mcxprinting' in computer:

        name = computer[:12].strip()
        beg = computer.index('com.apple.mcxprinting')

        # adas mcx settings end at the mcx printing so we can use a try/except to deal with that
        try:
            beg = computer.index('com.apple.mcxprinting')
            end = computer.index('com.microsoft.autoupdate2')
            mcxlist.append(computer[beg:end])

        except ValueError:
            mcxlist.append(computer[beg:])
    else:
        print "{} has no com.apple.mcxprinting plist !".format(computer[:12])



# here we create a dictionary for the name + match key value pairs
match_dict = {}

# loop through the list
for setting in range(len(mcxlist)):

    # slice the computer name
    name =  computerlist[setting][:12].strip()

    # create a blank match count for matches
    match_count = 0

    # loop again and see if one setting matches all the others
    for setting2 in mcxlist:
        if mcxlist[setting] == setting2:
            match_count += 1

    # add values to the dictionary
    match_dict[name] = match_count

# print results
print "="*25

print "{:15} {:3}".format("Computer", "Matches\n")
for k,v in match_dict.items():
    print "{:15} {:3}".format(k, v)






