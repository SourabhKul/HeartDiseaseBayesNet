from __future__ import division
import numpy as np
import time
import bn
import bn_custom



accuracy_bn = np.array(np.zeros(5))
Net1 = bn.BayesNet()
t0 = time.time()
for i in range(1,6):
    data_train = np.loadtxt(('data-train-'+str(i)+'.txt'), delimiter=',')
    data_test = np.loadtxt(('data-test-'+str(i)+'.txt'), delimiter=',')
    N,_ = data_test.shape
    Net1.fit(data_train)
    prediction = Net1.predict_hd(data_test)
    accuracy_bn[i-1] = np.sum(prediction==data_test[:,-1])/N

t1 = time.time()    
print(' Original Network Model \n Individual accuracies:'+str(accuracy_bn)+' \n Mean:'+ str(np.mean(accuracy_bn))+ ' \n Standard deviation:'+ str(np.std(accuracy_bn)*100)+ '%\n execution time:'+ str(t1-t0))


accuracy_bn_custom = np.array(np.zeros(5))
Net2 = bn_custom.BayesNetCustom()
t0 = time.time()
for i in range(1,6):
    data_train = np.loadtxt(('data-train-'+str(i)+'.txt'), delimiter=',')
    data_test = np.loadtxt(('data-test-'+str(i)+'.txt'), delimiter=',')
    N,_ = data_test.shape
    Net2.fit(data_train)
    prediction = Net2.predict_hd(data_test)
    accuracy_bn_custom[i-1] = np.sum(prediction==data_test[:,-1])/N

t1 = time.time()    
print(' \n Modified Network Model \n Individual accuracies:'+str(accuracy_bn_custom)+' \n Mean:'+ str(np.mean(accuracy_bn_custom))+ ' \n Standard deviation:'+ str(np.std(accuracy_bn_custom)*100)+ '%\n execution time:'+ str(t1-t0))