import numpy as np
from scipy.spatial import ConvexHull
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
points = np.empty(shape=[0, 2])
draw = ImageDraw.Draw(image)

for index, row in df.iterrows():
    x, y = row['y'], row['x']
    points = np.append(points, [[x, y]], axis=0)
    draw.point((x, 540-y), fill=ImageColor.getrgb("black"))


new_ds = []
hull = ConvexHull(points)
for i in range(points[hull.vertices, 0].size):
    new_ds.append([int(points[hull.vertices[i]][0]), int(points[hull.vertices[i]][1])])

new_df = pd.DataFrame(new_ds, columns=('x', 'y'))
name = input("Enter name for convex dataset(in format 'file_name.txt'):")
new_df.to_csv(name, header=None, index=None, sep=' ', mode='a')


for i in range(len(new_ds)):
    if i < len(new_ds) - 1:
        draw.line((new_ds[i][0], 540-new_ds[i][1], new_ds[i+1][0], 540-new_ds[i+1][1]), width=3, fill=(0, 0, 255))
    else:
        draw.line((new_ds[i][0], 540-new_ds[i][1], new_ds[0][0], 540-new_ds[0][1]), width=3, fill=(0, 0, 255))

image.show()
name = input("Enter name for saved image(in format 'file_name.png'):")
image.save(name, "PNG")
