
def query_5_a(bn):
    '''
    Please write a method which returns the distribution over the query
    variable, CH.

    You should return a dictionary, {"H":p1, "L":p2} where p1 and p2 are
    the probabilities that the patient has high or low cholesterol.

    You should be able to use the get method from your BayesNet class to implement
    this function.

    inputs:
        - bn: a parameterized Bayes Net
    returns:
        - out: a dictionary of probabilities, {"H":p1, "L":p2}

    '''
    
    instance = {'A': 2, 'G':2, 'CH':1, 'CP':4, 'BP' : 1, 'ECG' : 1, 'HR' : 1, 'EIA' : 1, 'HD' : 1} 
    num = bn.joint_prob(instance)
    dem = num
    instance['CH'] = 2
    dem += bn.joint_prob(instance)
    l_prob =  float(num)/float(dem)
    h_prob = 1-l_prob
    out = {"H": h_prob, "L": l_prob}
    print(l_prob,h_prob)
    return out


def query_5_b(bn):
    '''
    Please write a method which returns an answer to query 5b from the problem set
    input:
        - bn: a parameterized Bayes Net

    returns:
        answers, a dictionary with two keys, "H" and "L". "H" is the probability
        of high BP given the specified conditions. "L" is the probability
        of low BP, given the specified conditions
    '''
    '''
    alt_values = {'A' : ('>=55','45-55','<45'), 'G' : ('M','F'), 'CP' : ('Non-Angial','Atypical','None','Typical'), 'BP' : ('H', 'L'),'CH' : ('H','L'), 'ECG' : ('Abnormal','Normal'),
    'HR' : ('H','L'), 'EIA' : ('Y','N'), 'HD' : ('Y','N') }
    
    #instance2 = {'A' :2, 'G' : 1, 'CH':2, 'BP':1, 'ECG':1, 'HR':2, 'CP':1, 'EIA':2, 'HD':1}
    num = 0
    dem = 0
    
    for g in alt_values['G']:
        num += bn.get({'G': g},{})*bn.get({'CH':'H'},{'G': g,'A' :'45-55'})*bn.get({'BP':'L'},{'G': g})*bn.get({'HR':'H'},{'A' :'45-55','BP':'L','HD':'N'})* bn.get({'HD':'N'},{'BP':'L','CH':'H'})
    
    for g in alt_values['G']:
        for bp in alt_values['BP']:
            dem += bn.get({'G': g},{})*bn.get({'CH':'H'},{'G': g,'A' :'45-55'})*bn.get({'BP':bp},{'G': g})*bn.get({'HR':'H'},{'A' :'45-55','BP':bp,'HD':'N'})* bn.get({'HD':'N'},{'BP':bp,'CH':'H'})
    '''
    values = {'A' : (1,2,3), 'G' : (1,2), 'CP' : (1,2,3,4), 'BP' : (1, 2),'CH' : (1,2), 'ECG' : (1,2),
    'HR' : (1,2), 'EIA' : (1,2), 'HD' : (1,2) }
    instance = {'A' :2, 'G' : 1, 'CH':2, 'BP':1, 'ECG':1, 'HR':2, 'CP':1, 'EIA':2, 'HD':1}
    num = 0
    dem = 0
    for g in values['G']:
            instance['G'] = g
            num += bn.joint_prob(instance)
    for g in values['G']:
            for bp in values['BP']:
                instance['G'] = g
                instance['BP'] = bp
                dem += bn.joint_prob(instance)
    
    l_prob =  float(num)/float(dem)
    h_prob = 1-l_prob
    print(l_prob,h_prob)
    out = {"H": h_prob, "L": l_prob}

    return out
