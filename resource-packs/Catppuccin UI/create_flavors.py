# -*- coding: utf-8 -*-

# Standard imports
from json import (
    dump as json_dump,
    load as json_load)
from json.decoder import JSONDecodeError
from os import (
    listdir,
    makedirs,
    remove as os_remove,
    rename as os_rename,
    scandir,
    walk as os_walk)
from os.path import (
    exists as os_path_exists,
    isdir,
    isfile)
from pathlib import PurePath
from shutil import (
    copy2 as shutil_copy2,
    copytree,
    make_archive,
    rmtree)
from time import perf_counter as time_perf_counter

# 3rd party imports
from PIL import Image


class CatppuccinColors:
    __slots__ = (
        '__crust',
        '__mantle',
        '__base',
        '__surface0',
        '__surface1',
        '__surface2',
        '__overlay0',
        '__overlay1',
        '__overlay2',
        '__text',
        '__lavender',
        '__blue',
        '__sapphire',
        '__sky',
        '__teal',
        '__green',
        '__yellow',
        '__peach',
        '__maroon',
        '__red',
        '__red2',
        '__mauve',
        '__pink',
        '__flamingo',
        '__rosewater',
        '__text_color',
        '__green_text_color',
        '__yellow_text_color',
        '__purple_text_color')

    def __init__(
            self,
            *,
            crust,
            mantle,
            base,
            surface0,
            surface1,
            surface2,
            overlay0,
            overlay1,
            overlay2,
            text,
            lavender,
            blue,
            sapphire,
            sky,
            teal,
            green,
            yellow,
            peach,
            maroon,
            red,
            red2,
            mauve,
            pink,
            flamingo,
            rosewater,
            text_color,
            green_text_color,
            yellow_text_color,
            purple_text_color):
        self.__crust = crust
        self.__mantle = mantle
        self.__base = base
        self.__surface0 = surface0
        self.__surface1 = surface1
        self.__surface2 = surface2
        self.__overlay0 = overlay0
        self.__overlay1 = overlay1
        self.__overlay2 = overlay2
        self.__text = text

        self.__lavender = lavender
        self.__blue = blue
        self.__sapphire = sapphire
        self.__sky = sky
        self.__teal = teal
        self.__green = green
        self.__yellow = yellow
        self.__peach = peach
        self.__maroon = maroon
        self.__red = red
        self.__red2 = red2
        self.__mauve = mauve
        self.__pink = pink
        self.__flamingo = flamingo
        self.__rosewater = rosewater

        # Minecraft color codes.
        self.__text_color = text_color
        self.__green_text_color = green_text_color
        self.__yellow_text_color = yellow_text_color
        self.__purple_text_color = purple_text_color
        return

    @property
    def crust(self):
        return self.__crust

    @property
    def mantle(self):
        return self.__mantle

    @property
    def base(self):
        return self.__base

    @property
    def surface0(self):
        return self.__surface0

    @property
    def surface1(self):
        return self.__surface1

    @property
    def surface2(self):
        return self.__surface2

    @property
    def overlay0(self):
        return self.__overlay0

    @property
    def overlay1(self):
        return self.__overlay1

    @property
    def overlay2(self):
        return self.__overlay2

    @property
    def text(self):
        return self.__text

    @property
    def lavender(self):
        return self.__lavender

    @property
    def blue(self):
        return self.__blue

    @property
    def sapphire(self):
        return self.__sapphire

    @property
    def sky(self):
        return self.__sky

    @property
    def teal(self):
        return self.__teal

    @property
    def green(self):
        return self.__green

    @property
    def yellow(self):
        return self.__yellow

    @property
    def peach(self):
        return self.__peach

    @property
    def maroon(self):
        return self.__maroon

    @property
    def red(self):
        return self.__red

    @property
    def red2(self):
        return self.__red2

    @property
    def mauve(self):
        return self.__mauve

    @property
    def pink(self):
        return self.__pink

    @property
    def flamingo(self):
        return self.__flamingo

    @property
    def rosewater(self):
        return self.__rosewater

    @property
    def text_color(self):
        return self.__text_color

    @property
    def green_text_color(self):
        return self.__green_text_color

    @property
    def yellow_text_color(self):
        return self.__yellow_text_color

    @property
    def purple_text_color(self):
        return self.__purple_text_color


class CatppuccinMocha(CatppuccinColors):
    def __init__(self):
        super().__init__(
            crust=(17, 17, 27),
            mantle=(24, 24, 37),
            base=(30, 30, 46),
            surface0=(49, 50, 68),
            surface1=(69, 71, 90),
            surface2=(88, 91, 112),
            overlay0=(108, 112, 134),
            overlay1=(127, 132, 156),
            overlay2=(147, 153, 178),
            text=(205, 214, 244),
            lavender=(180, 190, 254),
            blue=(137, 180, 250),
            sapphire=(116, 199, 236),
            sky=(137, 220, 235),
            teal=(148, 226, 213),
            green=(166, 227, 161),
            yellow=(249, 226, 175),
            peach=(250, 179, 135),
            maroon=(235, 160, 172),
            red=(243, 139, 168),
            red2=(181, 103, 125),
            mauve=(203, 166, 247),
            pink=(245, 194, 231),
            flamingo=(242, 205, 205),
            rosewater=(245, 224, 220),
            text_color='§f',
            green_text_color='§a',
            yellow_text_color='§e',
            purple_text_color='§d')
        return


class CatppuccinMacchiato(CatppuccinColors):
    def __init__(self):
        super().__init__(
            crust=(24, 25, 38),
            mantle=(30, 32, 48),
            base=(36, 39, 58),
            surface0=(54, 58, 79),
            surface1=(73, 77, 100),
            surface2=(91, 96, 120),
            overlay0=(110, 115, 141),
            overlay1=(128, 135, 162),
            overlay2=(147, 154, 183),
            text=(202, 211, 245),
            lavender=(183, 189, 248),
            blue=(138, 173, 244),
            sapphire=(125, 196, 228),
            sky=(145, 215, 227),
            teal=(139, 213, 202),
            green=(166, 218, 149),
            yellow=(238, 212, 159),
            peach=(245, 169, 127),
            maroon=(238, 153, 160),
            red=(237, 135, 150),
            red2=(176, 100, 112),
            mauve=(198, 160, 246),
            pink=(245, 189, 230),
            flamingo=(240, 198, 198),
            rosewater=(244, 219, 214),
            text_color='§f',
            green_text_color='§a',
            yellow_text_color='§e',
            purple_text_color='§d')
        return


class CatppuccinFrappe(CatppuccinColors):
    def __init__(self):
        super().__init__(
            crust=(35, 38, 52),
            mantle=(41, 44, 60),
            base=(48, 52, 70),
            surface0=(65, 69, 89),
            surface1=(81, 87, 109),
            surface2=(98, 104, 128),
            overlay0=(115, 121, 148),
            overlay1=(131, 139, 167),
            overlay2=(148, 156, 187),
            text=(198, 208, 245),
            lavender=(186, 187, 241),
            blue=(140, 170, 238),
            sapphire=(133, 193, 220),
            sky=(153, 209, 219),
            teal=(129, 200, 190),
            green=(166, 209, 137),
            yellow=(229, 200, 144),
            peach=(239, 159, 118),
            maroon=(234, 153, 156),
            red=(231, 130, 132),
            red2=(172, 97, 98),
            mauve=(202, 158, 230),
            pink=(244, 184, 228),
            flamingo=(238, 190, 190),
            rosewater=(242, 213, 207),
            text_color='§f',
            green_text_color='§a',
            yellow_text_color='§e',
            purple_text_color='§d')
        return


class CatppuccinLatte(CatppuccinColors):
    def __init__(self):
        super().__init__(
            crust=(220, 224, 232),
            mantle=(230, 233, 239),
            base=(239, 241, 245),
            surface0=(204, 208, 218),
            surface1=(188, 192, 204),
            surface2=(172, 176, 190),
            overlay0=(156, 160, 176),
            overlay1=(140, 143, 161),
            overlay2=(124, 127, 147),
            text=(76, 79, 105),
            lavender=(114, 135, 253),
            blue=(30, 102, 245),
            sapphire=(32, 159, 181),
            sky=(4, 165, 229),
            teal=(23, 146, 153),
            green=(64, 160, 43),
            yellow=(223, 142, 29),
            peach=(254, 100, 11),
            maroon=(230, 69, 83),
            red=(210, 15, 57),
            red2=(156, 11, 42),
            mauve=(136, 57, 239),
            pink=(234, 118, 203),
            flamingo=(221, 120, 120),
            rosewater=(220, 138, 120),
            text_color='§7',
            green_text_color='§2',
            yellow_text_color='§6',
            purple_text_color='§5')
        return


class CatppuccinFlavors:
    mocha = 'Mocha'
    macchiato = 'Macchiato'
    frappe = 'Frappe'
    latte = 'Latte'

    __slots__ = ()

    def __init__(self):
        return

    @staticmethod
    def all():
        return (
            CatppuccinFlavors.mocha,
            CatppuccinFlavors.macchiato,
            CatppuccinFlavors.frappe,
            CatppuccinFlavors.latte)


def get_flavor_colors(flavor):
    if flavor == CatppuccinFlavors.mocha:
        return CatppuccinMocha()
    if flavor == CatppuccinFlavors.macchiato:
        return CatppuccinMacchiato()
    if flavor == CatppuccinFlavors.frappe:
        return CatppuccinFrappe()
    return CatppuccinLatte()


class CatppuccinAccentColors:
    lavender = 'Lavender'
    blue = 'Blue'
    sapphire = 'Sapphire'
    sky = 'Sky'
    teal = 'Teal'
    green = 'Green'
    yellow = 'Yellow'
    peach = 'Peach'
    maroon = 'Maroon'
    red = 'Red'
    mauve = 'Mauve'
    pink = 'Pink'
    flamingo = 'Flamingo'
    rosewater = 'Rosewater'

    __slots__ = ()

    def __init__(self):
        return

    @staticmethod
    def all():
        return (
            CatppuccinAccentColors.lavender,
            CatppuccinAccentColors.blue,
            CatppuccinAccentColors.sapphire,
            CatppuccinAccentColors.sky,
            CatppuccinAccentColors.teal,
            CatppuccinAccentColors.green,
            CatppuccinAccentColors.yellow,
            CatppuccinAccentColors.peach,
            CatppuccinAccentColors.maroon,
            CatppuccinAccentColors.red,
            CatppuccinAccentColors.mauve,
            CatppuccinAccentColors.pink,
            CatppuccinAccentColors.flamingo,
            CatppuccinAccentColors.rosewater)


def main():
    # Start to count the time it takes to run this script.
    starting_time = int(time_perf_counter())
    templates_folder = PurePath('template')

    while True:
        template_version = input(
            '-----------------------------------------------------------------------\n'
            'Enter which template version to use. Use names of the template folders.\n')

        if not template_version:
            continue

        template_folder = PurePath(templates_folder, template_version)

        if isdir(template_folder) and any(scandir(template_folder)):
            output_folder = PurePath('output', template_version)
            break
        elif isdir(templates_folder) and any(scandir(templates_folder)):
            templates = '\n'.join(sorted(listdir(templates_folder)))
            print(
                f'No template folder found for \'{template_version}\'!\n'
                f'Try to use one of these:\n{templates}')
        else:
            print('No templates folder found.')

    temporary_files_dir = PurePath('temp', template_version)

    # Get resource pack version from version file.
    if isfile(PurePath('version.txt')):
        with open(PurePath('version.txt'), 'r') as version_file:
            version = version_file.readline()

    # Delete the temporary files folder if it exists.
    # This is here just in case something goes wrong.
    # Temporary files folder will always be deleted before new files are started to get created.
    if isdir(temporary_files_dir):
        rmtree(temporary_files_dir)

    # Create temporary files folder.
    if not isdir(temporary_files_dir):
        makedirs(temporary_files_dir)

    # Start to generate different flavors and accent colors from the template.
    for flavor in CatppuccinFlavors.all():
        print(f'\nStarting to create flavor {flavor} from template {template_version}!\n')

        # Creating a temporary template for each flavor which is used later on just to change the accent colors.
        print(f'Starting to create a temporary template for {flavor}!\n')
        temporary_template_folder = PurePath(temporary_files_dir, flavor)
        copytree(template_folder, temporary_template_folder)

        # Checking if the template language file exists.
        template_lang_folder = PurePath(template_folder, 'assets', 'minecraft', 'lang')
        if isdir(template_lang_folder) and any(scandir(template_lang_folder)):
            if isfile(PurePath(template_lang_folder, 'template.json')):
                template_lang_file = PurePath(template_lang_folder, 'template.json')
            elif isfile(PurePath(template_lang_folder, 'template.lang')):
                template_lang_file = PurePath(template_lang_folder, 'template.lang')
            else:
                print(
                    f'ERROR: No template language file found for template {template_version}.\n'
                    f'You\'ll have to add one with the name \'template\'.')
                return
        else:
            print(f'ERROR: No template language folder found at path: {template_lang_folder}')
            return

        # Checking if language files exist for the latest version that the current template supports.
        parts = template_version.split()
        versions = parts[-1].strip()
        if '-' in versions:
            oldest_version, latest_version = versions.split('-', 1)
            lang_version = latest_version
        else:
            lang_version = versions
        language_files_folder = PurePath('lang', 'output', lang_version)
        mc_language_files_folder = PurePath(language_files_folder, 'minecraft')

        if isdir(mc_language_files_folder) and any(scandir(mc_language_files_folder)):
            # Try to load template language file in assets/minecraft/lang.
            with open(template_lang_file, 'r') as template_file:
                if template_lang_file.suffix == '.json':
                    try:
                        template = json_load(template_file)
                    except JSONDecodeError as e:
                        print(
                            'ERROR: Unable to load the template language file of minecraft.\n'
                            'Reason: ', e)
                        return

                elif template_lang_file.suffix == '.lang':
                    template_language_dict = {}
                    for line in template_file:
                        if '=' in line:
                            key, value = line.strip().split('=', 1)
                            template_language_dict[key] = value
                    template = template_language_dict
        else:
            print(
                f'Language files not found for version {lang_version}!\n'
                f'You can add language files by executing the '
                f'\'import_language_files.py\' script in the \'lang\' folder.')
            return

        # Get correct color values depending on flavor.
        flavor_colors = get_flavor_colors(flavor)

        # Create a temporary template for each flavor which is used later on just to change the accent colors.
        for dirpath, _, filenames in os_walk(temporary_template_folder):
            for filename in filenames:
                # Replace the correct colors for each image.
                if filename.endswith('.png'):
                    if not filename.startswith('$'):
                        image_path = PurePath(dirpath, filename)
                        with Image.open(str(image_path)) as image:
                            color_map = {
                                (17, 17, 27): flavor_colors.crust,
                                (24, 24, 37): flavor_colors.mantle,
                                (30, 30, 46): flavor_colors.base,
                                (49, 50, 68): flavor_colors.surface0,
                                (69, 71, 90): flavor_colors.surface1,
                                (88, 91, 112): flavor_colors.surface2,
                                (108, 112, 134): flavor_colors.overlay0,
                                (127, 132, 156): flavor_colors.overlay1,
                                (147, 153, 178): flavor_colors.overlay2,
                                (205, 214, 244): flavor_colors.text,
                                (180, 190, 254): flavor_colors.lavender,
                                (137, 180, 250): flavor_colors.blue,
                                (116, 199, 236): flavor_colors.sapphire,
                                (137, 220, 235): flavor_colors.sky,
                                (148, 226, 213): flavor_colors.teal,
                                (166, 227, 161): flavor_colors.green,
                                (249, 226, 175): flavor_colors.yellow,
                                (250, 179, 135): flavor_colors.peach,
                                (235, 160, 172): flavor_colors.maroon,
                                (243, 139, 168): flavor_colors.red,
                                (181, 103, 125): flavor_colors.red2,
                                (203, 166, 247): flavor_colors.mauve,
                                (245, 194, 231): flavor_colors.pink,
                                (242, 205, 205): flavor_colors.flamingo,
                                (245, 224, 220): flavor_colors.rosewater}

                            image = image.convert('RGBA')
                            width, height = image.size

                            for template_color, new_color in color_map.items():
                                # Process all pixels
                                for x in range(0, width):
                                    for y in range(0, height):
                                        r, g, b, a = image.getpixel((x, y))
                                        new_color_with_alpha = new_color + (a,)
                                        if (r, g, b) == template_color:
                                            image.putpixel((x, y), new_color_with_alpha)
                            image.save(str(image_path), 'PNG')

                    # If file has '$current_flavor$' prefix
                    #   remove the prefix so textures inside file will work in the pack.
                    elif filename.startswith(f'${flavor.lower()}$'):
                        os_rename(
                            PurePath(dirpath, filename),
                            PurePath(dirpath, filename.replace(f'${flavor.lower()}$', '')))

                    # Delete file if it doesn't have '$ignore$' or '$current_flavor$' prefixes.
                    elif not filename.startswith('$ignore$'):
                        os_remove(PurePath(dirpath, filename))

                # Create language files for Minecraft and mods that have language files.
                elif filename == 'template.json' or filename == 'template.lang':
                    if dirpath.endswith('lang'):
                        path_list = PurePath(dirpath).parts
                        mod_name = path_list[-2]
                        mod_language_files_folder = PurePath(language_files_folder, mod_name)
                        if isdir(mod_language_files_folder) and any(scandir(mod_language_files_folder)):
                            all_language_files = listdir(mod_language_files_folder)

                            # Load the template language file.
                            template_language_file = PurePath(dirpath, filename)
                            with open(template_language_file, 'r') as template_file:
                                if template_language_file.suffix == '.json':
                                    try:
                                        template = json_load(template_file)
                                    except JSONDecodeError as e:
                                        print(
                                            f'ERROR: Unable to load template language file at path: '
                                            f'{template_language_file}\nReason: ', e)
                                        return
                                elif template_language_file.suffix == '.lang':
                                    template_language_dict = {}
                                    for line in template_file:
                                        if '=' in line:
                                            key, value = line.strip().split('=', 1)
                                            template_language_dict[key] = value
                                    template = template_language_dict

                            # Create language files for every language available.
                            print(
                                f'Template language file found for {mod_name}! '
                                f'Starting to create language files of {mod_name} for flavor {flavor}!\n')
                            # Loop over all available language files.
                            for lang in sorted(all_language_files):
                                lang_dict = {}
                                # Load each language file correctly depending on game version.
                                with open(PurePath(
                                        mod_language_files_folder, lang), 'r', encoding='utf-8') as lang_file:
                                    if lang.endswith('.json'):
                                        try:
                                            lang_dict = json_load(lang_file)
                                        except JSONDecodeError as e:
                                            print(
                                                f'ERROR: Unable to load language file at path: '
                                                f'{lang_file}\nReason: ', e)
                                            return
                                    elif lang.endswith('.lang'):
                                        language_dict = {}
                                        for line in lang_file:
                                            if '=' in line:
                                                key, value = line.strip().split('=', 1)
                                                language_dict[key] = value
                                        lang_dict = language_dict

                                # Create a copy of the template with correct translations
                                #   from the original language file.
                                template_copy = template.copy()

                                # If the original language file doesn't have a certain translation
                                #   it'll be removed from template_copy.
                                #   Minecraft then just automatically uses en_us translations as a fallback.
                                for key in list(template_copy.keys()):
                                    if key not in lang_dict:
                                        del template_copy[key]

                                # Set correct colors and translations for each key in template_copy.
                                for key, value in lang_dict.items():
                                    if key in template_copy:
                                        template_value = template_copy[key]
                                        if '<value>' in template_value:
                                            if '<text_color>' in template_value:
                                                template_value = template_value.replace(
                                                    '<text_color>', flavor_colors.text_color)
                                            elif '<green_text_color>' in template_value:
                                                template_value = template_value.replace(
                                                    '<green_text_color>', flavor_colors.green_text_color)
                                            elif '<yellow_text_color>' in template_value:
                                                template_value = template_value.replace(
                                                    '<yellow_text_color>', flavor_colors.yellow_text_color)
                                            elif '<purple_text_color>' in template_value:
                                                template_value = template_value.replace(
                                                    '<purple_text_color>', flavor_colors.purple_text_color)
                                            template_copy[key] = template_value.replace('<value>', value)
                                        else:
                                            template_copy[key] = ''

                                # Save the updated template_copy as a new file.
                                new_file_name = PurePath(
                                    temporary_files_dir, flavor, 'assets', mod_name, 'lang', lang)
                                shutil_copy2(template_language_file, new_file_name)

                                with open(new_file_name, 'w', encoding='utf-8') as new_file:
                                    if lang.endswith('.json'):
                                        json_dump(template_copy, new_file, indent=4, ensure_ascii=False)
                                    elif lang.endswith('.lang'):
                                        for key, value in template_copy.items():
                                            new_file.write(f'{key}={value}\n')

                            print(
                                f'Language files of {mod_name} ready for the '
                                f'temporary template of flavor {flavor}!\n')

                # Delete the 'template_settings.json' file as it is not part of the resource pack.
                elif filename == 'template_settings.json':
                    file_path = PurePath(dirpath, filename)
                    os_remove(file_path)

        print(f'Temporary template for flavor {flavor} is ready!\n')

        # Generate resource packs for each accent color from the temporary template of flavor created earlier.
        for color in CatppuccinAccentColors.all():
            print(f'Starting to create flavor {flavor} with accent color {color}!')

            version_folder = PurePath(output_folder, f'Catppuccin {flavor} {color}')

            # Set correct color value for accent color.
            if color == CatppuccinAccentColors.lavender:
                accent_color = flavor_colors.lavender
            elif color == CatppuccinAccentColors.blue:
                accent_color = flavor_colors.blue
            elif color == CatppuccinAccentColors.sapphire:
                accent_color = flavor_colors.sapphire
            elif color == CatppuccinAccentColors.sky:
                accent_color = flavor_colors.sky
            elif color == CatppuccinAccentColors.teal:
                accent_color = flavor_colors.teal
            elif color == CatppuccinAccentColors.green:
                accent_color = flavor_colors.green
            elif color == CatppuccinAccentColors.yellow:
                accent_color = flavor_colors.yellow
            elif color == CatppuccinAccentColors.peach:
                accent_color = flavor_colors.peach
            elif color == CatppuccinAccentColors.maroon:
                accent_color = flavor_colors.maroon
            elif color == CatppuccinAccentColors.red:
                accent_color = flavor_colors.red
            elif color == CatppuccinAccentColors.mauve:
                accent_color = flavor_colors.mauve
            elif color == CatppuccinAccentColors.pink:
                accent_color = flavor_colors.pink
            elif color == CatppuccinAccentColors.flamingo:
                accent_color = flavor_colors.flamingo
            else:
                accent_color = flavor_colors.rosewater

            color_map = {(255, 0, 0): accent_color}

            # Delete version_folder if it exists so a new one can be created.
            if os_path_exists(version_folder):
                rmtree(version_folder)

            # Copy the temporary template to the final location
            #   and then update the accent color for each texture.
            copytree(temporary_template_folder, version_folder)
            for dirpath, _, filenames in os_walk(version_folder):
                for filename in filenames:
                    # Update accent color for all textures.
                    if filename.endswith('.png'):
                        if not filename.startswith('$'):
                            image_path = PurePath(dirpath, filename)
                            with Image.open(str(image_path)) as image:
                                image = image.convert('RGBA')
                                width, height = image.size

                                for template_color, new_color in color_map.items():
                                    # Process all pixels
                                    for x in range(0, width):
                                        for y in range(0, height):
                                            r, g, b, a = image.getpixel((x, y))
                                            new_color_with_alpha = new_color + (a,)
                                            if (r, g, b) == template_color:
                                                image.putpixel((x, y), new_color_with_alpha)
                                image.save(str(image_path), 'PNG')

                        # If file has '$current_accent_color$' prefix
                        #   remove the prefix so textures inside file will work in the pack.
                        elif filename.startswith(f'${color.lower()}$'):
                            os_rename(
                                PurePath(dirpath, filename),
                                PurePath(dirpath, filename.replace(f'${color.lower()}$', '')))

                        # Remove '$ignore$' prefix if file has it.
                        elif filename.startswith('$ignore$'):
                            os_rename(
                                PurePath(dirpath, filename),
                                PurePath(dirpath, filename.replace('$ignore$', '')))

                    # Update pack description.
                    elif filename == 'pack.mcmeta':
                        file_path = PurePath(dirpath, filename)
                        with open(file_path, 'r') as pack_mcmeta:
                            try:
                                mcmeta = json_load(pack_mcmeta)
                            except JSONDecodeError as e:
                                print(
                                    f'ERROR: Unable to load pack.mcmeta file at path: '
                                    f'{pack_mcmeta}\nReason: ', e)
                                return

                        mcmeta['pack']['description'] = (
                            mcmeta['pack']['description']
                            .replace('<pack_version>', version)
                            .replace('<mc_version>', versions))

                        with open(file_path, 'w') as pack_mcmeta:
                            json_dump(mcmeta, pack_mcmeta, indent=4)

            make_archive(str(version_folder), 'zip', str(version_folder))
            rmtree(version_folder)
        print(f'\nFlavor {flavor} is ready for every accent color!')

    # Delete the temporary files folder.
    if isdir(temporary_files_dir):
        rmtree(temporary_files_dir)

    # Calculate the time it took to run this script.
    ending_time = int(time_perf_counter())
    total_time = ending_time - starting_time
    minutes, seconds = divmod(total_time, 60)

    print(
        f'\nEverything done!\n'
        f'Completed in {minutes} minutes and {seconds} seconds.\n'
        f'You may close this window now!')
    return


if __name__ == '__main__':
    main()
    input()
