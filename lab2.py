from PIL import Image, ImageColor, ImageDraw
import pandas as pd

width = 960
height = 540
image = Image.new("RGB", (width, height), (255, 255, 255))
# C:\Users\galia\Downloads\DS0.txt
filepath = input("Input path to your file: ")
df = pd.read_csv(filepath, sep=" ", header=None)
head = ['x', 'y']
df.columns = head

draw = ImageDraw.Draw(image)
for index, row in df.iterrows():
    x, y = row['y'], 540 - row['x']
    draw.point((x, y), fill=ImageColor.getrgb("black"))
image.show()
name = input("Enter name for saved image(in format 'file_name.png'):")
image.save(name, "PNG")
