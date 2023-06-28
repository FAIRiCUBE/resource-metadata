import config


# There are two functions in this file that have the same implementation for ML resources and for no-ML resources

# This function builds, taking as input the array of the Reference link field and that of the Example field,
# the 'links' section of the STAC file.
def build_link(reference_link_array, example_array, ml=True):
    collection = config.ml_collection
    if not ml:
        collection = config.no_ml_collection
    # the fields are not mandatory
    if reference_link_array is None:
        reference_link_array = []
    if example_array is None:
        example_array = []
    link = []
    root = {
        "rel": "root",
        "href": "./index.json",
        "type": "application/json",
        "title": "Root Catalog"
    }
    parent = {
        "rel": "parent",
        "href": "./" + collection + ".json",
        "type": "application/json",
        "title": collection
    }
    collection = {
        "rel": "collection",
        "href": "./collection.json",
        "type": "application/json"
    }
    link.append(root)
    link.append(parent)
    link.append(collection)
    # Reference link appending
    for i in range(len(reference_link_array)):
        if len(reference_link_array) == 1:
            name = 'Reference link'
        else:
            name = 'Reference link-' + str(i + 1)
        d = {
            "href": reference_link_array[i],
            "rel": "about",
            "type": "text/html",
            "title": name
        }
        link.append(d)
    # Example appending
    for i in range(len(example_array)):
        if len(reference_link_array) == 1:
            name = 'Example'
        else:
            name = 'Example-' + str(i + 1)
        d = {
            "href": example_array[i],
            "rel": "about",
            "type": "text/html",
            "title": name
        }
        link.append(d)
    return link


# This function builds the part of the properties that contains the non-mandatory fields
def build_conditional_properties(dictionary):
    use_constraints = dictionary.get('UseConstraints')
    if use_constraints is None:
        return 'no Constraint of Use'
    return use_constraints
