#!/usr/bin/env python3
import os, sys
from PIL import Image

if(len(sys.argv) != 2):
    exit("error parameter 1 should be input file name")

inFileName = sys.argv[1]

outDirName = inFileName.split('.')[-2]
fileType = inFileName.split('.')[-1].lower()

if fileType not in ("jpg", "png"):
    exit("unknow file type")

im = Image.open(inFileName)

if(im.size[0] != im.size[1]):
    exit("error! image not square")

l = 400
g = 10
L = 3 * l + 2 * g

region = im.resize((L, L))

boxes = ((0, 0, l, l),
         (l+g, 0, 2*l+g, l),
         (2*(l+g), 0, L, l),
         (0, l+g, l, 2*l+g),
         (l+g, l+g, 2*l+g, 2*l+g),
         (2*(l+g), l+g, L, 2*l+g),
         (0, 2*(l+g), l, L),
         (l+g, 2*(l+g), 2*l+g, L),
         (2*(l+g), 2*(l+g), L, L),
         )

os.makedirs(outDirName,exist_ok=True)

for index, box in enumerate(iterable=boxes, start=1):
    out = region.crop(box)
    out.save(outDirName + "/" + str(index) + "." + fileType)

print("Done!")
