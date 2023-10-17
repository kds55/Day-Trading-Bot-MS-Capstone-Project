import numpy as np
import pandas as pd

def hard_voting_classifier_predict(models, vote_threshold, X_test):
    #setting up array for appropriate size
    pred_array = np.zeros(len(X_test))
    
    for model in models:

        model_name = str(model).split('(')[0]
          
        #making predictions and a adjustment for keras models to get predictions formatted
        pred = model.predict(X_test)
        if model_name[1:6] == 'keras':
            pred = np.where(pred > 0.5, 1, 0).flatten()

        #stacking current predictions onto the running array
        pred_array = np.vstack([pred_array, pred])
    
    #calculating predictions by summing all the arrays down their columns. Any sums beyond 3 are classified as 1.
    pred = np.where(pred_array.sum(axis = 0) >= vote_threshold, 1, 0)
    
    return pred