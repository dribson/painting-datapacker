# painting-datapacker
Create a Minecraft Datapack for custom paintings
Made with python 3.9 but should work with older versions of python.

## Setup
Open the *config.json* file in your preferred text editor, and update the following variables

- *root_loc*: Set to the exact file directory that this script is currently located.	
	
- *lang_author*: The name to appear as the creator of the resource pack.
	
- *resource_ver*: The resource pack format number.
	
- *data_ver*: The data pack format number
	
Create folders within `\Ready`. The name of the folder must be the **WIDTH**x**HEIGHT** of the painting

- For example, the folder `1x2` will create paintings that are **1** block wide and **2** blocks tall
	
Within the subfolders of `\Ready`, place your desired paintings in .PNG format. 

- The names of the paintings does not matter - two different paintings in different folders can have the same name
	
- The dimensions of the paintings are not critical, and do not have to be 16 pixels per block
	
  - A 1x1 painting can be 1000x1000 pixels, for example, and will appear as such when loaded in the game
		
- If the painting's dimensions do not match the expected dimension based on the folder name, the painting with appear stretched in game in order to fit the expected size
		
You may reference the existing example painting in `\Ready\16x9`


## Running
Open command prompt or PowerShell within the folder

- From the folder, you can hold shift and right click, then select Open PowerShell Window Here
	
With python installed, run the script with the following command

> python .\datapacker.py

The script will find all folders within `\Ready`

- For each folder found, it will create the appropriate destination folder and lang folder for the Resource Pack, if they do not exist
	
  - The script will then get each picture within the folder
	
    - For each picture found, it will check if it exists within the Resource Pack directory
		
      - If it does not exist, the picture will be copied to the Resource Pack
			
    - The script will create lang data for the Resource Pack, as well as writing Variant information for the painting in the Data Pack folder
			
  - Once all paintings have been finished for a folder, the script writes the lang data for the Resource Pack folder
		
- Once all folders have been processed, the script will write the Placeable information for the paintings for the Data Pack folder
	
- Once all paintings have been processed, the script checks the Resource Pack and Data Pack folders for *pack.mcmeta* and *pack.png* files

  - If a pack.mcmeta file is not found, one is created using the *resource_ver* and *data_ver* variables in the config file.
	
**NOTE**: The script will **_not_** update an existing resource or data pack if the provided *resource_ver* or *data_ver* variables are newer than the version in the pack.mcmeta file.
		
  - If a *pack.png* file is not found, a sample image is created. This image is a 1x1 black pixel.
	
When running, the script will output almost every step, so if anything appears missing in the final output, you can check the script output to see if there were any errors for a specific file

## Installing data pack and resource pack
When the script has finished running, there will be 2 new folders: `Painting_Datapack` and `Painting_Resourcepack`

- `Painting_Resourcepack` can be copied into your Resource Pack folder like a normal resource pack
	
- `Painting_Datapack` can be copied into the Data Pack folder of your world like a normal data pack
	
You can rename the `Painting_Resourcepack` and `Painting_Datapack` after they have been created. Running the script while the pack is there will overwrite all files within the `\assets` subfolders of both folders

You can update the _pack.png_ picture and the _pack.mcmeta_ files within both folders.

- *pack.png* can be updated within `Painting_Resourcepack` so it can be easily identified in game
	
- *pack.mcmeta* can be updated in both folders
	
  - *description* can be updated to give a better idea of what's in the pack
		
  - *pack_format* must be updated to match the version of Minecraft you are playing, and must be updated when the pack version is updated. See [The Minecraft Wiki Page](https://minecraft.wiki/w/Pack_format#List_of_resource_pack_formats) on pack formats to get the pack format for your target version of Minecraft

## Troubleshooting
**I tried running the script and it didn't work**: There's either an issue with the config file, python isn't installed (or installed properly) on your computer, or ~~it works on my machine~~ there's a technical issue that needs resolution.

**Minecraft failed to load the resource pack**: The resource pack is probably too big, and is likely overloading your video card's VRAM. Remove or downsize some of the larger paintings and try again. With a GTX 1080, I can reach ~750MB of paintings before Minecraft will fail to load the resource pack. Your mileage may vary depending on your specs.

**A painting isn't showing up in game**: The painting's data may be missing from the Resource Pack or Data Pack files. Rerun the script to regenerate those files. If the problem persists, ensure the painting is in the expected location within the `\Ready` folder.

**A painting is showing up as pink and black squares in game**: The painting's data exists, but the painting itself may be missing from the Resource Pack. Locate the expected painting, place it in the desired location within `\Ready`, and rerun the script.

**The painting looks super stretched in game**: The painting's dimensions do not match the folder it is in. Either change the folder the painting is in, or crop the picture so that it matches the expected dimensions

**Minecraft says the resource pack was created for an older/newer version of the game**: Update the pack formats within the pack.mcmeta files to the format expected by your version of Minecraft. I will not be doing ongoing updates to the config file for newer versions of Minecraft (this was written and is configured for 1.21-1.21.1), so you might as well update the pack formats in the config file as well.

**No custom paintings exist**: Ensure that the Data pack was added to your world.

**Can you do animated paintings with this?**: While this tool cannot create animated paintings at the moment, you can create animated paintings. Refer to [The Minecraft Wiki Page](https://minecraft.wiki/w/Resource_pack#Texture_animation) on Texture Animation in Resource Packs

**Can I have multiple packs at the same time**: You should be able to, so long as there is no overlapping paintings with the same name and dimensions (i.e. two different packs cannot both have a 2x2 Tree.png)

**Does this work on servers?**: No idea, I don't play this game with other people. Since this just uses Minecraft's default Resource Packs and Data Pack logic for paintings added in version 1.21, I would assume so.

**Bedrock edition?**: No clue, and I don't care enough to find out.
