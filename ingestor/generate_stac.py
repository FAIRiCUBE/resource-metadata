import os
import pystac


# update catalogs

directories = [
    os.path.join('stac', f) for f in os.listdir(
        os.path.join('stac')) if os.path.isdir(os.path.join('stac', f))]

for dir in directories:
    items = [
        f for f in os.listdir(dir) if not f.endswith(
            'catalog.json') and f.endswith('.json')]
    catalog = pystac.Catalog.from_file(os.path.join(dir, 'catalog.json'))
    for item in items:
        stac_item = pystac.Item.from_file(os.path.join(dir, item))
        catalog.add_item(stac_item)
    catalog.normalize_and_save(
        root_href=os.path.join(dir, 'stac_dist'),
        catalog_type=pystac.CatalogType.SELF_CONTAINED
    )
