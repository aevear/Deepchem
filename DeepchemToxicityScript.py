"""
Script that trains multitask models on Tox21 dataset.
"""
#---------------------------------------------------------------------------
# This is the text that lines the top of every deepchem function, though it is
# Also commonly used in tensor flow functions as well to make python 2 and 3
# compatible code
#---------------------------------------------------------------------------
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import numpy as np
import deepchem as dc

#---------------------------------------------------------------------------
# This is the base code from deepchem to solve their Tox21 Challange but I
# use it due to the already created toxicity data set provided by deepchem
# and the fact that the code also generates the models specifically for this
# dataset
#---------------------------------------------------------------------------
# Load Tox21 dataset
n_features = 1024
tox21_tasks, tox21_datasets, transformers = dc.molnet.load_tox21()
train_dataset, valid_dataset, test_dataset = tox21_datasets

# Fit models
metric = dc.metrics.Metric(dc.metrics.roc_auc_score, np.mean)

model = dc.models.MultitaskClassifier(
    len(tox21_tasks),
    n_features,
    layer_sizes=[1000],
    dropouts=[.25],
    learning_rate=0.001,
    batch_size=50,
    use_queue=False)

# Fit trained model
model.fit(train_dataset, nb_epoch=1)
model.save()

#print("Evaluating model")
train_scores = model.evaluate(train_dataset, [metric], transformers)
test_score = model.evaluate(test_dataset, [metric], transformers)
valid_scores = model.evaluate(valid_dataset, [metric], transformers)

print("Training set scores")
print(train_score)
print("Test set scores")
print(test_score)
print("Validation set scores")
print(valid_scores)

#---------------------------------------------------------------------------
# This is the code that I generated, the above code came from deepchems Tox21 example
#---------------------------------------------------------------------------
# Preparing for making the loader - it needs the tasks generated above and a
# Featureier
featurizer = dc.feat.CircularFingerprint(size=1024)

#---------------------------------------------------------------------------
# Making the loader with a CSV loader, though there are functions for other
# input data types as well
loader = dc.data.CSVLoader(tasks=tox21_tasks, smiles_field="smiles", featurizer = featurizer)

#---------------------------------------------------------------------------
# Now we need to load in the location of the experimental dataset. This just so
# happened to be where mine is though it would be easy to import another one -
# You could also have a parameter when calling the file to be the input location
dataset_file = "~/Downloads/deepchem-master/examples/ExpTox21.csv"
experimental_data_set = loader.featurize(dataset_file, shard_size=579)

#---------------------------------------------------------------------------
# run the prediction algorithum - This is the key to the actual program. The
# predictor algorithum test each sample with the model's 12 tasks and provides
# an estimate of its reactibility.
results = model.predict(experimental_data_set)
resultStr, counter, idsArray = [], 0, []

#---------------------------------------------------------------------------
# Get the name array so that we can export them together. This part is not really
# nessesary but it was helpful for me to confirm that the program worked. This
# Could be replaced if you have a more specific way of importing the data
for x, y, w, ids in experimental_data_set.itersamples():
  idsArray.append(ids)

#---------------------------------------------------------------------------
# Print usable info in a format that is easy for the viewer to see the results
# Again, if you have a more specific way that you would like to import than don't
# Bother with this section, just edit it out and use the raw results file
for molecularSample in results:
  print(idsArray[counter])
  for task in molecularSample:
    print(str(task).split(" ", 1)[1].strip("]").strip(" "))
  counter +=1


#---------------------------------------------------------------------------
# Fin
#---------------------------------------------------------------------------
