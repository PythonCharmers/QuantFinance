# Solution question 2
def prior(model):
    return {'chickenpox': 1e-4, 'not chickenpox': 1 - 1e-4}.get(model)

def posterior(model, data, normalize=True, x=0.2):
    """
    Posterior probability of the model ('chickenpox' / 'not chickenpox')
    given the data ('spots' / 'no spots')
    
    
    x here is P("not chickenpox" | "spots")
    """
    numerator = likelihood(data, model, x) * prior(model)
    if not normalize:
        return numerator
    else:
        return numerator / evidence(data)

def likelihood(data, model, x=0.2):
    """
    Conditional probability of the data ('spots' / 'no spots') given the model ('chickenpox' / 'not chickenpox').
    
    x here is P("not chickenpox" | "spots")
    """
    if data == 'spots':
        return {'chickenpox': 0.8, 'not chickenpox': x}[model]
    else:
        # no spots
        return {'chickenpox': 0.2, 'not chickenpox': 1 - x}[model]
    
def evidence(data):
    """
    The proportion of people in the general population who have spots or no spots
    """
    return (posterior('chickenpox', data, normalize=False) +
            posterior('not chickenpox', data, normalize=False))

conditional_sum = (posterior('chickenpox', 'spots', normalize=True) +
                   posterior('not chickenpox', 'spots', normalize=True))

conditional_sum

posterior('chickenpox', 'spots')
