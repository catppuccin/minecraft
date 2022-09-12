from PIL import Image
from PIL import ImageColor
import numpy as np
img = Image.open("file.png")

flavor = "macchiato" # latte, frappe or macchiato
### Colors for each flavor
if (flavor=="macchiato"):
    crust = [24, 25, 38]
    mantle = [30, 32, 48]
    base = [36, 39, 58]
    surface0 = [54, 58, 79]
    surface1 = [73, 77, 100]
    surface2 = [91, 96, 120]
    overlay0 = [110, 115, 141]
    overlay1 = [128, 135, 162]
    overlay2 = [147, 154, 183]
    text = [202, 211, 245]
    lavender = [183, 189, 248]
    red = [237, 135, 150]
    red2 = [176, 100, 112]
    green = [166, 218, 149]

if (flavor=="frappe"):
    crust = [35, 38, 52]
    mantle = [41, 44, 60]
    base = [48, 52, 70]
    surface0 = [65, 69, 89]
    surface1 = [81, 87, 109]
    surface2 = [98, 104, 128]
    overlay0 = [115, 121, 148]
    overlay1 = [131, 139, 167]
    overlay2 = [148, 156, 187]
    text = [198, 208, 245]
    lavender = [186, 187, 241]
    red = [231, 130, 132]
    red2 = [172, 97, 98]
    green = [166, 209, 137]

if (flavor=="latte"):
    crust = [220, 224, 232]
    mantle = [230, 233, 239]
    base = [239, 241, 245]
    surface0 = [204, 208, 218]
    surface1 = [188, 192, 204]
    surface2 = [172, 176, 190]
    overlay0 = [156, 160, 176]
    overlay1 = [140, 143, 161]
    overlay2 = [124, 127, 147]
    text = [76, 79, 105]
    lavender = [114, 135, 253]
    red = [210, 15, 57]
    red2 = [156, 11, 42]
    green = [64, 160, 43]


print(img.mode) #RGB
print(img.size)

width = img.size[0] 
height = img.size[1] 


for i in range(0,width):# process all pixels
    for j in range(0,height):
        data = img.getpixel((i,j))

# Crust
        if (data[0]==17 and data[1]==17 and data[2]==27):
            img.putpixel((i,j),(crust[0], crust[1], crust[2]))

# Mantle
        #print(data) #(255, 255, 255)
        if (data[0]==24 and data[1]==24 and data[2]==37):
            img.putpixel((i,j),(mantle[0], mantle[1], mantle[2]))

# Base
        #print(data) #(255, 255, 255)
        if (data[0]==30 and data[1]==30 and data[2]==46):
            img.putpixel((i,j),(base[0], base[1], base[2]))

# Surface 0
        #print(data) #(255, 255, 255)
        if (data[0]==49 and data[1]==50 and data[2]==68):
            img.putpixel((i,j),(surface0[0], surface0[1], surface0[2]))

# Surface 1
        #print(data) #(255, 255, 255)
        if (data[0]==69 and data[1]==71 and data[2]==90):
            img.putpixel((i,j),(surface1[0], surface1[1], surface1[2]))

# Surface 2
        #print(data) #(255, 255, 255)
        if (data[0]==88 and data[1]==91 and data[2]==112):
            img.putpixel((i,j),(surface2[0], surface2[1], surface2[2]))

# Overlay 0
        #print(data) #(255, 255, 255)
        if (data[0]==108 and data[1]==112 and data[2]==134):
            img.putpixel((i,j),(overlay0[0], overlay0[1], overlay0[2]))

# Overlay 1
        #print(data) #(255, 255, 255)
        if (data[0]==127 and data[1]==132 and data[2]==156):
            img.putpixel((i,j),(overlay1[0], overlay1[1], overlay1[2]))

# Overlay 2
        #print(data) #(255, 255, 255)
        if (data[0]==147 and data[1]==153 and data[2]==178):
            img.putpixel((i,j),(overlay2[0], overlay2[1], overlay2[2]))

# Text
        #print(data) #(255, 255, 255)
        if (data[0]==205 and data[1]==214 and data[2]==244):
            img.putpixel((i,j),(text[0], text[1], text[2]))

# Lavender
        #print(data) #(255, 255, 255)
        if (data[0]==180 and data[1]==190 and data[2]==254):
            img.putpixel((i,j),(lavender[0], lavender[1], lavender[2]))

# Red
        #print(data) #(255, 255, 255)
        if (data[0]==243 and data[1]==139 and data[2]==168):
            img.putpixel((i,j),(red[0], red[1], red[2]))

# Red2
        #print(data) #(255, 255, 255)
        if (data[0]==181 and data[1]==103 and data[2]==125):
            img.putpixel((i,j),(red2[0], red2[1], red2[2]))

# Green
        #print(data) #(255, 255, 255)
        if (data[0]==166 and data[1]==227 and data[2]==161):
            img.putpixel((i,j),(green[0], green[1], green[2]))

# Save image
img.save("output.png")