
from CIFAR10_loader import load_CIFAR10
import NearestNeighbor
import SVM
import Softmax
import time
import numpy as np


#nearest neightbor classffier
print "data loading...."
ticks = time.time()
trainData,trainLabels,trainBatchLabels,trainFilenames,testData,testLabels,testBatchLabels,testFilenames \
    = load_CIFAR10()
    #= load_CIFAR10('cifar-10-batches-py/data_batch_3')
print "data loading consuming %ds" %(time.time()-ticks)


'''
##################################################################
#        Nearest Neighbor classifier 
##################################################################
ticks = time.time()
trainData_rows = trainData.reshape(trainData.shape[0], 32 * 32 * 3) 
testData_rows = testData.reshape(testData.shape[0], 32 * 32 * 3) 
nn = NearestNeighbor.NearestNeighbor() 
nn.train(trainData_rows, trainLabels) 
testLabels_predict = nn.predict(testData_rows) 

print 'accuracy: %f' % ( np.mean(testLabels_predict == testLabels) )
print "taining loading consuming %ds" %(time.time()-ticks)
'''


'''
##################################################################
#        SVM classifier 
##################################################################
learning_rates = [1.4e-7, 1.5e-7, 1.6e-7]
regularization_strengths = [3e4, 3.1e4, 3.2e4, 3.3e4, 3.4e4]

#eta = learning_rates[0]
#lmbd = regularization_strengths[0]

#10000*3072 -> 10000*3073 add one more all-one line in the bottom
#trainData = np.concatenate((trainData,np.ones((trainData.shape[0],1))),axis=1) 
#testData = np.concatenate((testData,np.ones((testData.shape[0],1))),axis=1) 
trainData =  np.append(trainData,np.ones((1,trainData.shape[1])),axis=0)
testData =  np.append(testData,np.ones((1,testData.shape[1])),axis=0)

for eta in learning_rates:
    for lmbd in regularization_strengths:
        print "\n\nusing eta=%e lmbd=%e" %(eta,lmbd)
        svm = SVM.SVM()
        svm.SGD(trainData, trainLabels, 30, 10, eta, lmbd, testData, testLabels)

'''


##################################################################
#        Softmax classifier 
##################################################################
learning_rates = [1e-8, 5e-7, 1e-6, 1e-5]
regularization_strengths = [1e0, 1e2, 1e3, 5e3, 1e4, 5e4]
trainData = np.concatenate((trainData,np.ones((trainData.shape[0],1))),axis=1) 
testData = np.concatenate((testData,np.ones((testData.shape[0],1))),axis=1) 
eta = learning_rates[0]
lmbd = regularization_strengths[0]
#for eta in learning_rates:
    #for lmbd in regularization_strengths:
print "\n\nusing eta=%e lmbd=%e" %(eta,lmbd)
svm = Softmax.Softmax()
svm.SGD(trainData, trainLabels, 30, 10, eta, lmbd, testData, testLabels)
