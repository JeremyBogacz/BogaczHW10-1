# Created by Jeremy Bogacz on 11/30/2021

# This program takes in two files that have over other word
# of a scentence in reverse order inside them. The program
# will reconstruct the scentence and write that to an output
# file.

# Example invocation: python reconstructSentence.py input1.txt input2.txt
import sys

if (len(sys.argv) != 3):
    print "Usage: python reconstructSentence.py file1 file2"
    print "Example invocation: python reconstructSentence.py input1.txt input2.txt"
    exit()

# Opent the two input files
f1 = open(sys.argv[1],"r")
f2 = open(sys.argv[2],"r")

# Get the full line from each file
line1 = f1.readline()
line2 = f2.readline()

# Strip the newline off of the string
line1.strip()
line2.strip()

# Split the string into a list of words
list1 = line1.split()
list2 = line2.split()

# Get the length of each list
length1 = len(list1)
length2 = len(list2)

# Print out list data
print 
print "List 1: ", list1
print
print "List 1 Length: ", length1
print 
print
print "List 2: ", list2
print
print "List 2 Length: ", length2
print

# Decrement lengths to index of the last element
length1 -= 1
length2 -= 1

# Create output list
out = []

# Add items to the list until one of the inputs is empty
while ((length1 > 0) | (length2 > 0)):
    out.append(list1[length1])
    out.append(list2[length2])
    
    length1 -= 1
    length2 -= 1

# Add the leftovers of the list that didnt get emptied
while (length1 >= 0):
    out.append(list1[length1])
    length1 -= 1

while (length2 >= 0):
    out.append(list2[length2])
    length2 -= 1

# Print output data
print "The List Out is: ", out
print

# Write output to file
f3 = open("output.txt","w")
for i in out:
    f3.write(i + " ")
