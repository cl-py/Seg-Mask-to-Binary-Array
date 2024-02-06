import os

from PIL import Image

def writeRGBArray(image):
    image = image.convert("RGB")
    width, height = image.size
    rgb_values = []
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            #appends binary pixel values to a 2D array. 
            #CHANGE THESE VALUES IF NECESSARY
            if r == 0 and g == 0 and b == 0:
                rgb_values.append(0)
            else:
                rgb_values.append(1)
    return rgb_values
    
directory = "INSERT FOLDER PATH HERE"
numImg = 1
rgb_values = []
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        filepath = os.path.join(directory, filename)
        try:
            image = Image.open(filepath)
            outfile = f"frame{numImg}.txt"
            numImg += 1
            with open(outfile, "w") as f:
                f.write(" ".join(map(str, writeRGBArray(image))))
        except Exception as e:
            print(f"Error opening image {filename}: {e}")
            
print("Done. Quitting program...")
    