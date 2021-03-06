#! /usr/bin/python
import numpy as np
import xgboost as xgb
#import csv

# label need to be 0 to num_class -1
train_X = np.genfromtxt('../trainX.csv',delimiter=',')[1:,1:]

train_Y = np.genfromtxt('../trainY2.csv',delimiter=',')[1:,1:]
print ('Reading Completed')
#train = data[:int(sz[0] * 0.7), :]
#test = data[int(sz[0] * 0.7):, :]
#
#train_X = train[:,0:33]
#train_Y = train[:, 34]


#test_X = test[:,0:33]
#test_Y = test[:, 34]

xg_train = xgb.DMatrix( train_X, label=train_Y)
print ('xgb matrix Completed')
#xg_test = xgb.DMatrix(test_X, label=test_Y)
# setup parameters for xgboost
param = {}
# use softmax multi-class classification
param['objective'] = 'multi:softmax'
# scale weight of positive examples
param['eta'] = 0.1
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 12

#watchlist = [ (xg_train,'train'), (xg_test, 'test') ]
num_round = 5
bst = xgb.train(param, xg_train, num_round);
## get prediction
#pred = bst.predict( xg_test );
#
#print ('predicting, classification error=%f' % (sum( int(pred[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y)) ))
#
## do the same thing again, but output probabilities
#param['objective'] = 'multi:softprob'
#bst = xgb.train(param, xg_train, num_round, watchlist );
## Note: this convention has been changed since xgboost-unity
## get prediction, this is in 1D array, need reshape to (ndata, nclass)
#yprob = bst.predict( xg_test ).reshape( test_Y.shape[0], 6 )
#ylabel = np.argmax(yprob, axis=1)
#
#print ('predicting, classification error=%f' % (sum( int(ylabel[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y)) ))