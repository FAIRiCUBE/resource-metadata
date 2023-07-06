# dictionary for general fields (common between ML and non-ML resources)
def build():
    dictionary = dict()
    dictionary['Name of resource'] = 'title'
    dictionary['ID'] = 'id'
    dictionary['Description'] = 'description'
    dictionary['Main category'] = 'main-category'
    dictionary['Publication date'] = 'datetime'
    dictionary['Keyword'] = 'keywords'
    dictionary['Platform'] = 'platform'
    dictionary['Framework'] = 'framework'
    dictionary['Algorithm'] = 'algorithm'
    dictionary['Conditions for access and use'] = 'license'
    dictionary['Biases and ethical aspects'] = 'biases-and-ethical-aspects'
    return dictionary
