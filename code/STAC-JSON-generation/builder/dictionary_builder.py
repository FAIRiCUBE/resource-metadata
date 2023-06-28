import re


# The purpose of this function is to build a dictionary <key: value> from the markdown of the issue's body.
# keys -> information requirements
# value -> the value(s) of the corresponding field
def get_dictionary(input_txt):
    lines = []
    dictionary = dict()
    txt_document = open(input_txt, "r").readlines()
    # a list of fields having multiplicity 1...n or 0...n
    multiplicity_to_n_fields = ['Framework', 'Keyword', 'Reference link', 'Example']
    # a list of fields that have interconnected values.
    # for example, < Input data used - Characteristics of input data - Biases and ethical aspects >
    connected_fields = ['Input data used', 'Characteristics of input data', 'Output data obtained',
                        'Characteristics of output data', 'Biases and ethical aspects']
    fields = multiplicity_to_n_fields + connected_fields
    # building a list where each element is a line of Markdown text (with the necessary adjustments)
    for i in txt_document:
        if i != "\n":
            s = i.strip("\n")
            s = s.strip(" ")
            s = s.replace("'", "")
            lines.append(s)
    for line in lines:
        # checks if the line starts with '###' -> in this case it is the title of the field
        if line.startswith("### "):
            dictionary[line.replace('### ', '')] = []
        else:
            # in this case, the line is the value of the field
            # getting the last key entered
            last_key = list(dictionary.keys())[-1]
            # getting the value of the last key entered
            values = dictionary.get(last_key)
            # removing the values of the last key entered
            dictionary.pop(last_key)
            # there is no value for this field, so it can be skipped because the title has already been removed
            if line == '_No response_':
                continue
            if last_key in fields:
                # the field is included in the list of 'particular' ones (interconnected or with n multiplicity)
                if last_key in connected_fields:
                    # in this case, there is a substring '0-9. ' and will be removed
                    pattern = r'^\d+\. '
                    line = re.sub(pattern, '', line)
                    values.append(line)
                    # key-value pair is added to the dictionary
                    dictionary[last_key] = values
                else:
                    values = line.strip(" ").split(", ")
                    # key-value pair is added to the dictionary
                    dictionary[last_key] = values
            else:
                # key-value pair is added to the dictionary
                dictionary[last_key] = line
    # This field is not mandatory but belongs to the list of interconnected fields and should be handled,
    # like it is always filled in, using an empty array when values have not been entered.
    if 'Biases and ethical aspects' not in dictionary.keys():
        input_len = len(dictionary.get('Input data used'))
        bea = []
        for i in range(input_len):
            bea.append('')
        dictionary['Biases and ethical aspects'] = bea
    return dictionary


# dictionary print function -> used for debugging
def print_dict(dictionary):
    for i in dictionary.keys():
        print(i + ': ' + dictionary.get(i).__str__())
