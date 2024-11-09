import pandas as pd
from numpy import random

ACTUALMASS = 20

NUMOFDATA = 1000
NUMOFZEROES = NUMOFDATA * 5
NUMOFROWS = NUMOFDATA + NUMOFZEROES

MAX_ERROR_IN_FORCE = 20
MAX_ERROR_IN_ACCERLATION = 20
MAX_ACCERLATION = 200

accerlations = [0] * NUMOFROWS
forces = [0] * NUMOFROWS

for i in range(0,NUMOFDATA):
    accerlation = (random.rand() * 2 - 1) * MAX_ACCERLATION
    forces[i] = (random.rand() * 2 - 1) * MAX_ERROR_IN_FORCE + ACTUALMASS * accerlation
    accerlations[i] = accerlation + (random.rand() * 2 - 1) * MAX_ERROR_IN_ACCERLATION

for i in range(NUMOFDATA,NUMOFROWS):
    accerlations[i] = 0
    forces[i] = 0


data = {'accerlation' : accerlations, 'force' : forces}

df = pd.DataFrame(data)

df.to_csv('massForce.csv')


