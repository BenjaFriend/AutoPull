# This script will clone all repos from an organization
# using the GitHub API

import os
import json
import argparse
import requests

# Parse cmd line args
descriptionText = 'Clone all repos from a given organization using the GitHub API'
parser = argparse.ArgumentParser(descriptionText)
parser.add_argument("-o", "--org", help="The name of the organization you want to clone all repos from", required=True)
parser.add_argument("-t", "--token", help="GitHub API access token (if the organization has private repos)")
parser.add_argument("-d", "--directory", help="The output directory to clone the repos to")

# Get the outdir and parse args
args = parser.parse_args()
outDir = os.getcwd()
# org is a required argument
orgName = args.org

print("\n----- Batch cloning Config-----\n")
print("\tOrganization name: \t" + orgName)
if(args.token):
    print("\tToken: \t", args.token)
else:
    print("\tToken: \tNONE")

if(args.directory):
    outDir = args.directory
print("\tOutput Dir: \t", outDir)
print("\n-------------------------------\n")

# Make a curl request to the github API with the given arguments
getRequest = 'https://%24GITHUB_AT:@api.github.com/orgs/' + orgName + '/repos'

if(args.token):
    params = (
        ('access_token', args.token),
    )
    res = requests.get(getRequest, params=params)
else:
    res = requests.get(getRequest)

binary = res.content
jsonData = json.loads(binary)

#print(jsonData)

for repo in jsonData:
    print(repo['full_name'])
    
#print(json_obj[0])
