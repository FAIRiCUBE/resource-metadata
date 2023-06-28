import builder.ml_resources
import builder.no_ml_resources


# This function is the bridge between the ML-resource STAC-builder and the no-ML resource STAC-builder.
# It selects which one to call based on the value of the Main category.
def build_stac_file(dictionary, path):
    category = dictionary.get('Main category')
    if category == 'Deep Learning' or category == 'Machine Learning':
        builder.ml_resources.build_ml_stac(dictionary, path=path)
    else:
        builder.no_ml_resources.build_no_ml_stac(dictionary, path=path)
