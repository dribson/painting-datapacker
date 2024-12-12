# painting-datapacker
Create a Minecraft Datapack for custom paintings 

## Setup
Open the *config.json* file in your preferred text editor, and update the following variables

*root_loc*: Set to the exact file directory that this script is currently located.	
	
*lang_author*: The name to appear as the creator of the resource pack.
	
*resource_ver*: The resource pack format number.
	
*data_ver*: The data pack format number
	
Create folders within `\Ready`. The name of the folder must be the **WIDTH**x**HEIGHT** of the painting

For example, the folder `1x2` will create paintings that are **1** block wide and **2** blocks tall
	
Within the subfolders of `\Ready`, place your desired paintings in .PNG format. 

The names of the paintings does not matter - two different paintings in different folders can have the same name
	
The dimensions of the paintings are not critical, and do not have to be 16 pixels per block
	
A 1x1 painting can be 1000x1000 pixels, for example, and will appear as such when loaded in the game
		
If the painting's dimensions do not match the expected dimension based on the folder name, the painting with appear stretched in game in order to fit the expected size
		
You may reference the existing example painting in `\Ready\16x9`


## Running
Open command prompt and PowerShell within the folder

From the folder, you can hold shift and right click, then select Open PowerShell Window Here
	
With python installed, run the script with the following command

> python .\datapacker.py

The script will find all folders within `\Ready`

For each folder found, it will create the appropriate destination folder and lang folder for the Resource Pack, if they do not exist
	
The script will then get each picture within the folder
	
For each picture found, it will check if it exists within the Resource Pack directory
		
If it does not exist, the picture will be copied to the Resource Pack
			
The script will create lang data for the Resource Pack, as well as writing Variant information for the painting in the Data Pack folder
			
Once all paintings have been finished for a folder, the script writes the lang data for the Resource Pack folder
		
Once all folders have been processed, the script will write the Placeable information for the paintings for the Data Pack folder
	
Once all paintings have been processed, the script checks the Resource Pack and Data Pack folders for *pack.mcmeta* and *pack.png* files

If a pack.mcmeta file is not found, one is created using the *resource_ver* and *data_ver* variables in the config file.
	
**NOTE**: The script will **_not_** update an existing resource or data pack if the provided resource_ver or data_ver variables are newer than the version in the pack.mcmeta file.
		
If a *pack.png* file is not found, a sample image is created. This image is a 1x1 black pixel.
	
When running, the script will output almost every step, so if anything appears missing in the final output, you can check the script output to see if there were any errors for a specific file

## Installing data pack and resource pack
When the script has finished running, there will be 2 new folders: `Painting_Datapack` and `Painting_Resourcepack`

`Painting_Resourcepack` can be copied into your Resource Pack folder like a normal resource pack
	
`Painting_Datapack` can be copied into the Data Pack folder of your world like a normal data pack
	
You can rename the `Painting_Resourcepack` and `Painting_Datapack` after they have been created. Running the script while the pack is there will overwrite all files within the `\assets` subfolders of both folders

You can update the _pack.png_ picture and the _pack.mcmeta_ files within both folders.

*pack.png* can be updated within `Painting_Resourcepack` so it can be easily identified in game
	
*pack.mcmeta* can be updated in both folders
	
*description* can be updated to give a better idea of what's in the pack
		
*pack_format* must be updated to match the version of Minecraft you are playing, and must be updated when the pack version is updated. See [The Minecraft Wiki Page](https://minecraft.wiki/w/Pack_format#List_of_resource_pack_formats) on pack formats to get the pack format for your target version of Minecraft

## Troubleshooting
i dunno i did this for myself and it works for what i need it to do