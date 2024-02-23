import os

from PIL import Image

#------------------------------------#
#Appends binary pixel values to array.
#------------------------------------#
def writeRGBArray(image):
    image = image.convert("RGB")
    width, height = image.size
    rgb_values = []
    #iterates through entire image pixel by pixel.
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
    
#------------------------------------#
#Specify image path and output directory here.
#------------------------------------#
image_path = r""
output_dir = r""

numImg = 1
rgb_values = []
for filename in os.listdir(image_path):
    if filename.endswith(".png"):
        filepath = os.path.join(image_path, filename)
        try:
            image = Image.open(filepath)
            outfile = os.path.join(output_dir, f"frame{numImg}.txt")
            numImg += 1
            with open(outfile, "w") as f:
                f.write(" ".join(map(str, writeRGBArray(image))))
        except Exception as e:
            print(f"Error opening image {filename}: {e}")
            
print("Done. Quitting program...")
    


            
