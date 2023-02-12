import os
import sys
import shutil
import json
from PIL import Image
import time



# Start to count the time it takes to run this script.
starting_time = time.time()

flavors = ["Mocha", "Macchiato", "Frappe", "Latte"]
accent_colors = ["Lavender", "Blue", "Sapphire", "Sky", "Teal", "Green", "Yellow", "Peach", "Maroon", "Red", "Mauve", "Pink", "Flamingo", "Rosewater"]

script_directory = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(script_directory, "output")
template = ''
user_input = ''

while True:
    print("-----------------------------------------------------------------------\nEnter which template version to use. Use names of the template folders.")
    user_input = input()
    if len(user_input) == 0:
        continue
    
    templates_folder = os.path.join(script_directory, "template")
    template_folder = os.path.join(templates_folder, user_input)
    if os.path.isdir(template_folder) and any(os.scandir(template_folder)):
        template = template_folder
        output_folder = os.path.join(output_folder, user_input)
        break
    elif os.path.isdir(templates_folder) and any(os.scandir(templates_folder)):
        templates = os.listdir(templates_folder)
        print(f"No template folder found for '{user_input}'!\nTry to use one of these:\n" + "\n".join(str(template) for template in templates))
    else:
        print("No templates folder found.")

temporary_files_dir = os.path.join(script_directory, "temp", user_input)

# Load template settings.
template_settings_file = os.path.join(template, "template_settings.json")
ignored_files = []

if os.path.isfile(template_settings_file):
    with open(template_settings_file, "r") as settings_file:
        try:
            template_settings = json.load(settings_file)
        except json.decoder.JSONDecodeError as e:
            print("ERROR: Unable to load the template settings file. Reason: ", e)
        template_version = template_settings["version"]
        ignored_files = template_settings["ignored_files"]

# Delete the temporary files folder if it exists. This is here just in case something goes wrong temporary files folder will always be deleted before new files are started to get created.
if os.path.isdir(temporary_files_dir):
    shutil.rmtree(temporary_files_dir)

# Create temporary files folder.
if not os.path.isdir(temporary_files_dir):
    os.mkdir(temporary_files_dir)

# Start to generate different flavors and accent colors from the template.
for flavor in flavors:
    print(f"\nStarting to create flavor {flavor} from template {user_input}!\n")
    
    # Creating a temporary template for each flavor which is used later on just to change the accent colors.
    print(f"Starting to create a temporary template for {flavor}!\n")
    temporary_template_folder = os.path.join(temporary_files_dir, f"{flavor}")
    shutil.copytree(template_folder, temporary_template_folder)
    
    # Checking if the template language file exists.
    template_lang_folder = os.path.join(template_folder, "assets", "minecraft", "lang")
    if os.path.isdir(template_lang_folder) and any(os.scandir(template_lang_folder)):
        if os.path.isfile(os.path.join(template_lang_folder, "template.json")):
            template_lang_file = os.path.join(template_lang_folder, "template.json")
        elif os.path.isfile(os.path.join(template_lang_folder, "template.lang")):
            template_lang_file = os.path.join(template_lang_folder, "template.lang")
        else:
            print(f"ERROR: No template language file found for template {user_input}.\nYou'll have to add one with the name 'template'.")
            input()
            sys.exit()
    
    # Checking if language files exist for the latest version that the current template supports.
    u_input = user_input
    parts = u_input.split()
    versions = parts[-1].strip()
    if '-' in versions:
        oldest_version, new_version = map(str, versions.split('-', 1))
        lang_version = new_version
    else:
        lang_version = versions
    language_files_folder = os.path.join(script_directory, "lang", "output", f"{lang_version}")
    mc_language_files_folder = os.path.join(language_files_folder, "minecraft")
    
    if os.path.isdir(mc_language_files_folder) and any(os.scandir(mc_language_files_folder)):
        
        # Try to load template language file in assets/minecraft/lang.
        with open(template_lang_file, "r") as template_file:
            if template_lang_file.endswith(".json"):
                try:
                    template = json.load(template_file)
                except json.decoder.JSONDecodeError as e:
                    print("ERROR: Unable to load the template language file. Reason: ", e)
                    input()
                    sys.exit()
            
            elif template_lang_file.endswith(".lang"):
                template_language_dict = {}
                for line in template_file:
                    if "=" in line:
                        key, value = line.strip().split("=", 1)
                        template_language_dict[key] = value
                template = template_language_dict
    else:
        print(f"Language files not found for version {lang_version}!\nYou can add language files by executing the 'import_language_files.py' script in the 'lang' folder.")
        input()
        sys.exit()

    # Set correct color values depending on flavor.
    if (flavor=="Mocha"):
        crust = (17, 17, 27)
        mantle = (24, 24, 37)
        base = (30, 30, 46)
        surface0 = (49, 50, 68)
        surface1 = (69, 71, 90)
        surface2 = (88, 91, 112)
        overlay0 = (108, 112, 134)
        overlay1 = (127, 132, 156)
        overlay2 = (147, 153, 178)
        text = (205, 214, 244)
        
        lavender = (180, 190, 254)
        blue = (137, 180, 250)
        sapphire = (116, 199, 236)
        sky = (137, 220, 235)
        teal = (148, 226, 213)
        green = (166, 227, 161)
        yellow = (249, 226, 175)
        peach = (250, 179, 135)
        maroon = (235, 160, 172)
        red = (243, 139, 168)
        red2 = (181, 103, 125)
        mauve = (203, 166, 247)
        pink = (245, 194, 231)
        flamingo = (242, 205, 205)
        rosewater = (245, 224, 220)
        
        # Minecraft color codes.
        text_color = "§f"
        green_text_color = "§a"
        yellow_text_color = "§e"
        purple_text_color = "§d"
    
    elif (flavor=="Macchiato"):
        crust = (24, 25, 38)
        mantle = (30, 32, 48)
        base = (36, 39, 58)
        surface0 = (54, 58, 79)
        surface1 = (73, 77, 100)
        surface2 = (91, 96, 120)
        overlay0 = (110, 115, 141)
        overlay1 = (128, 135, 162)
        overlay2 = (147, 154, 183)
        text = (202, 211, 245)
        
        lavender = (183, 189, 248)
        blue = (138, 173, 244)
        sapphire = (125, 196, 228)
        sky = (145, 215, 227)
        teal = (139, 213, 202)
        green = (166, 218, 149)
        yellow = (238, 212, 159)
        peach = (245, 169, 127)
        maroon = (238, 153, 160)
        red = (237, 135, 150)
        red2 = (176, 100, 112)
        mauve = (198, 160, 246)
        pink = (245, 189, 230)
        flamingo = (240, 198, 198)
        rosewater = (244, 219, 214)
        
        # Minecraft color codes.
        text_color = "§f"
        green_text_color = "§a"
        yellow_text_color = "§e"
        purple_text_color = "§d"
    
    elif (flavor=="Frappe"):
        crust = (35, 38, 52)
        mantle = (41, 44, 60)
        base = (48, 52, 70)
        surface0 = (65, 69, 89)
        surface1 = (81, 87, 109)
        surface2 = (98, 104, 128)
        overlay0 = (115, 121, 148)
        overlay1 = (131, 139, 167)
        overlay2 = (148, 156, 187)
        text = (198, 208, 245)
        
        lavender = (186, 187, 241)
        blue = (140, 170, 238)
        sapphire = (133, 193, 220)
        sky = (153, 209, 219)
        teal = (129, 200, 190)
        green = (166, 209, 137)
        yellow = (229, 200, 144)
        peach = (239, 159, 118)
        maroon = (234, 153, 156)
        red = (231, 130, 132)
        red2 = (172, 97, 98)
        mauve = (202, 158, 230)
        pink = (244, 184, 228)
        flamingo = (238, 190, 190)
        rosewater = (242, 213, 207)
        
        # Minecraft color codes.
        text_color = "§f"
        green_text_color = "§a"
        yellow_text_color = "§e"
        purple_text_color = "§d"

    elif (flavor=="Latte"):
        crust = (220, 224, 232)
        mantle = (230, 233, 239)
        base = (239, 241, 245)
        surface0 = (204, 208, 218)
        surface1 = (188, 192, 204)
        surface2 = (172, 176, 190)
        overlay0 = (156, 160, 176)
        overlay1 = (140, 143, 161)
        overlay2 = (124, 127, 147)
        text = (76, 79, 105)
        
        lavender = (114, 135, 253)
        blue = (30, 102, 245)
        sapphire = (32, 159, 181)
        sky = (4, 165, 229)
        teal = (23, 146, 153)
        green = (64, 160, 43)
        yellow = (223, 142, 29)
        peach = (254, 100, 11)
        maroon = (230, 69, 83)
        red = (210, 15, 57)
        red2 = (156, 11, 42)
        mauve = (136, 57, 239)
        pink = (234, 118, 203)
        flamingo = (221, 120, 120)
        rosewater = (220, 138, 120)
        
        # Minecraft color codes.
        text_color = "§7"
        green_text_color = "§2"
        yellow_text_color = "§6"
        purple_text_color = "§5"
    
    # Create a temporary template for each flavor which is used later on just to change the accent colors.
    for dirpath, dirnames, filenames in os.walk(temporary_template_folder):
        for filename in filenames:
            
            # Replace the correct colors for each image.
            if filename.endswith('.png'):
                if filename not in ignored_files:
                    image_path = os.path.join(dirpath, filename)
                    with Image.open(image_path) as image:
        
                        color_map = {
                            (17, 17, 27): crust,
                            (24, 24, 37): mantle,
                            (30, 30, 46): base,
                            (49, 50, 68): surface0,
                            (69, 71, 90): surface1,
                            (88, 91, 112): surface2,
                            (108, 112, 134): overlay0,
                            (127, 132, 156): overlay1,
                            (147, 153, 178): overlay2,
                            (205, 214, 244): text,
                            (180, 190, 254): lavender,
                            (137, 180, 250): blue,
                            (116, 199, 236): sapphire,
                            (137, 220, 235): sky,
                            (148, 226, 213): teal,
                            (166, 227, 161): green,
                            (249, 226, 175): yellow,
                            (250, 179, 135): peach,
                            (235, 160, 172): maroon,
                            (243, 139, 168): red,
                            (181, 103, 125): red2,
                            (203, 166, 247): mauve,
                            (245, 194, 231): pink,
                            (242, 205, 205): flamingo,
                            (245, 224, 220): rosewater
                        }
                        
                        image = image.convert("RGBA")
                        
                        width = image.size[0]
                        height = image.size[1]
                        
                        for template_color, new_color in color_map.items():
                            # Process all pixels
                            for x in range(0,width):
                                for y in range(0,height):
                                    r,g,b,a = image.getpixel((x,y))
                                    
                                    if ((r,g,b) == template_color):
                                        image.putpixel((x,y), new_color)
                        image.save(image_path, "PNG")
            
            # Create language files for Minecraft and mods that have language files.
            elif filename == "template.json" or filename == "template.lang":
                if dirpath.endswith("lang"):
                    path_list = dirpath.split(os.sep)
                    mod_name = path_list[-2]
                    mod_language_files_folder = os.path.join(language_files_folder, mod_name)
                    if os.path.isdir(mod_language_files_folder) and any(os.scandir(mod_language_files_folder)):
                        all_language_files = os.listdir(mod_language_files_folder)
                        
                        # Load the template language file.
                        template_language_file = os.path.join(dirpath, filename)
                        with open(template_language_file, "r") as template_file:
                            
                            if template_language_file.endswith(".json"):
                                try:
                                    template = json.load(template_file)
                                except json.decoder.JSONDecodeError as e:
                                    print("ERROR: Unable to load the template language file. Reason: ", e)
                                    input()
                                    sys.exit()
                            
                            elif template_language_file.endswith(".lang"):
                                template_language_dict = {}
                                for line in template_file:
                                    if "=" in line:
                                        key, value = line.strip().split("=", 1)
                                        template_language_dict[key] = value
                                template = template_language_dict
                        
                        # Create language files for every language available.
                        print(f"Template language file found for {mod_name}! Starting to create language files of {mod_name} for flavor {flavor}!\n")
                        # Loop over all available language files.
                        for lang in all_language_files:
                            lang_dict = {}
                            # Load each language file correctly depending on game version.
                            with open(os.path.join(mod_language_files_folder, lang), "r", encoding="utf-8") as lang_file:
                                if lang.endswith(".json"):
                                    lang_dict = json.load(lang_file)
                                elif lang.endswith(".lang"):
                                    language_dict = {}
                                    for line in lang_file:
                                        if "=" in line:
                                            key, value = line.strip().split("=", 1)
                                            language_dict[key] = value
                                    lang_dict = language_dict
                            
                            # Create a copy of the template with correct translations from the original language file.
                            template_copy = template.copy()
                            
                            # If the original language file doesn't have a certain translation it'll be removed from template_copy. Minecraft then just automatically uses en_us translations as a fallback.
                            for key in list(template_copy.keys()):
                                if key not in lang_dict:
                                    del template_copy[key]
                            
                            # Set correct colors and translations for each key in template_copy.
                            for key, value in lang_dict.items():
                                if key in template_copy:
                                    template_value = template_copy[key]
                                    if "<value>" in template_value:
                                        if "<text_color>" in template_value:
                                            template_value = template_value.replace("<text_color>", text_color)
                                        elif "<green_text_color>" in template_value:
                                            template_value = template_value.replace("<green_text_color>", green_text_color)
                                        elif "<yellow_text_color>" in template_value:
                                            template_value = template_value.replace("<yellow_text_color>", yellow_text_color)
                                        elif "<purple_text_color>" in template_value:
                                            template_value = template_value.replace("<purple_text_color>", purple_text_color)
                                        template_copy[key] = template_value.replace("<value>", value)
                                    else:
                                        template_copy[key] = ""
                            
                            # Save the updated template_copy as a new file.
                            new_file_name = os.path.join(temporary_files_dir, f"{flavor}", "assets", f"{mod_name}", "lang", lang)
                            shutil.copy2(template_language_file, new_file_name)
                            
                            with open(new_file_name, "w", encoding='utf-8') as new_file:
                                if lang.endswith(".json"):
                                    json.dump(template_copy, new_file, indent=4, ensure_ascii=False)
                                elif lang.endswith(".lang"):
                                    for key, value in template_copy.items():
                                        new_file.write(f"{key}={value}\n")
                        
                        print(f"Language files of {mod_name} ready for the temporary template of flavor {flavor}!\n")
            
            # Delete the "template_settings.json" file as it is not part of the resource pack.
            elif filename == "template_settings.json":
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)
    
    print(f"Temporary template for flavor {flavor} is ready!\n")
    
    # Generate resource packs for each accent color from the temporary template of flavor created earlier.
    for accent_color in accent_colors:
        print(f"Starting to create flavor {flavor} with accent color {accent_color}!")
        
        version_folder = os.path.join(output_folder, f"Catppuccin {flavor} {accent_color}")
        
        # Set correct color value for accent color.
        if (accent_color == "Lavender"):
            accent_color = lavender
        elif (accent_color == "Blue"):
            accent_color = blue
        elif (accent_color == "Sapphire"):
            accent_color = sapphire
        elif (accent_color == "Sky"):
            accent_color = sky
        elif (accent_color == "Teal"):
            accent_color = teal
        elif (accent_color == "Green"):
            accent_color = green
        elif (accent_color == "Yellow"):
            accent_color = yellow
        elif (accent_color == "Peach"):
            accent_color = peach
        elif (accent_color == "Maroon"):
            accent_color = maroon
        elif (accent_color == "Red"):
            accent_color = red
        elif (accent_color == "Mauve"):
            accent_color = mauve
        elif (accent_color == "Pink"):
            accent_color = pink
        elif (accent_color == "Flamingo"):
            accent_color = flamingo
        elif (accent_color == "Rosewater"):
            accent_color = rosewater
        
        color_map = {(255, 0, 0): accent_color}
        
        # Delete version_folder if it exists so a new one can be created.
        if os.path.exists(version_folder):
            shutil.rmtree(version_folder)
        
        # Copy the temporary template to the final location and then update the accent color for each texture.
        shutil.copytree(temporary_template_folder, version_folder)
        for dirpath, dirnames, filenames in os.walk(version_folder):
            for filename in filenames:
                
                # Update accent color for all textures.
                if filename.endswith('.png'):
                    if filename not in ignored_files:
                        image_path = os.path.join(dirpath, filename)
                        with Image.open(image_path) as image:
                            
                            image = image.convert("RGBA")
                            
                            width = image.size[0]
                            height = image.size[1]
                            
                            for template_color, new_color in color_map.items():
                                # Process all pixels
                                for x in range(0,width):
                                    for y in range(0,height):
                                        r,g,b,a = image.getpixel((x,y))
                                        
                                        if ((r,g,b) == template_color):
                                            image.putpixel((x,y), new_color)
                            image.save(image_path, "PNG")
                
                # Update pack description.
                elif filename == "pack.mcmeta":
                    file_path = os.path.join(dirpath, filename)
                    with open(file_path, "r") as packmcmeta:
                        mcmeta = json.load(packmcmeta)
                    
                    mcmeta["pack"]["description"] = mcmeta["pack"]["description"].replace("<pack_version>", template_version).replace("<mc_version>", versions)
                    
                    with open(file_path, "w") as packmcmeta:
                        json.dump(mcmeta, packmcmeta, indent=4)
        
        shutil.make_archive(version_folder, "zip", version_folder)
        shutil.rmtree(version_folder)
    print(f"\nFlavor {flavor} is ready for every accent color!")

# Delete the temporary files folder.
if os.path.isdir(temporary_files_dir):
    shutil.rmtree(temporary_files_dir)

# Calculate the time it took to run this script.
ending_time = time.time()
total_time = ending_time - starting_time
min, sec = divmod(total_time, 60)

print(f"\nEverything done, took {int(min)} minutes and {int(sec)} seconds. You can close this window now!")
input()
