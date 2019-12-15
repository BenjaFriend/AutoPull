# This script will walk through all sub-directories in the current directory
# and pull the most recent updates

import os
import argparse

# Parse cmd line args
descriptionText = 'This script will walk through all sub-directories, fetch all tags, and pull.'
parser = argparse.ArgumentParser(descriptionText)
parser.add_argument("-t", "--tag", help="Checkout this branch or tag for each repo")
parser.add_argument("-d", "--directory", help="The direcotry that holds all the repos you want to update. Default is current dir.")
parser.add_argument("-b", "--branch", help="After pulling and checking out, create a new branch of this name for each repo")

args = parser.parse_args()

# Store the starting direcotry
rootDir = os.getcwd()

# If we used an arg for the direcotry, then use that instead of the current 
if args.directory:
    rootDir = args.directory

print("\n----- Auto Pull config --------")
print("Directory: " + rootDir)

if args.tag:
    print("Checkout: ", args.tag)
else:
    print("Checkout: NONE")

if args.branch:
    print("New branch: " + args.branch)
else:
    print("New branch: NONE")
print("-------------------------------\n")

for currentDir in filter(os.path.isdir, os.listdir(rootDir)):
    
    print("\n------\nUpdating: " + currentDir)
    # Change directories
    os.chdir(currentDir)

    # Get the most recent tags and pull latest
    os.system("git status")
    os.system("git checkout --theirs .")

    # Update all tags and check one out if specified
    os.system("git fetch --all --tags --prune -q")  
    os.system("git pull --quiet")

    if args.tag:
        os.system("git checkout " + args.tag)

    
    # Create a new branch if specified
    if args.branch:
        os.system("git checkout -b " + args.branch)

    # Go back to the original directory
    os.chdir(rootDir)

print("-------- Update complete! --------")
