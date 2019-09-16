# Auto Pull

This is a smiple python script that will pull and update the latest tags on 
a folder that is full of other git repos.


## Requirements

* [Python 3](https://www.python.org/)

## Folder Structure

This script will go through each folder in the current directory that it is ran
from, and will 

```
- Repos
- autoPull.py
--> Repo_1
--> Repo_2
--> Repo_3
--> Repo_4
```

## Usage

```
usage: This script will walk through all sub-directories, fetch all tags, and pull.
       [-h] [-t TAG] [-d DIRECTORY] [-b BRANCH]

optional arguments:
  -h, --help            show this help message and exit
  -t TAG, --tag TAG     Checkout this branch or tag for each repo
  -d DIRECTORY, --directory DIRECTORY
                        The direcotry that holds all the repos you want to
                        update. Default is current dir.
  -b BRANCH, --branch BRANCH
                        After pulling and checking out, create a new branch of
                        this name for each repo
```