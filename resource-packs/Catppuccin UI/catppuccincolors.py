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
        '__subtext0',
        '__subtext1',
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
            subtext0,
            subtext1,
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
        self.__subtext0 = subtext0
        self.__subtext1 = subtext1
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
    def subtext0(self):
        return self.__subtext0
    
    @property
    def subtext1(self):
        return self.__subtext1
    
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
            subtext0=(166, 173, 200),
            subtext1=(186, 194, 222),
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
            subtext0=(165, 173, 203),
            subtext1=(184, 192, 224),
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
            subtext0=(165, 173, 206),
            subtext1=(181, 191, 226),
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
            subtext0=(108, 111, 133),
            subtext1=(92, 95, 119),
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
            text_color='§8',
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