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

url = 'https://api.ncbi.nlm.nih.gov/datasets/v2/gene/accession/NM_021803.4?api-key=api_key'

r = requests.get(url, headers = headers)
##print(r.json())


dictionary = r.json()
for k in dictionary.keys():
    print(k) 


##############################
### Main body of the script
##############################