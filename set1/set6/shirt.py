import sys
from PIL import Image


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".jpg") == False and sys.argv[1].endswith(".jpeg") == False and sys.argv[1].endswith(".png") == False:
    sys.exit("Invalid input")
elif sys.argv[2].endswith(".jpg") == False and sys.argv[2].endswith(".jpeg") == False and sys.argv[2].endswith(".png") == False:
    sys.exit("Invalid output")

filename1, extension1 = sys.argv[1].split(sep=".")
filename2, extension2 = sys.argv[2].split(sep=".")

if extension1 != extension2:
    sys.exit("Input and output have different extensions")

try:
    input = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

# size = input.size
# mask = Image.open("shirt.png")
# # output = Image.new(sys.argv[2], (size[0], size[1]))
# output = Image.new("RGB", size)
# # output.paste(im=input, mask=mask)
# output.paste(input)
# output.paste(mask, (size[0], 0))

# images = []
# images.append(input)
# mask = Image.open("shirt.png")
# images.append(mask)

# images[0].save(
#     sys.argv[2], save_all=True, append_images=[images[1]], duration=100, loop=0
# )

shirt = Image.open("shirt.png")
size = input.size
input.paste(input, shirt)

input.save(
    sys.argv[2]
)
