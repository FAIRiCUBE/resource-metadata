from dictionaries import dictionary_no_ML, dictionary_General
from builder import common_blocks
import json
import config


# This function builds the 'assets' section of the STAC file for no-ML resources
def build_assets(input_array, characteristics_input_array, output_data, characteristics_output, biases):
    assets = {}
    # INPUT DATA
    for i in range(len(input_array)):
        b = biases[i]
        if len(b) == 2:
            b = 'No biases and ethical aspects'
        if len(input_array) == 1:
            name = 'input-data-used'
        else:
            name = 'input-data-used-' + str(i + 1)
        tmp = {
            "href": input_array[i],
            "type": "application/json",
            "title": "Input data used",
            "description": characteristics_input_array[i],
            'biases-and-ethical-aspects': b,
            "roles": [
                "data"
            ],
        }
        assets[name] = tmp
    # OUTPUT DATA
    name = 'output-data-obtained'
    out = {
        "href": output_data[0],
        "type": "application/json",
        "title": "Output data obtained",
        "description": characteristics_output[0],
        "roles": [
            "data"
        ]
    }
    assets[name] = out
    return assets


# This function constructs, taking as input the dictionary containing the field-value pairs,
# the corresponding STAC (JSON) file for no-ML resources.
def build_no_ml_stac(dictionary, path='file/no_ml.json'):
    # the pre-filled dictionaries containing the mapping <name of information requirements -> name in STAC> are used
    general = dictionary_General.build()
    no_ml = dictionary_no_ML.build()
    # start
    json_file = {
        "type": "Feature",
        "stac_version": "1.0.0",
        general.get('ID'): dictionary.get('ID'),
        "collection": config.no_ml_collection,
        "geometry": None,
        "properties": {
            general.get('Name of resource'): dictionary.get('Name of resource'),
            general.get('Description'): dictionary.get('Description'),
            general.get('Main category'): dictionary.get('Main category'),
            general.get('Publication date'): dictionary.get('Pubblication date'),
            general.get('Keyword'): dictionary.get('Keyword'),
            general.get('Platform'): dictionary.get('Platform'),
            general.get('Framework'): dictionary.get('Framework'),
            general.get('Algorithm'): dictionary.get('Algorithm'),
            general.get('Conditions for access and use'): dictionary.get('Conditions for access and use').upper(),
            no_ml.get('Processor'): dictionary.get('Processor'),
            no_ml.get('OS'): dictionary.get('OS'),
            "use-constraints": common_blocks.build_conditional_properties(dictionary),
        },
        "links": common_blocks.build_link(dictionary.get('Reference link'), dictionary.get('Example'), ml=False),
        "assets": build_assets(dictionary.get('Input data used'), dictionary.get('Characteristics of input data'),
                               dictionary.get('Output data obtained'),
                               dictionary.get('Characteristics of output data'),
                               dictionary.get('Biases and ethical aspects'))

    }
    # file saving
    with open(path, "w+") as outfile:
        json.dump(json_file, outfile, indent=4)
    outfile.close()
