#!/usr/bin/python3
#-*-coding: utf-8-*-

# A Python programme usually includes the following blocks, in order:
# - A few initialisation instructions (function and/or classes imports, eventually definition of global variables)
# - Local definitions of functions and/or classes
# - The main body of the programme

################################
### Import packages and load modules
################################

# The programme can use any number of functions, which are defined locally or imported from external modules.
# You can define such modules on your own.

import requests
from dotenv import load_dotenv
import os
import csv
import json
import urllib
##import numpy as np
##import pandas as pd

################################
### Function definitions
################################

load_dotenv()
api_key = os.getenv("API_KEY")

headers = {
    'api-key': api_key
}

url = 'https://api.ncbi.nlm.nih.gov/datasets/v2/gene/accession/NM_021803.4'
#url = 'https://api.ncbi.nlm.nih.gov/datasets/v2/gene/id/2/orthologs'
#url = 'https://api.ncbi.nlm.nih.gov/datasets/v2/gene/id/2'

# '?': after, there are parameters.

#r = requests.get(url, headers = headers)
#print(r.json())


### Explanations

# Download a genome and then store it in a file
# When I need data from the API:
# Shall I store the data, download them and store them, or shall I send them directly to treat them?
# => It depends on the size of the data, and the version of the data we need.
# Ex: If I have a genome which is 20Go size, it may be long to download and long to transfer from the server to the computer.
# In this case, we usually download the data and store it (in a file, on the computer).
# CPU manages everything; the data are either in RAM, either in disk, either in the network.
# To transfer data from disk to network, we have to use the CPU and RAM.

# API requests: the data is in the network: so, it will be sent to the RAM (mandatory).
# There is no direct flux from the network to the disk.
# When we do a HTTP request, the data are in the RAM, not in the disk.
# If we want to put the data into the disk, we have to create a file with write method, and write the content of the RAM
# into the disk.
# Ex: 20Go: retrieve small part by small part, and store these small packages into the disk. Then, we delete the packages 
# which are in the RAM. Python deletes the packages from the RAM on its own.

# When shall we store data on the disk?
# Ex: If we want to get the temperature of the day: storing it on the disk for 10 years is not useful.
# Information updated regularly => No need to store it on the disk.


# Write a function to retrieve information about genomic data from an accession number or a gene identifier using REST API
def info_accession(list_accession_nb): # The definition of a function often includes a list of parameters. 
    # These a always VARIABLES, which will receive their value when the function will be called.

    print(list_accession_nb)
    url = "https://api.ncbi.nlm.nih.gov/datasets/v2/gene/accession/"
    result = ",".join(list_accession_nb)
    url_encoded = urllib.parse.urlencode(result)
    r = requests.get(url_encoded, headers = headers)
    dictionary = r.json()
    return dictionary
#print(info_accession("NM_021803.4"))
print((info_accession(["NP_068575.1", "NP_851564.1"])))

def info_gene(gene_id): 
    # provide an integer (cf. NCBI REST API documentation:https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/rest-api/#)

    print(gene_id)
    url = "https://api.ncbi.nlm.nih.gov/datasets/v2/gene/id/" + gene_id
    r = requests.get(url, headers = headers)
    dictionary = r.json()
    return dictionary
dictionary = info_gene("2")

#for k in dictionary.keys():
    #print(k)

#for v in dictionary.values():
    #print(v)


### Writing a Python function to retrieve all companies in a specific activity sector (NAF code)
#def print_info_data(dictionary):



##############################
### Main body of the script
##############################