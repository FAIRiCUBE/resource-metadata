# dictionary for STAC ml-model fields
def build():
    dictionary = dict()
    dictionary['Objective'] = 'ml-model:prediction_type'
    dictionary['Approach'] = 'ml-model:learning_approach'
    dictionary['Architecture'] = 'ml-model:architecture'
    dictionary['Processor'] = 'ml-model:training-processor-type'
    dictionary['OS'] = 'ml-model:training-os'
    return dictionary
