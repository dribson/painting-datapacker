import json
import os
import shutil
import random

# TODO move to a function of its own
# TODO add a single root variable that the location variables append to. means config will be easier to update
with open('config.json', 'r') as config_file:
    data = json.load(config_file)
root_loc = data['root_loc']
paintings_source_loc = data['paintings_source_loc'].format(root_loc)
textures_loc = data['textures_loc'].format(root_loc, '{}')
json_lang_loc = data['json_lang_loc'].format(root_loc, '{}')
lang_author = data['lang_author']
lang_author_format = data['lang_author_format']
lang_title_format = data['lang_title_format']
lang_title = data['lang_title']
json_placeable_loc = data['json_placeable_loc'].format(root_loc, '{}')
json_placeable_title = data['json_placeable_title']
placeable_format = data['placeable_format']
json_variant_loc = data['json_variant_loc'].format(root_loc, '{}')
variant_title = data['variant_title']



def query_dimensions():
    dimension_list = os.listdir(paintings_source_loc)
    create_resourcepack(dimension_list)

def create_json():
    print('lol')
    
def create_lang_json():
    print('lol')

# TODO split appropriate functionality into create_json and create_lang_json functions
def create_resourcepack(dimension_list):
    print('Creating Resource Pack...')  
    pleaceable_list = []
    
    print('Iterating Source Folders...')
    
    for folder in dimension_list:
        print(f'Creating Target Directories for {folder} If Non-Existant...')
        texture_folder = textures_loc.format(folder)
        lang_folder = json_lang_loc.format(folder)
        
        if not os.path.exists(texture_folder):
            print(f'Target Directory {folder} Not Found, Creating...')
            os.makedirs(texture_folder)
        if not os.path.exists(lang_folder):
            print(f'Target Lang Directory {folder} Not Found, Creating...')
            os.makedirs(lang_folder)
            
        print(f'Initiailizing Lang JSON For {folder}...')
        lang_json = {}
        
        print(f'Moving Source Paintings To Target Directory {folder}...')
        for item in os.listdir(os.path.join(paintings_source_loc, folder)):
            item_full_loc = os.path.join(paintings_source_loc, folder, item)
            
            if not os.path.exists(os.path.join(texture_folder, item)):
                print(f'Destination Painting {item} Does Not Exist in {folder}, Creating...')
                new_painting = shutil.copy(item_full_loc, texture_folder)
                print(os.path.join(texture_folder, item))
                
            print(f'Formatting Lang JSON For {item}...')
            painting_name = item[:-4]
            lang_json[lang_author_format.format(folder, painting_name)] = lang_author
            lang_json[lang_title_format.format(folder, painting_name)] = painting_name
            
            print(f'Formatting Placeable JSON For {painting_name}...')
            pleaceable_list.append(placeable_format.format(folder, painting_name))
            
            print(f'Formatting Variant Definition JSON for {folder}:{painting_name}...')
            dimension = folder.index('x')
            x_dimension = int(folder[0:dimension])
            y_dimension = int(folder[dimension+1:])
            
            variant_location = json_variant_loc.format(folder)
            if not os.path.exists(variant_location):
                print(f'Painting Variant Directory for {painting_name} Not Found, Creating...')
                os.makedirs(variant_location)
            
            painting_variant_json = {}
            painting_variant_json["asset_id"] = f"{folder}:{painting_name}"
            painting_variant_json["width"] = x_dimension
            painting_variant_json["height"] = y_dimension
            
            print(f'Writing Painting Variant JSON File For {folder}:{painting_name}')
            painting_variant_title = variant_title.format(painting_name)
            variant_json_loc = os.path.join(variant_location, painting_variant_title)
            with open(variant_json_loc,  'w') as file:
                json.dump(painting_variant_json, file, indent=4)
            
        print(f'Writing Lang JSON file For {folder}...')
        lang_file_loc = os.path.join(lang_folder, lang_title)
        with open(lang_file_loc,  'w') as file:
            json.dump(lang_json, file, indent=4)
            
    print(f'Writing Placeable JSON...')
    final_pleaceable_json = {"values": pleaceable_list}
    placeable_json_file = os.path.join(json_placeable_loc, json_placeable_title)
    with open(placeable_json_file, 'w') as file:
        json.dump(final_pleaceable_json, file, indent=4)
        


def create_datapack():
    query_dimensions()

create_datapack()
