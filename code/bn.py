from __future__ import division
import numpy as np
import itertools

class BayesNet(object):
    """
    This class implements a Bayes Net
    """
    
    def __init__(self):
        '''
        This method will run upon initialization of the Bayes Net class
        You can structure this class in whatever way seems best.

        The class will need to support four methods by the end of the assignment.
            - fit: sets the parameters of the Bayes Net based on data
            - predict_hd: predicts a heart disease value, based on observed data
            - get: returns a given real-valued parameter
            - set: set the value of a parameter

        input:
            - None
        returns:
            - None
        '''
        """ values each discrete node can take """
        global values
        values = {'A' : (1,2,3), 'G' : (1,2), 'CP' : (1,2,3,4), 'BP' : (1, 2),'CH' : (1,2), 'ECG' : (1,2),
        'HR' : (1,2), 'EIA' : (1,2), 'HD' : (1,2) }
        #global alt_values
        #alt_values = {'A' : ('>=55','45-55','<45'), 'G' : ('M','F'), 'CP' : ('Non-Angial','Atypical','None','Typical'), 'BP' : ('H', 'L'),'CH' : ('H','L'), 'ECG' : ('Abnormal','Normal'),
        #'HR' : ('H','L'), 'EIA' : ('Y','N'), 'HD' : ('Y','N') }

        """ order in which data is stored in the file """
        global order
        order = ['A', 'G', 'CP', 'BP', 'CH', 'ECG', 'HR','EIA', 'HD']

        global CPT
        CPT = {}

        global instance

        instance = {}

        global bn
        bn = {}
        bn['A'] = []
        bn['G'] = []
        bn['CP'] = ['HD']
        bn['BP'] = ['G']
        bn['CH'] = ['A', 'G']
        bn['ECG'] = ['HD']
        bn['HR'] = ['HD', 'BP', 'A']
        bn['EIA'] = ['HD']
        bn['HD'] = ['CH', 'BP']

        ''' Setting up CPTs '''
        for node, parents in bn.items():
            #parents = bn[node]
            CPT[node] = {}
            if len(parents) == 0:
                for node_value in values[node]:
                    CPT[node][node_value]=1/len(values[node])
                         
            else:
                parent_values = [ values[parent] for parent in bn[node] ]
                for product in itertools.product(*parent_values):
                    for node_value in values[node]:
                        CPT[node][(node_value,)+ product]=float(1/len(values[node]))                       
        #print(CPT)               
        ''' Setting up Counters '''
        global counts
        counts = {}
        for node in bn.keys():
            counts[node] = {}
        for node, parents in bn.items():
            if len(parents) == 0 :
                for nodeval in values[node]:
                    counts[node][nodeval] = 0
            else :
                parentVals = [ values[parent] for parent in parents ] 
                for product in itertools.product(*parentVals):
                    counts[node][product] = 0
                    nodevals = values[node]
                    for nodeval in nodevals:
                        tmp = (nodeval, ) + product
                        counts[node][tmp] = 0
        
        pass

    def get(self, target_variable, condition_variables):
        '''
        This method does a lookup of a parameter value in your BayesNet
        For instance, you might want to lookup of p_theta(HD=N | CH=L, BP=L)

        inputs:
            - target_variable and value:
                - a dictionary, such as {'HD':'N'}
            - condition_variables and values
                - a dictionary, such as {'CH':'L', 'BP':'L'}
        returns:
            - The parameter value, a real value within [0,1]
            - If there is a no such parameter in the model, return None
        '''
        one_set = ['<45', 'Normal', 'L', 'F', 'N', 'Typical']
        two_set = ['45-55', 'Abnormal', 'H', 'M', 'Y', 'Atypical']
        three_set = ['>=55', 'Non-Angial']
        if target_variable.values()[0] in one_set :
            target_variable_value = 1
        
        elif target_variable.values()[0] in two_set :
            target_variable_value = 2

        elif target_variable.values()[0] in three_set:
            target_variable_value = 3

        else:
            target_variable_value = 4
                

        if condition_variables == {}:
            return CPT[target_variable.keys()[0]][target_variable_value]
        
        for variable in condition_variables.keys():
            if variable in bn[target_variable.keys()[0]]:
                pass
            else:
                return None
        condition_variables_values = tuple([condition_variables[variable] for variable in bn[target_variable.keys()[0]]])
        condition_variables_values_converted = []
        for value in condition_variables_values:
            if value in one_set:
                condition_variables_values_converted.append(1)
        
            elif value in two_set:
                condition_variables_values_converted.append(2)

            elif value in three_set:
                condition_variables_values_converted.append(3)

            else:
                condition_variables_values_converted.append(4)
       
        out = CPT[target_variable.keys()[0]][(target_variable_value,) + tuple(condition_variables_values_converted)]
        return out

    def set(self, target_variable, condition_variables, value):
        '''
        This method sets a parameter value in your BayesNet to value

        After you call the method, the parameter should be set to value
        For instance, you might want to set p(HD|BP,CH) = .222

        inputs:
            - target_variable and value:
                - a dictionary, such as {'HD':'N'}
            - condition_variables and values
                - a dictionary, such as {'CH':'L', 'BP':'L'}
            - value:
                -  probability between 0 and 1
        returns:
            - None
        '''
        probset = value
        one_set = ['<45', 'Normal', 'L', 'F', 'N', 'Typical']
        two_set = ['45-55', 'Abnormal', 'H', 'M', 'Y', 'Atypical']
        three_set = ['>=55', 'Non-Angial']
        if target_variable.values()[0] in one_set :
            target_variable_value = 1
        
        elif target_variable.values()[0] in two_set :
            target_variable_value = 2

        elif target_variable.values()[0] in three_set:
            target_variable_value = 3

        else:
            target_variable_value = 4
                

        if condition_variables == {}:
            CPT[target_variable.keys()[0]][target_variable.values()[0]] = probset

        '''
        for variable in condition_variables.keys():
            if variable in bn[target_variable.keys()[0]]:
                pass
            else:
                return 0
        condition_variables_values = tuple([condition_variables[variable] for variable in condition_variables])
        '''

        for variable in condition_variables.keys():
            if variable in bn[target_variable.keys()[0]]:
                pass
            else:
                return None
        condition_variables_values = tuple([condition_variables[variable] for variable in bn[target_variable.keys()[0]]])
        condition_variables_values_converted = []
        for value in condition_variables_values:
            if value in one_set:
                condition_variables_values_converted.append(1)
        
            elif value in two_set:
                condition_variables_values_converted.append(2)

            elif value in three_set:
                condition_variables_values_converted.append(3)

            else:
                condition_variables_values_converted.append(4)
        
        CPT[target_variable.keys()[0]][(target_variable_value,) + tuple(condition_variables_values_converted)] = probset
        
        pass   
 
    def fit(self, data):
        '''
        This method sets the parameters of your BayesNet to their MLEs
        based on the provided data. The layout of the data array and the
        coding used is described in the hadout.

        input:
            - data, a numpy array with the schema described in the handout
        returns:
            - None
        '''
        '''read data and count'''    
        for line in data:
            instance = {}
            vals = line           
            for i in range(len(vals)):
                instance[ order[i] ] = vals[i]
            for node, parents in bn.items():
                if len(parents) == 0 :
                    counts[node][ instance[node] ] += 1
                else :
                    parentval = tuple( [ instance[parent] for parent in parents ] )
                    nodeval = (instance[node], ) + parentval
                    counts[node][parentval] += 1
                    counts[node][nodeval] +=1	
		'''set CPTs based on counts'''
        for node, parents in bn.items():
            if len(parents) == 0 :
                total_cnt = 0
                for nodeval in values[node]:
                    total_cnt += counts[node][nodeval]
                for nodeval in values[node]:
                    CPT[node][nodeval] = float(counts[node][nodeval])/float(total_cnt)
            else :
                parentValues = [ values[parent] for parent in bn[node] ]
                for product in itertools.product(*parentValues):
                    countParent = counts[node][product]
                    if countParent == 0 : 
                        continue
                    for nodeval in values[node]:
                        query_set = {}
                        for parent in bn[node]:
                            query_set[parent] = values[parent]                  
                        CPT[node][(nodeval,)+ product] = float(counts[node][(nodeval,)+ product])/float(countParent)	        
        #print(CPT)
        pass

    def joint_prob(self, instance):
	""" get the joint probability given the instance """ 
	ans = 1
	for node, parents in bn.items():
		if len(parents) == 0 :
		    ans *= float(CPT[node][instance[node]])
		else :
		    parentval = tuple( [instance[parent] for parent in parents] )
		    nodeval = (instance[node], ) + parentval
		    ans *= float(CPT[node][nodeval])
	return ans


    def predict_hd(self, data):
        '''
        - input:
            - data. An array of shape (N,D). The layout of the data array and the
        coding used is described in the hadout.

        - returns:
            - the predictions for your data, a numpy array with shape = (N,)
        '''
        """ Classify the instance (patient) if he/she has heart-disease or not """
        N,D = data.shape
        #out = np.zeros((N,0))
        out = []
        for line in data:
            vals = line 
            for i in range(len(vals)):
                instance[ order[i] ] = vals[i]
            instance['HD'] = 1
            prob1 = self.joint_prob(instance)
            instance['HD'] = 2
            prob2 = self.joint_prob(instance)
            #print(prob1,prob2)
            if (prob1 >= prob2):
                out.append(1)
            else :
                out.append(2)                    
        output = np.array(out)
        return output
'''
data_train = np.loadtxt('data-train-2.txt', delimiter=',')
data_test = np.loadtxt('data-test-2.txt', delimiter=',')
Net1 = BayesNet()
Net1.fit(data_train)
print(Net1.predict_hd(data_test))
'''


#attempting query 5b locally

data_train = np.loadtxt('data-train-1.txt', delimiter=',')
print(data_train)
Net1 = BayesNet()
Net1.fit(data_train)
values = {'A' : (1,2,3), 'G' : (1,2), 'CP' : (1,2,3,4), 'BP' : (1, 2),'CH' : (1,2), 'ECG' : (1,2),
'HR' : (1,2), 'EIA' : (1,2), 'HD' : (1,2) }
instance = {'A' :2, 'G' : 1, 'CH':2, 'BP':1, 'ECG':1, 'HR':2, 'CP':1, 'EIA':2, 'HD':1}
num = 0
dem = 0
for g in values['G']:
        instance['G'] = g
        num += Net1.joint_prob(instance)
for g in values['G']:
        for bp in values['BP']:
            instance['G'] = g
            instance['BP'] = bp
            dem += Net1.joint_prob(instance)
    
l_prob =  float(num)/float(dem)
h_prob = 1-l_prob
print(l_prob,h_prob)
