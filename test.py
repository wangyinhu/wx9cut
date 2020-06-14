from PIL import Image, ImageDraw

im = Image.open("o.png")
print("im", im.format, im.size, im.mode)
box = (1, 2, 1434, 1435)
region = im.crop(box)

l = 1000
g = 25
L = 3 * l + 2 * g
region = region.resize((L, L))
print("region", region.format, region.size, region.mode)
draw = ImageDraw.Draw(region)


lineWidth = 5
draw.line((0, l, L, l), fill=255, width=lineWidth)
draw.line((0, l + g, L, l + g), fill=255, width=lineWidth)
draw.line((l, 0, l, L), fill=255, width=lineWidth)
draw.line((l + g, 0, l + g, L), fill=255, width=lineWidth)

draw.line((0, l + g + l, L, l + g + l), fill=255, width=lineWidth)
draw.line((0, l + g + l + g, L, l + g + l + g), fill=255, width=lineWidth)
draw.line((l + g + l, 0, l + g + l, L), fill=255, width=lineWidth)
draw.line((l + g + l + g, 0, l + g + l + g, L), fill=255, width=lineWidth)

draw.line((0, 0, L, L), fill=255, width=lineWidth)
draw.line((0, L, L, 0), fill=255, width=lineWidth)

draw.line((0, L, L, L), fill=255, width=lineWidth)
draw.line((L, 0, L, L), fill=255, width=lineWidth)


# region.show()
region.resize((l, l)).show()

# box1 = (0, 0, l, l)
# out1 = region.crop(box1)

# out1.show()

