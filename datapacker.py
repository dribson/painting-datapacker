import json
import os
import shutil
import random
from PIL import Image

def query_dimensions(config):
    dimension_list = os.listdir(config['paintings_source_loc'])
    create_resourcepack(dimension_list, config)
    
def create_mcmeta(config):
    pack_data = { "pack":{ "pack_format":"{}".format(config['resource_ver']), "description":"{} Custom Paintings".format(config['lang_author'])}}
    res_mcmeta = os.path.join(config['resource_root'], 'pack.mcmeta')
    with open(res_mcmeta, 'w') as file:
        json.dump(pack_data, file, indent=4)
    pack_data = { "pack":{ "pack_format":"{}".format(config['data_ver']), "description":"{} Custom Paintings".format(config['lang_author'])}}
    res_mcmeta = os.path.join(config['data_root'], 'pack.mcmeta')
    with open(res_mcmeta, 'w') as file:
        json.dump(pack_data, file, indent=4)
    
    def_pack = Image.new('RGB', (1,1))    
    res_pack = os.path.join(config['resource_root'], 'pack.png')
    if not os.path.exists(res_pack) :
        print('pack.png does not exist for Resource Pack. Creating a dummy file; replace pack.png with your own image')
        def_pack.save(res_pack, "PNG")
    res_pack = os.path.join(config['data_root'], 'pack.png')
    if not os.path.exists(res_pack) :
        print('pack.png does not exist for Data Pack. Creating a dummy file; replace pack.png with your own image')
        def_pack.save(res_pack, "PNG")

def create_resourcepack(dimension_list, config):
    print('Creating Resource Pack...')  
    pleaceable_list = []
    
    print('Iterating Source Folders...')
    
    for folder in dimension_list:
        print(f'Creating Target Directories for {folder} If Non-Existant...')
        texture_folder = config['textures_loc'].format(folder)
        lang_folder = config['json_lang_loc'].format(folder)
        
        if not os.path.exists(texture_folder):
            print(f'Target Directory {folder} Not Found, Creating...')
            os.makedirs(texture_folder)
        if not os.path.exists(lang_folder):
            print(f'Target Lang Directory {folder} Not Found, Creating...')
            os.makedirs(lang_folder)
            
        print(f'Initiailizing Lang JSON For {folder}...')
        lang_json = {}
        
        print(f'Moving Source Paintings To Target Directory {folder}...')
        for item in os.listdir(os.path.join(config['paintings_source_loc'], folder)):
            item_full_loc = os.path.join(config['paintings_source_loc'], folder, item)
            
            if not os.path.exists(os.path.join(texture_folder, item)):
                print(f'Destination Painting {item} Does Not Exist in {folder}, Creating...')
                new_painting = shutil.copy(item_full_loc, texture_folder)
                print(os.path.join(texture_folder, item))
                
            print(f'Formatting Lang JSON For {item}...')
            painting_name = item[:-4]
            lang_json[config['lang_author_format'].format(folder, painting_name)] = config['lang_author']
            lang_json[config['lang_title_format'].format(folder, painting_name)] = painting_name
            
            print(f'Formatting Placeable JSON For {painting_name}...')
            pleaceable_list.append(config['placeable_format'].format(folder, painting_name))
            
            print(f'Formatting Variant Definition JSON for {folder}:{painting_name}...')
            dimension = folder.index('x')
            x_dimension = int(folder[0:dimension])
            y_dimension = int(folder[dimension+1:])
            
            variant_location = config['json_variant_loc'].format(folder)
            if not os.path.exists(variant_location):
                print(f'Painting Variant Directory for {painting_name} Not Found, Creating...')
                os.makedirs(variant_location)
            
            painting_variant_json = {}
            painting_variant_json["asset_id"] = f"{folder}:{painting_name}"
            painting_variant_json["width"] = x_dimension
            painting_variant_json["height"] = y_dimension
            
            print(f'Writing Painting Variant JSON File For {folder}:{painting_name}')
            painting_variant_title = config['variant_title'].format(painting_name)
            variant_json_loc = os.path.join(variant_location, painting_variant_title)
            with open(variant_json_loc,  'w') as file:
                json.dump(painting_variant_json, file, indent=4)
            
        print(f'Writing Lang JSON file For {folder}...')
        lang_file_loc = os.path.join(lang_folder, config['lang_title'])
        with open(lang_file_loc,  'w') as file:
            json.dump(lang_json, file, indent=4)
            
    print(f'Writing Placeable JSON...')
    final_pleaceable_json = {"values": pleaceable_list}
    placeable_json_file = os.path.join(config['json_placeable_loc'], config['json_placeable_title'])
    if not os.path.exists(config['json_placeable_loc']):
        os.makedirs(config['json_placeable_loc'])
    with open(placeable_json_file, 'w') as file:
        json.dump(final_pleaceable_json, file, indent=4)
        

def create_datapack(config):
    query_dimensions(config)
    create_mcmeta(config)

if __name__ == "__main__":
    with open('config.json', 'r') as config_file:
        data = json.load(config_file)
    config = {}
    config['root_loc'] = data['root_loc']
    config['resource_root'] = data['resource_root'].format(config['root_loc'])
    config['resource_ver'] = data['resource_ver']
    config['data_root'] = data['data_root'].format(config['root_loc'])
    config['data_ver'] = data['data_ver']
    config['paintings_source_loc'] = data['paintings_source_loc'].format(config['root_loc'])
    config['textures_loc'] = data['textures_loc'].format(config['resource_root'], '{}')
    config['json_lang_loc'] = data['json_lang_loc'].format(config['resource_root'], '{}')
    config['lang_author'] = data['lang_author']
    config['lang_author_format'] = data['lang_author_format']
    config['lang_title_format'] = data['lang_title_format']
    config['lang_title'] = data['lang_title']
    config['json_placeable_loc'] = data['json_placeable_loc'].format(config['data_root'], '{}')
    config['json_placeable_title'] = data['json_placeable_title']
    config['placeable_format'] = data['placeable_format']
    config['json_variant_loc'] = data['json_variant_loc'].format(config['data_root'], '{}')
    config['variant_title'] = data['variant_title']
    create_datapack(config)