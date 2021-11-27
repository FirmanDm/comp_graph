import math

import numpy as np
from PIL import Image, ImageColor, ImageDraw
import pandas as pd

width = 960
height = 960
image = Image.new("RGB", (width, height), (255, 255, 255))
filepath = input("Input path to your file: ")
df = pd.read_csv(filepath, sep=" ", header=None)
head = ['x', 'y']
df.columns = head

alpha = math.pi/18

matrix = ([[math.cos(alpha), math.sin(alpha), 0],
           [(-1)*math.sin(alpha), math.cos(alpha), 0],
           [480*(math.sin(alpha)-math.cos(alpha)+1), 480*(1-math.cos(alpha)-math.sin(alpha)), 1]])

draw = ImageDraw.Draw(image)
for index, row in df.iterrows():
    x, y = row['x'], row['y']
    result = np.matmul(np.array([x, y, 1]), matrix)
    draw.point((int(result[0]), int(result[1])), fill=ImageColor.getrgb("blue"))


image.show()
name = input("Enter name for saved image(in format 'file_name.png'):")
image.save(name, "PNG")
