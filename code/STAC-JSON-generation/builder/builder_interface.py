import builder.ml_resources
import builder.no_ml_resources
import builder.common_blocks
import config


# This function is the bridge between the ML-resource STAC-builder and the no-ML resource STAC-builder.
# It selects which one to call based on the value of the Main category.
def build_stac_file(dictionary, path, title):
    category = dictionary.get('Main category')
    title = title+'.json'
    if category == 'Deep Learning' or category == 'Machine Learning':
        builder.ml_resources.build_ml_stac(dictionary, path=path)
        builder.common_blocks.update_collection(config.stac_files_folder + config.ml_collection + '.json', title)
        return config.stac_files_folder + config.ml_collection + '.json'
    else:
        builder.no_ml_resources.build_no_ml_stac(dictionary, path=path)
        builder.common_blocks.update_collection(config.stac_files_folder + config.no_ml_collection + '.json', title)
        return config.stac_files_folder + config.no_ml_collection + '.json'
