'''
This is a very short demo of the BayesNet API
'''
import numpy as np
from code.bn import BayesNet

bn = BayesNet() 
data = np.loadtxt("data/data-train-1.txt", delimiter=",")
bn.fit(data)
test_data = np.loadtxt("data/data-test-1.txt", delimiter=",")
predictions = bn.predict_hd(test_data)
accuracy = np.mean(predictions == test_data[:,-1])

print "accuracy = {}".format(accuracy)

v = .3
bn.set(target_variable={"BP":"L"}, condition_variables={"G":"M"}, value=v)
theta_i = bn.get(target_variable={"BP":"L"}, condition_variables={"G":"M"})
print v,theta_i
