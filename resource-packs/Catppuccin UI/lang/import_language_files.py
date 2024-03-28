import os
import shutil
import json



script_directory = os.path.dirname(os.path.abspath(__file__))
index_files_folder = os.path.join(script_directory, "indexes")

versions = []
versions_done = []

# Instructions on how to add an index file. Used if no index file is found for the given version.
index_file_instructions = "\nYou can add an index file by following these steps:\n1. Launch Minecraft with the version of which index file you need.\n2. After Minecraft has launched you should find the index file in the following locations depending on which laucher you use:\nMinecraft Launcher: .minecraft/assets/indexes/version.json\nPrism Launcher: PrismLauncher/assets/indexes/version.json\n3. Copy the index file to lang/indexes folder.\n4. Rename the index file to match the game version you launched the game.\n5. Done!"
# Instructions on how to add object folders. Used if object folders are not found for the given version.
object_folders_instructions = "\nYou can add the object folders by following these steps:\n1. Launch Minecraft with the version of which object folders you need.\n2. After Minecraft has launched you should find the object folders in the following locations depending on which launcher you use:\nMinecraft Launcher: .minecraft/assets/objects/\nPrism Launcher: PrismLauncher/assets/objects\n3. Create a new folder inside lang folder called 'objects' and then create second one inside the 'objects' folder and name it after the index file name, for example '1.19.3'.\n4. Copy everything from .minecraft/assets/objects folder to the folder you just created.\n5. Done!"

while True:
    print("-----------------------------------------------------------------------------------------------------------------------\nEnter the Minecraft version which language files you want to generate. Use 'all' for every version that has index file.")
    user_input = input()
    if len(user_input) == 0:
        continue
    
    # Lists all index files in the index files folder.
    index_files = os.listdir(index_files_folder)
    # This just copies the names of index files from the index files folder to a list.
    all_versions = [os.path.splitext(file)[0] for file in index_files if file.endswith(".json")]
    copy_of_all_versions = all_versions.copy()
    
    index_file = os.path.join(index_files_folder, f"{user_input}.json")
    objects_folder = os.path.join(script_directory, "objects", user_input)
    
    # Check that the user input is a valid version that has an index file and object folders. Otherwise, send instructions on how to add those.
    if user_input in all_versions or user_input == 'all':
        if user_input == 'all':
            i = int()
            for version in copy_of_all_versions:
                obj_folder = os.path.join(script_directory, "objects", version)
                if not os.path.isdir(obj_folder) or not any(os.scandir(obj_folder)):
                    i = i + 1
                    all_versions.remove(version)
                    print(f"Object folders for version {version} are missing!")
                if len(all_versions) != 0:
                    if version == copy_of_all_versions[-1] and i != 0:
                        print(object_folders_instructions)
                else:
                    print(object_folders_instructions)
            if len(all_versions) != 0:
                versions = all_versions
                break
        else:
            if os.path.isdir(objects_folder) and any(os.scandir(objects_folder)):
                versions = [user_input]
                break
            else:
                print(f"Object folders for version {user_input} are missing!")
                print(object_folders_instructions)
    else:
        if os.path.isdir(objects_folder) and any(os.scandir(objects_folder)):
            print(f"Index file for version {user_input} is missing!")
            print(index_file_instructions)
        else:
            print(f"Index file and object folders for version {user_input} are missing!")
            print(index_file_instructions)
            print(object_folders_instructions)

for version in versions:
    index_file = os.path.join(index_files_folder, f"{version}.json")
    objects_folder = os.path.join(script_directory, "objects", version)
    output_folder = os.path.join(script_directory, "output", version, "minecraft")
    # Create output folder.
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    # Open the index file and load the collection of files inside the index file.
    with open(index_file, "r") as file:
        files = json.loads(file.read())

    # Iterate over all the files in the files collection.
    for file, file_properties in files["objects"].items():
        # Check if the file is a language file.
        if file.startswith("minecraft/lang/"):
            # Get the hash from the file properties.
            file_hash = file_properties["hash"]
            # Get the first two characters of the hash, because those are used in the folder name which has the language file inside.
            folder_name = file_hash[:2]
            # Construct the source folder path.
            source_file_path = os.path.join(objects_folder, folder_name, file_hash)
            # Get the language code from the file path.
            language_code = file.split("/")[-1].split(".")[0]
            # Get the file extension. This is needed because of 1.13 version of Minecraft changed the file extension of language files. Before 1.13 it was '.lang' and after '.json'.
            _, file_extension = os.path.splitext(file)
            # Construct the target file path and rename the file correctly depending on the language and Minecraft version.
            target_file_path = os.path.join(f"{output_folder}", f"{language_code}{file_extension}")
            # If the output folder doesn't exist create it.
            if not os.path.exists(output_folder):
                os.mkdir(output_folder)
            # Copy the file to the target folder if the file exists.
            if os.path.exists(source_file_path):
                shutil.copy2(source_file_path, target_file_path)
    versions_done.append(version)
    # Remove the objects folder for the Minecraft version that already has language files generated. These files can be big. After this, it's no longer needed.
    shutil.rmtree(objects_folder)

if len(versions_done) == 1:
    print(f"\nCreated language files for version {versions_done[0]}!\n")
    print(f"Almost done, now you'll have to add the English (US) language file manually!\nYou can find the language file inside the Minecraft jar file.\nExact location: .minecraft/versions/{versions_done[0]}/{versions_done[0]}.jar/assets/minecraft/lang\nJust copy the en_us language file to folder lang/output/{versions_done[0]}/minecraft and then you'll have all language files in the correct location.\n")
else:
    print(f"\nCreated language files for versions " + ", ".join(str(ver) for ver in versions_done) + "!\n")
    print(f"Almost done, now you'll have to add the English (US) language files for all versions manually!\nYou can find the language file for each version inside the Minecraft jar file.\nExact location: .minecraft/versions/(version, for example '1.19.3')/1.19.3.jar/assets/minecraft/lang\nJust copy the en_us language file to folder lang/output/1.19.3/minecraft and then you'll have all language files in the correct location.\n")
print("Everything is done if you already added the English (US) language file!")
input()