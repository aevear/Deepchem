# Deepchem
A script I started working on but didn't finish during my Masters Internship for testing batches of canidate molecules for potential toxicity. 

#Setup
I ran this code using the default deepchem setup and running in the deepchem source enviroment, though if you install the deepchem python library that won't be nessesary.

#Input data
The code specifically runs a specific, hard coded are of my computer, but this will be changed in future edits of the code. Since I did not have a specific group of SMIlE codes to test, I just took the last 580 compounds in the tox21 database and stripped them of any values. 
Due to the way that deepchem imports the data it requires that you fill in the first 12 fields, even if they are blank. If you want to import your own data I would follow that format. 
The other option is to edit the parameters when making the model so that you can ignore some of the features in the sample file.

#Tox21 Data
At the momet the tox21 data is not easy to change as it is loaded in with the deepchem library on install. However if you have a more complete version of the the tox21 database you can either import the data similarly to what I did, though you will need to add a splitter code. 
The other option is to edit the source database for the chemical compounds so that they load in rather than the defaults. They are located in the datasets folder under tox21.csv.gz
